"""«Руководство» нового окна (задача 15, шаг 10.0; макет design/mockups/06_guide) — вместо ui/guide_tab.py.

Текст — guide/<язык>.md (нет — guide/en.md, потом guide/ru.md), разметка — design/GUIDE_FORMAT.md, разбор без Tk —
ui/guide_renderer.py. Файл перечитывается при каждом показе страницы (App._show_frame → refresh_data): поправили текст —
видно сразу, без перезапуска. Страница перестраивается, только если поменялся текст или язык окна.

Слева — оглавление: «Знакомство с ботом» (всё до первого ##) и разделы по порядку; щелчок прокручивает текст к разделу,
активный пункт синий (и при прокрутке колёсиком — тот, что сейчас вверху). Внизу — «Остались вопросы? Написать автору →»
(та же почта, что «Написать автору» в «О программе»). Справа — текст: каждая конструкция Markdown — свой «кирпичик»
(абзацы и списки, карточки шагов по 2 в ряд, плашки, картинка с подписью, линия). Картинки нет — серая рамка с подписью.

Окно в Windows не должно оставлять следов и тормозить при прокрутке (сессия 11, logs/session_11): на странице нет ни одного
элемента CustomTkinter. Прокрутка — light.ScrollArea, каждый раздел — своя часть: на одном листе во всю длину текст
обрывался на разделе 10 (у Tk координаты окон 16-битные, а раздел 10 начинался ниже 32 767 px). Полосы прокрутки —
light.Scrollbar: у CTkScrollbar каждый сдвиг ползунка звал update_idletasks, и в длинном руководстве полоса вызывала сама
себя по кругу (фризы ui_freeze_*.txt). Абзацы и списки подряд — одно текстовое поле (RichText: жирный, моноширинный,
ссылки, значки пунктов; текст можно выделить мышью и скопировать — Ctrl+C или правой кнопкой «Копировать»): полей
в 2 раза меньше, чем было по одному на абзац и пункт. Карточки и плашки — рамки Tk на готовых скруглённых подложках
(widgets.plain_card, RoundedBackdrop). Наведение меняет только цвета. Разделы строятся по частям: сначала видимые —
под заслонкой (widgets.LoadingCover: фон и крутящееся кольцо, пока их раскладка не улеглась; раньше страница проступала
кусками), остальные — порциями не дольше BUILD_BUDGET_MS, между ними окно обрабатывает свои события. Окно программы
строит руководство заранее, в фоне после запуска (App._prepare → build_ahead): к первому открытию оно уже готово.
Сессия 11б: строится оно запаркованным (страница разложена, но не показана — App._park_page), а на открытой странице
показаны только разделы рядом с видимой частью (light.ScrollArea паркует дальние): элементов, которые Windows держит
показанными, — сотни, а не 2070, как было.
"""
import os
import time
import tkinter as tk
import webbrowser
from functools import lru_cache

from PIL import Image as PILImage
from PIL import ImageDraw, ImageTk

from i18n import get_text
from ui import about_data, light, theme
from ui import guide_renderer as gr
from ui.widgets import (LoadingCover, PlainClickFrame, PlainLabel, PopupMenu, RoundedBackdrop, Toast, plain_card,
                        plain_icon, px, scaled_font, shared_photo)
from ui.widgets import _plain_icon_picture

C = theme.COLORS
T = theme.TINTS
F = theme.FONTS
S = theme.SIZES
PAGE = C["bg_primary"]
BG = C["bg_surface"]
ELEV = C["bg_elevated"]
TOC_WIDTH = 240
WHEEL_STEP = 40           # колёсико мыши: на столько пикселей за щелчок
BACKDROP_DELAY_MS = 40    # подложка карточки рисуется, когда её размер не менялся столько мс
IMAGE_DELAY_MS = 120      # картинка подгоняется под ширину не на каждый шаг растягивания окна
FIRST_SECTIONS = 2        # столько разделов строится сразу (их видно первыми), остальные — порциями
BUILD_BUDGET_MS = 25      # порция постройки: не дольше (потом окно обрабатывает свои события)
BUILD_PAUSE_MS = 15       # пауза между порциями
READY_CHECK_MS = 40       # заслонка: как часто проверять, улеглась ли раскладка первых разделов
READY_MAX_MS = 2000       # ... и не дольше (потом страница показывается как есть)
LINE_SPACING = 5          # между строками абзаца (макет: высота строки 1.6 при шрифте 14)
BLOCK_GAP = 14            # между абзацами, списками и плашками
ITEM_GAP = 8              # между пунктами списка
MARK_WIDTH, MARK_GAP = 14, 10   # значок пункта списка и отступ до текста
TEXT_TAG = "GuideText"    # общие привязки всех текстовых полей руководства (одна команда на все поля)

# Плашки: заливка, рамка, значок, цвет значка и заголовка, ключ заголовка (у «Готово» и подсказки заголовка нет)
CALLOUT_LOOK = {
    "tip": (PAGE, C["border"], None, C["text_secondary"], None),
    "note": (T["info_banner_bg"], T["info_banner_border"], "info", C["blue_text"], "gd_note"),
    "warning": (T["warning_banner_bg"], T["warning_banner_border"], "triangle-alert", C["warning"], "gd_warning"),
    "done": (T["done_bg"], T["done_border"], "check", C["success"], None),
}


@lru_cache(maxsize=1)
def icon_names():
    """Имена иконок ui/icons (без .png): «- :имя: пункт» с другим именем — пункт с точкой."""
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
    return frozenset(name[:-4] for name in os.listdir(folder) if name.endswith(".png"))


@lru_cache(maxsize=64)
def _disc_picture(size, color, icon_name, icon_color):
    """Кружок с прозрачными уголками (номер раздела и шага кладёт надпись поверх); icon_name — значок внутри."""
    k = 4
    big = size * k
    img = PILImage.new("RGBA", (big, big), light.rgb(color) + (0,))
    ImageDraw.Draw(img).ellipse((0, 0, big - 1, big - 1), fill=light.rgb(color) + (255,))
    if icon_name:
        from ui.icons import _colored
        glyph_px = big * 6 // 11
        glyph = _colored(icon_name, icon_color).resize((glyph_px, glyph_px), PILImage.LANCZOS)
        img.alpha_composite(glyph, ((big - glyph_px) // 2, (big - glyph_px) // 2))
    return img.resize((size, size), PILImage.LANCZOS)


def disc(master, size, color, icon_name="", icon_color=""):
    args = (px(master, size), color.upper(), icon_name, icon_color.upper())
    return shared_photo(master, ("guide_disc",) + args, lambda: _disc_picture(*args))


def _mark_picture(width, height, icon_name, color, size, top):
    """Значок пункта списка в начале строки текста: прозрачная картинка шириной со столбик значка и высотой со строку,
    значок (или точка) — на том же месте, где был в прежней раскладке (сверху на top, точка — посередине по ширине)."""
    img = PILImage.new("RGBA", (width, max(height, top + size)), (0, 0, 0, 0))
    if icon_name:
        img.alpha_composite(_plain_icon_picture(icon_name, color, size, 0, None, None, 0), (0, top))
    else:
        img.alpha_composite(_disc_picture(size, color, "", ""), ((width - size) // 2, top))
    return img


def bullet_mark(master, icon_name, color, line):
    """Картинка значка пункта (иконка 14 px — на 4 px ниже верха строки, точка 6 px — на 7 px), line — высота строки."""
    size, top = (px(master, 14), px(master, 4)) if icon_name else (px(master, 6), px(master, 7))
    args = (px(master, MARK_WIDTH), line, icon_name, color.upper(), size, top)
    return shared_photo(master, ("guide_mark",) + args, lambda: _mark_picture(*args))


class LazyBackdrop(RoundedBackdrop):
    """Скруглённая подложка (widgets.RoundedBackdrop), но картинка рисуется, когда размер рамки улёгся: пока длинное
    руководство раскладывается, рамки меняют высоту по нескольку раз, и картинка на каждый промежуточный размер
    стоила почти секунду."""

    def __init__(self, master, fill, border, outer, radius=8):
        self._event = None
        self._timer = None
        super().__init__(master, fill, border, outer, radius=radius)

    def _fit(self, event):
        self._event = event
        if self._timer is None:
            try:
                self._timer = self.after(BACKDROP_DELAY_MS, self._fit_now)
            except tk.TclError:
                self._timer = None

    def _fit_now(self):
        self._timer = None
        if self._event is not None and self.winfo_exists():
            super()._fit(self._event)

    def destroy(self):
        if self._timer:
            try:
                self.after_cancel(self._timer)
            except tk.TclError:
                pass
            self._timer = None
        super().destroy()


def lazy_card(master, outer, fill, border=None, radius=None):
    """Карточка как widgets.plain_card, но с LazyBackdrop."""
    frame = tk.Frame(master, bg=outer)
    frame.fill = fill
    frame.backdrop = LazyBackdrop(frame, fill, border or C["border"], outer,
                                  radius=S["radius_card"] if radius is None else radius)
    return frame


def wrap_label(label, start=560):
    """Перенос строк надписи — по её ширине (width=1: надпись не раздвигает рамку, а сжимается с ней)."""
    def fit(event):
        if event.width > 50 and int(float(label.cget("wraplength") or 0)) != event.width:
            label.configure(wraplength=event.width)
    label.configure(wraplength=px(label, start))
    label.bind("<Configure>", fit, add="+")
    return label


def runs(blocks):
    """Абзацы и списки подряд — одним текстовым полем (список блоков), остальное — по одному блоку."""
    run = []
    for block in blocks:
        if isinstance(block, (gr.Paragraph, gr.BulletList)):
            run.append(block)
            continue
        if run:
            yield run
            run = []
        yield block
    if run:
        yield run


class RichText(tk.Frame):
    """Текст с **жирным**, `кодом` и ссылками: обычное текстовое поле Tk только для чтения в рамке нужной высоты
    (высота поля Tk задаётся строками без межстрочного промежутка — поэтому высоту в пикселях держит рамка).
    Абзацы и пункты списка — строки одного поля (paragraph, bullet): отступ перед строкой — spacing1, у пункта значок
    в начале строки и отступ текста (табуляция и lmargin2). Текст можно выделить мышью: Ctrl+C или правая кнопка —
    «Копировать» (выделенное, а без выделения — абзац под мышью). Щелчок, колёсико и наведение на ссылку — общие
    привязки всех полей (TEXT_TAG, light.wheel_through), а не свои команды у каждого поля."""

    def __init__(self, page, master, font, color, bg, spacing=LINE_SPACING):
        super().__init__(master, bg=bg, height=1)
        self.pack_propagate(False)
        self.page = page
        self.font = font
        self.text = tk.Text(self, width=1, height=1, wrap="word", bd=0, highlightthickness=0, padx=0, pady=0, bg=bg,
                            fg=color, font=scaled_font(self, font), relief="flat", cursor="arrow", takefocus=0,
                            spacing2=px(self, spacing), selectbackground=C["blue_button"], selectforeground=C["white"],
                            inactiveselectbackground=C["blue_button"], exportselection=True, insertwidth=0)
        self.text.pack(fill="both", expand=True)
        self.text.rich = self
        family, size, *_rest = font
        # Порядок важен: тег, созданный позже, сильнее — `код` и ссылка внутри подзаголовка остаются кодом и ссылкой
        self.text.tag_configure("heading", font=scaled_font(self, F["body_bold"]), foreground=C["text"])
        self.text.tag_configure("bold", font=scaled_font(self, (family, size, "bold")))
        self.text.tag_configure("code", font=scaled_font(self, (theme.MONO_FAMILY, size - 1)), foreground=C["text"],
                                background=ELEV)
        self.text.tag_configure("link", foreground=C["blue_text"])
        indent = px(self, MARK_WIDTH + MARK_GAP)
        self.text.tag_configure("bullet", lmargin1=0, lmargin2=indent, tabs=(indent,))
        self.links = {}           # тег ссылки -> куда ведёт («#2» или https://…)
        self.lines = 0
        self.cursor = "arrow"
        self._gaps = set()
        self._height = None
        self._width = None
        tags = self.text.bindtags()
        self.text.bindtags(tags[:1] + (TEXT_TAG,) + tags[1:])
        light.wheel_through(self.text)     # колёсико над полем крутит страницу, а не поле

    # ── Строки ───────────────────────────────────────────────────────────────
    def _line(self, gap):
        """Новая строка поля (абзац или пункт); gap — отступ над ней (у первой строки — снаружи, в раскладке)."""
        if self.lines:
            self.text.insert("end", "\n")
        self.lines += 1
        tags = []
        if gap:
            tag = f"gap{gap}"
            if gap not in self._gaps:
                self._gaps.add(gap)
                self.text.tag_configure(tag, spacing1=px(self, gap))
                self.text.tag_lower(tag)
            tags.append(tag)
        return self.lines, tags

    def _spans(self, spans):
        for span in spans:
            if span.style == "link":
                tag = f"link{len(self.links)}"
                self.links[tag] = span.target
                self.text.insert("end", span.text, ("link", tag))
            else:
                self.text.insert("end", span.text, (span.style,) if span.style else ())

    def _tag_line(self, line, tags):
        for tag in tags:
            self.text.tag_add(tag, f"{line}.0", f"{line}.end")

    def paragraph(self, spans, gap=0, heading=False):
        line, tags = self._line(gap)
        self._spans(spans)
        self._tag_line(line, tags + (["heading"] if heading else []))

    def bullet(self, spans, mark, gap=0):
        line, tags = self._line(gap)
        self.text.image_create("end", image=mark, align="top")
        self.text.insert("end", "\t")
        self._spans(spans)
        self._tag_line(line, tags + ["bullet"])

    def finish(self):
        """Текст готов: только чтение; новая ширина — новая высота (_resized)."""
        self.text.configure(state="disabled")
        self.text.bind("<Configure>", self._resized, add="+")

    # ── Высота ───────────────────────────────────────────────────────────────
    def _resized(self, event):
        """Новая ширина — высоту пересчитает страница: все поля разом, одним проходом (page.fit_texts), а не по одному
        на каждое событие (длинное руководство иначе раскладывалось бы секундами)."""
        if event.width != self._width:
            self._width = event.width
            self.page.fit_later(self)

    def fit(self):
        try:
            height = int(self.text.tk.call(self.text._w, "count", "-update", "-ypixels", "1.0", "end"))
        except (tk.TclError, ValueError):
            return
        if height > 0 and height != self._height:
            self._height = height
            self.configure(height=height)

    def plain_text(self):
        return self.text.get("1.0", "end-1c")


def _text_click(event):
    """Щелчок по полю: фокус (Ctrl+C работает в фокусе); по ссылке — перейти."""
    text = event.widget
    rich = getattr(text, "rich", None)
    if rich is None:
        return None
    text.focus_set()
    for tag in text.tag_names("current"):
        if tag in rich.links:
            rich.page.follow(rich.links[tag])
            return "break"
    return None


def _text_motion(event):
    """Указатель над ссылкой — «рука» (меняется только курсор и только когда правда поменялся)."""
    text = event.widget
    rich = getattr(text, "rich", None)
    if rich is None or not rich.links:
        return
    cursor = "hand2" if "link" in text.tag_names("current") else "arrow"
    if cursor != rich.cursor:
        rich.cursor = cursor
        text.configure(cursor=cursor)


def _text_menu(event):
    text = event.widget
    rich = getattr(text, "rich", None)
    if rich is not None:
        rich.page.open_copy_menu(event, text)


def install_text_bindings(root):
    """Привязки TEXT_TAG — один раз на окно программы."""
    if getattr(root, "_guide_text_bindings", False):
        return
    root._guide_text_bindings = True
    root.bind_class(TEXT_TAG, "<Button-1>", _text_click)
    root.bind_class(TEXT_TAG, "<Motion>", _text_motion)
    root.bind_class(TEXT_TAG, "<Button-3>", _text_menu)


class TocItem(PlainClickFrame):
    """Пункт оглавления: кружок с номером (у вступления — значок «i») и название. Активный — синий, наведение — светлее.
    Меняются только цвета подложки, надписей и картинка кружка (готовая)."""

    def __init__(self, page, master, number, title):
        super().__init__(master, command=lambda: page.jump(number), bg=BG, cursor="hand2")
        self.number = number
        self.active = False
        self.backdrop = RoundedBackdrop(self, BG, BG, BG, radius=6)
        self.grid_columnconfigure(1, weight=1)
        self.mark = tk.Label(self, text="" if number == 0 else str(number), compound="center", bd=0,
                             highlightthickness=0, font=scaled_font(self, F["toc_number"]), cursor="hand2")
        self.mark.grid(row=0, column=0, sticky="n", padx=(px(self, 8), px(self, 10)), pady=px(self, 9))
        self.title = wrap_label(PlainLabel(self, title, font=F["text"], color=C["text_secondary"], bg=BG, anchor="w",
                                           justify="left", width=1, cursor="hand2"), 170)
        self.title.grid(row=0, column=1, sticky="ew", padx=(0, px(self, 8)), pady=px(self, 10))
        self.bind_parts(self.mark, self.title)
        self._look = None
        self._paint()

    def set_active(self, active):
        if active != self.active:
            self.active = active
            self._paint()

    def _paint(self):
        fill = T["blue_on_surface"] if self.active else (ELEV if self._hovering else BG)
        circle = C["blue_button"] if self.active else (C["border"] if self._hovering else ELEV)
        text = C["white"] if self.active else (C["text"] if self._hovering else C["text_secondary"])
        look = (fill, circle, text)
        if look == self._look:
            return
        self._look = look
        self.backdrop.restyle(fill, fill)
        self.configure(bg=fill)
        self.mark.photo = disc(self, 22, circle, "info" if self.number == 0 else "", text)
        self.mark.configure(image=self.mark.photo, bg=fill, fg=text)
        self.title.configure(bg=fill, fg=text)


class GuidePage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=PAGE)
        self.controller = controller
        self.lang = getattr(controller, "current_lang", "RU")
        self.shown = None                 # (язык, путь, текст) того, что сейчас на странице; None — ещё не строили
        self.guide = None
        self.path = None
        self.anchors = {}                 # номер раздела -> его часть прокрутки (0 — вступление)
        self.toc_items = {}
        self.active = None
        self._pinned = None               # раздел, к которому прыгнули щелчком (последние разделы не доезжают до верха)
        self._sync_id = None
        self._texts = []                  # (виджет, ключ надписи): язык меняется на лету
        self._menu_target = None
        self._unfitted = set()            # поля RichText, которым надо пересчитать высоту
        self._fit_id = None
        self._pending = []                # (номер по порядку, раздел), которые ещё не построены (строятся порциями)
        self._build_id = None
        self._ready_id = None
        self._ready_since = 0.0
        self._ready_sign = None
        self._sections = 0
        self.next_link = None
        install_text_bindings(self._root())
        self.copy_menu = PopupMenu(self)
        self.copy_menu.add_command(label="", command=self._copy)
        self.grid_columnconfigure(0, minsize=px(self, TOC_WIDTH))
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_toc()
        self._build_article()
        self.cover = LoadingCover(self, PAGE)
        self.update_language(self.lang)

    def text(self, key):
        return theme.plain_text(get_text(self.lang, key))

    def tr(self, widget, key):
        self._texts.append((widget, key))
        return widget

    # ── Каркас ──────────────────────────────────────────────────────────────
    def _build_toc(self):
        card = plain_card(self, PAGE)
        card.grid(row=0, column=0, sticky="nsew", padx=(0, px(self, 16)))
        card.grid_columnconfigure(0, weight=1)
        card.grid_rowconfigure(1, weight=1)
        self.tr(PlainLabel(card, "", font=F["label"], color=C["text_muted"], bg=BG, anchor="w"), "gd_contents").grid(
            row=0, column=0, sticky="ew", padx=px(self, 18), pady=(px(self, 14), px(self, 8)))
        # Отступы у ScrollArea — в пикселях макета (light.Scaled), как у элементов CustomTkinter
        self.toc = light.ScrollArea(card, bg=BG, side=False, auto_hide=True, bar_width=12, wheel_step=WHEEL_STEP,
                                    width=1, height=1)
        self.toc.grid(row=1, column=0, sticky="nsew", padx=(10, 4))
        self.toc_body = self.toc.piece()
        self.toc_body.grid_columnconfigure(0, weight=1)
        bottom = tk.Frame(card, bg=BG)
        bottom.grid(row=2, column=0, sticky="ew", padx=px(self, 18), pady=(px(self, 8), px(self, 14)))
        bottom.grid_columnconfigure(0, weight=1)
        tk.Frame(bottom, bg=C["border"], height=1).grid(row=0, column=0, sticky="ew", pady=(0, px(self, 12)))
        self.tr(PlainLabel(bottom, "", font=F["label"], color=C["text_muted"], bg=BG, anchor="w"), "gd_questions").grid(
            row=1, column=0, sticky="w")
        self.mail_link = PlainLabel(bottom, "", font=F["text"], color=C["blue_text"], bg=BG, anchor="w", cursor="hand2")
        self.mail_link.grid(row=2, column=0, sticky="w", pady=(px(self, 6), 0))
        self.mail_link.bind("<Button-1>", lambda _e: self.write_to_author(), add="+")

    def _build_article(self):
        card = plain_card(self, PAGE)
        card.grid(row=0, column=1, sticky="nsew")
        card.grid_columnconfigure(0, weight=1)
        card.grid_rowconfigure(0, weight=1)
        self.article = light.ScrollArea(card, bg=BG, side=False, on_scroll=self._schedule_sync, bar_width=12,
                                        wheel_step=WHEEL_STEP, width=1, height=1)
        self.article.grid(row=0, column=0, sticky="nsew", padx=(1, 4), pady=S["radius_card"])

    # ── Показ и перестройка ─────────────────────────────────────────────────
    def build_ahead(self):
        """Построить заранее (окно программы зовёт после запуска, пока страница запаркована)."""
        self.refresh_data()

    def refresh_data(self):
        """Перечитать файл (при каждом показе страницы). Текст, язык и картинки те же — ничего не перестраивается."""
        path, text = gr.read_guide(self.lang)
        key = (self.lang, path, text, gr.images_signature(path))
        if key == self.shown:
            return
        self.shown = key
        self.path = path
        self.guide = gr.parse(text) if text else None
        self._rebuild()

    def _rebuild(self):
        self._stop_building()
        self.cover.show()
        self.article.clear()
        for child in self.toc_body.winfo_children():
            child.destroy()
        self.toc.scroll_to(0)
        self.anchors.clear()
        self.toc_items.clear()
        self._unfitted.clear()
        self.active = None
        self._pinned = None
        self.next_link = None
        if self.guide is None:
            missing = self.path or os.path.join(gr.GUIDE_DIR, f"{self.lang.lower()}.md")
            note = gr.Callout("warning", [[gr.Span(self.text("gd_no_file").format(path=missing))]])
            piece = self.article.piece()
            piece.grid_columnconfigure(0, weight=1)
            frame = tk.Frame(piece, bg=BG)
            frame.grid(row=0, column=0, sticky="ew", padx=(px(self, 26), px(self, 24)), pady=px(self, 14))
            frame.grid_columnconfigure(0, weight=1)
            self._callout(frame, note).grid(row=0, column=0, sticky="ew")
            self._wait_ready()
            return
        sections = self.guide.all_sections()
        self._sections = len(sections)
        for row, section in enumerate(sections):
            title = self.text("gd_intro") if section.number == 0 else section.title
            item = TocItem(self, self.toc_body, section.number, title)
            item.grid(row=row, column=0, sticky="ew", pady=(0, px(self, 4)))
            self.toc_items[section.number] = item
        self._pending = list(enumerate(sections))
        self.finish_building(FIRST_SECTIONS)
        self._set_active(min(self.toc_items) if self.toc_items else None)
        self._wait_ready()

    def _wait_ready(self):
        """Заслонка уйдёт, когда раскладка первых разделов улеглась: высоты полей посчитаны, части разложены и два
        раза подряд одни и те же. Остальные разделы строятся потом — уже при открытой странице."""
        self._cancel("_ready_id")
        self._ready_since = time.monotonic()
        self._ready_sign = None
        self._ready_id = self.after(READY_CHECK_MS, self._check_ready)

    def _check_ready(self):
        self._ready_id = None
        area = self.article
        sign = (area.content_height(), area.top(), len(area.pieces))
        busy = bool(self._unfitted) or self._fit_id is not None or area._layout_id is not None or area.busy()
        late = (time.monotonic() - self._ready_since) * 1000 > READY_MAX_MS
        if (not busy and sign == self._ready_sign) or late:
            self.cover.hide()
            if self._pending and self._build_id is None:
                self._build_id = self.after(BUILD_PAUSE_MS, self._build_step)
            return
        self._ready_sign = sign
        self._ready_id = self.after(READY_CHECK_MS, self._check_ready)

    def _cancel(self, name):
        after_id = getattr(self, name)
        if after_id:
            try:
                self.after_cancel(after_id)
            except tk.TclError:
                pass
            setattr(self, name, None)

    def _build_step(self):
        """Следующие разделы — порцией не дольше BUILD_BUDGET_MS, потом пауза: окно обрабатывает свои события
        (раскладку, высоты текста, перерисовку) и не замирает."""
        self._build_id = None
        started = time.perf_counter()
        while self._pending and (time.perf_counter() - started) * 1000 < BUILD_BUDGET_MS:
            self.finish_building(1)
        if self._pending:
            self._build_id = self.after(BUILD_PAUSE_MS, self._build_step)

    def finish_building(self, count=None, upto=None):
        """Построить count следующих разделов; upto — до раздела с этим номером включительно; без них — все."""
        built = 0
        while self._pending and (count is None or built < count):
            row, section = self._pending.pop(0)
            self._section(row, section)
            built += 1
            if upto is not None and section.number >= upto:
                break

    def _stop_building(self):
        self._pending = []
        if self._build_id:
            try:
                self.after_cancel(self._build_id)
            except tk.TclError:
                pass
            self._build_id = None

    def _section(self, row, section):
        piece = self.article.piece()
        piece.grid_columnconfigure(0, weight=1)
        self.anchors[section.number] = piece
        frame = tk.Frame(piece, bg=BG)
        frame.grid(row=0, column=0, sticky="ew", padx=(px(self, 26), px(self, 24)))
        frame.grid_columnconfigure(0, weight=1)
        r = 0
        if row > 0:
            tk.Frame(frame, bg=C["border"], height=1).grid(row=r, column=0, sticky="ew", pady=(px(self, 28), 0))
            r += 1
        if section.number == 0:
            caption = self.text("gd_caption").upper()
            title, font = self.guide.title, F["guide_title"]
        else:
            caption = self.text("gd_section").format(n=section.number).upper()
            title, font = section.title, F["guide_heading"]
        PlainLabel(frame, caption, font=F["label_bold"], color=C["blue_text"], bg=BG, anchor="w").grid(
            row=r, column=0, sticky="w", pady=(px(self, 24 if row > 0 else 14), 0))
        r += 1
        if title:
            wrap_label(PlainLabel(frame, title, font=font, color=C["text"], bg=BG, anchor="w", justify="left",
                                  width=1)).grid(row=r, column=0, sticky="ew", pady=(px(self, 10), 0))
            r += 1
        for block in runs(section.blocks):
            widget = self._block(frame, block)
            if widget is not None:
                widget.grid(row=r, column=0, sticky="ew", pady=(px(self, BLOCK_GAP), 0))
                r += 1
        if row == self._sections - 1:
            tk.Frame(frame, bg=BG, height=px(self, 24)).grid(row=r, column=0)   # отступ под последним разделом
        return piece

    def _block(self, parent, block):
        if isinstance(block, list):
            return self._flow(parent, block)
        if isinstance(block, gr.Steps):
            return self._steps(parent, block)
        if isinstance(block, gr.Callout):
            return self._callout(parent, block)
        if isinstance(block, gr.Image):
            return GuideImage(self, parent, block)
        if isinstance(block, gr.Rule):
            return tk.Frame(parent, bg=C["border"], height=1)
        return None

    def _flow(self, parent, blocks):
        """Абзацы и списки подряд — одно поле: между блоками BLOCK_GAP, между пунктами ITEM_GAP (как было в раскладке)."""
        rich = RichText(self, parent, F["body"], C["guide_text"], BG)
        line = light.line_height(rich, F["body"])
        colors = theme.GUIDE_LIST_ICON_COLORS
        for n, block in enumerate(blocks):
            gap = BLOCK_GAP if n else 0
            if isinstance(block, gr.Paragraph):
                rich.paragraph(block.spans, gap=gap, heading=block.bold)
                continue
            for row, item in enumerate(block.items):
                has_icon = item.icon in icon_names()        # иконки нет в ui/icons — синяя точка, окно не падает
                mark = bullet_mark(rich, item.icon if has_icon else "",
                                   colors[row % len(colors)] if has_icon else C["blue_text"], line)
                rich.bullet(item.spans, mark, gap=gap if row == 0 else ITEM_GAP)
        rich.finish()
        return rich

    def _steps(self, parent, block):
        grid = tk.Frame(parent, bg=BG)
        grid.grid_columnconfigure((0, 1), weight=1, uniform="steps")
        gap = px(self, 6)
        for n, step in enumerate(block.items):
            card = lazy_card(grid, BG, ELEV)
            card.grid(row=n // 2, column=n % 2, sticky="nsew", padx=(0, gap) if n % 2 == 0 else (gap, 0),
                      pady=(0 if n < 2 else 2 * gap, 0))
            card.grid_columnconfigure(1, weight=1)
            number = tk.Label(card, image=disc(card, 28, C["blue_button"]), text=str(step.number), compound="center",
                              fg=C["white"], bg=ELEV, bd=0, highlightthickness=0,
                              font=scaled_font(card, F["button_bold"]))
            number.grid(row=0, column=0, sticky="n", padx=(px(self, 14), px(self, 12)), pady=px(self, 14))
            column = tk.Frame(card, bg=ELEV)
            column.grid(row=0, column=1, sticky="nsew", padx=(0, px(self, 14)), pady=px(self, 14))
            column.grid_columnconfigure(0, weight=1)
            r = 0
            if step.title:
                self._rich(column, [step.title], F["card_title"], C["text"], ELEV, 3).grid(
                    row=r, column=0, sticky="ew", pady=(px(self, 4), 0))
                r += 1
            if step.spans:
                self._rich(column, [step.spans], F["text"], C["guide_text"], ELEV, 4).grid(
                    row=r, column=0, sticky="ew", pady=(px(self, 6) if r else px(self, 4), 0))
                r += 1
            for tip in step.tips:
                box = tk.Frame(column, bg=ELEV)
                box.grid(row=r, column=0, sticky="ew", pady=(px(self, 8), 0))
                LazyBackdrop(box, PAGE, PAGE, ELEV, radius=6)
                box.grid_columnconfigure(0, weight=1)
                self._rich(box, [tip], F["label"], C["text_secondary"], PAGE, 3).grid(
                    row=0, column=0, sticky="ew", padx=px(self, 10), pady=px(self, 8))
                r += 1
        return grid

    def _rich(self, parent, paragraphs, font, color, bg, spacing, gap=0):
        """Поле с абзацами одного вида (шаг, подсказка, плашка); gap — между абзацами."""
        rich = RichText(self, parent, font, color, bg, spacing=spacing)
        for n, spans in enumerate(paragraphs):
            rich.paragraph(spans, gap=gap if n else 0)
        rich.finish()
        return rich

    def _callout(self, parent, block):
        fill, border, icon_name, color, title_key = CALLOUT_LOOK[block.kind]
        frame = tk.Frame(parent, bg=BG)
        LazyBackdrop(frame, fill, border, BG, radius=S["radius_card"])
        frame.grid_columnconfigure(1, weight=1)
        paragraphs = [list(p) for p in block.paragraphs]
        link = None
        if block.kind == "done" and paragraphs and paragraphs[-1] and paragraphs[-1][-1].style == "link":
            link = paragraphs[-1].pop()             # макет: ссылка «Следующий раздел →» — справа
            if paragraphs[-1] and not paragraphs[-1][-1].text.strip():
                paragraphs[-1].pop()
        if icon_name:
            photo = plain_icon(frame, icon_name, color, 18)
            mark = tk.Label(frame, image=photo, bg=fill, bd=0, highlightthickness=0)
            mark.photo = photo
            mark.grid(row=0, column=0, sticky="n", padx=(px(self, 14), px(self, 12)), pady=px(self, 13))
        column = tk.Frame(frame, bg=fill)
        column.grid(row=0, column=1, sticky="ew", padx=(0 if icon_name else px(self, 14), px(self, 14)),
                    pady=px(self, 12))
        column.grid_columnconfigure(0, weight=1)
        r = 0
        if title_key:
            PlainLabel(column, self.text(title_key), font=F["button_bold"], color=color, bg=fill, anchor="w").grid(
                row=r, column=0, sticky="w", pady=(px(self, 1), px(self, 4)))
            r += 1
        paragraphs = [p for p in paragraphs if p]
        if paragraphs:
            text_color = C["text_secondary"] if block.kind == "tip" else C["guide_text"]
            self._rich(column, paragraphs, F["text"], text_color, fill, 4, gap=6).grid(
                row=r, column=0, sticky="ew", pady=(px(self, 1), 0))
        if link is not None:
            label = PlainLabel(frame, link.text, font=F["text"], color=C["blue_text"], bg=fill, cursor="hand2")
            label.grid(row=0, column=2, sticky="e", padx=(px(self, 8), px(self, 14)))
            label.bind("<Button-1>", lambda _e, t=link.target: self.follow(t), add="+")
            self.next_link = label
        return frame

    def fit_later(self, text):
        self._unfitted.add(text)
        if self._fit_id is None:
            try:
                self._fit_id = self.after_idle(self.fit_texts)
            except tk.TclError:
                self._fit_id = None

    def fit_texts(self):
        """Высота всех полей, у которых поменялась ширина, — за один проход: раскладка пересчитается один раз."""
        self._fit_id = None
        texts, self._unfitted = self._unfitted, set()
        for text in texts:
            if text.winfo_exists():
                text.fit()

    # ── Ссылки, оглавление, прокрутка ───────────────────────────────────────
    def follow(self, target):
        """Ссылка из текста: #N — к разделу N, https:// и mailto: — в браузер (не открылась — в буфер обмена)."""
        if target.startswith("#"):
            number = target[1:]
            if number.isdigit():
                self.jump(int(number))
            return
        if not about_data.launch(target, opener=webbrowser.open):
            self._to_clipboard(target, "ab_open_failed", kind="warning")

    def jump(self, number):
        """К разделу: он встаёт наверх и держится там, пока разделы выше него ещё раскладываются (без «доделай всё
        сейчас» — update_idletasks в обработчике щелчка, см. правила в начале ui/widgets.py)."""
        if number not in self.toc_items:
            return
        if number not in self.anchors:
            self.finish_building(upto=number)      # раздел ещё не построен — достроить до него
        if number == min(self.anchors):
            self.article.scroll_to(0)
        else:
            self.article.show_piece(self.anchors[number])
        self._pinned = number
        self._set_active(number)

    def _schedule_sync(self):
        if self._sync_id is None:
            try:
                self._sync_id = self.after_idle(self._sync_active)
            except tk.TclError:
                self._sync_id = None

    def _sync_active(self):
        """Активный пункт — раздел, который сейчас вверху текста. После щелчка — тот, к которому прыгнули,
        пока он виден (последние разделы до верха не доезжают)."""
        self._sync_id = None
        if not self.anchors:
            return
        area = self.article
        top, view = area.top(), area.view_height()
        if self._pinned in self.anchors:
            piece = self.anchors[self._pinned]
            y = area.offset(piece)
            if y < top + view and y + area.piece_height(piece) > top:
                return
            self._pinned = None
        current = min(self.anchors)
        for number, piece in sorted(self.anchors.items()):
            if area.offset(piece) <= top + px(self, 40):
                current = number
        self._set_active(current)

    def _set_active(self, number):
        if number == self.active:
            return
        self.active = number
        for n, item in self.toc_items.items():
            item.set_active(n == number)
        item = self.toc_items.get(number)
        if item is not None and item.winfo_height() > 1:   # разложен (страница могла ещё показываться под заслонкой)
            self.toc.see(item.winfo_y(), item.winfo_height())

    # ── Копирование, почта ──────────────────────────────────────────────────
    def open_copy_menu(self, event, text):
        self._menu_target = (text, text.index(f"@{event.x},{event.y}"))
        self.copy_menu.tk_popup(event.x_root, event.y_root)

    def _copy(self):
        """«Копировать»: выделенное, а если ничего не выделено — абзац (пункт) под мышью или всё поле."""
        target = self._menu_target
        if target is None:
            return
        text, index = target if isinstance(target, tuple) else (target, None)
        try:
            chosen = text.get("sel.first", "sel.last")
        except tk.TclError:
            if index is None:
                chosen = text.get("1.0", "end-1c")
            else:
                line = index.split(".")[0]
                chosen = text.get(f"{line}.0", f"{line}.end")
        chosen = "\n".join(part.lstrip("\t") for part in chosen.split("\n"))   # у пунктов списка — без табуляции
        self.clipboard_clear()
        self.clipboard_append(chosen)

    def write_to_author(self):
        if not about_data.launch(about_data.mail_url(), opener=webbrowser.open):
            self._to_clipboard(about_data.EMAIL, "ab_open_failed", kind="warning")

    def _to_clipboard(self, text, message, kind="success"):
        self.clipboard_clear()
        self.clipboard_append(text)
        Toast(self, self.text(message), kind=kind)

    # ── Язык и закрытие ─────────────────────────────────────────────────────
    def update_language(self, lang):
        self.lang = lang
        for widget, key in self._texts:
            text = self.text(key)
            if widget.cget("text") != text:
                widget.configure(text=text)
        self.mail_link.configure(text=self.text("about_btn_mail") + " →")
        self.copy_menu.entryconfigure(0, label=self.text("ctx_copy"))
        if self.shown is not None:            # страницу уже показывали: другой язык — другой файл и подписи
            self.refresh_data()

    def destroy(self):
        self._stop_building()
        for name in ("_fit_id", "_sync_id", "_ready_id"):
            self._cancel(name)
        super().destroy()


class GuideImage(tk.Frame):
    """Картинка на всю ширину текста (больше своего размера не растягивается) и подпись снизу серым мелким шрифтом.
    Файл — из папки языка руководства (gr.find_image: guide/images/ru/имя.png, общая, en, ru). Нет или не читается — серая рамка
    «Картинки пока нет: images/ru/имя.png» — куда положить скриншот для этого языка (скриншоты пользователь добавит сам)."""

    def __init__(self, page, master, block):
        super().__init__(master, bg=BG)
        self.page = page
        self.block = block
        self.grid_columnconfigure(0, weight=1)
        self.source = None
        self._width = None
        self._timer = None
        path = gr.find_image(page.path, block.path)
        try:
            if path:
                with PILImage.open(path) as img:
                    self.source = img.convert("RGBA")
        except (OSError, ValueError):
            self.source = None
        if self.source is not None:
            self.picture = tk.Label(self, bg=BG, bd=0, highlightthickness=0)
            self.picture.grid(row=0, column=0)
            self.bind("<Configure>", self._resized, add="+")
        else:
            self.picture = tk.Frame(self, bg=BG, height=px(self, 150))
            self.picture.grid(row=0, column=0, sticky="ew")
            self.picture.grid_propagate(False)
            self.picture.grid_columnconfigure(0, weight=1)
            self.picture.grid_rowconfigure((0, 3), weight=1)
            LazyBackdrop(self.picture, ELEV, C["border_strong"], BG, radius=S["radius_card"])
            photo = plain_icon(self, "image", C["text_muted"], 28)
            mark = tk.Label(self.picture, image=photo, bg=ELEV, bd=0, highlightthickness=0)
            mark.photo = photo
            mark.grid(row=1, column=0)
            where = gr.expected_image(page.path, block.path)
            self.missing = PlainLabel(self.picture, page.text("gd_no_image").format(path=where), font=F["label"],
                                      color=C["text_muted"], bg=ELEV)
            self.missing.grid(row=2, column=0, pady=(px(self, 8), 0))
        if block.caption:
            wrap_label(PlainLabel(self, block.caption, font=F["label"], color=C["text_muted"], bg=BG, justify="center",
                                  width=1)).grid(row=1, column=0, sticky="ew", pady=(px(self, 8), 0))

    def _resized(self, event):
        if event.width < 50 or event.width == self._width:
            return
        if self._timer:
            try:
                self.after_cancel(self._timer)
            except tk.TclError:
                pass
        self._timer = self.after(IMAGE_DELAY_MS if self._width else 0, lambda: self._fit(event.width))

    def _fit(self, width):
        self._timer = None
        self._width = width
        w, h = self.source.size
        if w > width:
            w, h = width, max(1, round(h * width / w))
        self.photo = ImageTk.PhotoImage(self.source.resize((w, h), PILImage.LANCZOS) if (w, h) != self.source.size
                                        else self.source, master=self)
        self.picture.configure(image=self.photo)

    def destroy(self):
        if self._timer:
            try:
                self.after_cancel(self._timer)
            except tk.TclError:
                pass
            self._timer = None
        super().destroy()
