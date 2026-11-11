"""Разбор руководства в Markdown (задача 15, шаг 10.0) — без Tk, проверяется тестами.

Формат — design/GUIDE_FORMAT.md, текст — guide/<язык>.md. Разбор построчный, своими силами (без HTML и без новых
библиотек). Результат — Guide: заголовок (#), вступление (всё до первого ##) и разделы (## — номер ставится сам, с 1).
В каждом — список блоков, из которых ui/guide_page.py собирает виджеты:
- Paragraph — абзац (строки подряд до пустой);
- BulletList — «- пункт» (с иконкой «- :eye: пункт» или с точкой);
- Steps — «1. **Заголовок шага** — текст» подряд (сетка по 2 в ряд); «> [!tip]» с отступом под шагом — внутрь карточки;
- Callout — «> [!tip]», «> [!note]», «> [!warning]», «> [!done]» (следующие строки с «>» — продолжение плашки);
- Image — «![Подпись](images/имя.png)» отдельной строкой (файл — find_image: guide/images/<язык>/имя.png, общая, en, ru);
- Rule — «---».
Внутри текста (Span): **жирный**, `моноширинный`, [ссылка](#N) — к разделу N (#0 — к вступлению) или https:// — в браузер.
Всё, чего нет в таблице формата, показывается обычным текстом — ничего не ломается (значки разметки при этом убираются).

Файл: guide/<язык>.md (имя — код языка из i18n.py маленькими буквами), нет — guide/en.md, потом guide/ru.md (guide_file).
problems() — что в руководстве не так (иконки, которых нет, ссылки на несуществующие разделы, непонятные плашки).
"""
import os
import re
import sys
from dataclasses import dataclass, field


def guide_dir(frozen=None, bundle=None, isdir=os.path.isdir):
    """Папка руководства: guide/ рядом с программой; в собранном .exe её нет рядом — та, что внутри сборки
    (папка _internal, sys._MEIPASS). Положили свою guide/ рядом с .exe — берётся она."""
    frozen = getattr(sys, "frozen", False) if frozen is None else frozen
    bundle = getattr(sys, "_MEIPASS", None) if bundle is None else bundle
    if frozen and bundle and not isdir("guide"):
        return os.path.join(bundle, "guide")
    return "guide"


GUIDE_DIR = guide_dir()
FALLBACK_LANGS = ("en", "ru")
CALLOUTS = ("tip", "note", "warning", "done")


# ── Что получается из файла ──────────────────────────────────────────────────
@dataclass
class Span:
    text: str
    style: str = ""          # "", "bold", "code", "link"
    target: str = ""         # у ссылки: "#2" или "https://..."


@dataclass
class Paragraph:
    spans: list
    bold: bool = False       # «### подзаголовок» (его в формате нет) — жирным абзацем, без решёток


@dataclass
class BulletItem:
    spans: list
    icon: str = ""           # имя иконки из ui/icons без .png, "" — синяя точка


@dataclass
class BulletList:
    items: list


@dataclass
class Step:
    title: list              # Span-ы заголовка (то, что в **…** в начале), может быть пустым
    spans: list              # текст шага после « — »
    tips: list = field(default_factory=list)   # [[Span, ...], ...] — плашки «[!tip]» внутри карточки
    number: int = 0


@dataclass
class Steps:
    items: list


@dataclass
class Callout:
    kind: str                # tip / note / warning / done
    paragraphs: list         # [[Span, ...], ...]


@dataclass
class Image:
    caption: str
    path: str                # как написано в файле: images/usb.png


@dataclass
class Rule:
    pass


@dataclass
class Section:
    number: int              # 0 — вступление, дальше 1, 2, …
    title: str               # без разметки (для оглавления)
    blocks: list


@dataclass
class Guide:
    title: str
    intro: Section
    sections: list

    def all_sections(self):
        """Вступление (если в нём что-то есть) и разделы — по порядку, как в оглавлении."""
        return ([self.intro] if self.intro.blocks or self.title else []) + list(self.sections)


# ── Строка → куски текста ───────────────────────────────────────────────────
_INLINE = re.compile(r"\*\*(?P<bold>.+?)\*\*|`(?P<code>[^`]+)`|\[(?P<ltext>[^\]]+)\]\((?P<target>[^)\s]+)\)")


def inline(text):
    """Строка с **жирным**, `кодом` и [ссылками](#N) → список Span. Соседние куски одного вида склеиваются."""
    spans = []

    def add(piece, style="", target=""):
        if not piece:
            return
        if spans and spans[-1].style == style and spans[-1].target == target and style != "link":
            spans[-1].text += piece
        else:
            spans.append(Span(piece, style, target))

    pos = 0
    for m in _INLINE.finditer(text):
        add(text[pos:m.start()])
        if m.group("bold") is not None:
            add(m.group("bold"), "bold")
        elif m.group("code") is not None:
            add(m.group("code"), "code")
        else:
            label = m.group("ltext").replace("**", "")
            target = m.group("target")
            if target.startswith("#") or target.startswith(("http://", "https://", "mailto:")):
                add(label, "link", target)
            else:                       # ссылка на файл и прочее — просто текст
                add(label)
        pos = m.end()
    add(text[pos:])
    return spans


def plain(text):
    """Текст строки без разметки (для оглавления)."""
    return "".join(span.text for span in inline(text)).strip()


def spans_text(spans):
    return "".join(span.text for span in spans)


# ── Разбор файла ─────────────────────────────────────────────────────────────
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_STEP = re.compile(r"^(\d+)[.)]\s+(.*)$")
_BULLET = re.compile(r"^[-*+]\s+(.*)$")
_ICON = re.compile(r"^:([a-z0-9-]+):\s*(.*)$")
_CALLOUT = re.compile(r"^\[!(\w+)\]\s*(.*)$")
_IMAGE = re.compile(r"^!\[(?P<caption>[^\]]*)\]\((?P<path>[^)\s]+)\)\s*$")
_RULE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
_STEP_TITLE = re.compile(r"^\*\*(?P<title>.+?)\*\*\s*(?:[—–-]\s*)?(?P<rest>.*)$")


def _indent(line):
    return len(line) - len(line.lstrip(" \t"))


def _quote_body(line):
    """«> текст» → «текст» (один пробел после «>» убирается)."""
    body = line.strip()[1:]
    return body[1:] if body.startswith(" ") else body


def _callout(first, more):
    """Первая строка цитаты (уже без «>») и следующие строки с «>» → Callout или Paragraph (обычная цитата)."""
    m = _CALLOUT.match(first.strip())
    lines = [first if not m else m.group(2)] + more
    paragraphs, current = [], []
    for line in lines:
        if line.strip():
            current.append(line.strip())
        elif current:
            paragraphs.append(current)
            current = []
    if current:
        paragraphs.append(current)
    paragraphs = [inline(" ".join(p)) for p in paragraphs]
    kind = m.group(1).lower() if m else ""
    if kind in CALLOUTS:
        return [Callout(kind, paragraphs or [[]])]
    return [Paragraph(p) for p in paragraphs]       # обычная цитата или незнакомая плашка — простым текстом


def _step(number, text):
    m = _STEP_TITLE.match(text.strip())
    if m:
        rest = m.group("rest")
        rest = rest[:1].upper() + rest[1:]          # «… — на телефоне зайди» → «На телефоне зайди» (под заголовком)
        return Step(inline(m.group("title")), inline(rest), number=number)
    return Step([], inline(text.strip()), number=number)


def parse(text):
    """Текст файла → Guide."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    title = ""
    intro = Section(0, "", [])
    sections = []
    current = intro
    i = 0

    def blocks():
        return current.blocks

    def add_paragraph(parts, bold=False):
        if parts:
            blocks().append(Paragraph(inline(" ".join(p.strip() for p in parts)), bold=bold))

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        heading = _HEADING.match(stripped) if _indent(line) < 4 else None
        if heading:
            level, words = len(heading.group(1)), heading.group(2)
            if level == 1 and not title and not sections:
                title = plain(words)
            elif level == 2:
                current = Section(len(sections) + 1, plain(words), [])
                sections.append(current)
            else:                                   # «#» второй раз, «###» — в формате их нет: жирный абзац
                add_paragraph([words], bold=True)
            i += 1
            continue

        if _RULE.match(stripped):
            blocks().append(Rule())
            i += 1
            continue

        image = _IMAGE.match(stripped)
        if image:
            blocks().append(Image(plain(image.group("caption")), image.group("path")))
            i += 1
            continue

        if stripped.startswith(">"):
            first = _quote_body(line)
            more = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith(">"):
                more.append(_quote_body(lines[i]))
                i += 1
            blocks().extend(_callout(first, more))
            continue

        step = _STEP.match(stripped)
        if step:
            items = []
            while i < len(lines):
                if not lines[i].strip():            # пустая строка между шагами — шаги всё равно одной сеткой
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and _STEP.match(lines[j].strip()) and _indent(lines[j]) < 2:
                        i = j
                    else:
                        break
                m = _STEP.match(lines[i].strip())
                if not m or _indent(lines[i]) >= 2 and items:
                    break
                item = _step(int(m.group(1)), m.group(2))
                items.append(item)
                i += 1
                i = _step_tail(lines, i, item)
            for n, item in enumerate(items, start=1):
                item.number = n                     # номер по порядку (в Markdown все шаги можно писать «1.»)
            blocks().append(Steps(items))
            continue

        bullet = _BULLET.match(stripped)
        if bullet and not _RULE.match(stripped):
            items = []
            while i < len(lines):
                m = _BULLET.match(lines[i].strip())
                if not m or _RULE.match(lines[i].strip()):
                    break
                words = m.group(1)
                icon = _ICON.match(words)
                parts = [icon.group(2) if icon else words]
                i += 1
                while i < len(lines) and lines[i].strip() and _indent(lines[i]) >= 2 \
                        and not _BULLET.match(lines[i].strip()):
                    parts.append(lines[i].strip())  # перенос пункта на следующую строку (с отступом)
                    i += 1
                items.append(BulletItem(inline(" ".join(parts)), icon.group(1) if icon else ""))
            blocks().append(BulletList(items))
            continue

        parts = []
        while i < len(lines):
            s = lines[i].strip()
            if not s or (_HEADING.match(s) and _indent(lines[i]) < 4) or s.startswith(">") or _RULE.match(s) \
                    or _IMAGE.match(s) or _STEP.match(s) or _BULLET.match(s):
                break
            parts.append(s)
            i += 1
        add_paragraph(parts)
    return Guide(title, intro, sections)


def _step_tail(lines, i, item):
    """Строки под шагом с отступом: «> [!tip] …» — плашка внутри карточки, обычный текст — продолжение шага."""
    while i < len(lines):
        line = lines[i]
        if not line.strip() or _indent(line) < 2:
            if line.strip() or not _continues_step(lines, i):
                break
            i += 1                                   # пустая строка между шагом и его подсказкой
            continue
        body = line.strip()
        if body.startswith(">"):
            first = _quote_body(body)
            more = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith(">") and _indent(lines[i]) >= 2:
                more.append(_quote_body(lines[i]))
                i += 1
            for block in _callout(first, more):
                if isinstance(block, Callout):
                    for paragraph in block.paragraphs:
                        item.tips.append(paragraph)
                else:
                    item.tips.append(block.spans)
            continue
        if item.spans and not item.spans[-1].text.endswith(" "):
            item.spans.append(Span(" "))
        item.spans.extend(inline(body))
        i += 1
    return i


def _continues_step(lines, i):
    """После пустой строки шаг продолжается, только если дальше строка с отступом (подсказка шага)."""
    j = i
    while j < len(lines) and not lines[j].strip():
        j += 1
    return j < len(lines) and _indent(lines[j]) >= 2 and not _STEP.match(lines[j].strip())


# ── Файл руководства ─────────────────────────────────────────────────────────
def guide_file(lang, folder=GUIDE_DIR):
    """Путь к руководству на языке окна: guide/<код>.md, нет — en.md, потом ru.md. Нет ни одного — None."""
    for code in (lang.lower(),) + FALLBACK_LANGS:
        path = os.path.join(folder, f"{code}.md")
        if os.path.isfile(path):
            return path
    return None


def read_guide(lang, folder=GUIDE_DIR):
    """(путь, текст) руководства или (None, "") — файла нет или он не читается."""
    path = guide_file(lang, folder)
    if not path:
        return None, ""
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            return path, f.read()
    except (OSError, UnicodeDecodeError):
        return path, ""


def image_path(guide_path, path):
    """Картинка из файла (images/usb.png) — рядом с руководством: guide/images/usb.png."""
    return os.path.normpath(os.path.join(os.path.dirname(guide_path or os.path.join(GUIDE_DIR, "x")), path))


# ── Картинки по языкам ───────────────────────────────────────────────────────
# В тексте путь один на все языки (images/usb.png), а скриншоты лежат по папкам языков: guide/images/ru/usb.png,
# guide/images/en/usb.png. Переводчик (translate_guide.py) путь не трогает, поэтому новый скриншот достаточно положить
# в папку своего языка. Своей картинки нет — общая (guide/images/usb.png, для всех языков), потом английская, потом русская
# (как у самих файлов руководства). Расширение может быть любое из IMAGE_EXTS: usb.jpg подойдёт вместо usb.png.
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def guide_lang(guide_path):
    """Код языка руководства по имени файла: guide/ru.md → "ru" (нет файла — "ru")."""
    return os.path.splitext(os.path.basename(guide_path))[0].lower() if guide_path else "ru"


def image_dirs(guide_path, path):
    """Папки, где искать картинку images/usb.png, по порядку: images/<язык>, images (общая), images/en, images/ru."""
    folder = os.path.dirname(image_path(guide_path, path))
    langs = [guide_lang(guide_path)]
    dirs = [os.path.join(folder, langs[0]), folder]
    for code in FALLBACK_LANGS:
        if code not in langs:
            langs.append(code)
            dirs.append(os.path.join(folder, code))
    return dirs


def find_image(guide_path, path):
    """Файл картинки для руководства этого языка или None (тогда страница рисует серую рамку)."""
    stem = os.path.splitext(os.path.basename(path))[0]
    ext = os.path.splitext(path)[1].lower()
    exts = (ext,) + tuple(e for e in IMAGE_EXTS if e != ext)
    for folder in image_dirs(guide_path, path):
        for e in exts:
            candidate = os.path.join(folder, stem + e)
            if os.path.isfile(candidate):
                return candidate
    return None


def expected_image(guide_path, path):
    """Куда положить картинку для этого языка — для серой рамки: images/ru/usb.png."""
    head, name = os.path.split(path.replace("\\", "/"))
    return "/".join(part for part in (head, guide_lang(guide_path), name) if part)


def images_signature(guide_path, folder=None):
    """Что лежит в папках картинок (имя, время, размер): новый скриншот виден при следующем показе страницы."""
    folder = folder or os.path.join(os.path.dirname(guide_path or os.path.join(GUIDE_DIR, "x")), "images")
    found = []
    for sub in [folder] + [os.path.join(folder, code) for code in (guide_lang(guide_path),) + FALLBACK_LANGS]:
        try:
            with os.scandir(sub) as entries:
                for entry in entries:
                    if entry.is_file() and entry.name.lower().endswith(IMAGE_EXTS):
                        stat = entry.stat()
                        found.append((sub, entry.name, stat.st_mtime_ns, stat.st_size))
        except OSError:
            continue
    return tuple(sorted(set(found)))


# ── Проверка руководства ─────────────────────────────────────────────────────
def iter_spans(guide):
    for section in guide.all_sections():
        for block in section.blocks:
            if isinstance(block, Paragraph):
                yield from block.spans
            elif isinstance(block, BulletList):
                for item in block.items:
                    yield from item.spans
            elif isinstance(block, Steps):
                for item in block.items:
                    yield from item.title
                    yield from item.spans
                    for tip in item.tips:
                        yield from tip
            elif isinstance(block, Callout):
                for paragraph in block.paragraphs:
                    yield from paragraph


def problems(text, icon_names):
    """Что в руководстве не так: иконка, которой нет в ui/icons, ссылка #N на раздел, которого нет,
    плашка незнакомого вида. Пустой список — всё в порядке."""
    found = []
    guide = parse(text)
    for section in guide.all_sections():
        for block in section.blocks:
            if isinstance(block, BulletList):
                found += [f"нет иконки :{item.icon}:" for item in block.items if item.icon and item.icon not in icon_names]
    for span in iter_spans(guide):
        if span.style == "link" and span.target.startswith("#"):
            number = span.target[1:]
            if not number.isdigit() or int(number) > len(guide.sections):
                found.append(f"ссылка на раздел, которого нет: {span.target}")
    for line in text.splitlines():
        m = _CALLOUT.match(_quote_body(line.strip())) if line.strip().startswith(">") else None
        if m and m.group(1).lower() not in CALLOUTS:
            found.append(f"плашка незнакомого вида: [!{m.group(1)}]")
    return found
