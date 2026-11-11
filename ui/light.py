"""Лёгкие элементы окна (сессия 11): замена рамок, надписей, полей, полос прокрутки CustomTkinter.

Почему (разбор сессии 11, logs/session_11): у CustomTkinter каждый элемент — рамка, холст и надпись (2–4 окна Windows),
а скругления холст рисует десятками фигур кодом Python при каждом изменении размера. В окне программы таких элементов
были сотни: в Windows окно 3 с стояло белым, страницы проступали кусками, а «Мастер правил» строился дольше 5 с
(файлы ui_freeze_*.txt). Полоса прокрутки CustomTkinter при каждом сдвиге звала update_idletasks() — «доделай всё
сейчас», — и в руководстве она вызывала сама себя по кругу (десяток вложенных вызовов в одном файле фриза).

Здесь всё — обычные виджеты Tk, по одному окну Windows на элемент, без кода рисования при раскладке:
- Box — рамка со скруглением и рамкой 1–2 px одним холстом Tk: заливка — фон холста, уголки — четыре маленькие готовые
  картинки, края — четыре полоски; новый размер — только сдвиг уголков, наведение — другие цвета (CTkFrame с углами);
- Frame — плоская рамка (CTkFrame без скругления и «transparent»), Label — надпись (CTkLabel), Entry — поле ввода,
  Textbox — многострочный текст с полосой прокрутки, ProgressBar, SegmentedButton, CheckBox;
- Scrollbar — полоса прокрутки на холсте Tk (set() только сдвигает ползунок, без update_idletasks);
- ScrollArea — прокрутка частями без холста: части — рамки в окне просмотра, видимые на своих местах, ближние ждут
  сразу за краем, дальние запаркованы (разложены, но не показаны — сессия 11б); ни одна не выше и не дальше 32 000 px
  (у Tk координаты окон 16-битные: на одном листе руководство обрывалось на разделе 10); ScrollableFrame — то же
  с одной частью, ведёт себя как CTkScrollableFrame (grid/pack — у внешней рамки);
- Scaled — pack/grid/place с отступами в пикселях макета, как у CustomTkinter (без этого при масштабе Windows 125–150 %
  отступы были бы меньше прежних); размеры считаются так же, как у CustomTkinter (cpx).

Аргументы — как у CustomTkinter (fg_color, text_color, corner_radius, width/height в пикселях макета — масштаб Windows
применяется здесь), чтобы страницы переводились без переделки раскладки. Окна программы (App, AppWindow) остаются
CTk/CTkToplevel: от CustomTkinter нужны масштаб Windows и картинки CTkImage (ui/icons) — их здесь переводят в картинки Tk.
Правила окна (начало ui/widgets.py) те же: в наведении — только цвета, без update_idletasks в обработчиках.
NoAlpha — окнам не ставится -alpha (сессия 11б), still_mapping — показал ли Tk всё внутри (для заслонок).
"""
import sys
import time
import tkinter as tk
from functools import lru_cache

import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk

from ui import theme

C = theme.COLORS
F = theme.FONTS

DEFAULT_FONT = (theme.FONT_FAMILY, 13)          # как CTkFont() по умолчанию
DEFAULT_TEXT = theme.CTK_TEXT                   # цвет текста CTkLabel по умолчанию (тёмная тема CustomTkinter)


# ── Масштаб, шрифты, цвета ───────────────────────────────────────────────────
def scale_of(widget):
    """Масштаб Windows для виджета (как у CustomTkinter: 1.0, 1.25, 1.5 …). Окошко Tk без элементов CustomTkinter
    (подсказка, список) CustomTkinter не знает — у него масштаб окна программы."""
    try:
        return ctk.ScalingTracker.get_widget_scaling(widget)
    except KeyError:
        try:
            return ctk.ScalingTracker.get_widget_scaling(widget._root())
        except KeyError:
            return 1.0


def px(widget, value):
    """Пиксели макета → настоящие пиксели с масштабом Windows (для простых виджетов Tk: PlainLabel, tk.Frame)."""
    return round(value * scale_of(widget))


def cpx(widget, value):
    """Пиксели макета → настоящие так же, как у CustomTkinter: целое — с отбрасыванием дробной части, дробное —
    как есть (его округлит Tk). Так лёгкие элементы при масштабе Windows 125–150 % того же размера, что и элементы
    CustomTkinter, которые они заменили (px() округляет и где-то давал бы на 1 px больше)."""
    scale = scale_of(widget)
    return value * scale if isinstance(value, float) else int(value * scale)


def scaled_font(widget, font):
    """Шрифт из theme.FONTS для виджета Tk: размер в пикселях с учётом масштаба Windows (как у CustomTkinter)."""
    family, size, *rest = font or DEFAULT_FONT
    return (family, -round(abs(size) * scale_of(widget)), *rest)


def text_width(widget, font, text):
    """Ширина надписи в пикселях (font — как в theme.FONTS, уже без масштаба)."""
    return int(widget.tk.call("font", "measure", scaled_font(widget, font), "-displayof", widget, text))


def line_height(widget, font):
    return int(widget.tk.call("font", "metrics", scaled_font(widget, font), "-displayof", widget, "-linespace"))


def transparent(color):
    return color is None or color == "transparent"


def hex_color(widget, color):
    """Цвет Tk любого вида («gray85», «SystemButtonFace» в Windows) → #RRGGBB: картинки рисуются по числам."""
    if isinstance(color, str) and len(color) == 7 and color.startswith("#"):
        return color
    r, g, b = widget.winfo_rgb(color)
    return "#{:02X}{:02X}{:02X}".format(r // 257, g // 257, b // 257)


def surface(widget):
    """Цвет, на котором стоит виджет (#RRGGBB): заливка лёгкой рамки или карточки (.fill), иначе фон виджета Tk.
    У окна CustomTkinter (CTk, CTkToplevel) фон Tk — его цвет."""
    start = widget
    color = _surface(widget)
    return hex_color(start, color)


def _surface(widget):
    while widget is not None:
        fill = getattr(widget, "fill", None)
        if fill:
            return fill
        if isinstance(widget, (ctk.CTkBaseClass, ctk.CTkScrollableFrame)):   # старый элемент CustomTkinter
            try:
                color = widget.cget("fg_color")
            except (ValueError, tk.TclError):
                color = None
            if not transparent(color):
                return color if isinstance(color, str) else color[1]
        else:
            try:
                return widget.cget("bg")
            except (ValueError, tk.TclError):
                pass
        widget = widget.master
    return C["bg_primary"]


def rgb(color):
    color = color.lstrip("#")
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))


# ── Картинки ─────────────────────────────────────────────────────────────────
def shared_photo(master, key, make):
    """Картинка Tk одна на окно программы, а не на каждый виджет: одинаковых значков и уголков сотни.
    Картинка Tk принадлежит своему окну (интерпретатору Tk), поэтому запас — у корня: новое окно — новый запас.
    make() — картинка PIL. Виджет, который её показывает, держит ссылку сам (если запас её когда-нибудь выбросит)."""
    root = master._root()
    cache = root.__dict__.setdefault("_shared_photos", {})
    photo = cache.get(key)
    if photo is None:
        photo = cache[key] = ImageTk.PhotoImage(make(), master=root)
    return photo


def photo_of(master, image):
    """Картинка для виджета Tk: CTkImage (ui/icons.icon, dot) — в размере с масштабом Windows, картинка PIL — как есть,
    картинка Tk — как есть. Одна на окно программы."""
    if image is None or image == "":
        return None
    if isinstance(image, ctk.CTkImage):
        w, h = image.cget("size")
        size = (max(1, round(w * scale_of(master))), max(1, round(h * scale_of(master))))
        root = master._root()
        cache = root.__dict__.setdefault("_ctk_photos", {})
        key = (id(image), size)
        entry = cache.get(key)
        if entry is None or entry[1] is not image:
            pil = image.cget("dark_image") or image.cget("light_image")
            photo = ImageTk.PhotoImage(pil.resize(size, Image.LANCZOS) if pil.size != size else pil, master=root)
            entry = cache[key] = (photo, image)      # CTkImage держим: его id не достанется другой картинке
        return entry[0]
    if isinstance(image, Image.Image):
        return ImageTk.PhotoImage(image, master=master)
    return image


def blank_photo(master):
    """Прозрачная картинка 1×1: с ней ширина и высота надписи Tk — в пикселях, а не в буквах."""
    return shared_photo(master, ("blank",), lambda: Image.new("RGBA", (1, 1), (0, 0, 0, 0)))


@lru_cache(maxsize=512)
def corner_picture(radius, fill, border, outer, border_width, which="nw"):
    """Уголок скруглённой рамки radius × radius (PIL): рисуется в 4 раза крупнее и уменьшается — края гладкие.
    which — какой угол: nw, ne, sw, se. border — цвет рамки (None — без рамки)."""
    k = 4
    side = 2 * radius * k
    big = Image.new("RGB", (side, side), rgb(outer))
    ImageDraw.Draw(big).rounded_rectangle((0, 0, side - 1, side - 1), radius=radius * k, fill=rgb(fill),
                                          outline=rgb(border) if border and border_width else None,
                                          width=border_width * k if border and border_width else 0)
    tile = big.resize((2 * radius, 2 * radius), Image.LANCZOS).crop((0, 0, radius, radius))
    if which == "ne":
        tile = tile.transpose(Image.FLIP_LEFT_RIGHT)
    elif which == "sw":
        tile = tile.transpose(Image.FLIP_TOP_BOTTOM)
    elif which == "se":
        tile = tile.transpose(Image.ROTATE_180)
    return tile


def rounded_picture(w, h, fill, border, outer, radius, border_width=1):
    """Скруглённый прямоугольник w × h (PIL): заливка одним цветом, рамка — линиями, четыре готовых уголка.
    Без рисования всей картинки в 3–4 раза крупнее: так большая карточка рисуется за доли миллисекунды."""
    w, h = max(1, int(w)), max(1, int(h))
    img = Image.new("RGB", (w, h), rgb(fill))
    if border and border_width:
        ImageDraw.Draw(img).rectangle((0, 0, w - 1, h - 1), outline=rgb(border), width=border_width)
    r = min(int(radius), w // 2, h // 2)
    if r > 0:
        for which, at in (("nw", (0, 0)), ("ne", (w - r, 0)), ("sw", (0, h - r)), ("se", (w - r, h - r))):
            img.paste(corner_picture(r, fill, border if border_width else None, outer, border_width, which), at)
    return img


@lru_cache(maxsize=128)
def pill_rgba(w, h, fill, radius):
    """Скруглённая плашка с прозрачными уголками (PIL, RGBA) — для рисунка на холсте: под уголками видно то, что
    нарисовано под плашкой (заливка таблетки при наведении тоже)."""
    k = 4
    img = Image.new("RGBA", (w * k, h * k), rgb(fill) + (0,))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=radius * k, fill=rgb(fill) + (255,))
    return img.resize((w, h), Image.LANCZOS)


def rounded_photo(master, w, h, fill, border, outer, radius, border_width=1):
    """Скруглённый прямоугольник картинкой Tk (одна на окно для одного размера и цветов)."""
    key = ("rounded", w, h, fill, border, outer, radius, border_width)
    return shared_photo(master, key, lambda: rounded_picture(w, h, fill, border, outer, radius, border_width))


# ── Раскладка в пикселях макета ──────────────────────────────────────────────
def scaled_geometry(widget, options):
    """Как у CustomTkinter: padx, pady (число или пара) и x, y у place — в пикселях макета, на масштаб Windows (cpx)."""
    if scale_of(widget) == 1:
        return options
    options = dict(options)
    for key in ("padx", "pady"):
        value = options.get(key)
        if isinstance(value, (int, float)):
            options[key] = cpx(widget, value)
        elif isinstance(value, tuple):
            options[key] = tuple(cpx(widget, v) for v in value)
    for key in ("x", "y"):
        if isinstance(options.get(key), (int, float)):
            options[key] = cpx(widget, options[key])
    return options


class Scaled:
    """pack, grid и place как у элементов CustomTkinter: отступы — в пикселях макета (scaled_geometry). Лёгкие элементы
    заменили элементы CustomTkinter, и раскладка страниц написана в этих единицах: без этого при масштабе Windows
    125–150 % все отступы стали бы меньше, чем были. У простых виджетов Tk (tk.Frame, PlainLabel) отступы — через px()."""

    def pack_configure(self, cnf={}, **kw):    # noqa: B006 — как у tkinter
        tk.Pack.pack_configure(self, cnf, **scaled_geometry(self, kw))

    pack = pack_configure

    def grid_configure(self, cnf={}, **kw):    # noqa: B006
        tk.Grid.grid_configure(self, cnf, **scaled_geometry(self, kw))

    grid = grid_configure

    def place_configure(self, cnf={}, **kw):   # noqa: B006
        tk.Place.place_configure(self, cnf, **scaled_geometry(self, kw))

    place = place_configure


# ── События окна о себе ──────────────────────────────────────────────────────
OWN_EVENTS = ("<Configure>", "<Map>", "<Unmap>", "<FocusIn>")


class OwnEvents:
    """Для окон (CTk, CTkToplevel): bind на события окна о себе (<Configure>, <Map>, <Unmap>, <FocusIn>) — на свой тег,
    который есть только у самого окна. Tk кладёт имя окна в bindtags каждого виджета внутри, и window.bind на эти события
    срабатывал на каждое изменение размера и каждый показ любого виджета окна: при переходе на «Мастер правил» — сотни
    вызовов (App._on_map), при постройке руководства — тысячи (и CustomTkinter, и наши обработчики; сессия 11).
    Обработчики и так смотрели только на event.widget is окно — теперь их и не зовут зря."""

    def _own_tag(self):
        tag = getattr(self, "_own_events_tag", None)
        if tag is None:
            tag = self._own_events_tag = "Own" + self._w
            tags = self.tk.splitlist(self.tk.call("bindtags", self._w))
            self.tk.call("bindtags", self._w, (tags[0], tag) + tuple(tags[1:]))
        return tag

    def bind(self, sequence=None, func=None, add=None):
        if sequence in OWN_EVENTS:
            return self._bind(("bind", self._own_tag()), sequence, func, add)
        return super().bind(sequence, func, add)

    def unbind(self, sequence, funcid=None):
        if sequence not in OWN_EVENTS:
            return super().unbind(sequence, funcid)
        tag = self._own_tag()
        if funcid is None:
            self.tk.call("bind", tag, sequence, "")
            return None
        script = self.tk.call("bind", tag, sequence)
        kept = "\n".join(line for line in script.split("\n") if line and funcid not in line)
        self.tk.call("bind", tag, sequence, kept)
        self.deletecommand(funcid)
        return None


class NoAlpha:
    """Для окон (CTk, CTkToplevel): прозрачность -alpha не ставится (сессия 11б). Tk в Windows, однажды сделав окно
    «полупрозрачным» (WS_EX_LAYERED), обратно его не возвращает никогда («Only ever add the WS_EX_LAYERED bit» в исходниках
    Tk), даже при -alpha 1: такое окно Windows перерисовывает медленнее, и с сессии 11 так жило окно программы. Сами мы
    -alpha больше не ставим (окно появляется из-под «плаща», win_frame.cloak); CustomTkinter ставит её на миг, когда окно
    переехало на экран с другим масштабом (0.15 и обратно 1) — этот миг пропускаем, окно просто перестраивается."""

    def wm_attributes(self, *args, **kwargs):
        if "-alpha" in args or "alpha" in kwargs:
            args = list(args)
            if "-alpha" in args and args.index("-alpha") + 1 < len(args):
                i = args.index("-alpha")
                del args[i:i + 2]
            kwargs.pop("alpha", None)
            if not args and not kwargs:
                return None
        return super().wm_attributes(*args, **kwargs)

    attributes = wm_attributes


def still_mapping(widget):
    """Tk ещё показывает элементы внутри widget (True) или уже показал всё, что разложено. Показ идёт по уровням: каждый
    контейнер показывает своих детей, когда покажут его самого, — по проходу «потом» на уровень. Спрятанные нарочно
    (grid_remove, pack_forget — у них нет раскладки) и запаркованные (_parked: страница или часть прокрутки, которую
    держат разложенной, но не показанной) не ждём; отдельные окна (подсказки, диалоги) — тоже."""
    stack = [widget]
    while stack:
        current = stack.pop()
        try:
            if not current.winfo_ismapped():
                if current.winfo_manager() and not getattr(current, "_parked", False):
                    return True
                continue
            stack.extend(child for child in current.winfo_children() if not isinstance(child, (tk.Tk, tk.Toplevel)))
        except tk.TclError:
            continue
    return False


# ── Рамки ────────────────────────────────────────────────────────────────────
def _set_surface_of_children(widget, color):
    """Рамка сменила заливку: «прозрачные» лёгкие элементы внутри берут новый цвет (как CTkFrame.configure(fg_color))."""
    for child in widget.winfo_children():
        follow = getattr(child, "_follow_surface", None)
        if follow is not None:
            follow(color)


def configure_keeping_size(widget, cls, **options):
    """configure рамки или холста Tk без скачка раскладки. Tk при любом configure заново просит у раскладки размер из
    своих width и height (у рамки CustomTkinter по умолчанию 200, у контейнеров 10), хотя размер задают дети: на миг
    рамка сжималась бы, и вся страница раскладывалась бы заново (при наведении — на каждое движение мыши).
    Поэтому, если внутри есть дети, просим тот же размер, что и сейчас: Tk такую просьбу пропускает."""
    if widget.pack_slaves() or widget.grid_slaves():
        options.setdefault("width", widget.winfo_reqwidth())
        options.setdefault("height", widget.winfo_reqheight())
    cls.configure(widget, **options)


class Frame(Scaled, tk.Frame):
    """Плоская рамка вместо CTkFrame без скругления: fg_color="transparent" — цвет того, на чём стоит.
    width и height — в пикселях макета (у CTkFrame по умолчанию 200: контейнерам раскладки давай 10)."""

    def __init__(self, master, fg_color="transparent", width=200, height=200, corner_radius=None, border_width=0,
                 border_color=None, bg_color=None, cursor="", **kwargs):
        self._fg_color = fg_color
        self._transparent = transparent(fg_color)
        self.fill = surface(master) if self._transparent else fg_color
        self._width, self._height = width, height
        super().__init__(master, bg=self.fill, width=cpx(master, width), height=cpx(master, height), bd=0,
                         highlightthickness=0, cursor=cursor, **kwargs)

    def _follow_surface(self, color):
        if self._transparent and color != self.fill:
            self.fill = color
            configure_keeping_size(self, tk.Frame, bg=color)
            _set_surface_of_children(self, color)

    def configure(self, cnf=None, **kwargs):
        if "fg_color" in kwargs:
            self._fg_color = kwargs.pop("fg_color")
            self._transparent = transparent(self._fg_color)
            color = surface(self.master) if self._transparent else self._fg_color
            if color != self.fill:
                self.fill = color
                kwargs["bg"] = color
                _set_surface_of_children(self, color)
        for key in ("corner_radius", "border_width", "border_color", "bg_color"):
            kwargs.pop(key, None)
        if "width" in kwargs:
            self._width = kwargs["width"]
            kwargs["width"] = cpx(self, kwargs["width"])
        if "height" in kwargs:
            self._height = kwargs["height"]
            kwargs["height"] = cpx(self, kwargs["height"])
        if cnf:
            return tk.Frame.configure(self, cnf, **kwargs)
        if kwargs:
            configure_keeping_size(self, tk.Frame, **kwargs)
        return None

    config = configure

    def cget(self, key):
        if key == "fg_color":
            return self._fg_color
        if key == "width":
            return self._width
        if key == "height":
            return self._height
        return tk.Frame.cget(self, key)


class Box(Scaled, tk.Canvas):
    """Рамка со скруглёнными углами и рамкой 1–2 px одним холстом Tk (вместо CTkFrame с fg_color и corner_radius).
    Заливка — прямоугольник во весь холст, уголки — четыре маленькие готовые картинки, рамка — четыре полоски холста.
    Содержимое кладут прямо в неё (grid/pack/place), у надписей фон — fill (лёгкие элементы с "transparent" берут его
    сами); от краёв — не меньше радиуса, чтобы не закрыть скругление. Новый размер — только сдвиг уголков и полосок;
    restyle (наведение) меняет только цвета рисунков — configure холста при этом не зовётся (configure_keeping_size).
    width и height — в пикселях макета."""

    def __init__(self, master, fg_color=None, border_color=None, border_width=0, corner_radius=6, width=200,
                 height=200, bg_color=None, cursor="", **kwargs):
        self._box_bg_color = bg_color
        self._box_outer = surface(master) if transparent(bg_color) else bg_color
        self._box_fg_color = fg_color
        self._box_transparent = transparent(fg_color)
        self.fill = self._box_outer if self._box_transparent else fg_color
        self._box_border_color = border_color or C["border"]
        self._box_border_width = border_width or 0
        self._box_radius = corner_radius or 0
        self._box_width, self._box_height = width, height
        self._box_size = None
        self._box_drawn = None
        super().__init__(master, bg=self.fill, highlightthickness=0, bd=0, width=cpx(master, width),
                         height=cpx(master, height), cursor=cursor, **kwargs)
        # Рисунки рамки создаются сразу (спрятанными): так они всегда под надписями и значками наследников
        canvas = tk.Canvas
        self._box_fill_item = canvas.create_rectangle(self, 0, 0, 0, 0, width=0, outline="", fill=self.fill, tags="fill")
        self._box_corners = {which: canvas.create_image(self, 0, 0, anchor=which, state="hidden", tags="corner")
                             for which in ("nw", "ne", "sw", "se")}
        self._box_edges = [canvas.create_rectangle(self, 0, 0, 0, 0, width=0, outline="", state="hidden", tags="edge")
                           for _ in range(4)]
        tk.Canvas.bind(self, "<Configure>", self._box_resized, add="+")   # явно: у Entry и Textbox bind — у поля внутри

    # Холст Tk: lift/lower/focus у него — для рисунков. У рамки — как у обычного виджета.
    def lift(self, above=None):
        tk.Misc.tkraise(self, above)

    tkraise = lift

    def lower(self, below=None):
        tk.Misc.lower(self, below)

    def focus(self):
        tk.Misc.focus_set(self)

    def _box_resized(self, event):
        size = (event.width, event.height)
        if size != self._box_size:
            self._box_size = size
            self._box_draw()

    def _box_look(self):
        bw = cpx(self, self._box_border_width) if self._box_border_width else 0
        border = self._box_border_color if bw else None
        return (self._box_size, min(cpx(self, self._box_radius), self._box_size[0] // 2, self._box_size[1] // 2), self.fill, border,
                self._box_outer, bw)

    def _box_draw(self):
        if self._box_size is None:
            return
        look = self._box_look()
        if look == self._box_drawn:
            return
        self._box_drawn = look
        (w, h), r, fill, border, outer, bw = look
        canvas = tk.Canvas    # явно: у Entry и Textbox свои insert, delete, index (как у полей Tk)
        canvas.coords(self, self._box_fill_item, 0, 0, w, h)
        canvas.itemconfigure(self, self._box_fill_item, fill=fill)
        if r > 0:
            for which, x, y in (("nw", 0, 0), ("ne", w, 0), ("sw", 0, h), ("se", w, h)):
                key = ("corner", r, fill, border, outer, bw, which)
                photo = shared_photo(self, key, lambda which=which: corner_picture(r, fill, border, outer, bw, which))
                item = self._box_corners[which]
                canvas.coords(self, item, x, y)
                canvas.itemconfigure(self, item, image=photo, state="normal")
        else:
            for item in self._box_corners.values():
                canvas.itemconfigure(self, item, state="hidden")
        boxes = []
        if border:
            boxes = [(r, 0, w - r, bw), (r, h - bw, w - r, h), (0, r, bw, h - r), (w - bw, r, w, h - r)]
        for i, item in enumerate(self._box_edges):
            if i < len(boxes):
                canvas.coords(self, item, *boxes[i])
                canvas.itemconfigure(self, item, fill=border, state="normal")
            else:
                canvas.itemconfigure(self, item, state="hidden")
        self._after_box_draw()

    def _after_box_draw(self):
        """Рамка перерисована (новый размер или цвета): наследник раскладывает свои рисунки (надпись кнопки)."""

    @property
    def outer(self):
        """Цвет за скруглёнными углами (то, на чём рамка стоит)."""
        return self._box_outer

    def restyle(self, fill=None, border=None, outer=None):
        """Другие цвета (наведение, выбор): заливка, рамка, цвет за углами. Меняются только рисунки холста."""
        if fill is not None and fill != self.fill:
            self.fill = fill
            _set_surface_of_children(self, fill)
        if border is not None:
            self._box_border_color = border
        if outer is not None:
            self._box_outer = outer
        self._box_draw()

    def _follow_surface(self, color):
        """Родитель сменил заливку: «прозрачная» рамка и цвет за углами — следом."""
        if transparent(self._box_bg_color):
            self._box_outer = color
            if self._box_transparent:
                self.restyle(fill=color)
            else:
                self._box_draw()

    def configure(self, cnf=None, **kwargs):
        restyle = {}
        if "fg_color" in kwargs:
            self._box_fg_color = kwargs.pop("fg_color")
            self._box_transparent = transparent(self._box_fg_color)
            restyle["fill"] = self._box_outer if self._box_transparent else self._box_fg_color
        if "border_color" in kwargs:
            restyle["border"] = kwargs.pop("border_color")
        if "bg_color" in kwargs:
            self._box_bg_color = kwargs.pop("bg_color")
            restyle["outer"] = surface(self.master) if transparent(self._box_bg_color) else self._box_bg_color
            if self._box_transparent:
                restyle["fill"] = restyle["outer"]
        if "border_width" in kwargs:
            self._box_border_width = kwargs.pop("border_width") or 0
            self._box_drawn = None
        if "corner_radius" in kwargs:
            self._box_radius = kwargs.pop("corner_radius") or 0
            self._box_drawn = None
        if "width" in kwargs:
            self._box_width = kwargs["width"]
            kwargs["width"] = cpx(self, kwargs["width"])
        if "height" in kwargs:
            self._box_height = kwargs["height"]
            kwargs["height"] = cpx(self, kwargs["height"])
        if cnf:
            tk.Canvas.configure(self, cnf, **kwargs)
        elif kwargs:
            configure_keeping_size(self, tk.Canvas, **kwargs)
        if restyle or self._box_drawn is None:
            self.restyle(**restyle)

    config = configure

    def cget(self, key):
        values = {"fg_color": self._box_fg_color, "border_color": self._box_border_color, "border_width": self._box_border_width,
                  "corner_radius": self._box_radius, "bg_color": self._box_bg_color, "width": self._box_width,
                  "height": self._box_height}
        if key in values:
            return values[key]
        return tk.Canvas.cget(self, key)


# ── Надпись ──────────────────────────────────────────────────────────────────
class Label(Scaled, tk.Label):
    """Надпись вместо CTkLabel: обычная надпись Tk. width и height — наименьший размер в пикселях макета (как у CTkLabel:
    по умолчанию высота 28), текст больше — надпись больше. fg_color="transparent" — фон того, на чём стоит;
    fg_color с corner_radius — «таблетка»: скруглённая подложка готовой картинкой, текст поверх (значок «ВКЛ», счётчик).
    image — CTkImage (ui/icons), картинка PIL или картинка Tk. configure и cget — с именами CustomTkinter."""

    def __init__(self, master, text="", font=None, text_color=None, fg_color="transparent", width=0, height=28,
                 corner_radius=0, image=None, compound="center", anchor="center", justify="center", wraplength=0,
                 padx=0, pady=0, bg_color=None, cursor="", textvariable=None, **kwargs):
        self._text = text
        self._font = font or DEFAULT_FONT
        self._text_color = text_color or DEFAULT_TEXT
        self._fg_color = fg_color
        self._bg_color = bg_color
        self._width, self._height = width, height
        self._radius = corner_radius or 0
        self._image = image
        self._compound = compound
        self._padx, self._pady = padx, pady
        self._wraplength = wraplength
        self._outer = surface(master) if transparent(bg_color) else bg_color
        super().__init__(master, text=text, font=scaled_font(master, self._font), fg=self._text_color,
                         bg=self._background(), bd=0, highlightthickness=0, anchor=anchor, justify=justify,
                         wraplength=cpx(master, wraplength) if wraplength else 0, padx=0, pady=0, cursor=cursor,
                         textvariable=textvariable, **kwargs)
        self._shown = None
        self._fit()

    def _pill(self):
        return not transparent(self._fg_color) and self._radius > 0

    def _background(self):
        if transparent(self._fg_color) or self._pill():
            return self._outer
        return self._fg_color

    def _follow_surface(self, color):
        if transparent(self._bg_color) and color != self._outer:
            self._outer = color
            self._fit(force=True)

    def _fit(self, force=False):
        """Картинка, фон и размер: наименьший — width × height (в пикселях макета), больше — по тексту."""
        if self._pill():
            self._fit_pill(force)
            return
        photo = photo_of(self, self._image)
        compound = self._compound if photo is not None and self._text else "center"
        if photo is None:
            photo = blank_photo(self)
        self._photo = photo
        pad_x, pad_y = cpx(self, self._padx), cpx(self, self._pady)
        tk.Label.configure(self, image=photo, compound=compound, bg=self._background(), width=0, height=0,
                           padx=pad_x, pady=pad_y)
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        want_w, want_h = cpx(self, self._width), cpx(self, self._height)
        if want_w > w or want_h > h:
            tk.Label.configure(self, width=max(want_w, w) - 2 * pad_x if want_w > w else 0,
                               height=max(want_h, h) - 2 * pad_y if want_h > h else 0)

    def _fit_pill(self, force=False):
        h = max(cpx(self, self._height), line_height(self, self._font))
        pad = min(cpx(self, self._radius), h // 2) + cpx(self, self._padx)
        w = max(cpx(self, self._width), text_width(self, self._font, self._text) + 2 * pad)
        look = (w, h, self._fg_color, self._outer, cpx(self, self._radius))
        if look == self._shown and not force:
            return
        self._shown = look
        self._photo = rounded_photo(self, w, h, self._fg_color, None, self._outer, cpx(self, self._radius), 0)
        tk.Label.configure(self, image=self._photo, compound="center", bg=self._outer, width=0, height=0, padx=0,
                           pady=0)

    def configure(self, cnf=None, **kwargs):
        layout = False            # размер мог поменяться: заново подогнать (_fit)
        tk_kwargs = {}
        if "text" in kwargs:
            text = kwargs.pop("text")
            if text != self._text:
                # Новый текст в одну строку у простой надписи: Tk сам даст ей нужную ширину, высота та же —
                # подгонять не надо (таймеры и счётчики меняют текст каждую секунду)
                layout = layout or self._pill() or bool(self._width) or bool(self._wraplength) or \
                    "\n" in text or "\n" in self._text
                self._text = text
                tk_kwargs["text"] = text
        for key, attr in (("font", "_font"), ("fg_color", "_fg_color"), ("image", "_image"),
                          ("compound", "_compound"), ("width", "_width"), ("height", "_height"),
                          ("corner_radius", "_radius"), ("padx", "_padx"), ("pady", "_pady"),
                          ("wraplength", "_wraplength"), ("bg_color", "_bg_color")):
            if key in kwargs:
                value = kwargs.pop(key)
                if value != getattr(self, attr):
                    setattr(self, attr, value)
                    layout = True
        if "text_color" in kwargs:
            self._text_color = kwargs.pop("text_color")
            tk_kwargs["fg"] = self._text_color
        if layout:
            self._radius = self._radius or 0
            if not transparent(self._bg_color):
                self._outer = self._bg_color
            tk_kwargs.update(text=self._text, font=scaled_font(self, self._font),
                             wraplength=cpx(self, self._wraplength) if self._wraplength else 0)
        tk_kwargs.update(kwargs)
        if tk_kwargs or cnf:
            tk.Label.configure(self, cnf, **tk_kwargs)
        if layout:
            self._fit()

    config = configure

    def cget(self, key):
        values = {"text": self._text, "font": self._font, "text_color": self._text_color, "fg_color": self._fg_color,
                  "image": self._image, "compound": self._compound, "width": self._width, "height": self._height,
                  "corner_radius": self._radius, "wraplength": self._wraplength, "bg_color": self._bg_color}
        if key in values:
            return values[key]
        return tk.Label.cget(self, key)


# ── Кнопка ───────────────────────────────────────────────────────────────────
class Button(Box):
    """Кнопка вместо CTkButton одним холстом Tk: подложка — Box (скругление, рамка, заливка), значок и надпись —
    рисунки того же холста. Ширина — не меньше width и по содержимому (отступы по бокам — pad_x, без него — как
    у CTkButton), высота — height. Наведение — только цвет заливки. command — по отпусканию мыши над кнопкой
    (как у CTkButton), invoke() — то же из кода. configure и cget — с именами CustomTkinter."""

    IMAGE_SPACING = 6      # между значком и надписью, как у CTkButton

    def __init__(self, master, text="", command=None, width=140, height=28, corner_radius=6, border_width=0,
                 border_spacing=2, fg_color=None, hover_color=None, border_color=None, text_color=None,
                 text_color_disabled=None, font=None, image=None, compound="left", anchor="center", state="normal",
                 hover=True, bg_color=None, pad_x=None, cursor="hand2", **kwargs):
        self._text = text
        self._command = command
        self._fg_normal = fg_color or C["blue_button"]
        self._hover_color = hover_color or self._fg_normal
        self._text_color = text_color or DEFAULT_TEXT
        self._text_color_disabled = text_color_disabled or C["text_muted"]
        self._font = font or DEFAULT_FONT
        self._image = image
        self._compound = compound
        self._anchor = anchor
        self._state = state
        self._hover = hover
        self._border_spacing = border_spacing
        self._pad_x = pad_x
        self._inside = False
        self._cursor = cursor
        super().__init__(master, fg_color=self._fg_normal, border_color=border_color, border_width=border_width,
                         corner_radius=corner_radius, width=width, height=height, bg_color=bg_color,
                         cursor=cursor if state != "disabled" else "", **kwargs)
        self._image_item = tk.Canvas.create_image(self, 0, 0, anchor="w", tags="content")
        self._text_item = tk.Canvas.create_text(self, 0, 0, anchor="w", text=text, font=scaled_font(master, self._font),
                                                tags="content")
        tk.Canvas.bind(self, "<Enter>", self._pointer_in, add="+")
        tk.Canvas.bind(self, "<Leave>", self._pointer_out, add="+")
        tk.Canvas.bind(self, "<ButtonRelease-1>", self._released, add="+")
        self._fit()

    # ── Размер и содержимое ─────────────────────────────────────────────────
    def _content(self):
        """(картинка Tk или None, ширина картинки, ширина надписи, промежуток)."""
        photo = photo_of(self, self._image)
        # +2: у CTkButton значок и надпись — надписи Tk с рамкой 1 px, ширина кнопки — с ними
        image_w = photo.width() + 2 if photo is not None else 0
        text_w = text_width(self, self._font, self._text) + 2 if self._text else 0
        gap = cpx(self, self.IMAGE_SPACING) if photo is not None and self._text else 0
        return photo, image_w, text_w, gap

    def _side_pad(self):
        if self._pad_x is not None:
            return cpx(self, self._pad_x)
        return cpx(self, max(self._box_radius, self._box_border_width + 1, self._border_spacing))

    def _fit(self):
        """Нужная ширина — по содержимому (не меньше width), высота — height; потом разложить содержимое."""
        self._photo, image_w, text_w, gap = self._content()
        width = max(cpx(self, self._box_width), image_w + gap + text_w + 2 * self._side_pad())
        tk.Canvas.configure(self, width=width, height=cpx(self, self._box_height))
        tk.Canvas.itemconfigure(self, self._image_item, image=self._photo or "",
                                state="normal" if self._photo is not None else "hidden")
        tk.Canvas.itemconfigure(self, self._text_item, text=self._text, font=scaled_font(self, self._font),
                                fill=self._current_text_color())
        self._place_content()

    def _place_content(self):
        if self._box_size is None:
            return
        w, h = self._box_size
        _photo, image_w, text_w, gap = self._content()
        total = image_w + gap + text_w
        if "w" in self._anchor and self._anchor != "center":
            x = self._side_pad()
        elif "e" in self._anchor and self._anchor != "center":
            x = w - self._side_pad() - total
        else:
            x = (w - total) // 2
        y = h / 2
        if self._compound == "right":
            tk.Canvas.coords(self, self._text_item, x + 1, y)
            tk.Canvas.coords(self, self._image_item, x + text_w + gap + 1, y)
        else:
            tk.Canvas.coords(self, self._image_item, x + 1, y)
            tk.Canvas.coords(self, self._text_item, x + image_w + gap + 1, y)

    def _after_box_draw(self):
        if hasattr(self, "_text_item"):
            self._place_content()

    def _current_text_color(self):
        return self._text_color_disabled if self._state == "disabled" else self._text_color

    # ── Мышь ────────────────────────────────────────────────────────────────
    def _pointer_in(self, _event=None):
        self._inside = True
        if self._hover and self._state != "disabled":
            self.restyle(fill=self._hover_fill())

    def _pointer_out(self, _event=None):
        self._inside = False
        self.restyle(fill=self._normal_fill())

    def _hover_fill(self):
        return self._hover_color if not transparent(self._hover_color) else self._normal_fill()

    def _normal_fill(self):
        return self._box_outer if transparent(self._fg_normal) else self._fg_normal

    def _released(self, event):
        inside = 0 <= event.x < self.winfo_width() and 0 <= event.y < self.winfo_height()
        if inside:
            self.invoke()

    def invoke(self):
        if self._state != "disabled" and self._command:
            return self._command()
        return None

    def _follow_surface(self, color):
        if transparent(self._box_bg_color):
            self._box_outer = color
            fill = self._hover_fill() if self._inside and self._hover and self._state != "disabled" \
                else self._normal_fill()
            self.restyle(fill=fill)

    # ── Настройки ───────────────────────────────────────────────────────────
    def configure(self, cnf=None, **kwargs):
        fit = False
        for key, attr in (("text", "_text"), ("image", "_image"), ("font", "_font"), ("compound", "_compound"),
                          ("anchor", "_anchor"), ("pad_x", "_pad_x"), ("border_spacing", "_border_spacing")):
            if key in kwargs:
                setattr(self, attr, kwargs.pop(key))
                fit = True
        if "command" in kwargs:
            self._command = kwargs.pop("command")
        if "hover" in kwargs:
            self._hover = kwargs.pop("hover")
        if "hover_color" in kwargs:
            self._hover_color = kwargs.pop("hover_color")
        if "text_color" in kwargs:
            self._text_color = kwargs.pop("text_color")
            fit = True
        if "text_color_disabled" in kwargs:
            self._text_color_disabled = kwargs.pop("text_color_disabled")
            fit = True
        if "state" in kwargs:
            self._state = kwargs.pop("state")
            kwargs["cursor"] = self._cursor if self._state != "disabled" else ""
            fit = True
        if "fg_color" in kwargs:
            self._fg_normal = kwargs["fg_color"]
        for key in ("width", "height", "corner_radius", "border_width"):
            if key in kwargs:
                fit = True
        super().configure(cnf, **kwargs)
        if self._inside and self._hover and self._state != "disabled":
            self.restyle(fill=self._hover_fill())
        else:
            self.restyle(fill=self._normal_fill())
        if fit:
            self._fit()

    config = configure

    def cget(self, key):
        values = {"text": self._text, "image": self._image, "font": self._font, "state": self._state,
                  "text_color": self._text_color, "text_color_disabled": self._text_color_disabled,
                  "hover_color": self._hover_color, "fg_color": self._fg_normal, "command": self._command,
                  "compound": self._compound, "anchor": self._anchor}
        if key in values:
            return values[key]
        return super().cget(key)


# ── Поле ввода ───────────────────────────────────────────────────────────────
class Entry(Box):
    """Поле ввода вместо CTkEntry: рамка Box и обычное поле Tk внутри (отступы — как у CTkEntry). Методы поля Tk
    (get, insert, delete, bind, focus_set, icursor, select_range …) — у самого Entry, поле Tk — self.entry."""

    MIN_X_PADDING = 6

    def __init__(self, master, width=140, height=28, corner_radius=6, border_width=2, fg_color=None,
                 border_color=None, text_color=None, font=None, bg_color=None, placeholder_text=None,
                 placeholder_text_color=None, show="", textvariable=None, state="normal", justify="left", **kwargs):
        super().__init__(master, fg_color=fg_color or C["bg_elevated"], border_color=border_color or C["border"],
                         border_width=border_width, corner_radius=corner_radius, width=width, height=height,
                         bg_color=bg_color, cursor="xterm")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self._text_color = text_color or DEFAULT_TEXT
        self._font = font or DEFAULT_FONT
        self._placeholder = placeholder_text
        self._placeholder_color = placeholder_text_color or C["text_muted"]
        self._placeholder_on = False
        self._show = show
        self.entry = tk.Entry(self, bd=0, highlightthickness=0, relief="flat", font=scaled_font(master, self._font),
                              show=show, textvariable=textvariable, justify=justify, state=state, **kwargs)
        self._paint_entry()
        self._place_entry()
        self.entry.bind("<FocusIn>", self._focus_in, add="+")
        self.entry.bind("<FocusOut>", self._focus_out, add="+")
        tk.Canvas.bind(self, "<Button-1>", lambda _e: self.entry.focus_set(), add="+")
        self._show_placeholder()

    def _place_entry(self):
        h = cpx(self, self._box_height)
        bw = cpx(self, self._box_border_width) if self._box_border_width else 0
        radius = cpx(self, self._box_radius)
        pad = min(radius, round(h / 2)) if self._box_radius >= self.MIN_X_PADDING else cpx(self, self.MIN_X_PADDING)
        pad = max(pad, bw + 1)
        self.entry.place(x=pad, y=bw, relwidth=1, width=-2 * pad, relheight=1, height=-(2 * bw + 1))

    def _paint_entry(self):
        color = self._placeholder_color if self._placeholder_on else self._text_color
        self.entry.configure(bg=self.fill, disabledbackground=self.fill, readonlybackground=self.fill, fg=color,
                             disabledforeground=color, insertbackground=color, selectbackground=C["blue_button"],
                             selectforeground=C["white"])

    def restyle(self, fill=None, border=None, outer=None):
        super().restyle(fill, border, outer)
        if hasattr(self, "entry"):
            self._paint_entry()

    # Подсказка в пустом поле (placeholder_text), как у CTkEntry
    def _show_placeholder(self):
        if self._placeholder and not self.entry.get() and self.entry.focus_get() is not self.entry:
            self._placeholder_on = True
            self.entry.configure(show="")
            self.entry.insert(0, self._placeholder)
            self._paint_entry()

    def _hide_placeholder(self):
        if self._placeholder_on and self.entry.cget("state") != "readonly":
            self._placeholder_on = False
            self.entry.delete(0, "end")
            self.entry.configure(show=self._show)
            self._paint_entry()

    def _focus_in(self, _event=None):
        self._hide_placeholder()

    def _focus_out(self, _event=None):
        self._show_placeholder()

    # Как у поля Tk
    def get(self):
        return "" if self._placeholder_on else self.entry.get()

    def insert(self, index, text):
        self._hide_placeholder()
        return self.entry.insert(index, text)

    def delete(self, first, last=None):
        result = self.entry.delete(first, last)
        if not self.entry.get() and self.entry.focus_get() is not self.entry:
            self._show_placeholder()
        return result

    def bind(self, sequence=None, func=None, add=None):
        return self.entry.bind(sequence, func, add)

    def unbind(self, sequence, funcid=None):
        return self.entry.unbind(sequence, funcid)

    def focus_set(self):
        self.entry.focus_set()

    focus = focus_set

    def focus_force(self):
        self.entry.focus_force()

    def icursor(self, index):
        self.entry.icursor(index)

    def index(self, index):
        return self.entry.index(index)

    def select_range(self, start, end):
        self.entry.select_range(start, end)

    selection_range = select_range

    def select_clear(self):
        self.entry.select_clear()

    def xview(self, *args):
        return self.entry.xview(*args)

    def configure(self, cnf=None, **kwargs):
        entry = {}
        for key in ("state", "show", "textvariable", "justify", "validate", "validatecommand"):
            if key in kwargs:
                entry[key] = kwargs.pop(key)
        if "show" in entry:
            self._show = entry["show"]
            if self._placeholder_on:
                entry.pop("show")
        if "text_color" in kwargs:
            self._text_color = kwargs.pop("text_color")
        if "placeholder_text_color" in kwargs:
            self._placeholder_color = kwargs.pop("placeholder_text_color")
        if "font" in kwargs:
            self._font = kwargs.pop("font")
            entry["font"] = scaled_font(self, self._font)
        placement = any(key in kwargs for key in ("border_width", "corner_radius", "height"))
        super().configure(cnf, **kwargs)
        if entry:
            self.entry.configure(**entry)
        self._paint_entry()
        if placement:
            self._place_entry()

    config = configure

    def cget(self, key):
        if key in ("state", "show", "textvariable", "justify"):
            return self._show if key == "show" else self.entry.cget(key)
        if key == "text_color":
            return self._text_color
        if key == "font":
            return self._font
        if key == "placeholder_text":
            return self._placeholder
        return super().cget(key)


# ── Полоса прокрутки ─────────────────────────────────────────────────────────
class Scrollbar(tk.Canvas):
    """Вертикальная полоса прокрутки на холсте Tk (вместо CTkScrollbar): ползунок — готовая скруглённая картинка.
    set(first, last) только сдвигает ползунок — без update_idletasks (у CTkScrollbar он звал его при каждом сдвиге,
    и в руководстве полоса вызывала сама себя по кругу). Ползунок тянут мышью; щелчок мимо — ползунок туда;
    колёсико над полосой прокручивает. width — ширина полосы, border_spacing — отступ ползунка от краёв (как у CTk)."""

    MIN_THUMB = 20

    def __init__(self, master, command=None, width=16, border_spacing=4, fg_color=None, bg_color=None,
                 button_color=None, button_hover_color=None, wheel_step=None):
        self.command = command
        self._bg = fg_color if not transparent(fg_color) else (bg_color if not transparent(bg_color) else surface(master))
        self.fill = self._bg
        self._color = button_color or C["border_strong"]
        self._hover_color = button_hover_color or C["border_focus"]
        self._spacing = border_spacing
        self._first, self._last = 0.0, 1.0
        self._hover = False
        self._drag = None
        self._shown = None
        self.wheel_step = wheel_step
        super().__init__(master, width=cpx(master, width), height=1, bg=self._bg, highlightthickness=0, bd=0)
        self._thumb = self.create_image(0, 0, anchor="nw")
        self.bind("<Configure>", lambda _e: self._draw(), add="+")
        self.bind("<Enter>", lambda _e: self._set_hover(True), add="+")
        self.bind("<Leave>", lambda _e: self._set_hover(False), add="+")
        self.bind("<ButtonPress-1>", self._press, add="+")
        self.bind("<B1-Motion>", self._motion, add="+")
        self.bind("<ButtonRelease-1>", self._release, add="+")
        for sequence in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.bind(sequence, self._wheel, add="+")

    def set(self, first, last):
        first, last = float(first), float(last)
        if (first, last) != (self._first, self._last):
            self._first, self._last = first, last
            self._draw()

    def get(self):
        return self._first, self._last

    def _track(self):
        h = self.winfo_height()
        spacing = cpx(self, self._spacing)
        return spacing, max(1, h - 2 * spacing)

    def _thumb_box(self):
        top, length = self._track()
        y0 = top + round(self._first * length)
        y1 = top + round(self._last * length)
        if y1 - y0 < cpx(self, self.MIN_THUMB):
            y1 = min(top + length, y0 + cpx(self, self.MIN_THUMB))
            y0 = max(top, y1 - cpx(self, self.MIN_THUMB))
        return y0, y1

    def _draw(self):
        w = self.winfo_width()
        if w <= 1:
            return
        spacing = cpx(self, self._spacing)
        y0, y1 = self._thumb_box()
        tw, th = max(1, w - 2 * spacing), max(1, y1 - y0)
        color = self._hover_color if self._hover or self._drag is not None else self._color
        look = (tw, th, color)
        if look != self._shown:
            self._shown = look
            self._photo = rounded_photo(self, tw, th, color, None, self._bg, tw // 2, 0)
            self.itemconfigure(self._thumb, image=self._photo)
        self.coords(self._thumb, spacing, y0)

    def _set_hover(self, hover):
        if hover != self._hover:
            self._hover = hover
            self._draw()

    def _press(self, event):
        y0, y1 = self._thumb_box()
        top, length = self._track()
        if not y0 <= event.y <= y1:                      # мимо ползунка: ползунок серединой туда
            view = self._last - self._first
            self._moveto((event.y - top) / length - view / 2)
            y0, y1 = self._thumb_box()
        self._drag = event.y - y0
        self._draw()

    def _motion(self, event):
        if self._drag is None:
            return
        top, length = self._track()
        self._moveto((event.y - self._drag - top) / length)

    def _release(self, _event=None):
        self._drag = None
        self._draw()

    def _moveto(self, fraction):
        if self.command:
            self.command("moveto", max(0.0, min(1.0, fraction)))

    def _wheel(self, event):
        if self.command and (self._first > 0 or self._last < 1):
            self.command("scroll", wheel_units(event, self.wheel_step or 20), "units")
        return "break"


def wheel_units(event, step):
    """Сколько пикселей прокрутить за щелчок колёсика (минус — вверх). Windows: delta ±120 за щелчок,
    у сенсорной панели — меньше и чаще."""
    if event.num == 4:
        return -step
    if event.num == 5:
        return step
    delta = getattr(event, "delta", 0) or 0
    if sys.platform == "darwin":
        return -delta
    units = -round(delta / 120 * step)
    if units == 0 and delta:
        units = -1 if delta > 0 else 1
    return units


# ── Прокрутка частями ────────────────────────────────────────────────────────
MAX_PIECE = 32000   # координаты окон Tk — 16 бит (до 32 767 px): ни одна часть не выше и не ставится дальше
CATCH_UP_MS = 150         # невидимые части получают новую ширину, когда она столько не менялась (ScrollArea)
CATCH_UP_STEP_MS = 30     # ... по CATCH_UP_PIECES за раз, с такими паузами
CATCH_UP_PIECES = 2
INCOMING_CHECK_MS = 10    # часть, которую вот-вот покажут: как часто проверять, показал ли её Tk (ScrollArea)...
INCOMING_MAX_MS = 400     # ... и не дольше
WHEEL_TAG = "LightWheel"


class ScrollArea(Scaled, tk.Frame):
    """Прокрутка без холста. Содержимое — части (piece()): рамки Tk друг под другом в окне просмотра (self.viewport).
    Видимые части стоят на своих местах (place), остальные ждут сразу за краем окна просмотра: их не видно, но ширина
    у них та же, поэтому переносы строк и высоты посчитаны заранее — при прокрутке ничего не «догружается».
    Ни одно окно не ставится дальше 32 000 px: координаты окон у Tk 16-битные, и на холсте с одним листом во всю длину
    руководство обрывалось на разделе 10 (он начинался ниже 32 767 px). Поэтому и часть не выше MAX_PIECE.

    Полоса — Scrollbar: сбоку (side=True, как у CTkScrollableFrame) или поверх правого края (её появление не меняет
    ширину текста). auto_hide — полоса только когда не влезает. on_scroll() — после прокрутки и новой раскладки.
    Высота части поменялась (достроили раздел, текст перенёсся по ширине) — то, что сейчас вверху, остаётся на месте:
    части выше него не сдвигают текст под глазами. После show_piece() наверху держится эта часть, пока не прокрутят
    колёсиком или полосой.

    Сессия 11б: части далеко от видимого (дальше экрана выше и ниже) запаркованы — лежат в рамке parking, которую
    никогда не показывают: разложены по ширине (высоты известны), но не показаны. Показанный элемент Tk в Windows —
    отдельное окно; в руководстве их было 2070, и окно программы медленно сворачивалось, разворачивалось и двигалось.
    Часть, которая вот-вот станет видна (прокрутили далеко, щёлкнули в оглавлении), сначала показывается за краем,
    и только когда Tk показал её целиком, прокрутка встаёт на новое место: часть появляется готовой, а не по кускам."""

    def __init__(self, master, bg=None, side=True, auto_hide=False, on_scroll=None, bar_width=16, bar_spacing=4,
                 bar_color=None, bar_hover_color=None, wheel_step=None, width=200, height=200):
        bg = bg or surface(master)
        super().__init__(master, bg=bg, bd=0, highlightthickness=0)
        self.fill = bg
        self.side = side
        self.auto_hide = auto_hide
        self.on_scroll = on_scroll
        self.wheel_step = wheel_step or (20 if sys.platform == "win32" else 30)
        self.viewport = tk.Frame(self, bg=bg, bd=0, highlightthickness=0, width=cpx(master, width),
                                 height=cpx(master, height))
        self.viewport.fill = bg
        self.viewport._scroll_area = self
        self.parking = tk.Frame(self.viewport, bd=0, highlightthickness=0)   # её никогда не показывают
        self.bar = Scrollbar(self, command=self._bar_command, width=bar_width, border_spacing=bar_spacing,
                             fg_color=bg, button_color=bar_color, button_hover_color=bar_hover_color,
                             wheel_step=self.wheel_step)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.viewport.grid(row=0, column=0, sticky="nsew")
        self._bar_shown = False
        self.pieces = []               # рамки по порядку сверху вниз
        self.offsets = {}              # рамка -> y от начала содержимого
        self._heights = {}             # рамка -> высота при последней раскладке
        self._placed = {}              # рамка -> (y, ширина), как она стоит в окне просмотра
        self._width = 1                # ширина окна просмотра
        self._widths = {}              # рамка -> ширина, которую ей дали
        self._stale = set()            # части, которым ширину окна дадим позже (_catch_up)
        self._height = 0               # высота всего содержимого
        self._top = 0                  # сколько пикселей содержимого прокручено
        self._target = None            # часть из show_piece(): держим её наверху
        self._layout_id = None
        self._catch_id = None
        self._incoming = set()         # части, которые показываются за краем перед тем, как стать видимыми
        self._wanted = None            # (верх, notify): куда прокрутить, когда они покажутся
        self._incoming_id = None
        self.viewport.bind("<Configure>", self._viewport_changed, add="+")
        install_wheel(self)
        if not auto_hide:
            self._show_bar(True)

    # ── Части ───────────────────────────────────────────────────────────────
    def piece(self, frame=None, bg=None):
        """Новая часть внизу. frame — своя рамка (её master — self.viewport)."""
        if frame is None:
            frame = tk.Frame(self.viewport, bg=bg or self.fill, bd=0, highlightthickness=0)
            frame.fill = bg or self.fill
        frame._scroll_area = self
        self.pieces.append(frame)
        self.offsets[frame] = self._height
        self._heights[frame] = 0
        self._widths[frame] = self._width
        if self._near_view(frame, self.viewport.winfo_height()):
            self._unpark(frame, self._y_for(frame), self._width)
        else:
            self._park(frame, self._width)
        frame.bind("<Configure>", self._piece_changed, add="+")
        self.layout_later()
        return frame

    def clear(self):
        """Убрать все части (и их содержимое)."""
        for frame in self.pieces:
            frame.destroy()
        self.pieces = []
        self.offsets = {}
        self._heights = {}
        self._placed = {}
        self._widths = {}
        self._stale = set()
        self._height = 0
        self._target = None
        self._stop_incoming()
        self._move_to(0, notify=True)

    def _viewport_changed(self, event):
        """Новая ширина окна просмотра: видимые части получают её сразу, остальные — порциями, когда ширина перестанет
        меняться (растягивание окна за уголок — десятки шагов: раньше на каждом заново раскладывалось всё руководство).
        Верх видимого при этом на месте (layout), поэтому догоняющие части текст под глазами не сдвигают."""
        if event.width != self._width:
            self._width = event.width
            self._stale = set(self.pieces)
            self._catch_up_later()
        self._move_to(self._top, notify=True, keep=True)

    def _catch_up_later(self):
        if self._catch_id is not None:
            try:
                self.after_cancel(self._catch_id)
            except tk.TclError:
                pass
        try:
            self._catch_id = self.after(CATCH_UP_MS, self._catch_up)
        except tk.TclError:
            self._catch_id = None

    def _catch_up(self):
        self._catch_id = None
        for frame in [f for f in self.pieces if f in self._stale][:CATCH_UP_PIECES]:
            self._stale.discard(frame)
            self._widths[frame] = self._width
        self._move_to(self._top, keep=True)
        if self._stale:
            try:
                self._catch_id = self.after(CATCH_UP_STEP_MS, self._catch_up)
            except tk.TclError:
                self._catch_id = None

    def _near_view(self, frame, view, top=None):
        """Часть видна или вот-вот будет видна (на экран выше или ниже)."""
        y = self.offsets.get(frame, 0) - (self._top if top is None else top)
        return y < 2 * view and y + self._heights.get(frame, 0) > -view

    def _visible_at(self, frame, top, view):
        y = self.offsets.get(frame, 0) - top
        return y < view and y + self._heights.get(frame, 0) > 0

    # ── Стоянка частей ──────────────────────────────────────────────────────
    def _park(self, frame, width):
        """Убрать часть с экрана (Tk прячет её элементы), но оставить разложенной по ширине — в рамке parking."""
        if frame.winfo_manager() and not getattr(frame, "_parked", False):
            tk.Place.place_forget(frame)
        frame._parked = True
        self._placed[frame] = ("parked", width)
        tk.Place.place_configure(frame, in_=self.parking, x=0, y=0, width=width)   # не place() рамки (ScrollableFrame)

    def _unpark(self, frame, y, width):
        if getattr(frame, "_parked", False):
            tk.Place.place_forget(frame)
        frame._parked = False
        self._placed[frame] = (y, width)
        tk.Place.place_configure(frame, in_=self.viewport, x=0, y=y, width=width)

    def _wait_incoming(self, started=None):
        """Части за краем показаны (или прошло INCOMING_MAX_MS) — прокрутить туда, куда просили."""
        self._incoming_id = None
        now = time.monotonic()
        started = now if started is None else started
        incoming = [frame for frame in self._incoming if frame.winfo_exists()]
        if any(still_mapping(frame) for frame in incoming) and (now - started) * 1000 < INCOMING_MAX_MS:
            try:
                self._incoming_id = self.after(INCOMING_CHECK_MS, self._wait_incoming, started)
            except tk.TclError:
                self._incoming_id = None
            return
        wanted, self._wanted = self._wanted, None
        self._incoming.clear()
        if wanted is not None:
            self._move_to(*wanted)

    def _stop_incoming(self):
        if self._incoming_id is not None:
            try:
                self.after_cancel(self._incoming_id)
            except tk.TclError:
                pass
            self._incoming_id = None
        self._incoming.clear()
        self._wanted = None

    def busy(self):
        """Часть ещё показывается за краем, прокрутка ждёт её."""
        return bool(self._incoming)

    def _piece_changed(self, event):
        if event.height != self._heights.get(event.widget):
            self.layout_later()

    def layout_later(self):
        if self._layout_id is None:
            try:
                self._layout_id = self.after_idle(self.layout)
            except tk.TclError:
                self._layout_id = None

    def layout(self):
        """Части друг под другом по их нужной высоте. Верх видимого — на месте (или наверху часть из show_piece)."""
        if self._layout_id is not None:
            try:
                self.after_cancel(self._layout_id)
            except tk.TclError:
                pass
            self._layout_id = None
        anchor = self._anchor()
        self.pieces = [frame for frame in self.pieces if frame.winfo_exists()]
        y = 0
        for frame in self.pieces:
            self.offsets[frame] = y
            height = frame.winfo_reqheight()
            self._heights[frame] = height
            y += height
        self._height = y
        keep = self._target not in self.offsets
        if not keep:
            top = self.offsets[self._target]
        elif anchor is not None and anchor[0] in self.offsets:
            top = self.offsets[anchor[0]] + anchor[1]
        else:
            top = self._top
        self._move_to(top, notify=True, keep=keep)

    def _anchor(self):
        """Часть, в которой сейчас верх видимого, и насколько он ниже её начала."""
        found = None
        for frame in self.pieces:
            offset = self.offsets.get(frame)
            if offset is None or offset > self._top:
                break
            found = (frame, self._top - offset)
        return found

    def _y_for(self, frame):
        """Где поставить часть: на своё место, если её видно; иначе — сразу за краем окна просмотра."""
        view = self.viewport.winfo_height()
        height = self._heights.get(frame, 0)
        y = self.offsets.get(frame, 0) - self._top
        if y >= view:
            return view
        if y + height <= 0:
            return max(-MAX_PIECE, -height - view)     # с запасом: часть может подрасти, пока ждёт
        return y

    def _move_to(self, top, notify=False, keep=False):
        """Прокрутить так, чтобы верх видимого был top, и расставить части. keep — не просьба прокрутить, а «верх на
        месте» после новой раскладки: пока ждём части за краем (_wanted), такие вызовы пропускаем — в конце ожидания
        части всё равно расставятся заново."""
        view = self.viewport.winfo_height()
        top = max(0, min(int(round(top)), self._height - view))
        if self._wanted is not None:                    # ждём части за краем — запомнить, куда в итоге
            if not keep:
                self._wanted = (top, notify or self._wanted[1])
            return
        entering = [f for f in self.pieces if getattr(f, "_parked", False) and self._visible_at(f, top, view)]
        if entering and self.winfo_viewable():          # станут видны: сначала показать за краем (_wait_incoming)
            for frame in entering:
                if frame in self._stale:
                    self._stale.discard(frame)
                    self._widths[frame] = self._width
                self._unpark(frame, view, self._widths.get(frame, self._width))
            self._incoming.update(entering)
            self._wanted = (top, notify)
            self._wait_incoming()
            return
        moved = top != self._top
        self._top = top
        for frame in self.pieces:
            near = self._near_view(frame, view)
            if frame in self._stale and near:
                self._stale.discard(frame)
                self._widths[frame] = self._width
            width = self._widths.get(frame, self._width)
            if not near and frame not in self._incoming:
                if self._placed.get(frame) != ("parked", width):
                    self._park(frame, width)
                continue
            spot = (self._y_for(frame), width)
            if self._placed.get(frame) != spot:
                self._unpark(frame, *spot)
        if self.auto_hide:
            self._show_bar(self._height > view + 1)
        self.bar.set(*self.yview())
        if (moved or notify) and self.on_scroll:
            self.on_scroll()

    def content_height(self):
        return self._height

    def offset(self, frame):
        """y части от начала содержимого (для прокрутки к разделу)."""
        return self.offsets.get(frame, 0)

    def piece_height(self, frame):
        return self._heights.get(frame, 0)

    # ── Прокрутка ───────────────────────────────────────────────────────────
    def top(self):
        return self._top

    def view_height(self):
        return self.viewport.winfo_height()

    def yview(self):
        """Как у холста: какая доля содержимого сверху и снизу видна."""
        height = max(1, self._height)
        return self._top / height, min(1.0, (self._top + self.view_height()) / height)

    def at_bottom(self):
        return self._top >= self._height - self.view_height()

    def scroll_to(self, y):
        self._target = None
        self._move_to(y)

    def show_piece(self, frame):
        """Прокрутить так, чтобы часть была наверху, и держать её там, пока высоты выше неё ещё меняются (раздел
        достраивается, текст переносится по ширине), — до первой прокрутки колёсиком или полосой."""
        self._target = frame
        self._move_to(self.offsets.get(frame, 0))
        self.layout_later()

    def see(self, y, h):
        """Прокрутить так, чтобы полоса [y, y + h) содержимого была видна целиком."""
        top, view = self._top, self.view_height()
        if y < top:
            self.scroll_to(y)
        elif y + h > top + view:
            self.scroll_to(y + h - view)

    def scroll_by(self, pixels):
        if self._height > self.view_height():
            self.scroll_to(self._top + int(pixels))

    def _bar_command(self, *args):
        if args[0] == "moveto":
            self.scroll_to(float(args[1]) * self._height)
        elif args[0] == "scroll":
            self.scroll_by(int(args[1]) * (1 if args[2] == "units" else self.view_height()))

    def _show_bar(self, show):
        if show == self._bar_shown:
            return
        self._bar_shown = show
        if show:
            if self.side:
                self.bar.grid(row=0, column=1, sticky="ns", padx=(0, 1))   # как у CTkScrollableFrame: 1 px справа
            else:
                self.bar.place(relx=1, rely=0, relheight=1, anchor="ne")
                tk.Misc.tkraise(self.bar)
        elif self.side:
            self.bar.grid_remove()
        else:
            self.bar.place_forget()

    def destroy(self):
        self._stop_incoming()
        for name in ("_layout_id", "_catch_id"):
            after_id = getattr(self, name)
            if after_id is not None:
                try:
                    self.after_cancel(after_id)
                except tk.TclError:
                    pass
                setattr(self, name, None)
        super().destroy()


def install_wheel(widget):
    """Колёсико мыши для всех прокруток окна (как у CTkScrollableFrame): одна привязка на окно программы,
    прокручивается ближайшая прокрутка над тем, что под мышью. Текстовые поля и полосы прокручивают себя сами."""
    root = widget._root()
    if getattr(root, "_light_wheel", False):
        return
    root._light_wheel = True
    sequences = ("<Button-4>", "<Button-5>") if sys.platform.startswith("linux") else ("<MouseWheel>",)
    for sequence in sequences:
        root.bind_all(sequence, _wheel_all, add="+")
        root.bind_class(WHEEL_TAG, sequence, _wheel_through)


def area_of(widget):
    """Прокрутка, в которой лежит виджет (или None)."""
    while widget is not None and not isinstance(widget, str):
        area = getattr(widget, "_scroll_area", None)
        if area is not None:
            return area
        widget = getattr(widget, "master", None)
    return None


def _scroll_area_of(event):
    area = area_of(event.widget)
    try:
        if area is not None and area.winfo_exists():
            area.scroll_by(wheel_units(event, area.wheel_step))
    except tk.TclError:
        pass


def _wheel_all(event):
    widget = event.widget
    if isinstance(widget, (tk.Text, tk.Listbox, Scrollbar)):
        return None
    _scroll_area_of(event)
    return None


def _wheel_through(event):
    _scroll_area_of(event)
    return "break"


def wheel_through(widget):
    """Колёсико над этим виджетом (текстовым полем без своей прокрутки — абзац руководства) крутит прокрутку вокруг
    него, а не сам виджет. Одна общая привязка (WHEEL_TAG в bindtags перед классом), без новой команды на каждый виджет."""
    install_wheel(widget)
    tags = widget.bindtags()
    if WHEEL_TAG not in tags:
        widget.bindtags(tags[:1] + (WHEEL_TAG,) + tags[1:])


class ScrollableFrame(tk.Frame):
    """Как CTkScrollableFrame: сам — содержимое (одна часть ScrollArea), а grid/pack/place, lift и destroy — у внешней
    рамки (self.outer). Полоса — сбоку, ползунок 8 px на полосе 16 px (как у CustomTkinter)."""

    def __init__(self, master, fg_color="transparent", corner_radius=0, scrollbar_button_color=None,
                 scrollbar_button_hover_color=None, width=200, height=200, bar_width=16, bar_spacing=4, **kwargs):
        bg = surface(master) if transparent(fg_color) else fg_color
        self.outer = ScrollArea(master, bg=bg, bar_color=scrollbar_button_color,
                                bar_hover_color=scrollbar_button_hover_color, width=width, height=height,
                                bar_width=bar_width, bar_spacing=bar_spacing)
        tk.Frame.__init__(self, self.outer.viewport, bg=bg, bd=0, highlightthickness=0, **kwargs)
        self.fill = bg
        self.outer.piece(self)

    @property
    def area(self):
        return self.outer

    def pack(self, **kwargs):
        self.outer.pack(**kwargs)

    pack_configure = pack

    def grid(self, **kwargs):
        self.outer.grid(**kwargs)

    grid_configure = grid

    def place(self, **kwargs):
        self.outer.place(**kwargs)

    place_configure = place

    def pack_forget(self):
        self.outer.pack_forget()

    def grid_forget(self):
        self.outer.grid_forget()

    def grid_remove(self):
        self.outer.grid_remove()

    def place_forget(self):
        self.outer.place_forget()

    def lift(self, above=None):
        self.outer.lift(above)

    tkraise = lift

    def lower(self, below=None):
        self.outer.lower(below)

    def destroy(self):
        outer = self.outer
        tk.Frame.destroy(self)
        try:
            outer.destroy()
        except tk.TclError:
            pass


# ── Многострочный текст ──────────────────────────────────────────────────────
class Textbox(Box):
    """Многострочный текст вместо CTkTextbox: рамка Box, внутри поле Tk (self.textbox) и Scrollbar, когда текст
    не влезает. Методы поля Tk (insert, delete, get, see, yview, tag_config …) — у самого Textbox."""

    def __init__(self, master, fg_color=None, border_width=0, border_color=None, corner_radius=6, font=None,
                 text_color=None, wrap="char", border_spacing=3, scrollbar_button_color=None,
                 scrollbar_button_hover_color=None, width=200, height=200, bg_color=None, state="normal", **kwargs):
        super().__init__(master, fg_color=fg_color or C["bg_primary"], border_color=border_color,
                         border_width=border_width, corner_radius=corner_radius, width=width, height=height,
                         bg_color=bg_color)
        self.grid_propagate(False)
        self._font = font or DEFAULT_FONT
        self._text_color = text_color or DEFAULT_TEXT
        bw = border_width or 0
        # Отступы — как у CTkTextbox: текст на max(скругление, рамка + border_spacing) от края, полоса 8 px справа
        pad = cpx(self, max(corner_radius or 0, bw + border_spacing))
        self.textbox = tk.Text(self, bd=0, highlightthickness=0, relief="flat", wrap=wrap, bg=self.fill,
                               fg=self._text_color, insertbackground=self._text_color, font=scaled_font(master, self._font),
                               selectbackground=C["blue_button"], selectforeground=C["white"],
                               inactiveselectbackground=C["blue_button"], padx=0, pady=0, state=state,
                               width=1, height=1, **kwargs)
        self.bar = Scrollbar(self, command=self.textbox.yview, width=8, border_spacing=0, fg_color=self.fill,
                             button_color=scrollbar_button_color, button_hover_color=scrollbar_button_hover_color)
        self.textbox.configure(yscrollcommand=self._scrolled)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, minsize=pad)
        self.grid_columnconfigure(1, minsize=pad)
        self.textbox.grid(row=0, column=0, sticky="nsew", padx=(pad, 0), pady=(pad, 0))
        self._bar_grid = dict(row=0, column=1, sticky="nsw", padx=(cpx(self, 3), cpx(self, border_spacing + bw)),
                              pady=(pad, 0))
        self._bar_shown = False

    def _scrolled(self, first, last):
        self.bar.set(first, last)
        need = float(first) > 0 or float(last) < 1
        if need != self._bar_shown:
            self._bar_shown = need
            if need:
                self.bar.grid(**self._bar_grid)
            else:
                self.bar.grid_remove()

    # Как у поля Tk (у холста свои insert, delete, index, bbox — для рисунков, поэтому все — явно)
    def insert(self, index, chars, *args):
        return self.textbox.insert(index, chars, *args)

    def delete(self, index1, index2=None):
        return self.textbox.delete(index1, index2)

    def get(self, index1, index2=None):
        return self.textbox.get(index1, index2)

    def see(self, index):
        return self.textbox.see(index)

    def yview(self, *args):
        return self.textbox.yview(*args)

    def yview_moveto(self, fraction):
        return self.textbox.yview_moveto(fraction)

    def yview_scroll(self, number, what):
        return self.textbox.yview_scroll(number, what)

    def compare(self, index1, op, index2):
        return self.textbox.compare(index1, op, index2)

    def index(self, index):
        return self.textbox.index(index)

    def bbox(self, index):
        return self.textbox.bbox(index)

    def tag_config(self, tag, **kwargs):
        return self.textbox.tag_config(tag, **kwargs)

    tag_configure = tag_config

    def tag_add(self, tag, index1, *args):
        return self.textbox.tag_add(tag, index1, *args)

    def tag_remove(self, tag, index1, index2=None):
        return self.textbox.tag_remove(tag, index1, index2)

    def tag_bind(self, tag, sequence, func, add=None):
        return self.textbox.tag_bind(tag, sequence, func, add)

    def tag_ranges(self, tag):
        return self.textbox.tag_ranges(tag)

    def mark_set(self, name, index):
        return self.textbox.mark_set(name, index)

    def bind(self, sequence=None, func=None, add=None):
        return self.textbox.bind(sequence, func, add)

    def focus_set(self):
        self.textbox.focus_set()

    def configure(self, cnf=None, **kwargs):
        text = {}
        for key in ("state", "wrap"):
            if key in kwargs:
                text[key] = kwargs.pop(key)
        if "text_color" in kwargs:
            self._text_color = kwargs.pop("text_color")
            text.update(fg=self._text_color, insertbackground=self._text_color)
        if "font" in kwargs:
            self._font = kwargs.pop("font")
            text["font"] = scaled_font(self, self._font)
        super().configure(cnf, **kwargs)
        if text:
            self.textbox.configure(**text)

    config = configure

    def cget(self, key):
        if key in ("state", "wrap"):
            return self.textbox.cget(key)
        if key == "font":
            return self._font
        return super().cget(key)


# ── Полоска прогресса ────────────────────────────────────────────────────────
@lru_cache(maxsize=256)
def bar_picture(w, h, filled, track, color, outer, radius):
    """Полоска w × h: дорожка цвета track, слева заполнено filled px цвета color, концы скруглены (PIL, RGB).
    Полоска низкая (4–8 px), поэтому рисуется целиком в 4 раза крупнее — оба конца заполненной части гладкие."""
    k = 4
    img = Image.new("RGB", (w * k, h * k), rgb(outer))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=radius * k, fill=rgb(track))
    if filled > 0:
        fw = min(w, max(filled, 2 * radius))
        draw.rounded_rectangle((0, 0, fw * k - 1, h * k - 1), radius=radius * k, fill=rgb(color))
    return img.resize((w, h), Image.LANCZOS)


class ProgressBar(Scaled, tk.Label):
    """Полоска вместо CTkProgressBar: одна надпись Tk с готовой картинкой (дорожка и заполненная часть со скруглением).
    set(0..1) — новая картинка, только если длина заполненной части в пикселях поменялась."""

    def __init__(self, master, height=8, corner_radius=None, fg_color=None, progress_color=None, border_width=0,
                 width=200, bg_color=None, **kwargs):
        self._outer = surface(master) if transparent(bg_color) else bg_color
        self._track = fg_color or C["bg_primary"]
        self._color = progress_color or C["blue"]
        self._height = height
        self._radius = corner_radius if corner_radius is not None else height // 2
        self._value = 0.0
        self._shown = None
        super().__init__(master, bg=self._outer, bd=0, highlightthickness=0, padx=0, pady=0,
                         image=blank_photo(master), width=cpx(master, width), height=cpx(master, height))
        self.bind("<Configure>", lambda e: self._draw(e.width), add="+")

    def _follow_surface(self, color):
        self._outer = color
        tk.Label.configure(self, bg=color)
        self._shown = None
        self._draw()

    def set(self, value):
        value = max(0.0, min(1.0, float(value)))
        if value != self._value:
            self._value = value
            self._draw()

    def get(self):
        return self._value

    def _draw(self, width=None):
        w = width or self.winfo_width()
        h = cpx(self, self._height)
        if w <= 1:
            return
        filled = round(w * self._value)
        look = (w, h, filled, self._track, self._color, self._outer)
        if look == self._shown:
            return
        self._shown = look
        args = look + (min(cpx(self, self._radius), h // 2),)
        self._photo = shared_photo(self, ("progress",) + args, lambda: bar_picture(*args))
        # Нужный размер надписи (-width) не трогаем: иначе растянутая полоска не дала бы окну стать уже
        tk.Label.configure(self, image=self._photo)

    def configure(self, cnf=None, **kwargs):
        if "progress_color" in kwargs:
            self._color = kwargs.pop("progress_color")
        if "fg_color" in kwargs:
            self._track = kwargs.pop("fg_color")
        for key in ("corner_radius", "border_width", "bg_color"):
            kwargs.pop(key, None)
        if kwargs or cnf:
            tk.Label.configure(self, cnf, **kwargs)
        self._draw()

    config = configure

    def cget(self, key):
        if key == "progress_color":
            return self._color
        if key == "fg_color":
            return self._track
        return tk.Label.cget(self, key)


# ── Переключатель вкладок ────────────────────────────────────────────────────
class SegmentedButton(Box):
    """Ряд вкладок вместо CTkSegmentedButton («База и комнаты | Авто-тактика | Правила»): одна рамка-холст, выбранная
    вкладка — скруглённая плашка selected_color, остальные — надписи; наведение — плашка unselected_hover_color.
    Ширина вкладки — как у CTkSegmentedButton: по надписи, а лишнее место — всем поровну (_bounds).
    command(значение) — после щелчка; set(значение) — без него.
    text_colors — свой цвет текста у вкладок ({значение: цвет}, выбранная — белая в мастере правил)."""

    def __init__(self, master, values=(), command=None, height=28, corner_radius=6, border_width=3, fg_color=None,
                 selected_color=None, selected_hover_color=None, unselected_color=None, unselected_hover_color=None,
                 text_color=None, font=None, bg_color=None, dynamic_resizing=False, width=200, **kwargs):
        self._values = list(values)
        self._command = command
        self._selected = None
        self._hovered = None
        self._seg_radius = corner_radius
        self._spacing = border_width
        self._colors = dict(track=fg_color or C["bg_surface"], selected=selected_color or C["blue_button"],
                            selected_hover=selected_hover_color or selected_color or C["blue_button"],
                            unselected=unselected_color or fg_color or C["bg_surface"],
                            hover=unselected_hover_color or C["bg_elevated"])
        self._text_color = text_color or C["white"]
        self.text_colors = {}
        self._font = font or DEFAULT_FONT
        self._state = "normal"
        super().__init__(master, fg_color=self._colors["track"], corner_radius=corner_radius, width=width,
                         height=height, bg_color=bg_color, cursor="hand2")
        self._plates = {}
        self._texts = {}
        self._build()
        tk.Canvas.bind(self, "<Motion>", self._motion, add="+")
        tk.Canvas.bind(self, "<Leave>", lambda _e: self._set_hover(None), add="+")
        tk.Canvas.bind(self, "<Button-1>", self._click, add="+")

    def _build(self):
        for item in list(self._plates.values()) + list(self._texts.values()):
            self.delete(item)
        self._plates = {v: self.create_image(0, 0, anchor="nw", tags="plate") for v in self._values}
        font = scaled_font(self, self._font)
        self._texts = {v: self.create_text(0, 0, text=v, font=font, tags="label") for v in self._values}
        self._box_drawn = None
        self._box_draw()
        self._draw_segments()

    def _bounds(self):
        """Левый и правый край каждой вкладки. Как у CTkSegmentedButton (кнопки в колонках grid с весом 1): ширина —
        надпись и отступы скругления, лишнее место делится поровну, как его делит grid (с накоплением, без остатков)."""
        w = (self._box_size or (self.winfo_width(), 0))[0]
        pad = 2 * cpx(self, self._seg_radius + self._spacing)
        widths = [text_width(self, self._font, value) + pad for value in self._values]
        extra = max(0, w - sum(widths))
        bounds, left, used = [], 0, 0
        for i, width in enumerate(widths):
            used += width
            right = used + extra * (i + 1) // len(widths)
            bounds.append((left, right))
            left = right
        return bounds

    def _segment(self, index):
        """Плашка вкладки: кнопка без рамки шириной spacing (рамка у CTkSegmentedButton — цвета дорожки)."""
        h = (self._box_size or (0, self.winfo_height()))[1]
        s = cpx(self, self._spacing)
        x0, x1 = self._bounds()[index]
        return x0 + s, s, x1 - s, h - s

    def _after_box_draw(self):
        self._draw_segments()

    def _draw_segments(self):
        if not getattr(self, "_texts", None) or self._box_size is None:
            return
        r = max(0, cpx(self, self._seg_radius) - cpx(self, self._spacing) // 2)
        bounds = self._bounds()
        for i, value in enumerate(self._values):
            x0, y0, x1, y1 = self._segment(i)
            color = self._plate_color(value)
            plate = self._plates[value]
            if color is None:
                self.itemconfigure(plate, state="hidden")
            else:
                photo = rounded_photo(self, x1 - x0, y1 - y0, color, None, self.fill, r, 0)
                self.coords(plate, x0, y0)
                self.itemconfigure(plate, image=photo, state="normal")
            self.coords(self._texts[value], sum(bounds[i]) / 2, (y0 + y1) / 2)
            text_color = self.text_colors.get(value, self._text_color)
            if self._state == "disabled":
                text_color = C["text_muted"]
            self.itemconfigure(self._texts[value], fill=text_color)
        self.tag_raise("label")

    def _plate_color(self, value):
        if value == self._selected:
            return self._colors["selected_hover"] if value == self._hovered else self._colors["selected"]
        if value == self._hovered and self._state != "disabled":
            return self._colors["hover"]
        if self._colors["unselected"] != self._colors["track"]:
            return self._colors["unselected"]
        return None

    def _value_at(self, x):
        for value, (x0, x1) in zip(self._values, self._bounds()):
            if x0 <= x < x1:
                return value
        return None

    def _motion(self, event):
        self._set_hover(self._value_at(event.x))

    def _set_hover(self, value):
        if value != self._hovered:
            self._hovered = value
            self._draw_segments()

    def _click(self, event):
        value = self._value_at(event.x)
        if value is None or self._state == "disabled":
            return
        self.set(value)
        if self._command:
            self._command(value)

    def set(self, value):
        if value != self._selected:
            self._selected = value
            self._draw_segments()

    def get(self):
        return self._selected

    def set_text_colors(self, colors):
        """Свой цвет текста у вкладок (выбранная — белая, остальные — серые): только цвета."""
        if colors != self.text_colors:
            self.text_colors = dict(colors)
            self._draw_segments()

    def configure(self, cnf=None, **kwargs):
        if "values" in kwargs:
            self._values = list(kwargs.pop("values"))
            if self._selected not in self._values:
                self._selected = None
            self._build()
        if "command" in kwargs:
            self._command = kwargs.pop("command")
        if "state" in kwargs:
            self._state = kwargs.pop("state")
            tk.Canvas.configure(self, cursor="hand2" if self._state != "disabled" else "")
            self._draw_segments()
        if "text_color" in kwargs:
            self._text_color = kwargs.pop("text_color")
            self._draw_segments()
        super().configure(cnf, **kwargs)

    config = configure

    def cget(self, key):
        if key == "values":
            return list(self._values)
        if key == "state":
            return self._state
        return super().cget(key)


# ── Галочка ──────────────────────────────────────────────────────────────────
@lru_cache(maxsize=32)
def _check_picture(size, radius, fill, border, check, outer, border_width, checked):
    k = 4
    big = Image.new("RGBA", (size * k, size * k), rgb(outer) + (255,))
    draw = ImageDraw.Draw(big)
    if checked:
        draw.rounded_rectangle((0, 0, size * k - 1, size * k - 1), radius=radius * k, fill=rgb(fill) + (255,))
        line = max(2, size * k // 9)
        points = [(size * k * 0.24, size * k * 0.52), (size * k * 0.43, size * k * 0.70), (size * k * 0.77, size * k * 0.32)]
        draw.line(points, fill=rgb(check) + (255,), width=line, joint="curve")
    else:
        draw.rounded_rectangle((0, 0, size * k - 1, size * k - 1), radius=radius * k, fill=rgb(outer) + (255,),
                               outline=rgb(border) + (255,), width=border_width * k)
    return big.resize((size, size), Image.LANCZOS)


class CheckBox(Scaled, tk.Label):
    """Галочка с надписью вместо CTkCheckBox: одна надпись Tk (квадрат — картинка слева, зазор 6 px как у CTkCheckBox).
    get() — 1 или 0, select() и deselect() — без command; щелчок — переключить и command()."""

    GAP = 6

    def __init__(self, master, text="", command=None, font=None, text_color=None, text_color_disabled=None,
                 fg_color=None, hover_color=None, border_color=None, checkmark_color=None, checkbox_width=24,
                 checkbox_height=24, corner_radius=6, border_width=3, bg_color=None, state="normal", height=24,
                 **kwargs):
        self._outer = surface(master) if transparent(bg_color) else bg_color
        self._command = command
        self._value = 0
        self._state = state
        self._text_color = text_color or DEFAULT_TEXT
        self._disabled_color = text_color_disabled or C["text_muted"]
        self._look = dict(size=checkbox_width, radius=corner_radius, fill=fg_color or C["blue_button"],
                          hover=hover_color or fg_color or C["blue_button"], border=border_color or C["border_strong"],
                          check=checkmark_color or C["white"], border_width=border_width)
        self._hover = False
        super().__init__(master, text=text, font=scaled_font(master, font or DEFAULT_FONT), compound="left",
                         bg=self._outer, bd=0, highlightthickness=0, padx=0, pady=0, anchor="w", cursor="hand2",
                         **kwargs)
        self._min_height = height
        self.bind("<Button-1>", self._clicked, add="+")
        self.bind("<Enter>", lambda _e: self._set_hover(True), add="+")
        self.bind("<Leave>", lambda _e: self._set_hover(False), add="+")
        self._paint()

    def _follow_surface(self, color):
        self._outer = color
        self._paint()

    def _paint(self):
        look = self._look
        size = cpx(self, look["size"])
        fill = look["hover"] if self._hover and self._state != "disabled" else look["fill"]
        border = look["hover"] if self._hover and self._state != "disabled" else look["border"]
        if self._state == "disabled":
            fill, border = theme.blend(fill, self._outer, 0.4), theme.blend(look["border"], self._outer, 0.5)
        args = (size, cpx(self, look["radius"]), fill, border, look["check"], self._outer,
                max(1, cpx(self, look["border_width"])), bool(self._value))
        gap = cpx(self, self.GAP)
        key = ("check", gap) + args

        def make():
            box = _check_picture(*args)
            img = Image.new("RGBA", (size + gap, size), (0, 0, 0, 0))
            img.paste(box, (0, 0))
            return img
        self._photo = shared_photo(self, key, make)
        color = self._disabled_color if self._state == "disabled" else self._text_color
        tk.Label.configure(self, image=self._photo, fg=color, bg=self._outer,
                           cursor="hand2" if self._state != "disabled" else "")
        if getattr(self, "_padded", None) is None:     # высота не меньше 24, как у CTkCheckBox
            self._padded = max(0, (cpx(self, self._min_height) - self.winfo_reqheight()) // 2)
            tk.Label.configure(self, pady=self._padded)

    def _set_hover(self, hover):
        if hover != self._hover:
            self._hover = hover
            self._paint()

    def _clicked(self, _event=None):
        self.toggle()

    def toggle(self):
        """Как щелчок мышью (и как CTkCheckBox.toggle): переключить и позвать command."""
        if self._state == "disabled":
            return
        self._value = 0 if self._value else 1
        self._paint()
        if self._command:
            self._command()

    def select(self):
        self._value = 1
        self._paint()

    def deselect(self):
        self._value = 0
        self._paint()

    def get(self):
        return self._value

    def configure(self, cnf=None, **kwargs):
        if "state" in kwargs:
            self._state = kwargs.pop("state")
        if "command" in kwargs:
            self._command = kwargs.pop("command")
        if "text_color" in kwargs:
            self._text_color = kwargs.pop("text_color")
        if kwargs or cnf:
            tk.Label.configure(self, cnf, **kwargs)
        self._paint()

    config = configure

    def cget(self, key):
        if key == "state":
            return self._state
        return tk.Label.cget(self, key)
