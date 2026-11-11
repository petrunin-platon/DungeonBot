"""Сторож окна программы (задача 15): окно перестало отвечать — записать, где застрял код.

Окно раз в полсекунды ставит «отметку жизни» (root.after). Отдельный поток только смотрит на эту отметку и окно не трогает
(виджеты Tk из другого потока трогать нельзя). Отметки нет 5 с — значит, главный поток чем-то занят и Windows вот-вот
напишет «Не отвечает». Тогда поток записывает в bot_data/debug/ui_freeze_<время>.txt, на какой строке сейчас каждый поток
(faulthandler), и одну строку в консоль. Пока окно снова не ожило, второй раз не пишет.

Поток фоновый (daemon): закрыть программу он не мешает. stop() — при закрытии окна (и само по событию <Destroy> окна).
Модуль не импортирует tkinter (ошибки окна ловятся как Exception) — его можно проверить тестом без экрана.

Журнал задержек (сессия 11б): окно замерло дольше LAG_S, но меньше 5 с — строка в bot_data/debug/ui_lag_<время запуска>.txt:
когда, на сколько, что окно делало перед этим (note: «перетаскивание окна», «страница rules», «разворачивание окна»)
и где был главный поток через LAG_S после начала задержки. Последней строкой стека видно, где ждали: в нашем коде Python
или внутри Tk и Windows (стек кончается на mainloop/update). Файл появляется только при первой задержке, хранятся 10 последних.
"""
import collections
import datetime
import faulthandler
import glob
import os
import sys
import threading
import time
import traceback

import data_paths

HEARTBEAT_MS = 100   # как часто окно ставит отметку
FREEZE_S = 5.0       # столько без отметки — считаем, что окно зависло
CHECK_S = 0.1        # как часто поток смотрит на отметку
LAG_S = 0.5          # столько без отметки (сверх HEARTBEAT_MS) — задержка, строка в журнале задержек
LAG_FILES_KEPT = 10  # журналов задержек хранится столько (по одному на запуск программы)
NOTES_KEPT = 3       # сколько последних «что окно делало» писать в строку задержки


class FreezeGuard:
    def __init__(self, root, folder=None, freeze_s=FREEZE_S, clock=time.monotonic):
        self.root = root
        self.folder = folder
        self.freeze_s = freeze_s
        self.clock = clock
        self.last_beat = clock()
        self.reported = False
        self.reports = []
        self.lag_path = None             # журнал задержек этого запуска (появляется с первой задержкой)
        self.lags = []                   # (когда, сколько с) — записанные задержки
        self._stopped = threading.Event()
        self._after_id = None
        self._notes = collections.deque(maxlen=NOTES_KEPT)   # (когда, что окно делало)
        self._gaps = collections.deque()  # задержки, замеченные главным потоком: (начало, сколько с)
        self._sample = None              # (отметка, с которой началась задержка, стек главного потока)
        self._main = threading.main_thread().ident
        self._started = datetime.datetime.now()

    def start(self):
        """Начать отметки и запустить поток-наблюдатель. Вызывать из главного потока после создания окна."""
        self._beat()
        try:
            self.root.bind("<Destroy>", self._on_destroy, add="+")
        except Exception:  # окно уже закрыто
            pass
        threading.Thread(target=self._watch, name="ui-freeze-guard", daemon=True).start()
        return self

    def stop(self):
        self._stopped.set()
        if self._after_id is not None:
            try:
                self.root.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = None

    def _on_destroy(self, event):
        if event.widget is self.root:
            self.stop()

    def _beat(self):
        """Отметка жизни (в главном потоке)."""
        if self._stopped.is_set():
            return
        now = self.clock()
        stall = now - self.last_beat - HEARTBEAT_MS / 1000
        if stall >= LAG_S:
            self._gaps.append((self.last_beat, stall))
        self.last_beat = now
        self.reported = False
        try:
            self._after_id = self.root.after(HEARTBEAT_MS, self._beat)
        except Exception:  # окно уже закрыто
            self._stopped.set()

    def note(self, text):
        """Что окно сейчас делает (из главного потока): попадёт в строку журнала задержек, если окно замрёт."""
        self._notes.append((self.clock(), text))

    def _watch(self):
        while not self._stopped.wait(CHECK_S):
            self.check()

    def check(self):
        """Одна проверка (в потоке-наблюдателе). Возвращает путь к записанному файлу зависания или None.
        Заодно — журнал задержек: стек главного потока через LAG_S после начала задержки и строка, когда окно ожило."""
        if self._stopped.is_set():
            return None
        beat = self.last_beat
        stuck = self.clock() - beat
        if stuck >= LAG_S + HEARTBEAT_MS / 1000 and (self._sample is None or self._sample[0] != beat):
            self._sample = (beat, self._main_stack())
        while self._gaps:
            start, stall = self._gaps.popleft()
            stack = self._sample[1] if self._sample and self._sample[0] == start else ""
            self._write_lag(start, stall, stack)
        if self.reported or stuck < self.freeze_s:
            return None
        self.reported = True
        return self._report(stuck)

    def _main_stack(self):
        """Где сейчас главный поток (последние строки стека, сверху — самая глубокая)."""
        frame = sys._current_frames().get(self._main)
        if frame is None:
            return ""
        lines = traceback.format_list(traceback.extract_stack(frame)[-8:])
        return "".join(reversed(lines))

    def _write_lag(self, start, stall, stack):
        """Строка в журнал задержек (в потоке-наблюдателе). Ошибки записи не мешают окну."""
        when = datetime.datetime.now() - datetime.timedelta(seconds=self.clock() - start)
        notes = "; ".join(f"{text} ({start - at:.1f} с до)" for at, text in list(self._notes) if at <= start + stall)
        try:
            if self.lag_path is None:
                folder = self.folder or data_paths.debug_dir()
                os.makedirs(folder, exist_ok=True)
                old = sorted(glob.glob(os.path.join(folder, "ui_lag_*.txt")))
                for path in old[:max(0, len(old) - LAG_FILES_KEPT + 1)]:
                    try:
                        os.remove(path)
                    except OSError:
                        pass
                self.lag_path = os.path.join(folder, f"ui_lag_{self._started:%Y%m%d_%H%M%S}.txt")
                with open(self.lag_path, "w", encoding="utf-8") as f:
                    f.write(f"Задержки окна программы дольше {LAG_S:.1f} с (запуск {self._started:%d.%m.%Y %H:%M:%S}).\n"
                            "Строка: когда, на сколько окно замерло, что оно делало перед этим; ниже — где был код "
                            "(сверху — самая глубокая строка).\n\n")
            with open(self.lag_path, "a", encoding="utf-8") as f:
                f.write(f"{when:%H:%M:%S.%f}"[:-3] + f"  {stall:.1f} с  [{notes or 'нет отметок'}]\n")
                if stack:
                    f.write("".join("    " + line + "\n" for line in stack.rstrip().split("\n")))
                f.write("\n")
            self.lags.append((when, stall))
        except OSError:
            pass

    def _report(self, stuck):
        folder = self.folder or data_paths.debug_dir()
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"ui_freeze_{datetime.datetime.now():%Y%m%d_%H%M%S}.txt")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"Окно программы не отвечает {stuck:.0f} с. Где сейчас код "
                        f"(в каждом потоке последняя строка — сверху):\n\n")
                f.flush()
                faulthandler.dump_traceback(file=f, all_threads=True)
        except OSError as e:
            print(f"[GUI] Окно не отвечает {stuck:.0f} с, но записать отчёт не удалось: {e}", file=sys.__stderr__)
            return None
        self.reports.append(path)
        print(f"[GUI] Окно не отвечает {stuck:.0f} с. Где застрял код — в файле {path}", file=sys.__stderr__,
              flush=True)
        return path
