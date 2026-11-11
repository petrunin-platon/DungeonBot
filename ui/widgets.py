"""Общие виджеты нового интерфейса (задача 15, шаг 1): то, из чего собираются все экраны.

Card — карточка; Button — кнопка нужного вида (второстепенная, синяя, сохранить, «Начать фарм», опасная);
IconButton — квадратная кнопка с иконкой (шапка, сайдбар, мини-бар); Tooltip — подсказка при наведении;
TitanAvatar — квадрат титана цветом стихии (TitanTile — то же одной картинкой, для длинных списков);
Chip — фильтр-«таблетка»; Field — поле ввода с подписью и состояниями;
Switch — тумблер, Dropdown — выпадающий список (шаг 5а, мастер правил);
DialogBody / ConfirmDialog — подтверждение опасного действия; ToastBody / Toast — короткое уведомление.

Цвета, шрифты и размеры — только из ui/theme.py, иконки — ui/icons. Надписи передаёт тот, кто создаёт виджет (из i18n.py).
Виджеты трогаем только из главного потока Tk.

С сессии 11 внутри нет ни одного элемента CustomTkinter (ui/light.py): кнопка, таблетка, карточка — по одному окну Windows
(холст Tk с готовыми уголками), а не рамка, холст и надписи с рисованием скруглений кодом Python при каждом изменении размера.
Снаружи всё как было: те же классы, аргументы и методы. Окна (AppWindow) — по-прежнему CTkToplevel.

Чтобы окно в Windows не зависало (на этом уже обжигались):
- обработчики наведения (<Enter>/<Leave>) меняют только цвета и только если вид правда поменялся. Шрифт, текст и картинку
  в них не трогаем: CustomTkinter при этом убирает и заново ставит часть виджета под мышкой, Windows снова шлёт
  «мышь вошла» — и окно крутится в этом круге;
- никаких вложенных ожиданий (wait_visibility, wait_window): окно подтверждения ждёт показа через after;
- окошки без рамки (подсказка, уведомление) — обычные окна Tk, без особых режимов Windows (прозрачный цвет);
- никаких update_idletasks() в обработчиках: он доделывает всю отложенную работу окна сразу (раскладку всех страниц) —
  в руководстве так набегали фризы по 6 с. Размер нового окошка — из нужного размера надписей или после after_idle.
"""
import tkinter as tk
from functools import lru_cache

import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk

from i18n import get_text
from ui import light, theme
from ui import win_frame
from ui.icons import dot, icon
from ui.light import px, scaled_font, shared_photo, surface, text_width

C = theme.COLORS
T = theme.TINTS
F = theme.FONTS
S = theme.SIZES

# Уголки окошек без рамки: в цвет фона окна программы, поэтому скругление карточки внутри не видно как «квадрат»
_CORNER_COLOR = C["bg_primary"]


def _frameless_window(root, inactive=False):
    """Окошко без рамки поверх окна программы (не поверх всех окон: иначе оно может попасть на снимок игры).
    inactive — окошко не берёт фокус и не принимает нажатия (подсказка): окно программы не теряет активность."""
    top = tk.Toplevel(root)
    top.withdraw()
    top.overrideredirect(True)
    top.configure(bg=_CORNER_COLOR)
    top.transient(root)
    if inactive:
        try:
            top.wm_attributes("-disabled", True)  # есть только в Windows
        except tk.TclError:
            pass
    return top


POPUP_RADIUS = 8         # скругление углов всплывающих окон без рамки (как у главного окна, CORNER_RADIUS)
SHOW_DELAY_MS = 50       # окно показывается не сразу: даём окну достроиться (см. present_window)


class AppWindow(light.OwnEvents, light.NoAlpha, ctk.CTkToplevel):
    """Окно нового интерфейса (шаг 6а.1). CustomTkinter не перекрашивает заголовок: он прятал окно, вызывал update()
    и через 5 мс возвращал «как было» — окно, показанное в этот миг, пропадало, а захват мыши оставался у невидимого
    окна, и программа не отвечала на щелчки. Заголовок красит present_window (ui/win_frame.py), без withdraw и update."""
    _deactivate_windows_window_header_manipulation = True
    frameless = True         # шаг 6а.3: рамку Windows снимает present_window, вместо неё — шапка окна с крестиком

    def decorate(self):
        """Тонкая линия 1 px по краям: без рамки Windows окно сливается с фоном (как у главного окна, шаг 6а.2).
        Один раз; зовёт present_window, когда содержимое уже построено."""
        if not getattr(self, "_edges", None):
            self._edges = edge_lines(self)

    def make_movable(self, *roots):
        """Двигать окно за шапку: за сами рамки и их надписи, но не за кнопки и поля ввода."""
        def bind(widget):
            if isinstance(widget, (light.Button, light.Entry, light.Textbox, light.CheckBox, light.SegmentedButton,
                                   PlainSwitch, PlainIconButton, PlainClickFrame, ClickFrame, tk.Entry, tk.Text)):
                return
            widget.bind("<ButtonPress-1>", self._move_start, add="+")
            widget.bind("<B1-Motion>", self._move_drag, add="+")
            for child in widget.winfo_children():
                bind(child)
        for root in roots:
            bind(root)

    def _set_scaling(self, new_widget_scaling, new_window_scaling):
        """Окно переехало на экран с другим масштабом Windows (сессия 11б). CustomTkinter растягивал само окно — его
        прежний размер × новый масштаб, да ещё с жёсткими min/max, — а лёгкие элементы внутри (ui/light.py) нарисованы
        под масштаб при создании и не меняются: окно становилось шире, кнопки не помещались, и дальше окно уже
        не подгонялось под содержимое. Оставляем окно как есть: его размер задаёт содержимое."""

    def _move_start(self, event):
        self._move_from = (event.x_root - self.winfo_x(), event.y_root - self.winfo_y())

    def _move_drag(self, event):
        """В Windows с первого сдвига окно ведёт сама Windows (win_frame.drag_window, сессия 11), сам Tk окно не двигает:
        у окна без рамки его wm geometry дважды менял размер окна (сессия 11б). Вне Windows двигает Tk."""
        origin = getattr(self, "_move_from", None)
        if origin is None:
            return
        if win_frame.drag_window(win_frame.frame_hwnd(self)):
            self._move_from = None
            return
        tk.Wm.wm_geometry(self, f"+{event.x_root - origin[0]}+{event.y_root - origin[1]}")   # настоящие пиксели

    def strip_frame(self):
        """Снять заголовок, рамку и объёмные края Windows (только если стиль другой) и скруглить углы.
        Вне Windows ничего не делает."""
        win_frame.strip_caption(win_frame.frame_hwnd(self))
        round_window(self, getattr(self, "_edges", ()), self._get_window_scaling())


def edge_lines(window):
    """Линия 1 px цвета C["border"] по четырём краям окна без рамки (поверх содержимого)."""
    edges = []
    for kw in (dict(relx=0, rely=0, relwidth=1, height=1), dict(relx=0, rely=1, relwidth=1, height=1, anchor="sw"),
               dict(relx=0, rely=0, relheight=1, width=1), dict(relx=1, rely=0, relheight=1, width=1, anchor="ne")):
        edge = tk.Frame(window, bg=C["border"])
        edge.place(**kw)
        edge.lift()
        edges.append(edge)
    return edges


def round_window(window, edges=(), scale=1.0):
    """Скруглить углы окна без рамки (всплывающие окна и списки). Windows 11 — атрибутом окна, и тогда тонкую рамку
    рисует сама Windows, цветом C["border"] (свои линии edges убираются); Windows 10 — вырезанной областью по размеру
    окна (подгоняется на <Configure>). Вне Windows ничего не делает. scale — масштаб Windows для радиуса."""
    hwnd = win_frame.frame_hwnd(window)
    rounded = win_frame.round_corners(hwnd)
    if rounded and win_frame.border_color(hwnd, C["border"]):
        for edge in edges:
            edge.place_forget()
    elif not rounded and win_frame.windows_available():
        if not getattr(window, "_region_bound", False):
            window._region_bound = True
            window.bind("<Configure>", lambda _e: _region_corners(window, scale), add="+")
        _region_corners(window, scale)


def _region_corners(window, scale):
    size = (window.winfo_width(), window.winfo_height())
    if size != getattr(window, "_region_size", None):
        window._region_size = size
        win_frame.region_corners(win_frame.frame_hwnd(window), size[0], size[1], round(POPUP_RADIUS * scale))


def close_button(master, command, lang, bg):
    """Крестик в шапке окна без рамки Windows (как в «Новом правиле»): делает то же, что делал крестик Windows."""
    return IconButton(master, "x", size=32, icon_size=16, fg_color=bg, bg_color=bg, hover_color=C["bg_elevated"],
                      border_width=0, tooltip=lambda: get_text(lang, "win_close"), command=command)


def hold_grab(window, blocked=lambda: False, on_grab=None, tries=20):
    """Сделать окно модальным, но только пока оно видно. Захват берётся, когда окно на экране (без wait_visibility:
    в Windows он может не дождаться события и держать вложенный цикл); окно спрятали (<Unmap>) — захват отпускается,
    показали снова (<Map>) — берётся опять. Невидимое окно не держит мышь: раньше окно пропадало, а программа
    переставала отвечать на щелчки. blocked() — пока True, окно захват не берёт (закрыто, или открыт «Собери состав»).
    on_grab() — после того, как захват взят (например, поставить фокус). Возвращает функцию «взять захват сейчас»:
    она ждёт показа окна до tries · 50 мс."""
    def take(left=0):
        try:
            if blocked():
                return
            if window.winfo_viewable():
                window.grab_set()
                if on_grab:
                    on_grab()
            elif left > 0:
                window.after(50, take, left - 1)
        except tk.TclError:
            pass

    def on_unmap(event):
        if event.widget is window:
            try:
                window.grab_release()
            except tk.TclError:
                pass

    def on_map(event):
        if event.widget is window:
            take()

    window.bind("<Unmap>", on_unmap, add="+")
    window.bind("<Map>", on_map, add="+")
    return lambda: take(tries)


def present_window(window, place, hidden=lambda: False, on_shown=None):
    """Показать готовое окно (CTkToplevel): place() ставит размер и место, потом окно появляется сверху.

    Окно нового интерфейса — AppWindow: CustomTkinter не прячет его для перекраски заголовка (шаг 6а.1), поэтому
    показанное окно уже не пропадает. Заголовок красим мы, один раз после показа. Ожидание флага перекраски
    CustomTkinter оставлено: у обычного CTkToplevel (старые окна) оно по-прежнему нужно. Через 0,3 с проверяем,
    что окно правда на экране. hidden() — окно закрыли или спрятали нарочно: тогда не показываем."""
    def attempt(left):
        if hidden():
            return
        try:
            if getattr(window, "_windows_set_titlebar_color_called", False) and left > 0:
                window.after(20, attempt, left - 1)
                return
            in_mini = _detach_from_hidden_owner(window)
            frameless = getattr(window, "frameless", False)
            if frameless:
                window.decorate()
                window.strip_frame()
                window.bind("<Map>", lambda e: e.widget is window and window.strip_frame(), add="+")  # Tk мог вернуть рамку
            place()
            window.deiconify()
            window.lift()
            if in_mini:
                bring_to_front(window)
            window.focus_set()
            if frameless:
                window.focus_force()    # без рамки Windows окно само фокус не берёт — поля ввода не принимали бы клавиши
            else:
                win_frame.paint_title_dark(window)
            window.after(300, check, 3)
        except tk.TclError:
            return
        if on_shown:
            on_shown()

    def check(left):
        if hidden():
            return
        try:
            if window.state() == "withdrawn" and left > 0:
                window.deiconify()
                window.lift()
                window.after(300, check, left - 1)
        except tk.TclError:
            pass

    try:
        window.after(SHOW_DELAY_MS, attempt, 100)
    except tk.TclError:
        pass


def _app_of(widget):
    """Окно программы (ui/app.py: App), к которому относится виджет или окно, или None."""
    while widget is not None and not hasattr(widget, "mini"):
        widget = getattr(widget, "master", None)
    return widget


def _detach_from_hidden_owner(window):
    """Окно программы свёрнуто в мини-бар (шаг 4): окно, привязанное к нему (transient), Windows прячет вместе с ним.
    Тогда окно (SOS, «Собери состав») отвязывается и показывается само по себе над игрой (ваш ответ 22.10.2026).
    Возвращает True, если окно программы сейчас в мини-баре."""
    app = _app_of(window)
    if app is None or not app.mini:
        return False
    if window.master is app:
        try:
            window.wm_transient("")
        except tk.TclError:
            pass
    return True


def bring_to_front(window, hold_ms=400):
    """Поднять окно над всеми (над окном игры тоже) на миг и отпустить: окно SOS при свёрнутом окне программы
    иначе могло бы открыться под игрой. Поверх всех оно не остаётся."""
    try:
        window.lift()
        window.attributes("-topmost", True)
        window.after(hold_ms, lambda: window.winfo_exists() and window.attributes("-topmost", False))
    except tk.TclError:
        pass


def show_over_game(window):
    """Показать окно (SOS, «Собери состав») и поднять над всеми: кнопка мини-бара на SOS. В мини-баре окно
    отвязывается от свёрнутого окна программы, иначе Windows прячет его вместе с ним."""
    try:
        _detach_from_hidden_owner(window)
        if window.state() != "normal":
            window.deiconify()
        bring_to_front(window)
    except tk.TclError:
        pass


def anchor_area(root):
    """(x, y, ширина, высота): по центру чего ставить окно. Обычно — окно программы; свёрнуто в мини-бар —
    картинка игры (App.dialog_area), а если её не видно — весь экран."""
    app = _app_of(root)
    if app is not None and app.mini:
        area = app.dialog_area()
        if area:
            return area
        return 0, 0, root.winfo_screenwidth(), root.winfo_screenheight()
    return root.winfo_rootx(), root.winfo_rooty(), root.winfo_width(), root.winfo_height()


def requested_size(window):
    """Нужный размер окна (ширина, высота) по его содержимому. Tk считает его в своей очереди «потом», а окна мы
    показываем через after или after_idle — к этому времени размер уже есть. Запасной путь (размера ещё нет) —
    update_idletasks: он доделывает всю отложенную работу окна программы, поэтому только тут и только если нужно."""
    w, h = window.winfo_reqwidth(), window.winfo_reqheight()
    if w <= 1 or h <= 1:
        window.update_idletasks()
        w, h = window.winfo_reqwidth(), window.winfo_reqheight()
    return w, h


def _pointer_inside(widget):
    """Мышь над виджетом (или над его частями: у кнопок CustomTkinter внутри несколько виджетов)."""
    try:
        x, y = widget.winfo_pointerxy()
        left, top = widget.winfo_rootx(), widget.winfo_rooty()
        return left <= x < left + widget.winfo_width() and top <= y < top + widget.winfo_height()
    except tk.TclError:
        return False


class Card(light.Box):
    """Карточка: фон bg_surface, рамка 1 px, скругление 10 (один холст Tk, ui/light.py)."""

    def __init__(self, master, fg_color=None, border_color=None, corner_radius=None, **kwargs):
        kwargs.setdefault("width", 10)
        kwargs.setdefault("height", 10)
        super().__init__(master, fg_color=fg_color or C["bg_surface"], border_width=1,
                         border_color=border_color or C["border"],
                         corner_radius=S["radius_card"] if corner_radius is None else corner_radius, **kwargs)


# Виды кнопок (design/README.md, «Компоненты»). icon — цвет иконки, disabled — цвет текста неактивной кнопки
BUTTON_KINDS = {
    "secondary": dict(fg_color=C["bg_elevated"], hover_color=T["hover_elevated"], border_width=1,
                      border_color=C["border"], text_color=C["text"], font=F["button"], icon=C["text_secondary"]),
    "blue": dict(fg_color=C["blue_button"], hover_color=T["hover_blue"], border_width=0,
                 text_color=C["white"], font=F["button_bold"], icon=C["white"]),
    "save": dict(fg_color=C["green_button"], hover_color=T["hover_green_button"], border_width=0,
                 text_color=C["white"], font=F["button_bold"], icon=C["white"]),
    "cta": dict(fg_color=C["green"], hover_color=C["green_hover"], border_width=0,
                text_color=C["white"], font=F["cta"], icon=C["white"]),
    "danger": dict(fg_color="transparent", hover_color=T["danger_badge_bg"], border_width=1,
                   border_color=C["danger"], text_color=C["danger_text"], font=F["button"], icon=C["danger_text"]),
    "danger_solid": dict(fg_color=C["danger_button"], hover_color=T["hover_danger_button"], border_width=0,
                         text_color=C["white"], font=F["button_bold"], icon=C["white"]),
    "ghost_danger": dict(fg_color="transparent", hover_color=C["bg_elevated"], border_width=0,
                         text_color=C["danger_text"], font=F["button"], icon=C["danger_text"]),
    "ghost": dict(fg_color="transparent", hover_color=C["bg_elevated"], border_width=0,
                  text_color=C["text_secondary"], font=F["button"], icon=C["text_secondary"]),
    "link": dict(fg_color="transparent", hover_color=C["bg_surface"], border_width=0,
                 text_color=C["blue_text"], font=F["button"], icon=C["blue_text"]),
}


class Button(light.Button):
    """Кнопка с текстом нужного вида (BUTTON_KINDS). Ширина — по надписи: длинные немецкие тексты не обрезаются.
    icon_name — иконка слева (имя файла из ui/icons), compound="right" — справа от надписи («RU ▾»).
    set_kind() меняет вид (пауза и стоп становятся яркими во время фарма). Один холст Tk (ui/light.py)."""

    def __init__(self, master, text="", kind="secondary", icon_name=None, icon_size=16, command=None, height=None,
                 pad_x=14, compound="left", **kwargs):
        self._kind = kind
        self._icon_name = icon_name
        self._icon_size = icon_size
        style = dict(BUTTON_KINDS[kind])
        icon_color = style.pop("icon")
        style.update(kwargs)
        height = height or (S["cta_height"] if kind == "cta" else S["control_height"])
        super().__init__(master, text=text, command=command, height=height, width=0,
                         corner_radius=S["radius_control"] if kind != "cta" else 8, border_spacing=2,
                         text_color_disabled=C["text_muted"], compound=compound, pad_x=pad_x,
                         image=icon(icon_name, icon_color, icon_size) if icon_name else None, **style)

    def set_kind(self, kind):
        changed = kind != self._kind
        self._kind = kind
        style = dict(BUTTON_KINDS[kind])
        icon_color = style.pop("icon")
        if not changed:
            # Тот же вид (кнопку просто выключили или включили): шрифт не трогаем — ширина кнопки та же
            style.pop("font")
        disabled = self.cget("state") == "disabled"
        if disabled:
            # Неактивная кнопка бледная (экран 4: «Внедрить золотые правила», пока нечего внедрять)
            icon_color = C["text_muted"]
            if style["fg_color"] != "transparent":
                style["fg_color"] = theme.blend(style["fg_color"], C["bg_surface"], 0.3)
            if style.get("border_width"):
                style["border_color"] = theme.blend(style["border_color"], C["bg_surface"], 0.4)
        if self._icon_name:
            style["image"] = icon(self._icon_name, icon_color, self._icon_size)
        self.configure(**style)

    def set_icon(self, icon_name):
        self._icon_name = icon_name
        self.set_kind(self._kind)

    def set_enabled(self, enabled):
        self.configure(state="normal" if enabled else "disabled")
        self.set_kind(self._kind)


class IconButton(light.Button):
    """Квадратная кнопка с иконкой: шапка (34 px), сайдбар (44 px, kind="nav"), док-плеер (38 px).
    tooltip — подсказка при наведении (у кнопок без текста она обязательна). set_active() — выбранный пункт сайдбара.
    Один холст Tk (ui/light.py): наведение меняет только цвет заливки."""

    def __init__(self, master, icon_name, command=None, size=None, icon_size=None, tooltip=None, tooltip_side="bottom",
                 kind="default", icon_color=None, **kwargs):
        self._icon_name = icon_name
        self._kind = kind
        self._icon_size = icon_size or (S["icon_nav"] if kind == "nav" else S["icon"])
        self._icon_color = icon_color
        self._active = False
        self._state = "normal"
        size = size or (S["rail_button"] if kind == "nav" else S["header_button"])
        if kind == "nav":
            style = dict(fg_color="transparent", hover_color=T["hover_primary"], border_width=1,
                         border_color=C["bg_primary"], corner_radius=8)
        else:
            style = dict(fg_color=C["bg_surface"], hover_color=C["bg_elevated"], border_width=1,
                         border_color=C["border"], corner_radius=S["radius_control"])
        style.update(kwargs)
        super().__init__(master, text="", width=size, height=size, border_spacing=0, command=command,
                         image=self._icon_image(), **style)
        self.tooltip = Tooltip(self, tooltip, side=tooltip_side) if tooltip else None

    def _icon_image(self):
        if getattr(self, "_state", "normal") == "disabled":
            color = C["text_muted"]
        elif self._kind == "nav":
            color = C["blue_text"] if self._active else C["text_secondary"]
        else:
            color = self._icon_color or C["text_secondary"]
        return icon(self._icon_name, color, self._icon_size)

    def set_active(self, active):
        """Выбранный пункт сайдбара: синеватый фон, синяя рамка и иконка."""
        self._active = active
        self.configure(fg_color=T["nav_active_bg"] if active else "transparent",
                       border_color=T["nav_active_border"] if active else C["bg_primary"],
                       hover_color=T["nav_active_bg"] if active else T["hover_primary"], image=self._icon_image())

    def set_icon(self, icon_name, color=None):
        self._icon_name = icon_name
        if color:
            self._icon_color = color
        self.configure(image=self._icon_image())

    def set_enabled(self, enabled):
        self.configure(state="normal" if enabled else "disabled")
        self.configure(image=self._icon_image())


class Tooltip:
    """Подсказка при наведении: маленькое окошко без рамки рядом с виджетом (справа для сайдбара, снизу для шапки).
    text — строка или функция без аргументов (тогда подсказка всегда на текущем языке)."""

    def __init__(self, widget, text, side="bottom", delay=None):
        self.widget = widget
        self.text = text
        self.side = side
        self.delay = S["tooltip_delay_ms"] if delay is None else delay
        self._after_id = None
        self._leave_id = None
        self._top = None
        self.attach(widget)
        widget.bind("<Destroy>", self._hide, add="+")  # виджет убрали, пока подсказка видна, — убрать и её

    def attach(self, widget):
        """Показывать подсказку и над этим виджетом (например, над картинкой внутри квадрата титана)."""
        widget.bind("<Enter>", self._on_enter, add="+")
        widget.bind("<Leave>", self._on_leave, add="+")
        widget.bind("<ButtonPress>", self._hide, add="+")

    def _current_text(self):
        return self.text() if callable(self.text) else self.text

    def _on_enter(self, _event=None):
        self._cancel_leave()
        if self._top is None and self._after_id is None:
            try:
                self._after_id = self.widget.after(self.delay, self._show)
            except tk.TclError:
                pass

    def _on_leave(self, _event=None):
        # Мышь могла перейти на часть того же виджета: проверяем чуть позже, где она (одна проверка, не очередь)
        self._cancel_leave()
        try:
            self._leave_id = self.widget.after(30, self._hide_if_outside)
        except tk.TclError:
            pass

    def _hide_if_outside(self):
        self._leave_id = None
        if not _pointer_inside(self.widget):
            self._hide()

    def _cancel_leave(self):
        if self._leave_id:
            try:
                self.widget.after_cancel(self._leave_id)
            except tk.TclError:
                pass
            self._leave_id = None

    def _cancel(self):
        if self._after_id:
            try:
                self.widget.after_cancel(self._after_id)
            except tk.TclError:
                pass
            self._after_id = None

    def _show(self):
        self._after_id = None
        text = self._current_text()
        if not text or self._top is not None or not _pointer_inside(self.widget):
            return
        top = _frameless_window(self.widget.winfo_toplevel(), inactive=True)
        label = light.Label(top, text=text, font=F["label"], text_color=C["text"], fg_color=C["bg_elevated"],
                            bg_color=_CORNER_COLOR, corner_radius=S["radius_control"], height=26, padx=8)
        label.pack()
        # Размер — у самой надписи (Tk знает его сразу): без update_idletasks, который доделал бы всю отложенную
        # работу окна (раскладку страниц) — так подсказка однажды запустила фриз руководства на 6 с
        w, h = label.winfo_reqwidth(), label.winfo_reqheight()
        wx, wy = self.widget.winfo_rootx(), self.widget.winfo_rooty()
        ww, wh = self.widget.winfo_width(), self.widget.winfo_height()
        gap = 8
        if self.side == "right":
            x, y = wx + ww + gap, wy + (wh - h) // 2
        elif self.side == "top":
            x, y = wx + (ww - w) // 2, wy - h - gap
        else:
            x, y = wx + (ww - w) // 2, wy + wh + gap
        screen_w = top.winfo_screenwidth()
        x = max(0, min(x, screen_w - w))
        top.geometry(f"{w}x{h}+{x}+{max(0, y)}")
        top.deiconify()
        self._top = top

    def _hide(self, _event=None):
        self._cancel()
        self._cancel_leave()
        if self._top is not None:
            try:
                self._top.destroy()
            except tk.TclError:
                pass
            self._top = None


@lru_cache(maxsize=64)
def _titan_pixels(key, stamp):
    """Картинка титана целиком (PIL, RGBA) или None, если она не читается (битый файл или assets_db.py): тогда в квадрате
    две буквы имени, а окно не падает. Читается один раз на картинку, а не по разу на каждый размер квадрата.
    key и stamp — из theme.titan_icon_source (отметка — время изменения: заменённая картинка перечитается)."""
    try:
        with theme.open_titan_icon(key) as img:
            return img.convert("RGBA")
    except Exception:
        return None


def titan_source(titan):
    """(ключ, отметка) картинки титана — из папки assets/icons или из assets_db.py, — если она читается;
    иначе None, и в квадрате две буквы имени."""
    source = theme.titan_icon_source(titan)
    if source is not None and _titan_pixels(*source) is not None:
        return source
    return None


def _square_picture(key, stamp, side, radius):
    """Квадрат side × side пикселей из середины картинки титана, углы скруглены радиусом radius (PIL, RGBA)."""
    pic = _titan_pixels(key, stamp)
    edge = min(pic.size)
    left, top = (pic.width - edge) // 2, (pic.height - edge) // 2
    pic = pic.crop((left, top, left + edge, top + edge)).resize((side, side), Image.LANCZOS)
    mask = Image.new("L", (side, side), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, side - 1, side - 1), radius=radius, fill=255)
    pic.putalpha(Image.composite(pic.getchannel("A"), mask, mask))
    return pic


def titan_name(lang, titan):
    """Имя титана на языке окна; новый титан без перевода — по имени файла."""
    name = get_text(lang, f"titan_{titan}")
    return titan.capitalize() if name == f"titan_{titan}" else name


class TitanAvatar(light.Scaled, tk.Label):
    """Квадрат титана: рамка цветом стихии, фон — оттенок стихии, внутри картинка assets/icons/<титан>.png
    или две буквы имени, пока картинки нет. Подсказка с именем при наведении. command(titan) — по клику.
    С сессии 11 — одна надпись Tk с готовой картинкой (как TitanTile), а не рамка и надпись CustomTkinter;
    self.label — она же (картинка и две буквы — у self.label, как раньше)."""

    def __init__(self, master, titan, lang="RU", size=None, command=None, tooltip=True, bg_color=None, **kwargs):
        self.titan = titan
        self.lang = lang
        self.size = size or S["avatar"]
        self.command = command
        self._bg_color = bg_color
        self._outer = surface(master) if light.transparent(bg_color) else bg_color
        self._dim = False
        super().__init__(master, bd=0, highlightthickness=0, padx=0, pady=0, compound="center", bg=self._outer)
        self.label = self
        self.tooltip = Tooltip(self, lambda: titan_name(self.lang, self.titan)) if tooltip else None
        self.bind("<Button-1>", self._on_click, add="+")
        self._render()

    def _render(self):
        scale = light.scale_of(self)
        side = round(self.size * scale)
        source = titan_source(self.titan)
        args = (self.titan, side, max(1, round(S["avatar_border"] * scale)), self._outer,
                round(S["radius_control"] * scale), round(4 * scale), self._dim) + (source or (None, 0))
        self.photo = shared_photo(self, ("avatar",) + args, lambda: _avatar_picture(*args))
        text = "" if source else theme.initials(titan_name(self.lang, self.titan))
        color = C["text_muted"] if self._dim else C["text"]
        font = (theme.FONT_FAMILY, -round((12 if self.size >= 32 else 10) * scale), "bold")
        self.configure(image=self.photo, text=text, fg=color, font=font, bg=self._outer)

    def _on_click(self, _event=None):
        if self.command:
            self.command(self.titan)

    def _follow_surface(self, color):
        if light.transparent(self._bg_color) and color != self._outer:
            self._outer = color
            self._render()

    def set_language(self, lang):
        self.lang = lang
        self._render()

    def set_titan(self, titan):
        if titan != self.titan:
            self.titan = titan
            self._render()

    def set_dim(self, dim):
        """Бледный квадрат: титана нельзя выбрать (чужая стихия, уже выбрано 5). Только картинка — без перестройки."""
        if dim != self._dim:
            self._dim = dim
            self._render()


@lru_cache(maxsize=256)
def _avatar_picture(titan, side, border, bg, radius, inner_radius, dim, key, stamp):
    """Квадрат титана как у прежнего TitanAvatar (PIL): рамка цветом стихии толщиной border и скруглением radius,
    фон — оттенок стихии, внутри картинка титана (inner_radius) с отступом в 1 px от рамки. dim — бледные рамка и фон
    (картинка — как была)."""
    style = theme.element_style(theme.element_of(titan))
    color, tint = style["color"], style["tint"]
    if dim:
        color = theme.blend(color, C["bg_surface"], 0.4)
        tint = theme.blend(tint, C["bg_surface"], 0.4)
    k = 4
    big = side * k
    img = Image.new("RGBA", (big, big), _rgb(bg) + (255,))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, big - 1, big - 1), radius=radius * k, fill=_rgb(tint) + (255,),
                                          outline=_rgb(color) + (255,), width=border * k)
    if key:
        inner = side - 2 * border - 2
        pic = _square_picture(key, stamp, inner * k, inner_radius * k)
        offset = (big - inner * k) // 2
        img.alpha_composite(pic, (offset, offset))
    return img.resize((side, side), Image.LANCZOS)


# ── Лёгкие элементы для длинных прокручиваемых списков (мастер правил, проверка шага 5а) ─────────────────
# У каждой надписи и рамки CustomTkinter внутри свой холст: в Windows при прокрутке и раскрытии списка каждый
# перерисовывается отдельно, и элементы дорисовывались с заметной задержкой. В повторяющихся строках — обычные
# надписи и рамки Tk: цвет фона задаём сами (bg — цвет того, на чём они стоят), размер шрифта — с масштабом Windows.
# px, scaled_font, shared_photo, text_width — из ui/light.py (импортированы вверху, по старым именам).
class PopupMenu:
    """Свой выпадающий список вместо меню Windows (шаг 6а.3, дополнение). У меню Windows своя светлая рамка в 3 px
    (серая линия и две белые), перекрасить её из Tk нельзя — на тёмном окне это белая полоса (скриншот пользователя,
    выбор языка). Здесь — окошко без рамки (как подсказка) в цветах поля ввода: по краям линия 1 px C["border"],
    углы скруглены, как у всплывающих окон (round_window), пункты — обычные надписи Tk, наведение меняет только цвета.
    Колонки (длинный список титанов по стихиям) — сетка, пустого места Windows под короткой колонкой больше нет.

    Открытое окошко держит захват мыши (hold_grab): щелчок мимо закрывает его, как меню Windows. Закрывается и по Escape,
    по выбору пункта и когда программа перестаёт быть активной. Окно, которое было модальным до списка («Новое правило»,
    «Личный порог»), после закрытия снова берёт захват.
    Похож на tk.Menu, чтобы заменить его без переделок: add_command, entryconfigure, entrycget, tk_popup, grab_release.
    Выпадающий список: values и command (команда получает надпись пункта, как у меню CustomTkinter), breaks — номера
    пунктов, с которых начинается новая колонка, open(x, y)."""

    def __init__(self, master, values=(), command=None, breaks=(), min_width=0):
        self.master = master
        self.entries = []          # [надпись, команда]
        self.breaks = set()
        self.min_width = min_width
        self.top = None
        self._items = []
        self._poll_id = None
        self._had_focus = False
        self._previous_grab = None
        self._previous_focus = None
        if values:
            self.set_values(values, command, breaks)

    # ── Пункты ──────────────────────────────────────────────────────────────
    def add_command(self, label="", command=None):
        self.entries.append([label, command])

    def entryconfigure(self, index, label=None, command=None):
        if label is not None:
            self.entries[index][0] = label
        if command is not None:
            self.entries[index][1] = command

    def entrycget(self, index, option):
        return self.entries[index][0 if option == "label" else 1]

    def set_values(self, values, command, breaks=()):
        """Пункты выпадающего списка: щелчок по пункту — command(надпись)."""
        self.close()
        self.entries = [[text, (lambda t=text: command(t)) if command else None] for text in values]
        self.breaks = {i for i in breaks if i}

    def columns(self):
        """Пункты по колонкам (списки номеров) — как они встанут в окошке."""
        cols = []
        for i in range(len(self.entries)):
            if not cols or i in self.breaks:
                cols.append([])
            cols[-1].append(i)
        return cols

    # ── Показ ───────────────────────────────────────────────────────────────
    def tk_popup(self, x, y):
        self.open(x, y)

    def grab_release(self):
        """Как у tk.Menu (после tk_popup его звали). Захват окошка отпускает close."""

    def is_open(self):
        return self.top is not None

    def open(self, x, y, anchor="nw", flip_y=None, width=0):
        """Показать окошко: левый верхний угол в (x, y); anchor="sw" — (x, y) — левый нижний угол.
        flip_y — если снизу не влезает в экран, окошко встаёт над этой высотой (верх поля списка).
        width — не уже этого (настоящие пиксели: ширина поля списка)."""
        self.close()
        if not self.entries:
            return
        try:
            self._build()
            top = self.top
            w, h = self._measure()
            w = max(w, round(width))
            if anchor == "sw":
                y -= h
            elif y + h > top.winfo_screenheight() and flip_y is not None:
                y = flip_y - h
            top.geometry(f"{w}x{h}+{round(x)}+{max(0, round(y))}")
            top.deiconify()
            top.lift()
        except tk.TclError:
            self.close()
            return
        self._poll_id = top.after(250, self._poll)

    def _measure(self):
        """Размер окошка по пунктам: нужный размер надписи Tk известен сразу, поэтому без update_idletasks
        (он доделал бы всю отложенную работу окна программы — раскладку страниц)."""
        scale = light.scale_of(self.master)
        pad = round(4 * scale)
        widths, heights = [], []
        for col, indexes in enumerate(self.columns()):
            items = [self._items[i] for i in indexes]
            width = max(item.winfo_reqwidth() for item in items)
            if col == 0:
                width = max(width, round(self.min_width * scale))
            widths.append(width)
            heights.append(sum(item.winfo_reqheight() for item in items))
        return sum(widths) + 2 * pad, max(heights) + 2 * pad

    def _build(self):
        master = self.master
        scale = light.scale_of(master)
        try:
            self._previous_grab = master.grab_current()
        except (tk.TclError, KeyError):
            self._previous_grab = None
        try:
            self._previous_focus = master.focus_get()
        except (tk.TclError, KeyError):
            self._previous_focus = None
        top = _frameless_window(master.winfo_toplevel())
        self.top = top
        bg = C["bg_elevated"]
        top.configure(bg=bg)
        body = tk.Frame(top, bg=bg, bd=0, highlightthickness=0)
        body.pack(fill="both", expand=True, padx=round(4 * scale), pady=round(4 * scale))
        font = scaled_font(master, F["text"])
        self._items = []
        for col, indexes in enumerate(self.columns()):
            body.grid_columnconfigure(col, weight=1, minsize=round(self.min_width * scale) if col == 0 else 0)
            for row, i in enumerate(indexes):
                text, command = self.entries[i]
                item = tk.Label(body, text=text, font=font, bg=bg, fg=C["text"], anchor="w", bd=0,
                                highlightthickness=0, padx=round(12 * scale), pady=round(5 * scale))
                item.grid(row=row, column=col, sticky="ew")
                item.bind("<Enter>", lambda _e, it=item: self._hover(it, True))
                item.bind("<Leave>", lambda _e, it=item: self._hover(it, False))
                item.bind("<ButtonRelease-1>", lambda _e, c=command: self._choose(c))
                self._items.append(item)
        edges = edge_lines(top)
        top.bind("<Map>", lambda e: e.widget is top and round_window(top, edges, scale), add="+")
        top.bind("<ButtonPress>", self._press, add="+")
        top.bind("<Escape>", lambda _e: self.close(), add="+")
        top.bind("<Unmap>", lambda e: e.widget is top and top.after_idle(self.close, False),  # окно программы свернули
                 add="+")
        hold_grab(top, on_grab=top.focus_set)()

    def _hover(self, item, inside):
        look = (C["blue_button"], C["white"]) if inside else (C["bg_elevated"], C["text"])
        if item.cget("bg") != look[0]:
            item.configure(bg=look[0], fg=look[1])

    def _press(self, event):
        """Щелчок мимо окошка (захват присылает его сюда) — закрыть, как меню Windows."""
        top = self.top
        if top is None:
            return
        try:
            x, y = top.winfo_rootx(), top.winfo_rooty()
            inside = x <= event.x_root < x + top.winfo_width() and y <= event.y_root < y + top.winfo_height()
        except tk.TclError:
            inside = False
        if not inside:
            self.close()

    def _choose(self, command):
        self.close()
        if command:
            command()

    def _poll(self):
        """Программа перестала быть активной (щёлкнули в другое окно Windows) — закрыть, как меню Windows."""
        self._poll_id = None
        top = self.top
        if top is None:
            return
        try:
            focused = top.focus_displayof() is not None
        except (tk.TclError, KeyError):
            focused = False
        if focused:
            self._had_focus = True
        elif self._had_focus:
            self.close(give_back=False)     # фокус ушёл в другую программу — туда его и оставляем
            return
        try:
            self._poll_id = top.after(250, self._poll)
        except tk.TclError:
            self._poll_id = None

    def close(self, give_back=True):
        """Закрыть окошко. give_back — вернуть фокус клавиатуры окну программы (выбрали пункт, Escape, щелчок мимо):
        окошко без рамки Tk в Windows делает отдельным окном, не привязанным к окну программы («Parent must be desktop
        even if we have a transient parent» в исходниках Tk), и, забрав фокус для Escape, после закрытия его не
        возвращало — после выбора цели в поле рядом нельзя было ввести число (сессия 11б). Поэтому фокус возвращаем
        сами и с force: окно программы снова активное, клавиши — туда, где были до списка."""
        top, self.top = self.top, None
        self._items = []
        self._had_focus = False
        if top is None:
            return
        try:
            if self._poll_id:
                top.after_cancel(self._poll_id)
        except tk.TclError:
            pass
        self._poll_id = None
        try:
            top.grab_release()
            top.destroy()
        except tk.TclError:
            pass
        previous, self._previous_grab = self._previous_grab, None
        focus, self._previous_focus = self._previous_focus, None
        try:
            if previous is not None and previous.winfo_exists() and previous.winfo_viewable():
                previous.grab_set()    # модальное окно под списком снова модальное (его hold_grab сам этого не сделает)
        except tk.TclError:
            pass
        try:
            if focus is not None and focus.winfo_exists():
                (focus.focus_force if give_back else focus.focus_set)()
            elif give_back and self.master.winfo_exists():
                self.master.winfo_toplevel().focus_force()
        except tk.TclError:
            pass

    def destroy(self):
        self.close(give_back=False)


def menu_breaks(items, breaks):
    """Номера пунктов, с которых начинается новая колонка: items — (ключ, надпись), breaks — ключи начала колонок."""
    return {i for i, (key, _text) in enumerate(items) if i and key in breaks}


def open_under(menu, field):
    """Открыть список под полем (не влезает в экран снизу — над ним), вровень с левым краем поля и не уже его."""
    gap = px(field, 2)
    menu.open(field.winfo_rootx(), field.winfo_rooty() + field.winfo_height() + gap, flip_y=field.winfo_rooty() - gap,
              width=field.winfo_width())


class PlainLabel(tk.Label):
    """Обычная надпись Tk вместо CTkLabel (без своего холста)."""

    def __init__(self, master, text="", font=None, color=None, bg=None, **kwargs):
        super().__init__(master, text=text, font=scaled_font(master, font or F["text"]), fg=color or C["text"],
                         bg=bg or C["bg_surface"], bd=0, highlightthickness=0, padx=0, pady=0, **kwargs)


def plain_icon(master, name, color, size, box=None, tint=None, bg=None, radius=8):
    """Иконка для обычной надписи Tk (ImageTk.PhotoImage, в настоящих пикселях с учётом масштаба Windows).
    box — сторона квадрата-подложки цвета tint со скруглением radius (значок стихии 40×40), фон вокруг — bg."""
    scale = light.scale_of(master)
    args = (name, color.upper(), round(size * scale), round(box * scale) if box else 0, tint, bg, round(radius * scale))
    return shared_photo(master, ("icon",) + args, lambda: _plain_icon_picture(*args))


@lru_cache(maxsize=128)
def _plain_icon_picture(name, color, px, box_px, tint, bg, radius):
    from ui.icons import _colored
    k = 4
    glyph = _colored(name, color).resize((px * k, px * k), Image.LANCZOS)
    if not box_px:
        return glyph.resize((px, px), Image.LANCZOS)
    rgb = lambda c: tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))  # noqa: E731
    big = box_px * k
    img = Image.new("RGBA", (big, big), rgb(bg) + (255,))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, big - 1, big - 1), radius=radius * k, fill=rgb(tint) + (255,))
    img.alpha_composite(glyph, ((big - px * k) // 2, (big - px * k) // 2))
    return img.resize((box_px, box_px), Image.LANCZOS)


class TitanTile(tk.Label):
    """Лёгкий квадрат титана для длинных прокручиваемых списков (мастер правил): то же, что TitanAvatar
    (рамка цветом стихии, фон — оттенок стихии, картинка или две буквы, подсказка с именем), но одна обычная
    надпись Tk с готовой картинкой. У TitanAvatar внутри два холста CustomTkinter, и при прокрутке и раскрытии
    списков Windows перерисовывает каждый отдельно — элементы дорисовывались с задержкой (проверка шага 5а).
    bg — цвет того, на чём квадрат стоит (уголки скругления — его цвета). dim — бледный (выключенное правило, шаг 5в)."""

    def __init__(self, master, titan, lang="RU", size=None, bg=None, command=None, dim=False):
        self.titan = titan
        self.lang = lang
        self.command = command
        scale = light.scale_of(master)   # масштаб Windows: картинка — в настоящих пикселях
        px = round((size or S["avatar"]) * scale)
        source = titan_source(titan)
        bg = bg or C["bg_surface"]
        args = (titan, px, max(1, round(S["avatar_border"] * scale)), bg) + (source or (None, 0))

        def picture():
            tile = _tile_picture(*args)
            if dim:
                tile = Image.blend(Image.new("RGBA", tile.size, _rgb(bg) + (255,)), tile, theme.RULE_DIM)
            return tile
        self.photo = shared_photo(master, ("tile", dim) + args, picture)
        text = "" if source else theme.initials(titan_name(lang, titan))
        font_px = round((12 if px >= 30 * scale else 10) * scale)
        super().__init__(master, image=self.photo, text=text, compound="center", bg=bg,
                         fg=theme.blend(C["text"], bg, theme.RULE_DIM) if dim else C["text"],
                         font=(theme.FONT_FAMILY, -font_px, "bold"), bd=0,
                         highlightthickness=0, padx=0, pady=0, width=px, height=px)
        self.tooltip = Tooltip(self, lambda: titan_name(self.lang, self.titan))
        if command:
            self.bind("<Button-1>", lambda _e: self.command(self.titan), add="+")


@lru_cache(maxsize=256)
def _tile_picture(titan, px, border, bg, key, stamp):
    """Готовый квадрат титана (PIL): скруглённый квадрат цвета стихии на фоне bg, внутри картинка титана (key, stamp —
    из titan_source; None — без картинки). Рисуется в 4 раза крупнее и уменьшается — края гладкие.
    bg=None — уголки прозрачные: для надписи, у которой фон меняется при наведении (поле выбора титана)."""
    style = theme.element_style(theme.element_of(titan))
    k = 4
    big = px * k
    rgb = lambda color: tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))  # noqa: E731
    img = Image.new("RGBA", (big, big), rgb(bg) + (255,) if bg else (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, big - 1, big - 1), radius=S["radius_control"] * px * k // S["avatar"],
                                          fill=rgb(style["tint"]) + (255,), outline=rgb(style["color"]) + (255,),
                                          width=border * k)
    if key:
        inner = px - 2 * border - 2
        pic = _square_picture(key, stamp, inner * k, 4 * k * px // S["avatar"])
        offset = (big - inner * k) // 2
        img.alpha_composite(pic, (offset, offset))
    return img.resize((px, px), Image.LANCZOS)


def titan_photo(master, titan, size=None):
    """Квадрат титана для обычной надписи Tk с прозрачными уголками (поле выбора титана в Dropdown): (картинка, есть ли
    на ней титан). Нет картинки — квадрат пустой, две буквы имени надписи кладёт тот, кто её показывает."""
    scale = light.scale_of(master)
    px = round((size or S["avatar"]) * scale)
    source = titan_source(titan)
    args = (titan, px, max(1, round(S["avatar_border"] * scale)), None) + (source or (None, 0))
    return shared_photo(master, ("tile", False) + args, lambda: _tile_picture(*args)), source is not None


def _rgb(color):
    return tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))


def pill_label(master, text, font, fg, fill, bg, height=20, radius=4, pad_x=7):
    """Значок с надписью на скруглённой подложке («Смешанная», «ЛЕЧЕНИЕ», «Спросить вас» в строке правила, шаг 5в):
    обычная надпись Tk поверх готовой картинки подложки — без своего холста, как TitanTile (длинные списки)."""
    scale = light.scale_of(master)
    w = text_width(master, font, text) + round(2 * pad_x * scale)
    args = (w, round(height * scale), fill, bg, round(radius * scale))
    photo = shared_photo(master, ("pill",) + args, lambda: _pill_picture(*args))
    label = tk.Label(master, image=photo, text=text, compound="center", fg=fg, bg=bg,
                     font=scaled_font(master, font), bd=0, highlightthickness=0, padx=0, pady=0)
    label.photo = photo
    return label


@lru_cache(maxsize=64)
def _pill_picture(w, h, fill, bg, radius):
    k = 4
    img = Image.new("RGBA", (w * k, h * k), _rgb(bg) + (255,))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=radius * k, fill=_rgb(fill) + (255,))
    return img.resize((w, h), Image.LANCZOS)


class ElidedLabel(PlainLabel):
    """Надпись в одну строку, которая не раздвигает строку списка: длинный текст обрезается по ширине с «…»,
    полный — в подсказке. Ширину надписи задаёт сетка (sticky="ew"), текст подгоняется при изменении ширины."""

    def __init__(self, master, text="", font=None, **kwargs):
        super().__init__(master, "", font=font, width=1, anchor="w", **kwargs)
        self._font = font or F["text"]
        self.full = text
        self._fitted_for = None
        self.tooltip = Tooltip(self, lambda: self.full if self.cget("text") != self.full else "")
        self.bind("<Configure>", lambda _e: self.fit(), add="+")

    def fit(self):
        width = self.winfo_width()
        if width <= 1 or width == self._fitted_for:
            return
        self._fitted_for = width
        text = self.full
        if text_width(self, self._font, text) > width:
            low, high = 0, len(text)
            while low < high:   # самая длинная начальная часть, которая влезает вместе с «…»
                mid = (low + high + 1) // 2
                if text_width(self, self._font, text[:mid].rstrip() + "…") <= width:
                    low = mid
                else:
                    high = mid - 1
            text = text[:low].rstrip() + "…"
        if self.cget("text") != text:
            self.configure(text=text)


class PlainSwitch(tk.Label):
    """Лёгкий тумблер 36×20 для строк длинного списка (макет 03c, «Вкл.»): картинка, без своего холста.
    command(включён) — после щелчка; set_on() — без вызова command. size — другой размер (Switch: 40×22)."""

    def __init__(self, master, value=False, command=None, bg=None, tooltip=None, size=(36, 20)):
        self._bg = bg or C["bg_elevated"]
        scale = light.scale_of(master)
        size = (round(size[0] * scale), round(size[1] * scale))
        self._pictures = {on: shared_photo(master, ("switch", on, self._bg) + size,
                                           lambda on=on: _switch_picture(*size, on, self._bg)) for on in (True, False)}
        super().__init__(master, bg=self._bg, bd=0, highlightthickness=0, padx=0, pady=0, cursor="hand2")
        self.command = command
        self.on = None
        self.set_on(value)
        self.bind("<Button-1>", self._clicked, add="+")
        self.tooltip = Tooltip(self, tooltip) if tooltip else None

    def set_on(self, value):
        value = bool(value)
        if value != self.on:
            self.on = value
            self.configure(image=self._pictures[value])

    def _clicked(self, _event=None):
        self.set_on(not self.on)
        if self.command:
            self.command(self.on)


@lru_cache(maxsize=8)
def _switch_picture(w, h, on, bg):
    k = 4
    img = Image.new("RGBA", (w * k, h * k), _rgb(bg) + (255,))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=h * k // 2,
                           fill=_rgb(C["blue"] if on else C["border_strong"]) + (255,))
    pad = 2 * h * k // 20
    knob = h * k - 2 * pad
    x = w * k - pad - knob if on else pad
    draw.ellipse((x, pad, x + knob - 1, pad + knob - 1), fill=_rgb(C["white"] if on else C["text_secondary"]) + (255,))
    return img.resize((w, h), Image.LANCZOS)


class RoundedBackdrop(tk.Label):
    """Скруглённая подложка с рамкой 1 px под содержимым рамки Tk (строка длинного списка, шаг 5в): готовая картинка
    вместо холста CustomTkinter. Ставится первой в рамку (place во всю рамку), содержимое кладётся поверх; при новом
    размере рамки — картинка этого размера (одна на окно для всех строк одного размера)."""

    def __init__(self, master, fill, border, outer, radius=8):
        super().__init__(master, bg=outer, bd=0, highlightthickness=0, padx=0, pady=0)
        self._look = (fill, border, outer, round(radius * light.scale_of(master)))
        self._size = None
        self.photo = None
        self.place(x=0, y=0, relwidth=1, relheight=1)
        master.bind("<Configure>", self._fit, add="+")

    def _fit(self, event):
        size = (event.width, event.height)
        if size == self._size or min(size) < 4:
            return
        self._size = size
        key = ("backdrop",) + size + self._look
        cache = self._root().__dict__.setdefault("_shared_photos", {})
        if key not in cache:   # размеров при изменении окна много — старые подложки не копим
            for old in [k for k in cache if k[0] == "backdrop"][:-8]:
                del cache[old]
        self.photo = shared_photo(self, key, lambda: _backdrop_picture(*size, *self._look))
        self.configure(image=self.photo)


    def restyle(self, fill, border):
        """Другие цвета подложки (наведение на кнопку): готовая картинка того же размера, виджеты не перестраиваются."""
        look = (fill, border) + self._look[2:]
        if look == self._look:
            return
        self._look = look
        if self._size:
            key = ("backdrop",) + self._size + look
            self.photo = shared_photo(self, key, lambda: _backdrop_picture(*self._size, *look))
            self.configure(image=self.photo)


def _backdrop_picture(w, h, fill, border, outer, radius):
    """Подложка w × h: заливка одним цветом, рамка 1 px линиями и четыре готовых уголка (ui/light.py). Раньше вся
    картинка рисовалась в 3 раза крупнее и уменьшалась: большая карточка стоила 15 мс на каждый новый размер."""
    return light.rounded_picture(w, h, fill, border, outer, radius, 1)


class PlainIconButton(tk.Label):
    """Лёгкая кнопка-значок для строк длинного списка (↑↓, карандаш, ✕ в «Правилах и перехватах»): картинка без
    своего холста. Наведение меняет только цвет фона; недоступная — бледный значок и щелчок не работает."""

    def __init__(self, master, icon_name, command=None, size=14, bg=None, hover=None, color=None, tooltip=None,
                 pad=8, pad_y=8):
        self._bg = bg or C["bg_elevated"]
        self._hover = hover or T["hover_elevated"]
        self._pictures = {state: plain_icon(master, icon_name, c, size)
                          for state, c in (("on", color or C["text_secondary"]), ("off", C["border_focus"]))}
        scale = light.scale_of(master)
        # У надписи-картинки Tk padx не работает: место вокруг значка задаёт ширина и высота (в пикселях)
        super().__init__(master, image=self._pictures["on"], bg=self._bg, bd=0, highlightthickness=0,
                         width=round((size + 2 * pad) * scale), height=round((size + 2 * pad_y) * scale),
                         cursor="hand2")
        self.command = command
        self.enabled = True
        self._look = self._bg
        self.bind("<Button-1>", self._clicked, add="+")
        self.bind("<Enter>", lambda _e: self._paint(True), add="+")
        self.bind("<Leave>", lambda _e: self._paint(False), add="+")
        self.tooltip = Tooltip(self, tooltip) if tooltip else None

    def _paint(self, hovering):
        look = self._hover if hovering and self.enabled else self._bg
        if look != self._look:
            self._look = look
            self.configure(bg=look)

    def _clicked(self, _event=None):
        if self.enabled and self.command:
            self.command()

    def set_enabled(self, enabled):
        if enabled != self.enabled:
            self.enabled = enabled
            self.configure(image=self._pictures["on" if enabled else "off"], cursor="hand2" if enabled else "")
            if not enabled:
                self._paint(False)


def plain_card(master, outer, fill=None, border=None, radius=None):
    """Карточка без холста CustomTkinter (страница «О программе», шаг 7): рамка Tk с готовой скруглённой подложкой.
    outer — цвет за карточкой (в углах), содержимое кладут прямо в неё (grid/pack), у надписей bg=fill, а от краёв — не меньше
    радиуса, чтобы квадратные уголки надписей не закрыли скругление. Прокрутка страницы с такими карточками не оставляет следов."""
    card = tk.Frame(master, bg=outer)
    card.fill = fill or C["bg_surface"]
    card.backdrop = RoundedBackdrop(card, card.fill, border or C["border"], outer,
                                    radius=S["radius_card"] if radius is None else radius)
    return card


class PlainClickFrame(tk.Frame):
    """Рамка-кнопка без холста CustomTkinter: щелчок по ней или по любой её части — command(), наведение — _paint() по
    self._hovering (только цвета). Уход мыши проверяется через 30 мс по положению указателя: при переходе между частями рамки
    «ушла/пришла» не мигает. Части, добавленные после создания, подключает bind_parts()."""

    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.enabled = True
        self._hovering = False
        self._leave_id = None
        self.bind_parts(self)
        self.bind("<Destroy>", self._cancel_leave, add="+")

    def bind_parts(self, *parts):
        for part in parts:
            part.bind("<Button-1>", self._click, add="+")
            part.bind("<Enter>", self._enter, add="+")
            part.bind("<Leave>", self._leave, add="+")

    def _paint(self):
        pass

    def _click(self, _event=None):
        if self.enabled and self.command:
            self.command()

    def _enter(self, _event=None):
        if not self._hovering:
            self._hovering = True
            self._paint()

    def _leave(self, _event=None):
        self._cancel_leave()
        try:
            self._leave_id = self.after(30, self._leave_if_outside)
        except tk.TclError:
            self._leave_id = None

    def _cancel_leave(self, _event=None):
        if self._leave_id:
            try:
                self.after_cancel(self._leave_id)
            except tk.TclError:
                pass
            self._leave_id = None

    def _leave_if_outside(self):
        self._leave_id = None
        if not _pointer_inside(self):
            self._hovering = False
            self._paint()


# Виды лёгкой кнопки: заливка, рамка, заливка при наведении, цвет текста, цвет значка
PLAIN_BUTTON_KINDS = {
    "secondary": dict(fill=C["bg_elevated"], border=C["border"], hover=T["hover_elevated"], text=C["text"],
                      icon=C["text_secondary"]),
    "blue": dict(fill=C["blue_button"], border=C["blue_button"], hover=T["hover_blue"], text=C["white"],
                 icon=C["white"]),
    "outline": dict(fill=None, border=C["border_strong"], hover=T["hover_elevated"], text=C["text"],
                    icon=C["text_secondary"]),
}


class PlainButton(PlainClickFrame):
    """Кнопка со скруглением без холста CustomTkinter (страница «О программе», шаг 7): рамка Tk, скругление — готовая
    картинка (RoundedBackdrop), внутри одна надпись Tk со значком. Наведение — другая картинка подложки и цвет надписи.
    kind: secondary / blue / outline (без заливки: цвет за кнопкой — outer). outer — цвет за кнопкой, он же заливка outline.
    Ширина — по надписи (меньше не бывает), в сетке с sticky="ew" растягивается; text="" — квадрат с одним значком.
    icon_gap — зазор между значком и надписью (у кнопки с одним значком — 0). set_text() меняет надпись и ширину (язык окна)."""

    def __init__(self, master, text="", command=None, kind="secondary", icon_name=None, icon_size=15, height=36,
                 pad_x=12, anchor="center", outer=None, font=None, width=None, tooltip=None, icon_gap=12):
        self._style = dict(PLAIN_BUTTON_KINDS[kind])
        self._outer = outer or C["bg_surface"]
        if self._style["fill"] is None:
            self._style["fill"] = self._outer
        fill = self._style["fill"]
        scale = light.scale_of(master)
        super().__init__(master, command=command, bg=self._outer, height=round(height * scale), cursor="hand2")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self._font = font or F["button"]
        self._pad_x = pad_x
        self._min_width = width
        self._icon_gap = icon_gap if icon_name else 0
        self.backdrop = RoundedBackdrop(self, fill, self._style["border"], self._outer, radius=S["radius_control"])
        # Значок на подложке цвета заливки: по одной картинке на обычный вид и на наведение (наведение только меняет их)
        self.photos = {hovering: plain_icon(self, icon_name, self._style["icon"], icon_size,
                                            box=icon_size + self._icon_gap, tint=color, bg=color, radius=0)
                       for hovering, color in ((False, fill), (True, self._style["hover"]))} if icon_name else {}
        self.photo = self.photos.get(False)
        self.label = tk.Label(self, text=text, image=self.photo, compound="left" if icon_name else "none", fg=self._style["text"],
                              bg=fill, font=scaled_font(self, self._font), bd=0, highlightthickness=0, padx=0, pady=0,
                              anchor=anchor, cursor="hand2", width=1)
        # У значка своя подложка шире самого значка (на gap): половина зазора уже внутри картинки, отступ слева — без неё
        # Сверху и снизу — рамка 1 px, по бокам — не меньше 3 px: надпись не должна закрыть рамку и скругление подложки
        self.label.pack(fill="both", expand=True, pady=max(1, round(scale)),
                        padx=max(round(3 * scale), round((pad_x - (self._icon_gap / 2)) * scale)))
        self.bind_parts(self.label)
        self.icon_size = icon_size
        self.fit_width()
        if tooltip:
            self.tooltip = Tooltip(self, tooltip)
            self.tooltip.attach(self.label)

    def fit_width(self):
        """Ширина не меньше, чем надо надписи со значком (в языках надписи разной длины)."""
        scale = light.scale_of(self)
        text = self.label.cget("text")
        inner = text_width(self, self._font, text) if text else 0
        if self.photo is not None:
            inner += round((self.icon_size + self._icon_gap) * scale)
        width = round(2 * (self._pad_x - (self._icon_gap / 2)) * scale) + inner
        self.configure(width=max(width, round((self._min_width or 0) * scale)))

    def set_text(self, text):
        if self.label.cget("text") != text:
            self.label.configure(text=text)
            self.fit_width()

    def _paint(self):
        fill = self._style["hover"] if self._hovering else self._style["fill"]
        self.backdrop.restyle(fill, self._style["border"])
        if self.label.cget("bg") != fill:
            self.label.configure(bg=fill)
            if self.photos:   # у значка своя подложка цвета заливки: на наведении — подложка цвета наведения
                self.label.configure(image=self.photos[self._hovering])


class Chip(light.Box):
    """Фильтр-«таблетка» высотой 30: выбранный — фон bg_elevated и светлая рамка, невыбранный — прозрачный.
    dot_color — цветная точка слева (фильтр стихии), count — красный счётчик справа («Ошибки 1»).
    Один холст Tk: рамка — Box, точка, надпись и счётчик — рисунки холста. Наведение меняет только цвета;
    жирный шрифт и ширина меняются только при выборе (как раньше)."""

    def __init__(self, master, text, selected=False, command=None, dot_color=None, count=None, **kwargs):
        self.command = command
        self.selected = selected
        self._hovering = False
        self._look = None        # что нарисовано сейчас: перекрашиваем, только если вид поменялся
        self._leave_id = None
        self._text = text
        self._count = None
        self._bold = None
        super().__init__(master, fg_color="transparent", border_width=1, border_color=C["border"],
                         corner_radius=S["radius_chip"], width=10, height=S["chip_height"], cursor="hand2", **kwargs)
        canvas = tk.Canvas
        self._dot_photo = light.photo_of(self, dot(dot_color, 8)) if dot_color else None
        self._dot_item = canvas.create_image(self, 0, 0, anchor="w", image=self._dot_photo or "",
                                             state="normal" if dot_color else "hidden")
        self._text_item = canvas.create_text(self, 0, 0, anchor="w", text=text)
        self._count_back = canvas.create_image(self, 0, 0, anchor="w", state="hidden")
        self._count_item = canvas.create_text(self, 0, 0, anchor="center", text="", fill=C["danger_text"],
                                              font=scaled_font(self, F["small_bold"]), state="hidden")
        for sequence, handler in (("<Button-1>", self._on_click), ("<Enter>", self._chip_enter),
                                  ("<Leave>", self._chip_leave)):
            canvas.bind(self, sequence, handler, add="+")
        self.set_count(count)
        self._paint()

    def _font(self):
        return F["label_bold"] if self.selected else F["label"]

    def _fit(self):
        """Ширина по содержимому: 12 | точка 8 и 6 | надпись | 12 (или 6 | счётчик 18 | 8), как у прежней таблетки."""
        left = px(self, 12)
        dot_w = px(self, 8 + 6) if self._dot_photo is not None else 0
        text_w = text_width(self, self._font(), self._text)
        right = px(self, 6) + self._count_width() + px(self, 8) if self._count else px(self, 12)
        tk.Canvas.configure(self, width=left + dot_w + text_w + right, height=px(self, S["chip_height"]))
        self._place()

    def _count_width(self):
        return max(px(self, 18), text_width(self, F["small_bold"], str(self._count)) + px(self, 8))

    def _place(self):
        if self._box_size is None:
            return
        _w, h = self._box_size
        x = px(self, 12)
        y = h / 2
        if self._dot_photo is not None:
            tk.Canvas.coords(self, self._dot_item, x, y)
            x += px(self, 8 + 6)
        tk.Canvas.coords(self, self._text_item, x, y)
        if self._count:
            x += text_width(self, self._font(), self._text) + px(self, 6)
            tk.Canvas.coords(self, self._count_back, x, y)
            tk.Canvas.coords(self, self._count_item, x + self._count_width() / 2, y)

    def _after_box_draw(self):
        if hasattr(self, "_count_item"):
            self._place()

    def _paint(self):
        if self.selected:
            look = (C["bg_elevated"], C["border_focus"], C["text"], True)
        else:
            look = (C["bg_elevated"] if self._hovering else None, C["border"], C["text_secondary"], False)
        if look == self._look:
            return
        fg, border, text, bold = look
        self._look = look
        self.restyle(fill=fg or self._box_outer, border=border)
        tk.Canvas.itemconfigure(self, self._text_item, fill=text)
        if bold != self._bold:
            # Шрифт меняется только при выборе (не при наведении): ширина таблетки — по жирной надписи
            self._bold = bold
            tk.Canvas.itemconfigure(self, self._text_item, font=scaled_font(self, self._font()))
            self._fit()

    def _on_click(self, _event=None):
        if self.command:
            self.command()

    def _chip_enter(self, _event=None):
        if not self._hovering:
            self._hovering = True
            self._paint()

    def _chip_leave(self, _event=None):
        if self._leave_id:
            try:
                self.after_cancel(self._leave_id)
            except tk.TclError:
                pass
        try:
            self._leave_id = self.after(30, self._leave_if_outside)
        except tk.TclError:
            self._leave_id = None

    def _leave_if_outside(self):
        self._leave_id = None
        if not _pointer_inside(self):
            self._hovering = False
            self._paint()

    def _follow_surface(self, color):
        self._box_outer = color
        if not self.selected and not self._hovering:
            self.restyle(fill=color)
        else:
            self._box_draw()

    def set_selected(self, selected):
        self.selected = selected
        self._paint()

    def set_text(self, text):
        if text != self._text:
            self._text = text
            tk.Canvas.itemconfigure(self, self._text_item, text=text)
            self._fit()

    @property
    def count(self):
        """Число в красном счётчике (None — счётчика нет)."""
        return self._count

    @property
    def text(self):
        return self._text

    def set_count(self, count):
        """Счётчик справа; 0 или None — счётчика нет."""
        count = count or None
        if count == self._count and self._count is not None:
            return
        self._count = count
        if count:
            w, h = self._count_width(), px(self, 18)
            radius = px(self, 9)
            # Уголки прозрачные: под счётчиком — заливка таблетки (у наведения своя), картинка одна на все
            self._count_photo = shared_photo(self, ("count", w, h, radius),
                                             lambda: light.pill_rgba(w, h, T["danger_badge_bg"], radius))
            tk.Canvas.itemconfigure(self, self._count_back, image=self._count_photo, state="normal")
            tk.Canvas.itemconfigure(self, self._count_item, text=str(count), state="normal")
        else:
            tk.Canvas.itemconfigure(self, self._count_back, state="hidden")
            tk.Canvas.itemconfigure(self, self._count_item, state="hidden")
        self._fit()


class ClickFrame(light.Box):
    """Рамка, которая ведёт себя как кнопка: щелчок по ней или по любой её части — command(), наведение — _paint().
    Наследник рисует себя в _paint() по self._hovering и сам решает, что перекрасить (только цвета и только если вид
    поменялся — правило в начале файла). Части, добавленные после создания, подключает bind_parts().
    С сессии 11 — холст Tk со скруглением (light.Box) вместо CTkFrame: configure(fg_color=…) на наведении меняет только
    цвет рисунков, лёгкие надписи с "transparent" берут новый фон сами."""

    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.enabled = True
        self._hovering = False
        self._leave_id = None
        self.bind_parts(self)

    def bind_parts(self, *parts):
        for part in parts:
            part.bind("<Button-1>", self._frame_click, add="+")
            part.bind("<Enter>", self._frame_enter, add="+")
            part.bind("<Leave>", self._frame_leave, add="+")

    def _paint(self):
        pass

    def _frame_click(self, _event=None):
        if self.enabled and self.command:
            self.command()

    def _frame_enter(self, _event=None):
        if not self._hovering:
            self._hovering = True
            self._paint()

    def _frame_leave(self, _event=None):
        if self._leave_id:
            try:
                self.after_cancel(self._leave_id)
            except tk.TclError:
                pass
        try:
            self._leave_id = self.after(30, self._leave_if_outside)
        except tk.TclError:
            self._leave_id = None

    def _leave_if_outside(self):
        self._leave_id = None
        if not _pointer_inside(self):
            self._hovering = False
            self._paint()

    def set_enabled(self, enabled):
        if enabled != self.enabled:
            self.enabled = enabled
            self._paint()


# Кнопки «Пауза F9», «Продолжить F9», «СТОП F10» (главная, макет 01_main): цвет рамки, цвет текста, иконка
KEY_BUTTON_KINDS = {
    "pause": (C["warning"], C["warning"], "pause-filled"),
    "continue": (C["success"], C["success"], "play-filled"),
    "stop": (C["danger"], C["danger_text"], "square-filled"),
}


class KeyButton(ClickFrame):
    """Контурная кнопка с подписью клавиши справа (рамочка «F9»): высота 38, прозрачная, рамка и текст цвета вида.
    Неактивная — бледная (пока бот не работает). set_kind() меняет вид и надпись («Пауза» ⇄ «Продолжить»).
    Один холст Tk: иконка, надпись и рамочка клавиши — рисунки холста, по середине кнопки."""

    def __init__(self, master, text, key, kind="pause", command=None, tooltip=None, height=38, width=100, **kwargs):
        # width — наименьшая ширина: в сетке кнопка растягивается по колонке
        super().__init__(master, command=command, width=width, height=height, corner_radius=S["radius_control"],
                         border_width=1, fg_color="transparent", cursor="hand2", **kwargs)
        self.kind = kind
        self._look = None
        self._text = text
        self._key = key
        canvas = tk.Canvas
        self._icon_item = canvas.create_image(self, 0, 0, anchor="w")
        self._text_item = canvas.create_text(self, 0, 0, anchor="w", text=text, font=scaled_font(self, F["button"]))
        self._kbd_item = canvas.create_image(self, 0, 0, anchor="w")
        self._kbd_text = canvas.create_text(self, 0, 0, anchor="center", text=key,
                                            font=scaled_font(self, (theme.MONO_FAMILY, 10)))
        self.tooltip = Tooltip(self, tooltip) if tooltip else None
        self._paint()

    def _kbd_size(self):
        return (max(px(self, 14), text_width(self, (theme.MONO_FAMILY, 10), self._key)) + px(self, 8) + 2,
                px(self, 16))

    def _place(self):
        if self._box_size is None:
            return
        w, h = self._box_size
        icon_w, gap = px(self, 14), px(self, 6)
        text_w = text_width(self, F["button"], self._text)
        kbd_w, _kbd_h = self._kbd_size()
        x = (w - (icon_w + gap + text_w + gap + kbd_w)) // 2
        y = h / 2
        canvas = tk.Canvas
        canvas.coords(self, self._icon_item, x, y)
        canvas.coords(self, self._text_item, x + icon_w + gap, y)
        canvas.coords(self, self._kbd_item, x + icon_w + gap + text_w + gap, y)
        canvas.coords(self, self._kbd_text, x + icon_w + gap + text_w + gap + kbd_w / 2, y)

    def _after_box_draw(self):
        if hasattr(self, "_kbd_text"):
            self._place()

    def _paint(self):
        border, text, icon_name = KEY_BUTTON_KINDS[self.kind]
        if not self.enabled:
            border, text = theme.blend(border, C["bg_surface"], 0.4), theme.blend(text, C["bg_surface"], 0.4)
        fg = theme.blend(border, C["bg_surface"], 0.12) if self._hovering and self.enabled else None
        look = (border, text, icon_name, fg)
        if look == self._look:
            return
        old = self._look or (None, None, None, None)
        self._look = look
        if (border, fg) != (old[0], old[3]):
            self.restyle(fill=fg or self._box_outer, border=border)
        if (text, icon_name) != old[1:3]:
            # Цвет текста и иконка меняются только при смене вида или выключении, не при наведении
            canvas = tk.Canvas
            self._icon_photo = light.photo_of(self, icon(icon_name, text, 14))
            canvas.itemconfigure(self, self._icon_item, image=self._icon_photo)
            canvas.itemconfigure(self, self._text_item, fill=text)
            canvas.itemconfigure(self, self._kbd_text, fill=text)
            kbd_w, kbd_h = self._kbd_size()
            frame_color = theme.blend(text, C["bg_surface"], 0.5)
            self._kbd_photo = shared_photo(self, ("kbd", kbd_w, kbd_h, frame_color),
                                           lambda: _outline_rgba(kbd_w, kbd_h, frame_color, px(self, 3)))
            canvas.itemconfigure(self, self._kbd_item, image=self._kbd_photo)
        self._place()

    def _follow_surface(self, color):
        self._box_outer = color
        self._look = None
        self._paint()

    def set_kind(self, kind, text=None):
        self.kind = kind
        if text is not None and text != self._text:
            self.set_text(text)
        self._paint()

    def set_text(self, text):
        if text != self._text:
            self._text = text
            tk.Canvas.itemconfigure(self, self._text_item, text=text)
            self._place()

    @property
    def text(self):
        return self._text


@lru_cache(maxsize=32)
def _outline_rgba(w, h, color, radius):
    """Рамочка 1 px со скруглением и прозрачной серединой (рамочка клавиши «F9» на кнопке)."""
    k = 4
    img = Image.new("RGBA", (w * k, h * k), (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=radius * k,
                                          outline=_rgb(color) + (255,), width=k)
    return img.resize((w, h), Image.LANCZOS)


class Field(light.Frame):
    """Поле ввода с подписью сверху и подсказкой снизу (экран 8). Состояния: обычное; в фокусе — рамка 2 px синяя;
    ошибка (set_error) — рамка 2 px красная, текст ошибки под полем; недоступно (set_enabled(False)) — серый текст.
    Поле — light.Entry (рамка-холст и поле Tk), подписи — light.Label."""

    def __init__(self, master, label="", hint="", value="", mono=True, width=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.hint = hint
        self.error = None
        self.enabled = True
        self._look = (1, C["border"], C["bg_elevated"], C["text"])  # так поле создаётся ниже
        self.grid_columnconfigure(0, weight=1)
        self.label = light.Label(self, text=label, font=F["label"], text_color=C["text_secondary"], anchor="w",
                                 height=18)
        self.label.grid(row=0, column=0, sticky="w", pady=(0, 6))
        self.entry = light.Entry(self, height=S["control_height"], width=width or 140,
                                 corner_radius=S["radius_control"], border_width=1, border_color=C["border"],
                                 fg_color=C["bg_elevated"], text_color=C["text"],
                                 font=F["mono_field"] if mono else F["body"])
        self.entry.grid(row=1, column=0, sticky="ew")
        self.entry.insert(0, str(value))
        self.note = light.Label(self, text=hint, font=F["label"], text_color=C["text_muted"], anchor="w", height=18,
                                compound="left")
        self.note.grid(row=2, column=0, sticky="w", pady=(6, 0))
        if not hint:
            self.note.grid_remove()
        self._focus = False
        self.entry.bind("<FocusIn>", lambda _e: self._set_focus(True), add="+")
        self.entry.bind("<FocusOut>", lambda _e: self._set_focus(False), add="+")

    def _set_focus(self, focus):
        self._focus = focus
        self._paint(focus)

    def _paint(self, focus=False):
        if not self.enabled:
            look = (1, C["border"], T["field_disabled_bg"], C["text_muted"])
        elif self.error:
            look = (2, C["danger"], T["field_error_bg"], C["text"])
        elif focus:
            look = (2, C["blue"], C["bg_elevated"], C["text"])
        else:
            look = (1, C["border"], C["bg_elevated"], C["text"])
        if look == self._look:  # толщина рамки перестраивает поле — только если вид правда поменялся
            return
        self._look = look
        width, border, fg, text = look
        self.entry.configure(border_width=width, border_color=border, fg_color=fg, text_color=text)

    def show_focus(self):
        """Нарисовать поле «в фокусе», не забирая фокус (для витрины)."""
        self._paint(focus=True)

    def set_error(self, message):
        """Показать ошибку под полем; None — убрать её и вернуть подсказку."""
        self.error = message
        if message:
            # Пробел — зазор между значком и текстом (у надписи нет своего отступа для картинки)
            self.note.configure(text=" " + message, text_color=C["danger_text"],
                                image=icon("triangle-alert", C["danger_text"], 13))
            self.note.grid()
        else:
            self.note.configure(text=self.hint, text_color=C["text_muted"], image=None)
            if self.hint:
                self.note.grid()
            else:
                self.note.grid_remove()
        self._paint(focus=self._focus)

    def set_hint(self, hint):
        self.hint = hint
        if not self.error:
            self.set_error(None)

    def set_enabled(self, enabled, hint=None):
        """Недоступное поле (например, во время фарма); hint — почему его нельзя менять."""
        self.enabled = enabled
        self.entry.configure(state="normal" if enabled else "disabled")
        if hint is not None:
            self.set_hint(hint)
        self._paint()

    def get(self):
        return self.entry.get()

    def set(self, value):
        state = self.entry.cget("state")
        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, str(value))
        self.entry.configure(state=state)


class Switch(light.Scaled, PlainSwitch):
    """Тумблер 40×22 (макет 03a): включён — синий трек и белая ручка, выключен — серый трек и серая ручка.
    command(включён) — после переключения мышью (и toggle()); set_on() меняет положение без вызова command.
    Одна надпись Tk с готовой картинкой (PlainSwitch), а не холст CTkSwitch."""

    def __init__(self, master, value=False, command=None, bg_color=None, **kwargs):
        super().__init__(master, value=value, command=command, size=(40, 22),
                         bg=surface(master) if light.transparent(bg_color) else bg_color)

    def is_on(self):
        return bool(self.on)

    def toggle(self):
        """Как щелчок мышью (и как CTkSwitch.toggle): переключить и позвать command."""
        self._clicked()


def plain_disc(master, size, color):
    """Кружок цвета color на прозрачном фоне (картинка для обычной надписи Tk: номер места поверх — compound="center").
    Прозрачные уголки: при наведении надпись меняет только свой фон — без новой картинки."""
    scale = light.scale_of(master)
    return ImageTk.PhotoImage(_disc_picture(round(size * scale), color), master=master)


@lru_cache(maxsize=16)
def _disc_picture(px, color):
    k = 4
    rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
    img = Image.new("RGBA", (px * k, px * k), rgb + (0,))
    ImageDraw.Draw(img).ellipse((0, 0, px * k - 1, px * k - 1), fill=rgb + (255,))
    return img.resize((px, px), Image.LANCZOS)


class Dropdown(ClickFrame):
    """Выпадающий список в цветах поля ввода (макет 03a: «Титанит ▾», «05:00»): высота 36, слева значок (по желанию),
    надпись, справа стрелка. Пункты — (ключ, надпись); command(ключ) — после выбора. icons — {ключ: (иконка, цвет)}.
    Список — PopupMenu (шаг 6а.3: своё окошко вместо меню Windows с белой рамкой).
    Шаг 5б (макет 03b): badge — номер места в кружке слева («1» в «Приоритете дверей»), colors — {ключ: цвет надписи}
    (стихия своим цветом), breaks — с каких пунктов начинать новую колонку меню (длинный список титанов — по стихиям).
    Шаг 8 (макет 03d): titans=True — ключи пунктов — титаны, и вместо значка слева в поле стоит квадрат выбранного титана
    с картинкой (пока картинки нет — две буквы имени на языке lang); в раскрытом списке — одни имена.
    Внутри — обычные надписи Tk, рамка — холст Tk (ClickFrame): у CustomTkinter свой холст на каждую надпись, а списков
    на вкладке много — в Windows они дорисовывались с задержкой. Наведение меняет только цвет фона рамки и надписей."""

    def __init__(self, master, items, value, command=None, icons=None, width=140, mono=False, badge=None,
                 colors=None, breaks=(), titans=False, lang="RU", **kwargs):
        super().__init__(master, command=self.open, width=width, height=S["control_height"],
                         corner_radius=S["radius_control"], border_width=1, border_color=C["border"],
                         fg_color=C["bg_elevated"], **kwargs)
        self.items = list(items)
        self.value = value
        self.icons = icons or {}
        self.colors = colors or {}
        self.titans = titans
        self.lang = lang           # язык окна: две буквы имени, пока у титана нет картинки
        self.breaks = set(breaks)
        self.on_choose = command
        self._look = None
        self._pictures = {}
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        bg = C["bg_elevated"]
        self._badge = None
        if badge is not None:
            self._disc = plain_disc(self, 22, C["bg_primary"])
            self._badge = tk.Label(self, text=str(badge), image=self._disc, compound="center", bg=bg,
                                   fg=C["text_secondary"], font=scaled_font(self, F["label"]), bd=0,
                                   highlightthickness=0, padx=0, pady=0)
            self._badge.grid(row=0, column=0, padx=(8, 0))
        self._icon_label = tk.Label(self, bg=bg, bd=0, highlightthickness=0, padx=0, pady=0)
        self._label = PlainLabel(self, "", font=F["mono_field"] if mono else F["body"], color=C["text"], bg=bg,
                                 anchor="w")
        self._label.grid(row=0, column=2, sticky="ew", padx=(10, 4))
        self._arrow_picture = plain_icon(self, "chevron-down", C["text_muted"], 16)
        self._arrow = tk.Label(self, image=self._arrow_picture, bg=bg, bd=0, highlightthickness=0)
        self._arrow.grid(row=0, column=3, padx=(0, 10))
        self._parts = [p for p in (self._badge, self._icon_label, self._label, self._arrow) if p is not None]
        self.bind_parts(*self._parts)
        self.menu = PopupMenu(self)
        self._fill_menu()
        self._show_value()
        self._paint()

    def _paint(self):
        look = T["hover_elevated"] if self._hovering and self.enabled else C["bg_elevated"]
        if look != self._look:
            self._look = look
            self.configure(fg_color=look)
            for part in self._parts:
                part.configure(bg=look)

    def _icon_picture(self, name, color):
        key = (name, color)
        if key not in self._pictures:
            self._pictures[key] = plain_icon(self, name, color, 15)
        return self._pictures[key]

    def _show_value(self):
        text = next((t for k, t in self.items if k == self.value), str(self.value))
        if self._label.cget("text") != text:
            self._label.configure(text=text)
        color = self.colors.get(self.value, C["text"])
        if self._label.cget("fg") != color:
            self._label.configure(fg=color)
        if self.titans and self.value:
            photo, has_picture = titan_photo(self, self.value, S["avatar_small"])
            scale = light.scale_of(self)
            self._icon_label.configure(image=photo, compound="center", fg=C["text"],
                                       text="" if has_picture else theme.initials(titan_name(self.lang, self.value)),
                                       font=(theme.FONT_FAMILY, -round(10 * scale), "bold"))
            self._icon_label.photo = photo
            self._icon_label.grid(row=0, column=1, padx=(8, 0))
            self._label.grid_configure(padx=(8, 4))
        elif self.value in self.icons:
            self._icon_label.configure(image=self._icon_picture(*self.icons[self.value]))
            self._icon_label.grid(row=0, column=1, padx=(10, 0))
            self._label.grid_configure(padx=(8, 4))
        else:
            self._icon_label.grid_forget()
            self._label.grid_configure(padx=(10, 4))

    def _fill_menu(self):
        self.menu.set_values([text for _k, text in self.items], self._chosen, menu_breaks(self.items, self.breaks))

    def open(self):
        if self.menu.is_open():
            self.menu.close()
            return
        open_under(self.menu, self)

    def _chosen(self, text):
        key = next((k for k, t in self.items if t == text), None)
        if key is None:
            return
        self.set(key)
        if self.on_choose:
            self.on_choose(key)

    def set(self, value):
        self.value = value
        self._show_value()

    def get(self):
        return self.value

    def set_items(self, items):
        """Новые надписи (другой язык)."""
        self.items = list(items)
        self._fill_menu()
        self._show_value()

    def destroy(self):
        self.menu.destroy()  # окошко списка живёт у окна, а не у поля: убираем вместе с полем
        super().destroy()


# Значок диалога: иконка, её цвет, цвет подложки; кнопка подтверждения по умолчанию (вид и иконка)
DIALOG_KINDS = {
    "danger": dict(icon="trash-2", color=C["danger_text"], bg=T["danger_on_surface"],
                   button="danger_solid", button_icon="trash-2"),
    "warning": dict(icon="triangle-alert", color=C["warning"], bg=T["warning_on_surface"],
                    button="save", button_icon="save"),
    "info": dict(icon="info", color=C["blue_text"], bg=T["blue_icon_bg"], button="blue", button_icon=None),
}


def icon_badge(master, icon_name, color, tint, box=40, size=20, radius=10):
    """Значок в цветной подложке (окна подтверждения, SOS, Telegram, «Собери состав»): одна надпись Tk с готовой
    картинкой — квадрат box × box цвета tint со скруглением radius, иконка size по центру."""
    photo = plain_icon(master, icon_name, color, size, box=box, tint=tint, bg=surface(master), radius=radius)
    label = BadgeLabel(master, image=photo, bg=surface(master), bd=0, highlightthickness=0, padx=0, pady=0)
    label.photo = photo
    return label


class BadgeLabel(light.Scaled, tk.Label):
    """Надпись-значок icon_badge: отступы в раскладке — в пикселях макета (как у подложки CustomTkinter, которую она заменила)."""


class DialogBody(light.Box):
    """Содержимое диалога подтверждения (экран 8): значок 40×40 в цветной подложке, заголовок, текст, кнопки справа.
    discard_text — третья кнопка слева красным текстом («Не сохранять»). Сам по себе не окно: окно — ConfirmDialog."""

    def __init__(self, master, title, text, confirm_text, cancel_text, kind="danger", on_confirm=None,
                 on_cancel=None, discard_text=None, on_discard=None, confirm_kind=None, confirm_icon=None,
                 wraplength=380, on_close=None, lang="RU", **kwargs):
        kwargs.setdefault("fg_color", C["bg_surface"])
        kwargs.setdefault("corner_radius", S["radius_dialog"])
        super().__init__(master, **kwargs)
        look = DIALOG_KINDS[kind]
        self.grid_columnconfigure(1, weight=1)

        icon_badge(self, look["icon"], look["color"], look["bg"]).grid(row=0, column=0, rowspan=2, sticky="n",
                                                                      padx=(20, 14), pady=(20, 0))
        light.Label(self, text=title, font=F["dialog_title"], text_color=C["text"], anchor="w",
                    justify="left").grid(row=0, column=1, sticky="w", padx=(0, 20), pady=(20, 6))
        light.Label(self, text=text, font=F["text"], text_color=C["text_secondary"], anchor="w", justify="left",
                    wraplength=wraplength).grid(row=1, column=1, sticky="w", padx=(0, 20))

        self.close_button = None
        if on_close:    # окно без рамки Windows (шаг 6а.3): крестик в правом верхнем углу, вровень с заголовком
            self.close_button = close_button(self, on_close, lang, kwargs["fg_color"])
            self.close_button.grid(row=0, column=2, sticky="ne", padx=(0, 10), pady=(10, 0))

        row = light.Frame(self, fg_color="transparent", width=10, height=10)
        row.grid(row=2, column=0, columnspan=3, sticky="ew", padx=20, pady=20)
        if discard_text:
            Button(row, discard_text, kind="ghost_danger", height=S["button_height_footer"], pad_x=12,
                   command=on_discard).pack(side="left")
        self.confirm_button = Button(row, confirm_text, kind=confirm_kind or look["button"],
                                     icon_name=confirm_icon if confirm_icon is not None else look["button_icon"],
                                     icon_size=14, height=S["button_height_footer"], command=on_confirm)
        self.confirm_button.pack(side="right")
        self.cancel_button = Button(row, cancel_text, kind="secondary", height=S["button_height_footer"],
                                    command=on_cancel)
        self.cancel_button.pack(side="right", padx=(0, 10))


class ConfirmDialog(AppWindow):
    """Модальное окно подтверждения: «Удалить все правила?», «Сохранить изменения?» и т.п.
    Закрытие крестиком или Esc — то же, что «Отмена». Обработчик вызывается после закрытия окна."""

    def __init__(self, master, title, text, confirm_text, on_confirm=None, kind="danger", lang="RU",
                 cancel_text=None, on_cancel=None, discard_text=None, on_discard=None, confirm_kind=None,
                 confirm_icon=None):
        root = master.winfo_toplevel()
        super().__init__(root, fg_color=C["bg_surface"])
        self.withdraw()
        self.title(title)
        self.resizable(False, False)
        self.transient(root)
        self._handlers = {"confirm": on_confirm, "cancel": on_cancel, "discard": on_discard}
        self.body = DialogBody(self, title, text, confirm_text, cancel_text or get_text(lang, "btn_cancel"),
                               kind=kind, discard_text=discard_text, confirm_kind=confirm_kind,
                               confirm_icon=confirm_icon, on_confirm=lambda: self._finish("confirm"),
                               on_cancel=lambda: self._finish("cancel"),
                               on_discard=lambda: self._finish("discard"), corner_radius=0,
                               on_close=lambda: self._finish("cancel"), lang=lang)
        self.body.pack(fill="both", expand=True)
        self.make_movable(self.body)
        self._done = False
        self.protocol("WM_DELETE_WINDOW", lambda: self._finish("cancel"))
        self.bind("<Escape>", lambda _e: self._finish("cancel"))
        grab = hold_grab(self, blocked=lambda: self._done, on_grab=lambda: self.body.cancel_button.focus_set())
        present_window(self, lambda: self._place_centered(root), hidden=lambda: self._done, on_shown=grab)

    def _place_centered(self, root):
        w, h = requested_size(self)
        ax, ay, aw, ah = anchor_area(root)
        x = ax + (aw - w) // 2
        y = ay + (ah - h) // 3
        self.geometry(f"+{max(0, x)}+{max(0, y)}")

    def close(self):
        """Закрыть без ответа (вопрос устарел: например, бот уже решил сам)."""
        if self._done:
            return
        self._done = True
        try:
            self.grab_release()
            self.destroy()
        except tk.TclError:
            pass

    @property
    def done(self):
        return self._done

    def _finish(self, result):
        if self._done:  # двойной щелчок или Esc после кнопки — второй раз не обрабатываем
            return
        self._done = True
        try:
            self.grab_release()
        except tk.TclError:
            pass
        self.destroy()
        handler = self._handlers.get(result)
        if handler:
            handler()


# Значки уведомлений: иконка и её цвет
TOAST_KINDS = {
    "success": ("check", C["success"]),
    "deleted": ("trash-2", C["text_secondary"]),
    "info": ("info", C["blue_text"]),
    "warning": ("triangle-alert", C["warning"]),
    "error": ("triangle-alert", C["danger_text"]),
}


class LoadingCover(tk.Frame):
    """Заслонка поверх страницы, пока страница достраивается (сессия 11: страница проступала кусками — рамки, потом
    заголовки, потом текст): фон страницы и крутящееся кольцо посередине. show() и hide(); кольцо крутится, только пока
    заслонку видно (одна картинка на холсте: каждый шаг меняет только угол дуги)."""

    SPIN_MS = 60
    SIZE = 36

    def __init__(self, master, bg):
        super().__init__(master, bg=bg, bd=0, highlightthickness=0)
        size, width = px(master, self.SIZE), px(master, 4)
        self.ring = tk.Canvas(self, width=size, height=size, bg=bg, highlightthickness=0, bd=0)
        self.ring.place(relx=0.5, rely=0.5, anchor="center")
        box = (width, width, size - width, size - width)
        self.ring.create_oval(*box, outline=C["border"], width=width)
        self._arc = self.ring.create_arc(*box, start=90, extent=100, style="arc", outline=C["blue_button"], width=width)
        self._angle = 90
        self._timer = None
        self.shown = False

    def show(self):
        if self.shown:
            return
        self.shown = True
        tk.Place.place_configure(self, x=0, y=0, relwidth=1, relheight=1)
        tk.Misc.tkraise(self)
        self._spin()

    def hide(self):
        if not self.shown:
            return
        self.shown = False
        self._stop()
        self.place_forget()

    def _spin(self):
        self._timer = None
        if not self.shown:
            return
        self._angle = (self._angle - 30) % 360
        self.ring.itemconfigure(self._arc, start=self._angle)
        try:
            self._timer = self.after(self.SPIN_MS, self._spin)
        except tk.TclError:
            self._timer = None

    def _stop(self):
        if self._timer:
            try:
                self.after_cancel(self._timer)
            except tk.TclError:
                pass
            self._timer = None

    def destroy(self):
        self._stop()
        super().destroy()


class ToastBody(light.Box):
    """Содержимое уведомления (экран 8): значок, текст, кнопка действия («Вернуть»), крестик."""

    def __init__(self, master, text, kind="success", action_text=None, on_action=None, on_close=None, **kwargs):
        kwargs.setdefault("bg_color", "transparent")
        super().__init__(master, height=S["toast_height"], width=10, fg_color=C["bg_elevated"], border_width=1,
                         border_color=C["border_strong"], corner_radius=8, **kwargs)
        name, color = TOAST_KINDS[kind]
        light.Label(self, text="", image=icon(name, color, 16), width=16).pack(side="left", padx=(14, 10), pady=4)
        light.Label(self, text=text, font=F["text"], text_color=C["text"]).pack(side="left", pady=4)
        if action_text:
            Button(self, action_text, kind="link", height=28, pad_x=10, border_width=1,
                   border_color=C["border_strong"], font=F["button_bold"], command=on_action).pack(
                side="left", padx=(14, 0), pady=7)
        IconButton(self, "x", size=28, icon_size=13, icon_color=C["text_muted"], fg_color="transparent",
                   hover_color=C["bg_surface"], border_width=0, command=on_close).pack(side="left", padx=(6, 8))

    def natural_size(self):
        """Размер, который уведомлению даст раскладка (как pack: части в ряд с отступами), — сразу. Раскладка сама
        считает его только в своём проходе «потом», а уведомление должно появиться сразу (сессия 11б: пока окно
        было занято, проход «потом» не наступал, и уведомление закрывалось по таймеру, так и не показавшись)."""
        def total(value):
            parts = value if isinstance(value, (tuple, list)) else str(value).split()
            parts = [int(float(p)) for p in parts] or [0]
            return sum(parts) if len(parts) > 1 else 2 * parts[0]
        width, height = 0, 0
        for part in self.pack_slaves():
            info = part.pack_info()
            width += part.winfo_reqwidth() + total(info.get("padx", 0)) + 2 * int(info.get("ipadx", 0))
            height = max(height, part.winfo_reqheight() + total(info.get("pady", 0)) + 2 * int(info.get("ipady", 0)))
        return width, height


class Toast:
    """Короткое уведомление в правом нижнем углу окна программы, на 4 с. Несколько уведомлений встают друг над другом.
    Окно программы свёрнуто — уведомление не показывается (не закрывать им игру)."""

    _open = []

    def __init__(self, master, text, kind="success", action_text=None, on_action=None, duration=None):
        self.root = master.winfo_toplevel()
        self.on_action = on_action
        self.top = None
        if self.root.state() != "normal" and self.root.state() != "zoomed":
            return
        self.top = _frameless_window(self.root)
        self.body = ToastBody(self.top, text, kind=kind, action_text=action_text, on_action=self._action,
                              on_close=self.close, bg_color=_CORNER_COLOR)
        self.body.pack()
        Toast._open.append(self)
        # Сразу на место и на экран: размер — natural_size (без прохода раскладки «потом» и без update_idletasks)
        self._timers = [self.top.after(duration or S["toast_ms"], self.close)]
        Toast._restack(self.root)
        try:
            self.top.deiconify()
            self.top.lift()
        except tk.TclError:
            pass

    @classmethod
    def close_all(cls, root=None):
        """Закрыть все уведомления (при закрытии окна программы)."""
        for toast in list(cls._open):
            if root is None or toast.root is root:
                toast.close()

    def _action(self):
        self.close()
        if self.on_action:
            self.on_action()

    def close(self):
        if self.top is None:
            return
        for after_id in self._timers:    # окно закрыли раньше: его «потом» не должно сработать после закрытия программы
            if after_id:
                try:
                    self.top.after_cancel(after_id)
                except tk.TclError:
                    pass
        try:
            self.top.destroy()
        except tk.TclError:
            pass
        self.top = None
        if self in Toast._open:
            Toast._open.remove(self)
        Toast._restack(self.root)

    @classmethod
    def _restack(cls, root):
        """Расставить открытые уведомления окна снизу вверх у правого нижнего угла."""
        try:
            right = root.winfo_rootx() + root.winfo_width() - 24
            bottom = root.winfo_rooty() + root.winfo_height() - 24
        except tk.TclError:
            return
        for toast in reversed([t for t in cls._open if t.root is root and t.top is not None]):
            try:
                w, h = toast.body.natural_size()
                toast.top.geometry(f"{w}x{h}+{right - w}+{bottom - h}")
            except tk.TclError:
                continue
            bottom -= h + 10
