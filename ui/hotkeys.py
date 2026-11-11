"""Горячие клавиши окна программы (задача 15, шаг 2): F9 — мягкая пауза / снять паузу, F10 — экстренный стоп.

Без новой библиотеки, тем же способом, каким бот ловит Ctrl+Q (main.py:background_hotkey_listener): раз в 50 мс
спрашиваем у Windows, нажата ли клавиша (GetAsyncKeyState). Клавиатура не перехватывается: нажатие доходит и до игры.
Клавиши работают, только когда активно окно игры (scrcpy, заголовок HeroWarsBot_Arena) или окно программы
(ответ пользователя 22.10.2026): F10, нажатая в браузере, бота не останавливает.

Поток только смотрит на клавиши и кладёт в очередь ("hotkey", "F9"); окно забирает её через after
(виджеты Tk из другого потока трогать нельзя). Поток фоновый (daemon) и закрыть программу не мешает.
Модуль без Tk: нажатия проверяют тесты на поддельной клавиатуре.
"""
import os
import sys
import threading

import win_focus

VK_F9 = 0x78
VK_F10 = 0x79
HOTKEYS = {"F9": VK_F9, "F10": VK_F10}
POLL_S = 0.05   # 20 проверок в секунду, как у бота


class KeyEdges:
    """Нажатие — клавиша опущена сейчас и не была опущена при прошлой проверке: удержание не повторяет команду.
    Клавишу, опущенную в чужой программе, не засчитываем и потом, когда окно игры станет активным."""

    def __init__(self, keys=None):
        self.keys = dict(keys or HOTKEYS)
        self.down = {name: False for name in self.keys}

    def poll(self, key_down, allowed=lambda: True):
        """key_down(vk) — опущена ли клавиша; allowed() — активно ли окно игры или программы.
        Возвращает имена только что нажатых клавиш (["F9"])."""
        pressed = []
        for name, vk in self.keys.items():
            now = bool(key_down(vk))
            if now and not self.down[name] and allowed():
                pressed.append(name)
            self.down[name] = now
        return pressed


def win_key_down(vk):
    """Клавиша опущена прямо сейчас (старший бит GetAsyncKeyState), как у бота."""
    return win_focus.key_down(vk)


def win_foreground_is(game_title, pid=None):
    """Активно окно игры (в заголовке game_title) или любое окно этой программы (главное, диалоги, позже мини-бар)."""
    return win_focus.foreground_is(game_title, (pid or os.getpid(),))


class HotkeyWatcher:
    """Фоновый поток: нажатые F9/F10 → в очередь events. Вне Windows (и без поддельной клавиатуры) не запускается."""

    def __init__(self, events, game_title, key_down=None, allowed=None, interval=POLL_S):
        self.events = events
        self.edges = KeyEdges()
        self.interval = interval
        self.key_down = key_down
        self.allowed = allowed
        if key_down is None and sys.platform == "win32":
            self.key_down = win_key_down
            self.allowed = allowed or (lambda: win_foreground_is(game_title))
        self._stopped = threading.Event()

    @property
    def available(self):
        return self.key_down is not None

    def start(self):
        if self.available:
            threading.Thread(target=self._run, name="ui-hotkeys", daemon=True).start()
        return self

    def stop(self):
        self._stopped.set()

    def check(self):
        """Одна проверка клавиш (в потоке)."""
        for name in self.edges.poll(self.key_down, self.allowed or (lambda: True)):
            self.events.put(("hotkey", name))

    def _run(self):
        while not self._stopped.wait(self.interval):
            try:
                self.check()
            except Exception:  # сбой Windows при проверке клавиш не должен убивать поток
                pass
