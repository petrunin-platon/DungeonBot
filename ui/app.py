"""Новое окно программы (задача 15, шаг 2 — каркас).

Запуск: start.bat, python gui.py или собранный .exe (build_exe.bat). Старое окно удалено на шаге 9.

Каркас — по design/README.md («Каркас окна»): слева полоска 64 px (логотип, 5 разделов с подсказками, Telegram, язык),
сверху шапка 56 px (название раздела, плашка телефона, три кнопки), ниже — страница. С шага 3 главная новая
(ui/main_page.py), с шага 5а — «Мастер правил» (ui/rules_page.py), с шага 6 — «Статистика»
(ui/stats_page.py; «Аналитику» убрали 25.10.2026: золотые правила бот при «Бот решает сам» создаёт сам), с шага 7 — «О программе» (ui/about_page.py), с шага 10.0 — «Руководство» (ui/guide_page.py, текст — guide/<язык>.md).
Старых вкладок больше нет. Страницам окно — controller: current_lang, frames, select_frame; главная — frames["dash"] с append_log().

Связь с ботом не меняется (протокол тот же): бота запускает, читает и останавливает главная через ui/bot_link.py.
Кнопки шапки и F9/F10 вызывают её же: та же пауза (pause.flag), тот же стоп, те же строки в журнале.

Чтобы окно не зависало и закрывалось крестиком (правила — в начале ui/widgets.py):
- всё, что ждёт (окно scrcpy, клавиши, profile.yml, кнопки шапки, строки бота, Telegram), работает в фоновых потоках;
  в окно — через очередь self.events, её окно разбирает раз в 100 мс (after);
- крестик: если бот работает — вопрос «Остановить бота?»; потом остановить потоки и свои after, спрятать окно,
  остановить бота и scrcpy (как старое окно) и закрыть окно — mainloop кончается, процесс выходит сам;
- сторож ui/freeze_guard.py пишет bot_data/debug/ui_freeze_*.txt, если окно не отвечает 5 с.

Без рамки Windows (шаг 6а.2, ui/win_frame.py): в шапке кнопки «Свернуть / Развернуть / Закрыть», окно двигают за шапку
и растягивают за уголок справа внизу.

Мини-бар (шаг 4, ui/hud.py): бот запустился (или «Свернуть в мини-бар») — окно сворачивается на панель задач,
под игрой появляется мини-бар (ваш ответ 22.10.2026). «Развернуть» в мини-баре или кнопка окна на панели задач —
окно снова целиком, мини-бар прячется. Бот остановился — окно разворачивается само (там «Итог сессии»).
Пока окно в мини-баре (mini), окна SOS и «Собери состав» показываются сами по себе над игрой (ui/widgets.py).
"""
import os
import queue
import sys
import time
import tkinter as tk

import customtkinter as ctk

from config import GAME_WINDOW_TITLE, PAUSE_FLAG_FILE
from i18n import LANGUAGES, get_text
from ui import hud_place, light, phone, theme, ui_settings, win_frame
from ui.about_page import AboutPage
from ui.freeze_guard import FreezeGuard
from ui.guide_page import GuidePage
from ui.hotkeys import HotkeyWatcher
from ui.hud import Hud
from ui.icons import dot, icon_with_dot
from ui.main_page import MainPage
from ui.rules_page import RulesPage
from ui.stats_page import StatsPage
from ui.status import StatusWatcher
from ui.widgets import Button, ConfirmDialog, IconButton, PopupMenu, Toast, Tooltip
from ui.window_fit import fit_window, work_area

C = theme.COLORS
T = theme.TINTS
F = theme.FONTS
S = theme.SIZES

# Разделы: имя (как в старом окне), старая вкладка, иконка, подсказка в полоске, заголовок в шапке
PAGES = (
    ("dash", MainPage, "house", "btn_main", "page_title_main"),
    ("rules", RulesPage, "sliders-vertical", "btn_rules", "btn_rules"),
    ("stats", StatsPage, "chart-no-axes-column", "btn_stats", "page_title_stats"),
    ("guide", GuidePage, "book-open", "btn_guide", "btn_guide"),
    ("about", AboutPage, "info", "btn_about", "btn_about"),
)
CORNER_RADIUS = 8        # скругление углов окна, px макета
GRIP_SIZE = 14           # уголок справа внизу, за который растягивают окно
DRAIN_MS = 100          # как часто окно забирает события из очереди
RESTART_PAUSE_MS = 1000  # перезапуск scrcpy: пауза между остановкой и запуском (как в старом окне)
REVEAL_MS = 30           # Windows: «плащ» снимается, когда окно уже нарисовано (см. App._reveal)
OFFSCREEN = -32000       # Windows: окно в первый раз появляется за краем экрана (App._reveal)
PREPARE_MS = 2500        # через столько после запуска «Руководство» строится заранее, спрятанным (App._prepare)
COVER_CHECK_MS = 10      # заслонка: как часто проверять, показал ли Tk всё под ней (App._uncover_when_ready)
COVER_MAX_MS = 700       # ... и не дольше: потом заслонка уходит, даже если что-то ещё показывается


class DotIconButton(IconButton):
    """Кнопка полоски с точкой состояния у иконки (Telegram: зелёная — включён, серая — не настроен)."""

    def __init__(self, master, icon_name, dot_color, **kwargs):
        self._dot_color = dot_color
        super().__init__(master, icon_name, kind="nav", **kwargs)

    def _icon_image(self):
        color = C["blue_text"] if self._active else C["text_secondary"]
        return icon_with_dot(self._icon_name, color, self._icon_size, self._dot_color)

    def set_dot(self, color):
        if color != self._dot_color:
            self._dot_color = color
            self.configure(image=self._icon_image())


class DevicePlate(light.Box):
    """Плашка в шапке: «● HeroWarsBot_Arena подключено» (зелёная) или «● Ожидание телефона…» (красная).
    Подключено — есть окно scrcpy (ui/status.py)."""

    def __init__(self, master):
        super().__init__(master, fg_color=C["bg_surface"], border_width=1, border_color=C["border"],
                         corner_radius=S["radius_control"], width=10, height=10)
        self.connected = None
        self._dot = light.Label(self, text="", width=8, height=24)
        self._dot.pack(side="left", padx=(12, 8), pady=5)
        self._name = light.Label(self, text=GAME_WINDOW_TITLE, font=F["mono"], text_color=C["text"], height=24)
        self._status = light.Label(self, text="", font=F["text"], height=24)
        self._status.pack(side="left", padx=(0, 12), pady=5)

    def show(self, connected, lang):
        self.connected = connected
        self._dot.configure(image=dot(C["success"] if connected else C["danger"], 8))
        if connected:
            self._name.pack(side="left", padx=(0, 8), pady=5, before=self._status)
            self._status.configure(text=get_text(lang, "hdr_connected"), text_color=C["success"])
        else:
            self._name.pack_forget()
            self._status.configure(text=get_text(lang, "hdr_waiting"), text_color=C["danger_text"])


def find_game_window():
    """Окно игры для мини-бара (hud_place.GameWindow) или None. Вне Windows окна scrcpy нет."""
    if not hud_place.windows_available():
        return None
    return hud_place.win_find_game(GAME_WINDOW_TITLE)


class App(light.OwnEvents, light.NoAlpha, ctk.CTk):
    # Заголовок не перекрашивает CustomTkinter (он прячет окно и возвращает «как было»): красим сами, см. ui/win_frame.py
    _deactivate_windows_window_header_manipulation = True

    def __init__(self, settings_path=None, status_watcher=None, hotkey_watcher=None, game_locator=None):
        super().__init__(fg_color=C["bg_primary"])
        self.withdraw()                  # окно собирается невидимым и появляется готовым (сессия 11: 3 с белого окна)
        self.settings_path = settings_path
        saved = ui_settings.load(settings_path).get("language")
        self.current_lang = saved if saved in LANGUAGES else "RU"
        self.events = queue.Queue()      # события из фоновых потоков: ("log", текст), ("phone", да/нет), ...
        self.page = None
        self.phone_connected = False
        self.telegram_on = False
        self._closing = False
        self._close_dialog = None
        self._timers = {}                # свои after, которые надо отменить при закрытии
        self.mini = False                # окно свёрнуто в мини-бар (шаг 4)
        self.hud = None
        self.game_locator = game_locator or find_game_window
        self._corners = None             # как скруглены углы: "dwm" (Windows 11) или "region" (Windows 10)
        self._region_size = None
        self.maximized = False           # «Развернуть» (шаг 6а.2): окно на всю свободную часть экрана
        self._normal_rect = None         # где окно было до «Развернуть»: (x, y, ширина, высота) в настоящих пикселях
        self._move_from = None           # перетаскивание за шапку: смещение курсора внутри окна
        self._grow_from = None           # растягивание за уголок: (курсор x, y, ширина, высота окна)

        self._cover_id = None            # заслонка над страницами: ждём, пока Tk покажет новую страницу
        self._veil_id = None             # заслонка над всем окном после сворачивания
        self.title(get_text(self.current_lang, "app_title"))
        width, height, min_w, min_h, x, y = fit_window(work_area(self), self._get_window_scaling())
        self._home = (x, y)              # где окно появляется (настоящие пиксели экрана)
        self._initial_size = (round(width * self._get_window_scaling()), round(height * self._get_window_scaling()))
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.minsize(min_w, min_h)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.bind("<Map>", self._on_map, add="+")
        self.bind("<Unmap>", self._on_unmap, add="+")
        self.bind("<Configure>", self._on_configure, add="+")

        # Как старое окно: пауза, оставшаяся от прошлого запуска, не должна держать бота
        if os.path.exists(PAUSE_FLAG_FILE):
            os.remove(PAUSE_FLAG_FILE)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self._build_rail()
        tk.Frame(self, width=1, bg=C["border"]).grid(row=0, column=1, sticky="ns")
        main = light.Frame(self, fg_color=C["bg_primary"])
        main.grid(row=0, column=2, sticky="nsew")
        main.grid_rowconfigure(2, weight=1)
        main.grid_columnconfigure(0, weight=1)
        self._build_header(main)
        tk.Frame(main, height=1, bg=C["border"]).grid(row=1, column=0, sticky="ew")
        self.content = light.Frame(main, fg_color=C["bg_primary"])
        self.content.grid(row=2, column=0, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # Спрятанные страницы «запаркованы» (сессия 11б): разложены в своём размере, но не показаны (_park_page).
        # Показанные элементы Tk в Windows — отдельные окна, и при сворачивании Tk прячет, а при разворачивании
        # показывает по одному каждый из них: со стопкой из всех страниц (сессия 11) их было 2600, из них 2070 —
        # «Руководство». Теперь — только видимая страница.
        self.parking = tk.Frame(self.content, bd=0, highlightthickness=0)    # её никогда не показывают
        # Заслонка над областью страниц на время смены страницы: Tk показывает элементы новой страницы по уровням,
        # под заслонкой этого не видно — страница появляется целиком (_show_frame)
        self.curtain = tk.Frame(self.content, bg=C["bg_primary"], bd=0, highlightthickness=0)
        self.frames = {name: page(self.content, self) for name, page, *_ in PAGES}
        self.plate.show(False, self.current_lang)
        self.select_frame("dash")
        self.set_language(self.current_lang, force=True)

        self.status = (status_watcher or StatusWatcher(self.events, GAME_WINDOW_TITLE)).start()
        self.hotkeys = (hotkey_watcher or HotkeyWatcher(self.events, GAME_WINDOW_TITLE)).start()
        self._timers["drain"] = self.after(DRAIN_MS, self._drain)
        self.guard = FreezeGuard(self).start()
        self._build_frame_decor()
        self._reveal()
        self._timers["prepare"] = self.after(PREPARE_MS, self._prepare)
        self.after_idle(lambda: win_frame.paint_title_dark(self))
        self.after_idle(self._strip_frame)

    def _reveal(self):
        """Показать собранное окно. Раскладка — пока окно невидимо (при запуске, не в обработчике). В Windows окно
        в первый раз появляется за краем экрана и сразу уходит под «плащ» (win_frame.cloak: Windows его рисует, но на
        экран не выводит), там же снимаются заголовок и рамка; потом окно встаёт на место, рисуется целиком (update —
        тоже при запуске, не в обработчике), и плащ снимается: без белого прямоугольника и без элементов, которые
        проступают по одному (проверка 26.10.2026). Раньше вместо плаща была прозрачность -alpha — после неё окно
        оставалось «полупрозрачным» навсегда (light.NoAlpha), и Windows перерисовывала его медленнее (сессия 11б)."""
        self.update_idletasks()
        if not win_frame.windows_available():
            self.deiconify()
            return
        tk.Wm.wm_geometry(self, f"+{OFFSCREEN}+{OFFSCREEN}")
        self.deiconify()
        hwnd = win_frame.frame_hwnd(self)
        cloaked = win_frame.cloak(hwnd, True)
        width, height = self.winfo_width(), self.winfo_height()    # нужный размер (с заголовком — его внутренняя часть)
        self._strip_frame()
        if width > 1 and height > 1:
            win_frame.set_window_rect(hwnd, *self._home, width, height)   # без заголовка окно того же размера
        else:
            win_frame.set_window_rect(hwnd, *self._home)
        self.update()                    # нарисовать всё, пока окно под плащом
        if cloaked:
            self._timers["reveal"] = self.after(REVEAL_MS, self._uncloak)

    def _uncloak(self):
        self._timers.pop("reveal", None)
        win_frame.cloak(win_frame.frame_hwnd(self), False)

    # ── Окно без рамки Windows (шаг 6а.2) ───────────────────────────────────
    def _build_frame_decor(self):
        """Без рамки Windows окно сливается с тёмным рабочим столом: тонкая линия по краям и уголок для растягивания.
        Ещё — заслонка над всем окном (veil): её ставят, когда окно свернули (_on_unmap)."""
        self.veil = tk.Frame(self, bg=C["bg_primary"], bd=0, highlightthickness=0)
        self.edges = []
        for kw in (dict(relx=0, rely=0, relwidth=1, height=1), dict(relx=0, rely=1, relwidth=1, height=1, anchor="sw"),
                   dict(relx=0, rely=0, relheight=1, width=1), dict(relx=1, rely=0, relheight=1, width=1, anchor="ne")):
            edge = tk.Frame(self, bg=C["border"])
            edge.place(**kw)
            edge.lift()
            self.edges.append(edge)
        grip = tk.Canvas(self, width=GRIP_SIZE, height=GRIP_SIZE, bg=C["bg_primary"], highlightthickness=0, bd=0,
                         cursor="size_nw_se" if sys.platform == "win32" else "bottom_right_corner")
        for offset in (3, 7, 11):    # три короткие косые чёрточки
            grip.create_line(GRIP_SIZE - 1, offset, offset, GRIP_SIZE - 1, fill=C["text_muted"])
        grip.place(relx=1, rely=1, anchor="se")
        tk.Misc.tkraise(grip)   # у Canvas tkraise() и lift() поднимают рисунки, а не сам холст
        grip.bind("<ButtonPress-1>", self._grow_start)
        grip.bind("<B1-Motion>", self._grow_move)
        grip.bind("<ButtonRelease-1>", lambda e: setattr(self, "_grow_from", None))
        self.grip = grip
        self._tint_grip()

    def _tint_grip(self):
        """Уголок растягивания лежит поверх страницы: его фон — цвет страницы в этом углу (у мастера правил там футер)."""
        grip = getattr(self, "grip", None)    # при сборке окна страница показывается раньше, чем появляется уголок
        if grip is not None and self.page:
            grip.configure(bg=getattr(self.frames[self.page], "corner_color", C["bg_primary"]))

    def _strip_frame(self):
        """Снять заголовок и рамку Windows (только если стиль правда другой — иначе окно перерисовывалось бы)."""
        if not self._closing:
            hwnd = win_frame.frame_hwnd(self)
            win_frame.strip_caption(hwnd)
            self._round_corners(hwnd)

    def _round_corners(self, hwnd=None):
        """Скруглённые углы, как были с рамкой Windows: Windows 11 — сама (атрибут окна), Windows 10 — вырезаем область
        по размеру окна. Развёрнутое на весь экран окно — прямоугольное."""
        if self._closing or not win_frame.windows_available():
            return
        hwnd = hwnd or win_frame.frame_hwnd(self)
        if self._corners is None:
            self._corners = "dwm" if win_frame.round_corners(hwnd, not self.maximized) else "region"
            if self._corners == "dwm" and win_frame.border_color(hwnd, C["border"]):
                for edge in self.edges:     # Windows 11 рисует тонкую серую рамку сама — своя линия не нужна
                    edge.place_forget()
        elif self._corners == "dwm":
            win_frame.round_corners(hwnd, not self.maximized)
        if self._corners == "region":
            size = (self.winfo_width(), self.winfo_height(), self.maximized)
            if size != self._region_size:
                self._region_size = size
                radius = 0 if self.maximized else round(CORNER_RADIUS * self._get_window_scaling())
                win_frame.region_corners(hwnd, size[0], size[1], radius)

    def window_minimize(self):
        """«Свернуть» — просто свернуть окно (не мини-бар: self.mini не трогаем)."""
        try:
            if sys.platform == "win32":
                self.iconify()
            else:
                self.withdraw()   # без диспетчера окон (виртуальный экран тестов) iconify ждёт его 2 с впустую
        except tk.TclError:
            pass

    def toggle_maximize(self):
        """«Развернуть» на всю свободную часть экрана (без панели задач) и обратно. Размеры — в настоящих пикселях,
        поэтому Tk-геометрия без умножения CustomTkinter на масштаб Windows."""
        if self.maximized:
            self._set_rect(*self._normal_rect)
            self.maximized = False
        else:
            self._normal_rect = (self.winfo_x(), self.winfo_y(), self.winfo_width(), self.winfo_height())
            self._set_rect(*work_area(self))
            self.maximized = True
        self.window_buttons["maximize"].set_icon("copy" if self.maximized else "square")
        self._round_corners()

    def _set_rect(self, x, y, w, h):
        """Место и размер окна в настоящих пикселях. В Windows — сразу Windows (win_frame.set_window_rect: Tk у окна
        без заголовка менял бы размер дважды и делал окно на 16 px шире), иначе — Tk."""
        if not win_frame.set_window_rect(win_frame.frame_hwnd(self), x, y, w, h):
            tk.Wm.wm_geometry(self, f"{w}x{h}+{x}+{y}")

    def _move_start(self, event):
        self._move_from = (event.x_root - self.winfo_x(), event.y_root - self.winfo_y())

    def _move_drag(self, event):
        """Двигаем окно за шапку. Развёрнутое окно сначала возвращает размер, курсор остаётся на том же месте шапки.
        В Windows с первого же сдвига окно дальше ведёт сама Windows (win_frame.drag_window, без следов; сессия 11) —
        с первого сдвига, а не с нажатия: щелчок и двойной щелчок по шапке остаются обычными щелчками Tk.
        Сам Tk окно в Windows не двигает (сессия 11б): его wm geometry у окна без заголовка дважды менял размер окна —
        всё окно раскладывалось и перерисовывалось, это и были 3 с фриза и следы при захвате шапки."""
        if self._move_from is None:
            return
        if self.maximized:
            old_w = max(1, self.winfo_width())
            x, y, w, h = self._normal_rect
            self._move_from = (round(self._move_from[0] * w / old_w), self._move_from[1])
            self._normal_rect = (event.x_root - self._move_from[0], event.y_root - self._move_from[1], w, h)
            self.toggle_maximize()
            return
        if win_frame.drag_window(win_frame.frame_hwnd(self)):
            self._move_from = None
            self.guard.note("перетаскивание окна")
            return
        tk.Wm.wm_geometry(self, f"+{event.x_root - self._move_from[0]}+{event.y_root - self._move_from[1]}")

    def _grow_start(self, event):
        self._grow_from = (event.x_root, event.y_root, self.winfo_width(), self.winfo_height())

    def _grow_move(self, event):
        """Растягиваем за уголок справа внизу; меньше минимума окно не становится."""
        if self._grow_from is None or self.maximized:
            return
        x0, y0, w0, h0 = self._grow_from
        min_w = self._apply_window_scaling(self._min_width)
        min_h = self._apply_window_scaling(self._min_height)
        width = max(round(min_w), w0 + event.x_root - x0)
        height = max(round(min_h), h0 + event.y_root - y0)
        if not win_frame.set_window_rect(win_frame.frame_hwnd(self), width=width, height=height):
            tk.Wm.wm_geometry(self, f"{width}x{height}")

    # ── Полоска слева ───────────────────────────────────────────────────────
    def _build_rail(self):
        rail = light.Frame(self, width=S["rail_width"], fg_color=C["bg_primary"])
        rail.grid(row=0, column=0, sticky="ns")
        rail.pack_propagate(False)

        self.nav = {}
        for name, _page, icon_name, tip_key, _title_key in PAGES:
            button = IconButton(rail, icon_name, kind="nav", tooltip_side="right",
                                tooltip=lambda k=tip_key: theme.plain_text(get_text(self.current_lang, k)),
                                command=lambda n=name: self.select_frame(n))
            button.pack(pady=(12 if not self.nav else 0, 6))
            self.nav[name] = button

        bottom = light.Frame(rail, fg_color="transparent", width=10, height=10)
        # Низ кнопки языка — вровень с низом «Сохранить лог» (футер журнала главной: pady=(0, 12) внутри карточки)
        bottom.pack(side="bottom", pady=(0, S["content_padding"] + 12))
        self.tg_button = DotIconButton(bottom, "send", C["text_muted"], icon_size=18, tooltip_side="right",
                                       tooltip=self._telegram_tip, command=self.open_telegram)
        self.tg_button.pack(pady=(0, 8))
        self.lang_button = Button(bottom, self.current_lang, kind="secondary", height=34, pad_x=4,
                                  fg_color=C["bg_surface"],
                                  hover_color=T["hover_surface"], font=F["label_bold"], command=self.open_language_menu)
        self.lang_button.configure(width=44)
        self.lang_button.pack()
        Tooltip(self.lang_button, lambda: f'{get_text(self.current_lang, "nav_language")}: '
                                          f'{LANGUAGES[self.current_lang]}', side="right")
        self.lang_menu = PopupMenu(self, list(LANGUAGES.values()), self._language_chosen, min_width=96)

    def _telegram_tip(self):
        return get_text(self.current_lang, "nav_tg_on" if self.telegram_on else "nav_tg_off")

    # ── Шапка ───────────────────────────────────────────────────────────────
    def _build_header(self, main):
        header = light.Frame(main, height=S["header_height"], fg_color=C["bg_primary"])
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)
        header.grid_rowconfigure(0, weight=1)
        header.grid_columnconfigure(0, weight=1)
        pad = S["content_padding"]
        self.title_label = light.Label(header, text="", font=F["page_title"], text_color=C["text"], anchor="w")
        self.title_label.grid(row=0, column=0, sticky="w", padx=(pad, 16))
        right = light.Frame(header, fg_color="transparent", width=10, height=10)
        right.grid(row=0, column=1, sticky="e", padx=(0, pad))
        self.plate = DevicePlate(right)
        self.plate.pack(side="left")
        self.header_buttons = {}
        for name, tip_key, command in (("moon", "hdr_tip_sleep", self.sleep_phone),
                                       ("refresh-cw", "hdr_tip_restart", self.restart_scrcpy),
                                       ("maximize-2", "hdr_tip_reset_size", self.reset_window_size)):
            button = IconButton(right, name, icon_size=16, command=command,
                                tooltip=lambda k=tip_key: get_text(self.current_lang, k))
            button.pack(side="left", padx=(8, 0))
            self.header_buttons[name] = button
        tk.Frame(right, width=1, height=24, bg=C["border"]).pack(side="left", padx=12)
        self._build_window_buttons(right)
        for widget in (header, self.title_label, right):    # двигать окно — за пустое место шапки и заголовок
            widget.bind("<ButtonPress-1>", self._move_start, add="+")
            widget.bind("<B1-Motion>", self._move_drag, add="+")
            widget.bind("<ButtonRelease-1>", lambda e: setattr(self, "_move_from", None), add="+")
            widget.bind("<Double-Button-1>", lambda e: self.toggle_maximize(), add="+")

    def _build_window_buttons(self, right):
        """«Свернуть, Развернуть, Закрыть» на одной общей подложке. Наведение — только цвет, иконка не меняется."""
        plate = light.Box(right, corner_radius=S["radius_control"], fg_color=C["bg_surface"], border_width=1,
                          border_color=C["border"], width=10, height=10)
        plate.pack(side="left")
        self.window_buttons = {}
        for name, icon_name, tip, command, hover in (
                ("minimize", "minus", lambda: get_text(self.current_lang, "win_minimize"), self.window_minimize,
                 C["bg_elevated"]),
                ("maximize", "square", lambda: get_text(self.current_lang,
                                                        "win_restore" if self.maximized else "win_maximize"),
                 self.toggle_maximize, C["bg_elevated"]),
                ("close", "x", lambda: get_text(self.current_lang, "win_close"), self.on_close,
                 T["danger_on_surface"])):
            button = IconButton(plate, icon_name, size=30, icon_size=14, command=command, tooltip=tip,
                                fg_color=C["bg_surface"], hover_color=hover, border_width=0,
                                corner_radius=S["radius_control"] - 1)
            button.pack(side="left", padx=2, pady=2)
            self.window_buttons[name] = button

    # ── Страницы и язык ─────────────────────────────────────────────────────
    def select_frame(self, frame_name):
        """Открыть раздел. Уходим из «Мастера правил» с несохранёнными изменениями — сначала «Сохранить изменения?»."""
        if self.page == "rules" and frame_name != "rules":
            self.frames["rules"].ask_leave(lambda: self._show_frame(frame_name))
            return
        self._show_frame(frame_name)

    def _show_frame(self, frame_name):
        """Показать страницу. Видна только она, остальные запаркованы (_park_page: разложены, но не показаны) — сессия 11б.
        Пока Tk по уровням показывает элементы новой страницы, область страниц закрыта заслонкой (curtain): страница
        появляется целиком, а не кусками. Спрятанная страница замирает в своём размере: растягивание окна
        пересчитывает только видимую, остальные — когда их покажут."""
        frame = self.frames[frame_name]
        refresh = getattr(frame, "refresh_data", None)
        if refresh is not None:
            refresh()   # цифры статистики, компоненты, текст руководства, правила с диска — при каждом показе
        previous = self.frames.get(self.page)
        if previous is not frame:
            if previous is not None and self.winfo_viewable():
                self._cover()
            for other in self.frames.values():
                if other is not frame:
                    self._park_page(other)
            self._place_page(frame)
            if self._cover_id is not None or self.curtain.winfo_manager():
                self._uncover_when_ready(self._holder(frame))
            guard = getattr(self, "guard", None)
            if guard is not None:
                guard.note(f"страница {frame_name}")
        self._drop_hidden_focus(frame)
        self.page = frame_name
        self._tint_grip()
        for name, button in self.nav.items():
            button.set_active(name == frame_name)
        self._show_title()

    @staticmethod
    def _holder(frame):
        return getattr(frame, "outer", frame)     # «О программе» — прокрутка: в области страниц лежит её внешняя рамка

    def _pad(self, frame):
        """Отступ страницы — content_padding (у мастера правил его нет: футер во всю ширину)."""
        return 0 if getattr(frame, "full_bleed", False) else light.cpx(self, S["content_padding"])

    def _place_page(self, frame):
        """Показать страницу во всю область страниц (с отступом)."""
        holder = self._holder(frame)
        pad = self._pad(frame)
        if getattr(holder, "_parked", False):
            tk.Place.place_forget(holder)
            holder._parked = False
        tk.Place.place_configure(holder, in_=self.content, x=pad, y=pad, relwidth=1, relheight=1, width=-2 * pad,
                                 height=-2 * pad)

    def _park_page(self, frame):
        """Запарковать страницу: убрать с экрана (Tk прячет её элементы), но оставить разложенной в нынешнем размере —
        внутри рамки parking, которую никогда не показывают. Ещё ни разу не раскладывалась — размер области страниц.
        Разложенная страница строится и меняется без показа (руководство строится заранее, App._prepare)."""
        holder = self._holder(frame)
        if getattr(holder, "_parked", False):
            return
        pad = self._pad(frame)
        width, height = holder.winfo_width(), holder.winfo_height()
        if width <= 1 or height <= 1:
            width = self.content.winfo_width() - 2 * pad
            height = self.content.winfo_height() - 2 * pad
            if width <= 1 or height <= 1:     # окно ещё не разложено — по размеру, который ему задали
                width = self._initial_size[0] - light.cpx(self, S["rail_width"]) - 1 - 2 * pad
                height = self._initial_size[1] - light.cpx(self, S["header_height"]) - 1 - 2 * pad
        if holder.winfo_manager():
            tk.Place.place_forget(holder)
        holder._parked = True
        tk.Place.place_configure(holder, in_=self.parking, x=0, y=0, relwidth=0, relheight=0, width=max(1, width),
                                 height=max(1, height))

    def _cover(self):
        """Заслонка над областью страниц (цвет фона): под ней Tk показывает элементы новой страницы."""
        tk.Place.place_configure(self.curtain, x=0, y=0, relwidth=1, relheight=1)
        tk.Misc.tkraise(self.curtain)

    def _uncover_when_ready(self, holder, started=None):
        """Убрать заслонку, когда Tk показал всё на новой странице (light.still_mapping), но не позже COVER_MAX_MS."""
        if self._cover_id is not None:
            try:
                self.after_cancel(self._cover_id)
            except tk.TclError:
                pass
        self._cover_id = None
        now = time.monotonic()
        started = now if started is None else started
        if not self._closing and light.still_mapping(holder) and (now - started) * 1000 < COVER_MAX_MS:
            self._cover_id = self.after(COVER_CHECK_MS, self._uncover_when_ready, holder, started)
            return
        if self.curtain.winfo_manager():
            tk.Place.place_forget(self.curtain)

    def _prepare(self):
        """Через PREPARE_MS после запуска «Руководство» строится заранее, порциями (build_ahead), — запаркованным: его
        элементы раскладываются, но не показываются, поэтому стройка не нагружает Windows. Сначала спрятанные страницы
        получают размер области страниц: при запуске окно ещё не было разложено."""
        self._timers.pop("prepare", None)
        if self._closing:
            return
        width, height = self.content.winfo_width(), self.content.winfo_height()
        for name, frame in self.frames.items():
            holder = self._holder(frame)
            if name != self.page and getattr(holder, "_parked", False) and width > 1 and height > 1:
                pad = self._pad(frame)
                tk.Place.place_configure(holder, width=max(1, width - 2 * pad), height=max(1, height - 2 * pad))
        for frame in self.frames.values():
            if hasattr(frame, "build_ahead"):
                frame.build_ahead()          # «Руководство» строится в фоне, порциями (ui/guide_page.py)

    def _drop_hidden_focus(self, shown):
        """Фокус ввода остался в поле страницы, которая теперь под другой, — снять: клавиши не должны уходить туда."""
        try:
            widget = self.focus_get()
        except (KeyError, tk.TclError):
            return
        pages = {str(getattr(f, "outer", f)): f for f in self.frames.values()}
        while widget is not None:
            page = pages.get(str(widget))
            if page is not None:
                if page is not shown:
                    self.focus_set()
                return
            widget = widget.master

    def _show_title(self):
        title_key = next(title for name, _p, _i, _t, title in PAGES if name == self.page)
        self.title_label.configure(text=theme.plain_text(get_text(self.current_lang, title_key)))

    def open_language_menu(self):
        button = self.lang_button
        if self.lang_menu.is_open():
            self.lang_menu.close()
            return
        self.lang_menu.open(button.winfo_rootx() + button.winfo_width() + 8, button.winfo_rooty() + button.winfo_height(),
                            anchor="sw")

    def _language_chosen(self, name):
        code = next((code for code, native in LANGUAGES.items() if native == name), None)
        if code:
            self.set_language(code)
            try:
                ui_settings.save(self.settings_path, language=code)
            except OSError as e:
                self.frames["dash"].append_log(f"[ОШИБКА] Не удалось запомнить язык окна: {e}\n")

    def set_language(self, lang, force=False):
        if lang == self.current_lang and not force:
            return
        self.current_lang = lang
        if not force:  # при запуске журнал пустой: язык окна не новость (макет первого запуска)
            self.frames["dash"].append_log(f"[GUI] Язык интерфейса изменен: {LANGUAGES[lang]} ({lang})\n")
        self.title(get_text(lang, "app_title"))
        self.lang_button.configure(text=lang)
        self._show_title()
        self.plate.show(self.phone_connected, lang)
        for frame in self.frames.values():
            if hasattr(frame, "update_language"):
                frame.update_language(lang)
        if self.hud is not None:
            self.hud.set_language(lang)

    # ── События из фоновых потоков ──────────────────────────────────────────
    def log_later(self, text):
        """Строка в журнал из любого потока: окно покажет её при следующем разборе очереди."""
        self.events.put(("log", text))

    def _drain(self):
        self._timers.pop("drain", None)
        if self._closing:
            return
        try:
            for _ in range(200):
                try:
                    kind, value = self.events.get_nowait()
                except queue.Empty:
                    break
                self._handle_event(kind, value)
            self.frames["dash"].flush_log()
            self.frames["rules"].update_bot_state(self.bot_running())
        finally:
            if not self._closing:
                self._timers["drain"] = self.after(DRAIN_MS, self._drain)

    def _handle_event(self, kind, value):
        dash = self.frames["dash"]
        if kind == "log":
            dash.append_log(value)
        elif kind == "phone":
            self.phone_connected = value
            self.plate.show(value, self.current_lang)
            dash.set_phone(value)
        elif kind == "telegram":
            self.telegram_on = value
            self.tg_button.set_dot(C["success"] if value else C["text_muted"])
            dash.set_telegram(value)
        elif kind == "hotkey":
            self.on_hotkey(value)
        else:  # строки и события бота, ответ scrcpy, ответ из Telegram — главной
            dash.on_event(kind, value)

    # ── Кнопки шапки, Telegram, F9/F10 ──────────────────────────────────────
    def sleep_phone(self):
        phone.in_background(phone.sleep_screen, self.log_later)

    def reset_window_size(self):
        phone.in_background(phone.reset_window_size, self.log_later)

    def restart_scrcpy(self):
        """Как «Перезапуск» старой главной, но пауза между остановкой и запуском — через after, окно не замирает."""
        dash = self.frames["dash"]
        dash.append_log("[ADB] Перезапуск scrcpy...\n")
        proc = dash.scrcpy_process
        if proc and proc.poll() is None:
            proc.terminate()
        if "restart" in self._timers:
            self.after_cancel(self._timers.pop("restart"))
        self._timers["restart"] = self.after(RESTART_PAUSE_MS, self._launch_phone)

    def _launch_phone(self):
        self._timers.pop("restart", None)
        self.frames["dash"].launch_phone()

    def open_telegram(self):
        """Настройки Telegram (ответ пользователя 22.10.2026): окно Telegram «Мастера правил» (ui/telegram_window.py),
        сохраняется оно там же, кнопкой «Сохранить настройки»."""
        self.select_frame("rules")
        self.frames["rules"].open_tg_dialog()

    def bot_running(self):
        return self.frames["dash"].bot_running()

    def on_hotkey(self, name):
        """F9 — как кнопка «Пауза» главной (мягкая пауза, снять паузу, «Продолжить» после паузы отладки),
        F10 — как «СТОП»."""
        dash = self.frames["dash"]
        if not self.bot_running():
            dash.append_log(f"[GUI] Нажата {name}, но бот не запущен.\n")
            return
        dash.append_log(f"[GUI] Нажата {name}.\n")
        if name == "F9":
            dash.pause_or_continue()
        elif name == "F10":
            dash.stop_bot()

    # ── Мини-бар (шаг 4) ────────────────────────────────────────────────────
    def enter_mini(self):
        """Свернуть окно в мини-бар под игрой. Только пока бот работает: без него мини-бару нечего показывать."""
        if self._closing or self.mini or not self.bot_running():
            return
        if self.hud is None:
            self.hud = Hud(self, self.current_lang, self.game_locator, self.hud_command)
        self.mini = True
        self.update_hud()
        self.hud.show()
        try:
            if sys.platform == "win32":
                self.iconify()     # кнопка окна остаётся на панели задач
            else:
                self.withdraw()    # в Linux без диспетчера окон (виртуальный экран тестов) iconify ждёт его 2 с впустую
        except tk.TclError:
            pass
        self.frames["dash"].raise_questions()  # открытые окна SOS не прячутся вместе с окном программы

    def leave_mini(self, restore=True):
        """Окно снова целиком, мини-бар прячется. restore=False — окно уже развернули (кнопка на панели задач)."""
        if not self.mini:
            return
        self.mini = False
        if self.hud is not None:
            self.hud.hide()
        if restore and not self._closing:
            try:
                self.deiconify()
                self.lift()
                self.focus_force()
            except tk.TclError:
                pass

    def _on_configure(self, event):
        """Размер окна поменялся — подогнать вырезанные углы (Windows 10; в Windows 11 углы делает сама Windows)."""
        if event.widget is self and self._corners == "region":
            self._round_corners()

    def _on_unmap(self, event):
        """Окно свернули (или спрятали в мини-бар). Tk при этом прячет каждый элемент окна, а при разворачивании
        показывает их снова по одному, по уровням — окно «собиралось» на глазах (сессия 11б). Поэтому сейчас, пока
        окна не видно, над всем окном встаёт заслонка цвета фона (veil): при разворачивании Tk показывает её первой,
        а остальное собирается под ней (_on_map)."""
        if event.widget is not self or self._closing:
            return
        self._cancel_veil()
        tk.Place.place_configure(self.veil, x=0, y=0, relwidth=1, relheight=1)
        tk.Misc.tkraise(self.veil)
        for edge in self.edges:              # линия по краям и уголок — поверх заслонки
            tk.Misc.tkraise(edge)
        tk.Misc.tkraise(self.grip)

    def _on_map(self, event):
        """Окно снова на экране (после сворачивания или мини-бара). Развернули с панели задач, пока оно было в мини-баре, —
        мини-бар больше не нужен. Заслонка уходит, когда Tk показал всё окно, — тогда видимая страница и обновляется,
        как при переходе на неё: за время фарма бот мог запомнить новые правила, а статистика — вырасти."""
        if event.widget is not self:
            return
        self._strip_frame()     # Tk мог вернуть рамку после сворачивания
        if self.mini and self.state() == "normal":
            self.leave_mini(restore=False)
        if self.veil.winfo_manager():
            self.guard.note("разворачивание окна")
            self._cancel_veil()
            self._lift_veil_when_ready()
        else:
            self._refresh_shown()

    def _lift_veil_when_ready(self, started=None):
        self._veil_id = None
        now = time.monotonic()
        started = now if started is None else started
        if self._closing:
            return
        if light.still_mapping(self) and (now - started) * 1000 < COVER_MAX_MS:
            self._veil_id = self.after(COVER_CHECK_MS, self._lift_veil_when_ready, started)
            return
        tk.Place.place_forget(self.veil)
        self._refresh_shown()

    def _cancel_veil(self):
        if self._veil_id is not None:
            try:
                self.after_cancel(self._veil_id)
            except tk.TclError:
                pass
            self._veil_id = None

    def _refresh_shown(self):
        refresh = getattr(self.frames.get(self.page), "refresh_data", None)
        if refresh is not None and not self._closing:
            refresh()

    def update_hud(self):
        if self.mini and self.hud is not None:
            self.hud.render(self.frames["dash"].hud_view())

    def hud_command(self, name):
        """Кнопки мини-бара — те же действия, что кнопки главной и шапки."""
        dash = self.frames["dash"]
        if name == "pause":
            dash.pause_or_continue()
        elif name == "sos":
            dash.raise_questions(open_missing=True)
        elif name == "stop":
            dash.stop_bot()
        elif name == "sleep":
            self.sleep_phone()
        elif name == "expand":
            self.leave_mini()

    def dialog_area(self):
        """По центру чего ставить окна SOS, пока окно программы в мини-баре: картинка игры (или None)."""
        return self.hud.game_area() if self.hud is not None else None

    # ── Закрытие ────────────────────────────────────────────────────────────
    def on_close(self):
        """Крестик окна. Бот работает — сначала вопрос (ответ пользователя 22.10.2026), иначе закрываем сразу."""
        if self._closing:
            return
        if self.frames["rules"].dirty():
            # Несохранённые настройки мастера правил — сначала «Сохранить изменения?» (ваш ответ 22.10.2026)
            if self.state() != "normal":
                self.deiconify()
            self.frames["rules"].ask_leave(self._close_after_rules)
            return
        self._close_after_rules()

    def _close_after_rules(self):
        if self._closing:
            return
        if not self.bot_running():
            self.shutdown()
            return
        if self._close_dialog is not None and self._close_dialog.winfo_exists():
            self._close_dialog.lift()
            return
        if self.state() != "normal":
            self.deiconify()  # окно подтверждения привязано к главному: у свёрнутого окна его не видно
        lang = self.current_lang
        self._close_dialog = ConfirmDialog(self, get_text(lang, "close_bot_title"), get_text(lang, "close_bot_text"),
                                           get_text(lang, "close_bot_ok"), on_confirm=self.shutdown, kind="warning",
                                           lang=lang, confirm_kind="danger_solid", confirm_icon="square-filled")

    def shutdown(self):
        """Остановить всё своё и закрыть окно: процесс программы после этого выходит сам."""
        if self._closing:
            return
        self._closing = True
        self.guard.stop()
        self.status.stop()
        self.hotkeys.stop()
        for after_id in self._timers.values():
            try:
                self.after_cancel(after_id)
            except tk.TclError:
                pass
        self._timers.clear()
        self._cancel_veil()
        if self._cover_id is not None:
            try:
                self.after_cancel(self._cover_id)
            except tk.TclError:
                pass
            self._cover_id = None
        Toast.close_all(self)
        if self.hud is not None:
            self.hud.destroy()
        try:
            self.withdraw()  # окно пропадает сразу; остановка бота и scrcpy — до 2 с на каждый
        except tk.TclError:
            pass
        try:
            self.frames["dash"].shutdown_processes()
        except Exception as e:
            print(f"[GUI] Не удалось остановить бота или scrcpy: {e}", file=sys.__stderr__)
        self.destroy()


def run():
    ctk.set_appearance_mode("Dark")
    app = App()
    app.mainloop()
