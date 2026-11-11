"""Перевод руководства guide/ru.md на другие языки окна программы через Gemini (задача 15, шаг 10.16).

Основа — скрипт пользователя для заметок Obsidian (translator.py, на ПК пользователя). Что добавлено:
- переводит руководство **по разделам** (вступление и каждый «##» — отдельный запрос): длинный файл целиком модель
  переводит хуже и обрывает;
- **названия кнопок и окон** берёт из i18n.py и telegram_i18n.py: в запросе — словарь «как это называется в окне на этом
  языке» (только то, что есть в этом разделе), имена титанов — тоже;
- **проверяет каждый перевод** строка в строку (check): те же строки разметки (##, «- :иконка:», «1. **…**», «> [!tip]»,
  картинки, «---»), `код` и адреса ссылок без изменений, перевод не по-русски, программа нарисует ту же раскладку
  (ui/guide_renderer.parse). Ошибка — перевод заново, с перечнем ошибок (ATTEMPTS попыток). Не вышло — в файле остаётся
  прежний перевод раздела, английский или русский текст, а в итоге — какой раздел и почему;
- **помнит, что уже переведено** (guide/translate_state.json): поменял один раздел в ru.md — переводится только он.
  Правки, которые ты сделал в переводе руками, сохраняются, пока русский раздел не поменялся;
- после каждого раздела сохраняет файл: оборвалось (лимит запросов, Ctrl+C) — следующий запуск продолжит с того же места.

Картинки переводить не нужно: путь в тексте общий (images/имя.png), окно берёт скриншот из папки своего языка
(guide/images/ru/, guide/images/en/ — ui/guide_renderer.find_image).

Как запустить на ПК (cmd в папке бота) — проще всего двойной щелчок по translate_guide.bat. Вручную:
    venv\\Scripts\\activate
    pip install google-genai==2.33.0            (один раз)
    set GEMINI_API_KEY=ключ                     (ключ: https://aistudio.google.com/apikey; навсегда: setx GEMINI_API_KEY "ключ")
    python translate_guide.py                   все языки (сначала английский)
    python translate_guide.py EN DE             только эти языки
    python translate_guide.py --check           ничего не переводить, только проверить готовые guide/<язык>.md
    python translate_guide.py DE --section 7    перевести заново раздел 7 (0 — вступление)
    python translate_guide.py DE --force        перевести заново все разделы
Ключ берётся только из переменной окружения (GEMINI_API_KEY или GOOGLE_API_KEY) — в файлы он не пишется.
"""
import argparse
import hashlib
import json
import logging
import os
import re
import sys
import threading
import time
from collections import Counter

import i18n
import telegram_i18n
from ui import guide_renderer as gr
from ui.theme import plain_text

GUIDE_DIR = gr.GUIDE_DIR
SOURCE_LANG = "RU"
STATE_FILE = "translate_state.json"            # в папке guide/
ICONS_DIR = os.path.join("ui", "icons")
MODEL = "gemini-3.6-flash"                       # gemini-3.5-flash
PAUSE_S = 10                                   # между запросами (бесплатный ключ: ~10 запросов в минуту)
ATTEMPTS = 3                                   # попыток перевести раздел без ошибок разметки
# Несколько разделов в одном запросе, пока русский текст не длиннее этого (знаков). У бесплатного ключа бывает всего
# 20 запросов в день на модель (ответ Gemini пользователю 26.10.2026: «limit: 20 requests per day on Free Tier»),
# а по одному разделу руководство — 16 запросов на язык. Так — около 5. Не прошедший проверку раздел переводится
# потом отдельно. 0 — каждый раздел своим запросом (--batch 0).
MAX_BATCH_CHARS = 30000
# Откуда брать ключ — по порядку. google-genai сама берёт GOOGLE_API_KEY раньше GEMINI_API_KEY и об этом не пишет:
# поменял GEMINI_API_KEY на ключ второго аккаунта — а запросы шли с первого (26.10.2026). Поэтому ключ выбираем сами.
KEY_VARS = ("GEMINI_API_KEY", "GOOGLE_API_KEY")
# Ключи можно хранить в файле в папке бота (по одному в строке, в .gitignore): `setx GEMINI_API_KEY` у пользователя ключ
# не менял (27.10.2026 — уже открытые окна держат старое значение), а файл читается заново при каждом запуске.
# При запуске из translate_guide.bat скрипт спрашивает, какой ключ взять (choose_key), и сам дописывает новый ключ сюда.
KEYS_FILE = "gemini_keys.txt"
RATE_WAITS_S = (30, 60, 120, 240)              # «слишком много запросов» (429) — подождать и снова
RETRY_WAITS_S = (30, 60, 120)                  # сервер не ответил, обрыв связи
# Сколько ждать ответа на один запрос — по часам, своим «будильником» (Asker.ask_in_time), что бы ни делала библиотека.
# У пользователя перевод раздела 9 висел часами (26.10.2026): кончился лимит ключа, Gemini ответил «повтори через N»,
# а google-genai сама молча спала это время, и не раз (свои повторы на 429 по заголовку Retry-After, без предела).
# Обычно раздел переводится за 1–3 мин; не ответил за 5 — запрос повторяется (RETRY_WAITS_S).
REQUEST_TIMEOUT_S = 600                        # 10 мин: в одном запросе бывает несколько разделов (MAX_BATCH_CHARS)
HEARTBEAT_S = 60                               # пока ждём ответа — раз в минуту строка «жду ответа Gemini: N мин»
MAX_RATE_WAIT_S = 300                          # Gemini просит подождать дольше — лимит ключа исчерпан: остановка
LIMITS_URL = "https://ai.dev/rate-limit"       # лимиты ключа (ссылка из ответа самого Gemini)
LANG_NAMES = {
    "EN": "английский", "UK": "украинский", "KK": "казахский", "DE": "немецкий", "ES": "испанский",
    "FR": "французский", "PL": "польский", "PT": "португальский (бразильский)", "TR": "турецкий",
    "ZH": "китайский (упрощённые иероглифы)", "KO": "корейский", "JA": "японский",
}
# Буквы, без которых текст на этом языке не обходится (украинский и казахский — тоже кириллица, их по доле кириллицы
# не отличить от русского)
OWN_LETTERS = {"UK": "іїєґІЇЄҐ", "KK": "әғқңөұүһіӘҒҚҢӨҰҮҺІ"}
CYRILLIC_LANGS = {"RU", "UK", "KK"}
TEXT_START = "=== ТЕКСТ ДЛЯ ПЕРЕВОДА ==="
TEXT_END = "=== КОНЕЦ ТЕКСТА ==="

RULES = f"""Ты — профессиональный переводчик руководств к программам и играм. Ты переводишь руководство пользователя
к программе-боту «Hero Wars: Knowledge Engine Bot»: бот сам проходит Подземелье титанов в игре Hero Wars на Android-телефоне,
подключённом к компьютеру с Windows. Читатели — обычные игроки, не программисты (и школьники, и пожилые люди).

Текст написан в Markdown с особой разметкой: программа рисует из неё карточки, плашки и оглавление. Сломанная разметка
ломает страницу, поэтому соблюдай правила строго.

ПРАВИЛА:
1. Переведи текст между строками «{TEXT_START}» и «{TEXT_END}» с русского на {{language}}.
   Верни ТОЛЬКО перевод — без пояснений, без ``` и без этих двух строк.
2. Строка в строку: сколько строк в оригинале, столько и в переводе, пустые строки — на тех же местах.
   Не склеивай и не разбивай строки, даже очень длинные.
3. Разметку оставь как есть, переводи только текст:
   - начало строки — «#», «##», «###», «- », «1. », «> », «---» и пробелы перед ними — без изменений;
   - плашки «> [!tip]», «> [!note]», «> [!warning]», «> [!done]» — слово в квадратных скобках не переводи;
   - иконки вида «:eye:», «:door-open:» в начале пункта списка — не переводи и не убирай;
   - **жирный** текст оставь жирным (тот же кусок, переведённый); в шаге «1. **Заголовок** — текст» жирный заголовок
     и тире после него обязательны;
   - `текст в обратных кавычках` не переводи и не меняй совсем (команды, имена файлов, строки журнала бота);
   - ссылки [текст](#5) и [текст](https://…): переводи только текст в квадратных скобках, адрес в круглых не меняй;
   - картинки ![подпись](images/имя.png): переводи подпись, путь не меняй.
4. Названия кнопок, вкладок, окон и надписей программы бери из словаря — слово в слово, как в окне программы на этом
   языке, в кавычках «…». Русские падежи значения не имеют: «Мастера правил», «в Мастере правил» — это «Мастер правил».
   Названия, которых нет в словаре (кнопки самой игры Hero Wars, настройки Android и Windows), пиши так, как они
   называются на этом языке в самой игре или системе, если знаешь, и тоже в «…».
5. Строки журнала бота (с меткой в квадратных скобках, например «[НАВИГАЦИЯ] …», «[ТАКТИКА] …», «[ОШИБКА]») бот пишет
   по-русски на любом языке — оставь их по-русски слово в слово; перевод можно дать рядом в скобках.
6. Имена титанов — как в словаре. Числа, проценты, время и клавиши (F9, F10, Ctrl+Q) не меняй. Названия программ
   и сайтов (Hero Wars, scrcpy, adb, Telegram, Windows, Android, GitHub, @BotFather) не переводи.
7. Игровые слова Hero Wars (Подземелье, титаны, титанит, стихии, точка сохранения, зелья) переводи так, как они
   называются в игре на этом языке. Если не знаешь — простым понятным словом, одинаково по всему тексту.
8. Тон — как в оригинале: дружелюбно, просто, короткими фразами. К читателю — на «ты», если в этом языке так пишут
   для игроков (du, tu, tú, ти…); иначе — как принято в руководствах к играм.
"""


class Stop(Exception):
    """Дальше переводить нельзя: кончился дневной лимит, неверный ключ, нет такой модели."""


# ── Куски руководства ────────────────────────────────────────────────────────
def is_section_heading(line):
    m = gr._HEADING.match(line.strip()) if gr._indent(line) < 4 else None
    return bool(m) and len(m.group(1)) == 2


def split_pieces(text):
    """Текст → куски: [0] — вступление (всё до первого «##», может быть пустым), дальше разделы со своей строкой «##».
    "".join(split_pieces(text)) == text."""
    pieces, current = [], []
    for line in text.splitlines(keepends=True):
        if is_section_heading(line):
            pieces.append("".join(current))
            current = []
        current.append(line)
    pieces.append("".join(current))
    return pieces


def frame(piece):
    """Кусок → (пустые строки в начале, текст, пустые строки и пробелы в конце)."""
    m = re.match(r"^(\s*)(.*?)(\s*)$", piece, re.S)
    return m.group(1), m.group(2), m.group(3)


def piece_title(piece):
    """Заголовок раздела без разметки ("" у вступления) — по нему узнаём раздел, если в ru.md их переставили."""
    for line in piece.splitlines():
        if is_section_heading(line):
            return gr.plain(gr._HEADING.match(line.strip()).group(2))
    return ""


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            return f.read().replace("\r\n", "\n")
    except FileNotFoundError:
        return ""


def write_text(path, text):
    """Запись через временный файл: оборвалось посередине — старый файл цел."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def icon_names():
    return {name[:-4] for name in os.listdir(ICONS_DIR) if name.endswith(".png")}


# ── Словарь: как называется в окне на этом языке ────────────────────────────
def _norm(text):
    return re.sub(r"\s+", " ", text).strip().rstrip("….:").strip()


def _tables():
    return (i18n.TRANSLATIONS, telegram_i18n.TG_TEXTS)


def window_terms(lang):
    """Надписи окна и сообщений Telegram: русский текст → варианты на языке lang (у одного русского бывает несколько).
    Шаблоны с подстановками ({n}) — отдельно: [(regex по русскому, русский шаблон, шаблон на языке lang)]."""
    terms, templates = {}, []
    for table in _tables():
        ru, other = table[SOURCE_LANG], table.get(lang, {})
        for key, value in ru.items():
            if not isinstance(value, str) or not isinstance(other.get(key), str) or key.startswith("titan_"):
                continue
            source, target = _norm(plain_text(value)), _norm(plain_text(other[key]))
            if not source or not target:
                continue
            if "{" in source:
                literal = re.sub(r"\{[^}]*\}", "", source)
                if sum(ch.isalpha() for ch in literal) >= 5:     # «{a} из {b}» подходит к чему угодно — не берём
                    regex = re.compile(re.sub(r"\\\{[^}]*\\\}", "(.+?)", re.escape(source)))
                    templates.append((regex, source, target))
                continue
            variants = terms.setdefault(source, [])
            if target not in variants:
                variants.append(target)
    return terms, templates


def titan_names(lang):
    ru, other = i18n.TRANSLATIONS[SOURCE_LANG], i18n.TRANSLATIONS.get(lang, {})
    return [(ru[key], other.get(key, ru[key])) for key in sorted(ru) if key.startswith("titan_")]


def _mentions(text, name):
    """Имя титана есть в тексте, в том числе в другом падеже: «Ригеля», «Сигурдом»."""
    return name in text or (len(name) >= 5 and name[:-1] in text)


class Glossary:
    """Что из словаря нужно этому куску: entries — [(русский, [варианты]), ...] для запроса,
    names — названия окна в «…», которые перевод обязан содержать, keep — строки журнала, которые остаются по-русски."""

    def __init__(self, piece, lang, terms, templates, titans):
        self.entries, self.names, self.keep = [], [], []
        seen = set()
        for quoted in re.findall(r"«([^«»\n]+)»", piece):
            source = _norm(quoted)
            if not source or source in seen:
                continue
            seen.add(source)
            if source.startswith("["):
                self.keep.append(quoted.strip())
            elif source in terms:
                self.entries.append((source, terms[source]))
                self.names.append((source, terms[source]))
            else:
                for regex, ru_template, target in templates:
                    if regex.fullmatch(source):
                        if ru_template not in seen:
                            seen.add(ru_template)
                            self.entries.append((ru_template, [target]))
                        break
        for ru_name, target in titans:
            if _mentions(piece, ru_name) and ru_name not in seen:
                seen.add(ru_name)
                self.entries.append((ru_name, [target]))

    @classmethod
    def merged(cls, glossaries):
        """Один словарь на несколько разделов (общий запрос): без повторов."""
        merged = cls.__new__(cls)
        merged.entries, merged.names, merged.keep = [], [], []
        for glossary in glossaries:
            for field in ("entries", "names", "keep"):
                target = getattr(merged, field)
                target.extend(item for item in getattr(glossary, field) if item not in target)
        return merged

    def lines(self):
        return [f"«{source}» → " + " или ".join(f"«{t}»" for t in targets) for source, targets in self.entries]

    def signature(self):
        return "\n".join(self.lines())


# ── Запрос ───────────────────────────────────────────────────────────────────
def build_prompt(body, lang, number, total, glossary, feedback=None):
    language = f"{LANG_NAMES.get(lang, lang)} язык ({i18n.LANGUAGES.get(lang, lang)}, код {lang})"
    numbers = number if isinstance(number, (list, tuple)) else [number]
    if len(numbers) > 1:
        names = ", ".join("вступление" if n == 0 else str(n) for n in numbers)
        part = (f"несколько частей руководства подряд ({names}; всего разделов {total - 1}). Каждый раздел начинается "
                "со строки «## …», вступление — со строки «# …». Переведи все части целиком, по порядку, ничего не пропуская, "
                "не объединяя и не добавляя")
    else:
        part = "вступление (до первого раздела)" if numbers[0] == 0 else f"раздел {numbers[0]} из {total - 1}"
    lines = [RULES.format(language=language), f"Язык перевода: {language}.", f"Что переводим: {part}."]
    if glossary.entries:
        lines += ["", "СЛОВАРЬ (русский → как в окне программы на этом языке):"] + glossary.lines()
    if feedback:
        lines += ["", "ПРОШЛЫЙ ПЕРЕВОД НЕ ПРОШЁЛ ПРОВЕРКУ. Переведи заново и исправь:"] + [f"- {p}" for p in feedback]
    lines += ["", TEXT_START, body, TEXT_END]
    return "\n".join(lines)


def clean_output(text):
    """Ответ модели → текст перевода: без ```markdown, без строк-границ, без пустых строк по краям."""
    text = (text or "").replace("\r\n", "\n").strip()
    text = re.sub(r"^```[a-zA-Z]*[ \t]*\n", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    lines = text.split("\n")
    lines = [line for line in lines if line.strip() not in (TEXT_START, TEXT_END)]
    return "\n".join(lines).strip("\n")


# ── Проверка перевода ────────────────────────────────────────────────────────
_CODE = re.compile(r"`([^`\n]+)`")
_TARGET = re.compile(r"\]\(([^)\s]+)\)")


def skeleton(line):
    """Что программа видит в начале строки (в том же порядке, что ui/guide_renderer.parse)."""
    indent = len(line) - len(line.lstrip(" \t"))
    s = line.strip()
    if not s:
        return ("blank",)
    heading = gr._HEADING.match(s) if indent < 4 else None
    if heading:
        return ("heading", indent, len(heading.group(1)))
    if gr._RULE.match(s):
        return ("rule", indent)
    image = gr._IMAGE.match(s)
    if image:
        return ("image", indent, image.group("path"))
    if s.startswith(">"):
        callout = gr._CALLOUT.match(gr._quote_body(s).strip())
        return ("callout", indent, callout.group(1).lower()) if callout else ("quote", indent)
    step = gr._STEP.match(s)
    if step:
        return ("step", indent, bool(gr._STEP_TITLE.match(step.group(2).strip())))
    bullet = gr._BULLET.match(s)
    if bullet:
        icon = gr._ICON.match(bullet.group(1))
        return ("bullet", indent, icon.group(1) if icon else "")
    return ("text", indent)


def describe(kind):
    name = kind[0]
    where = f" с отступом {kind[1]}" if len(kind) > 1 and kind[1] else ""
    if name == "blank":
        return "пустая строка"
    if name == "heading":
        return f"заголовок {'#' * kind[2]}{where}"
    if name == "rule":
        return f"линия ---{where}"
    if name == "image":
        return f"картинка с путём ({kind[2]}){where}"
    if name == "callout":
        return f"плашка > [!{kind[2]}]{where}"
    if name == "quote":
        return f"строка цитаты >{where}"
    if name == "step":
        return f"шаг «1.»{' с жирным заголовком **…**' if kind[2] else ''}{where}"
    if name == "bullet":
        return f"пункт списка{f' с иконкой :{kind[2]}:' if kind[2] else ''}{where}"
    return f"обычный текст{where}"


def layout(text):
    """Раскладка, которую нарисует программа: виды блоков, число пунктов и шагов, иконки, плашки, картинки."""
    guide = gr.parse(text)
    shape = [len(guide.sections), bool(guide.title)]
    for section in guide.all_sections():
        for block in section.blocks:
            if isinstance(block, gr.BulletList):
                shape.append(("list", tuple(item.icon for item in block.items)))
            elif isinstance(block, gr.Steps):
                shape.append(("steps", tuple((bool(item.title), len(item.tips)) for item in block.items)))
            elif isinstance(block, gr.Callout):
                shape.append(("callout", block.kind, len(block.paragraphs)))
            elif isinstance(block, gr.Image):
                shape.append(("image", block.path))
            else:
                shape.append(type(block).__name__)
    return shape


def numbers(line):
    """Числа строки без `кода`: «50 000», «50,000» и «50000» — одно число (разделитель тысяч в языках разный)."""
    text = re.sub(r"(?<=\d)[ \u00a0\u202f,.'’](?=\d{3}(?!\d))", "", _CODE.sub("", line))
    return Counter(re.findall(r"\d+", text))


def _letters(text):
    text = _CODE.sub(" ", text)
    text = re.sub(r"«\[[^«»\n]*»", " ", text)             # строки журнала остаются по-русски
    text = _TARGET.sub("]", text)
    return [ch for ch in text if ch.isalpha()]


def _is_cyrillic(ch):
    return "Ѐ" <= ch <= "ӿ"


def check(source, translated, lang, glossary):
    """(ошибки, замечания) перевода куска. Ошибки — разметка сломана или текст не переведён: такой перевод не берём.
    Замечания — нет названия из окна, строки журнала или числа: перевод можно взять, но лучше попробовать ещё раз."""
    errors, warnings = [], []
    if not translated.strip():
        return ["ответ пустой"], []
    src_lines, tr_lines = source.split("\n"), translated.split("\n")
    if len(src_lines) != len(tr_lines):
        errors.append(f"в оригинале {len(src_lines)} строк, в переводе {len(tr_lines)}: строки нельзя склеивать и разбивать, "
                      "пустые строки должны остаться на своих местах")
    for n, (src, tr) in enumerate(zip(src_lines, tr_lines), start=1):
        a, b = skeleton(src), skeleton(tr)
        if a != b:
            errors.append(f"строка {n}: в оригинале — {describe(a)}, в переводе — {describe(b)}")
            if len(src_lines) != len(tr_lines):
                break                                     # дальше строки съехали — хватит первой
            continue
        if a[0] == "blank":
            continue
        codes = Counter(_CODE.findall(src))
        if Counter(_CODE.findall(tr)) != codes:
            if codes:
                kept = ", ".join(f"`{c}`" for c in sorted(codes))
                errors.append(f"строка {n}: текст в обратных кавычках не переводится и не меняется, оставь ровно: {kept}")
            else:
                errors.append(f"строка {n}: в оригинале в этой строке нет обратных кавычек ` — не добавляй их")
        if Counter(_TARGET.findall(src)) != Counter(_TARGET.findall(tr)):
            errors.append(f"строка {n}: адреса в круглых скобках ссылок и картинок должны остаться как в оригинале: "
                          + ", ".join(_TARGET.findall(src)))
        if tr.count("**") % 2:
            errors.append(f"строка {n}: непарные ** (жирный текст не закрыт)")
        if _CODE.sub("", tr).count("`") % 2:
            errors.append(f"строка {n}: непарная обратная кавычка `")
        if src.count("**") != tr.count("**") and not tr.count("**") % 2:
            warnings.append(f"строка {n}: жирных кусков было {src.count('**') // 2}, стало {tr.count('**') // 2}")
        digits = numbers(src)
        if numbers(tr) != digits:
            warnings.append(f"строка {n}: числа должны остаться те же ({', '.join(sorted(digits)) or 'чисел нет'})")
    if not errors and layout(source) != layout(translated):
        errors.append("программа нарисует перевод иначе, чем оригинал (другие плашки, списки или шаги)")

    letters = _letters(translated)
    if translated.strip() == source.strip() and _letters(source):
        errors.append("текст не переведён")
    elif len(letters) >= 80 and lang not in CYRILLIC_LANGS:
        share = sum(map(_is_cyrillic, letters)) / len(letters)
        if share > 0.25:
            errors.append(f"перевод почти весь по-русски ({share:.0%} русских букв)")
    elif len(letters) >= 150 and lang in OWN_LETTERS and not any(ch in OWN_LETTERS[lang] for ch in letters):
        errors.append(f"это не {LANG_NAMES[lang]} язык: нет ни одной из букв {OWN_LETTERS[lang]}")

    source_title = next((l.strip() for l in src_lines if skeleton(l)[:1] == ("heading",) and skeleton(l)[2] == 1), None)
    if source_title and source_title not in (l.strip() for l in tr_lines):
        errors.append(f"заголовок «{source_title}» — название программы, его не переводят")

    lowered = translated.lower()
    missing = [source for source, targets in glossary.names
               if not any(_norm(t).lower() in lowered for t in targets)]
    if missing:
        warnings.append("нет названий из окна программы (возьми их из словаря слово в слово): "
                        + ", ".join(f"«{m}»" for m in missing))
    lost = [line for line in glossary.keep if line not in translated]
    if lost:
        warnings.append("строки журнала бота должны остаться по-русски слово в слово: " + ", ".join(f"«{l}»" for l in lost))
    return errors, warnings


# ── Запросы к Gemini ─────────────────────────────────────────────────────────
def timed_out(exc):
    """Запрос оборвался по пределу ожидания (httpx.ReadTimeout и подобные)."""
    return isinstance(exc, TimeoutError) or "timeout" in type(exc).__name__.lower() or "timed out" in str(exc).lower()


def error_kind(exc):
    """Что делать с ошибкой запроса: "rate" — подождать, "day" — дневной лимит, "fatal" — дальше нельзя, "retry" — ещё раз."""
    code = getattr(exc, "status_code", None) or getattr(exc, "code", None)
    text = str(exc)
    if code == 429 or "429" in text or "RESOURCE_EXHAUSTED" in text or "too_many_requests" in text.lower():
        return "day" if "PerDay" in text or "per day" in text.lower() else "rate"
    if code in (400, 401, 403, 404) or any(word in text for word in (
            "API key not valid", "API_KEY_INVALID", "PERMISSION_DENIED", "NOT_FOUND", "INVALID_ARGUMENT")):
        return "fatal"
    return "retry"


class Gemini:
    """Запрос к Gemini — так же, как в скрипте пользователя (client.interactions.create)."""

    def __init__(self, model=MODEL, key=None, source=None):
        if key:
            self.key_var, self.key_note = source or "", ""
        else:
            key, self.key_var, self.key_note = api_key()
            self.key_var = f"переменная {self.key_var}" if key else ""
        if not key:
            raise Stop("нет ключа Gemini API. Получи его на https://aistudio.google.com/apikey, запусти translate_guide.bat "
                       f"и вставь ключ, когда он спросит (сохранится в {KEYS_FILE}).")
        try:
            from google import genai
        except ImportError:
            raise Stop("нет библиотеки google-genai. В cmd в папке бота: venv\\Scripts\\activate, "
                       "потом pip install google-genai==2.33.0") from None
        # библиотека пишет «Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.», хотя берёт наш ключ
        # (api_key=...): строка сбивала с толку, какой ключ на самом деле — его пишем сами (main)
        logging.getLogger("google_genai._api_client").setLevel(logging.ERROR)
        self.client = self._client(genai, key)
        self.model = model
        self.timeout = REQUEST_TIMEOUT_S
        self.version = getattr(genai, "__version__", "?")
        self.key_hint = masked(key)

    @staticmethod
    def _client(genai, key):
        """Клиент с пределом ожидания (в миллисекундах) и без своих повторов библиотеки: на «слишком много запросов»
        она молча спала столько, сколько скажет сервер (часами). Повторяет наш Asker — с паузами и строками в окне.
        Повторы выключены так: повторять только ответ 599, которого не бывает (attempts=0 библиотека не принимает)."""
        types = getattr(genai, "types", None)
        variants = []
        try:
            retry = types.HttpRetryOptions(attempts=1, http_status_codes=[599])
            variants.append(dict(timeout=REQUEST_TIMEOUT_S * 1000, retry_options=retry))
        except (AttributeError, TypeError, ValueError):
            pass
        variants.append(dict(timeout=REQUEST_TIMEOUT_S * 1000))
        for options in variants:
            try:
                return genai.Client(api_key=key, http_options=types.HttpOptions(**options))
            except (AttributeError, TypeError, ValueError):
                continue
        return genai.Client(api_key=key)

    def __call__(self, prompt):
        if self.timeout:
            try:
                interaction = self.client.interactions.create(model=self.model, input=prompt, timeout=self.timeout)
                return interaction.output_text or ""
            except TypeError as exc:                    # старая google-genai не знает timeout у запроса
                if "timeout" not in str(exc):
                    raise
                self.timeout = None
        interaction = self.client.interactions.create(model=self.model, input=prompt)
        return interaction.output_text or ""


class RequestTimeout(TimeoutError):
    """Ответа нет дольше REQUEST_TIMEOUT_S — запрос брошен (его поток доживёт сам, ответ не нужен)."""


def retry_delay(exc):
    """Сколько секунд Gemini просит подождать после «слишком много запросов»: заголовок Retry-After (retry-after-ms)
    или retryDelay / «retry in N s» в тексте ошибки. Не сказал — None."""
    headers = getattr(getattr(exc, "response", None), "headers", None) or {}
    for name, scale in (("retry-after-ms", 0.001), ("retry-after", 1)):
        try:
            value = headers.get(name)
            if value:
                return float(value) * scale
        except (AttributeError, TypeError, ValueError):
            pass
    text = str(exc)
    m = (re.search(r"retryDelay['\"]?\s*:\s*['\"]?(\d+(?:\.\d+)?)s", text)
         or re.search(r"retry in (\d+(?:\.\d+)?)\s*s", text, re.I))
    return float(m.group(1)) if m else None


def say_time(seconds):
    """125 → «2 мин», 5400 → «1 ч 30 мин», 40 → «40 с»."""
    seconds = int(round(seconds))
    if seconds < 60:
        return f"{seconds} с"
    hours, minutes = divmod(round(seconds / 60), 60)
    return f"{hours} ч {minutes} мин" if hours and minutes else f"{hours} ч" if hours else f"{minutes} мин"


def api_key():
    """(ключ, имя переменной, предупреждение): первая непустая из KEY_VARS. Вторая с другим ключом — предупреждение."""
    found = [(name, os.environ.get(name, "").strip()) for name in KEY_VARS]
    found = [(name, value) for name, value in found if value]
    if not found:
        return None, None, ""
    name, key = found[0]
    others = [f"{other} (ключ {masked(value)})" for other, value in found[1:] if value != key]
    note = f"задана и {', '.join(others)} — её не беру" if others else ""
    return key, name, note


def read_keys(path=KEYS_FILE):
    """Ключи из файла: по одному в строке, пустые строки и строки с # пропускаются, без повторов."""
    keys = []
    for line in read_text(path).splitlines():
        line = line.strip()
        if line and not line.startswith("#") and line not in keys:
            keys.append(line)
    return keys


def save_keys(keys, path=KEYS_FILE):
    write_text(path, "# Ключи Gemini API для translate_guide.py — по одному в строке, сверху тот, что берётся по Enter.\n"
                     "# Файла нет в git (.gitignore). Никому его не присылай.\n" + "\n".join(keys) + "\n")


def key_choices(path=KEYS_FILE):
    """[(ключ, откуда)] — сначала из файла, потом из переменных окружения, без повторов."""
    found = [(key, f"файл {path}") for key in read_keys(path)]
    for name in KEY_VARS:
        value = os.environ.get(name, "").strip()
        if value and value not in [key for key, _ in found]:
            found.append((value, f"переменная {name}"))
    return found


def looks_like_key(text):
    return len(text) >= 20 and not re.search(r"\s", text)


def choose_key(ask=input, interactive=None, log=print, path=KEYS_FILE):
    """(ключ, откуда) для запроса. Из окна (translate_guide.bat) — список ключей и вопрос: номер, Enter — первый,
    или вставить новый ключ (он сохранится первым в файле). Без окна — первый ключ без вопросов. Нет ключа — (None, None)."""
    choices = key_choices(path)
    if interactive is None:
        interactive = bool(getattr(sys.stdin, "isatty", lambda: False)())
    if not interactive:
        return choices[0] if choices else (None, None)
    if choices:
        log("[ПЕРЕВОД] Ключи Gemini:")
        for n, (key, where) in enumerate(choices, start=1):
            log(f"    {n} — {masked(key)} ({where})")
        question = "Какой ключ взять? Номер (Enter — 1) или вставь новый ключ: "
    else:
        log("[ПЕРЕВОД] Ключа Gemini ещё нет. Его дают на https://aistudio.google.com/apikey (кнопка «Create API key»).")
        question = "Вставь ключ и нажми Enter: "
    try:
        answer = ask(question).strip()
    except EOFError:
        answer = ""
    if not answer:
        return choices[0] if choices else (None, None)
    if answer.isdigit() and 1 <= int(answer) <= len(choices):
        return choices[int(answer) - 1]
    if looks_like_key(answer):
        save_keys([answer] + [key for key in read_keys(path) if key != answer], path)
        log(f"[ПЕРЕВОД] Новый ключ {masked(answer)} сохранён в {path} — в следующий раз он будет первым.")
        return answer, f"файл {path}"
    log(f"[ПЕРЕВОД] Не понял ответ «{answer[:20]}» — беру первый ключ.")
    return choices[0] if choices else (None, None)


def masked(key):
    """Ключ для строки в окне: только последние 4 знака."""
    return "…" + key[-4:] if key else "—"


class Asker:
    """Запрос с паузой между запросами и повторами при «слишком много запросов» и обрыве связи. Ответа ждём не дольше
    limit секунд по часам (ask_in_time): что бы ни случилось внутри библиотеки, скрипт не висит."""

    def __init__(self, ask, log, sleep=time.sleep, pause=PAUSE_S, clock=time.monotonic,
                 limit=REQUEST_TIMEOUT_S, heartbeat=HEARTBEAT_S):
        self.ask, self.log, self.sleep, self.pause, self.clock = ask, log, sleep, pause, clock
        self.limit, self.heartbeat = limit, heartbeat
        self.last = None
        self.requests = 0
        self.seconds = 0.0                              # сколько шёл последний удачный запрос

    def ask_in_time(self, prompt):
        """Запрос в отдельном потоке: ждём ответа не дольше limit с, раз в heartbeat с пишем, что ждём.
        Так и Ctrl+C работает сразу (главный поток не сидит внутри сетевого вызова)."""
        box = {}

        def work():
            try:
                box["answer"] = self.ask(prompt)
            except BaseException as exc:                # noqa: BLE001 — любую ошибку отдаём главному потоку
                box["error"] = exc

        worker = threading.Thread(target=work, name="gemini-request", daemon=True)
        started = time.monotonic()
        worker.start()
        next_note = self.heartbeat
        while True:
            worker.join(min(1.0, self.limit, self.heartbeat))
            if not worker.is_alive():
                break
            waited = time.monotonic() - started
            if waited >= self.limit:
                raise RequestTimeout(f"Gemini не ответил за {say_time(self.limit)}")
            if waited >= next_note:
                next_note += self.heartbeat
                self.log(f"[ПЕРЕВОД]    жду ответа Gemini: {say_time(waited)} (предел {say_time(self.limit)})")
        if "error" in box:
            raise box["error"]
        return box["answer"]

    def __call__(self, prompt):
        rate = retry = 0
        while True:
            if self.last is not None:
                wait = self.pause - (self.clock() - self.last)
                if wait > 0:
                    self.sleep(wait)
            self.last = self.clock()
            self.requests += 1
            try:
                answer = self.ask_in_time(prompt)
                self.seconds = self.clock() - self.last
                return answer
            except KeyboardInterrupt:
                raise
            except Exception as exc:                      # noqa: BLE001 — у google-genai и httpx свои классы ошибок
                kind = error_kind(exc)
                message = str(exc).splitlines()[0][:300] if str(exc) else type(exc).__name__
                if kind == "day":
                    raise Stop(f"дневной лимит запросов Gemini закончился ({message}). Запусти скрипт завтра — "
                               f"он продолжит с того же места. Лимиты ключа и моделей: {LIMITS_URL} (у другой модели "
                               "свой лимит: при вопросе о языке можно написать, например, «EN --model имя-модели»)") from exc
                if kind == "fatal":
                    raise Stop(f"Gemini не принимает запрос: {message}. Проверь ключ (GEMINI_API_KEY) "
                               "и название модели (--model).") from exc
                asked = retry_delay(exc) if kind == "rate" else None
                if asked is not None and asked > MAX_RATE_WAIT_S:
                    raise Stop(f"кончился лимит запросов ключа Gemini: он просит подождать {say_time(asked)} ({message}). "
                               f"Запусти скрипт после этого — он продолжит с того же места. Лимиты ключа: {LIMITS_URL}") \
                        from exc
                waits = RATE_WAITS_S if kind == "rate" else RETRY_WAITS_S
                tried = rate if kind == "rate" else retry
                if tried >= len(waits):
                    if kind == "rate":
                        raise Stop(f"Gemini всё ещё отвечает «слишком много запросов» ({message}): похоже, кончился "
                                   f"лимит ключа. Запусти скрипт позже — он продолжит с того же места. Лимиты: {LIMITS_URL}") \
                            from exc
                    raise Stop(f"Gemini не отвечает: {message}. Запусти скрипт позже — он продолжит с того же места.") \
                        from exc
                if kind == "rate":
                    rate += 1
                else:
                    retry += 1
                wait = round(asked) + 1 if asked is not None else waits[tried]     # просит подождать — столько и ждём
                what = ("слишком много запросов" if kind == "rate"
                        else f"Gemini не ответил за {say_time(self.limit)}" if timed_out(exc) else "нет ответа")
                detail = "" if isinstance(exc, RequestTimeout) else f" ({message})"
                self.log(f"[ПЕРЕВОД]    {what}{detail}. Жду {say_time(wait)} и пробую снова.")
                self.sleep(wait)


def translate_piece(asker, piece, lang, number, total, glossary, attempts, log, feedback=None):
    """Перевести кусок. (перевод с теми же пустыми строками по краям или None, ошибки или замечания последней попытки).
    feedback — ошибки прошлого перевода (например, в общем запросе): модель сразу узнает, что исправить."""
    lead, body, tail = frame(piece)
    best, problems = None, []
    for attempt in range(1, attempts + 1):
        answer = clean_output(asker(build_prompt(body, lang, number, total, glossary, feedback)))
        errors, warnings = check(body, answer, lang, glossary)
        if not errors and not warnings:
            return lead + answer + tail, []
        if not errors:
            best = (lead + answer + tail, warnings)
        problems = errors or warnings
        shown = "; ".join(problems[:3]) + (f" и ещё {len(problems) - 3}" if len(problems) > 3 else "")
        log(f"[ПЕРЕВОД]    попытка {attempt}: {'ошибки' if errors else 'замечания'} — {shown}")
        if best and attempt >= 2:
            break                                         # разметка цела, замечания — одна лишняя попытка
        feedback = problems
    return best if best else (None, problems)


def make_batches(todo, pieces, limit):
    """Номера разделов по запросам: по порядку, пока русский текст запроса не длиннее limit знаков (раздел длиннее —
    своим запросом). limit 0 — каждый раздел своим запросом."""
    batches, size = [], 0
    for i in todo:
        length = len(frame(pieces[i])[1])
        if limit > 0 and batches and size + length <= limit:
            batches[-1].append(i)
            size += length
        else:
            batches.append([i])
            size = length
    return batches


def split_batch(answer, batch):
    """Общий ответ → куски по номерам batch (по строкам «##»; вступление — до первой). Не делится как надо — None."""
    chunks = split_pieces(answer)
    if batch[0] != 0:
        if chunks[0].strip():
            return None
        chunks = chunks[1:]
    return chunks if len(chunks) == len(batch) else None


def translate_batch(asker, pieces, batch, lang, total, glossaries):
    """Несколько разделов одним запросом. ({номер: (перевод, замечания)} — прошли проверку,
    {номер: ошибки} — не прошли: их переводим потом по одному, с этими ошибками в запросе)."""
    bodies = [frame(pieces[i])[1] for i in batch]
    glossary = Glossary.merged([glossaries[i] for i in batch])
    answer = clean_output(asker(build_prompt("\n\n".join(bodies), lang, batch, total, glossary)))
    chunks = split_batch(answer, batch)
    if chunks is None:
        problem = "в общем ответе разделы не разделились по строкам «##» (что-то пропущено или склеено)"
        return {}, {i: [problem] for i in batch}
    good, bad = {}, {}
    for i, chunk in zip(batch, chunks):
        lead, body, tail = frame(pieces[i])
        text = frame(chunk)[1]
        errors, warnings = check(body, text, lang, glossaries[i])
        if errors:
            bad[i] = errors
        else:
            good[i] = (lead + text + tail, warnings)
    return good, bad


# ── Язык целиком ─────────────────────────────────────────────────────────────
def load_state(folder):
    try:
        with open(os.path.join(folder, STATE_FILE), "r", encoding="utf-8") as f:
            state = json.load(f)
        return state if isinstance(state, dict) else {}
    except (OSError, ValueError):
        return {}


def save_state(folder, state):
    state["note"] = ("Служебный файл translate_guide.py: из какого русского текста переведён каждый раздел guide/<язык>.md. "
                     "Руками не править.")
    write_text(os.path.join(folder, STATE_FILE), json.dumps(state, ensure_ascii=False, indent=1) + "\n")


def piece_hash(piece, glossary):
    return hashlib.sha256((frame(piece)[1] + "\n\0" + glossary.signature()).encode("utf-8")).hexdigest()[:16]


def _old_translation(folder, lang, state):
    """Прежний перевод: (куски файла, записи состояния) — если файл и состояние совпадают по числу разделов."""
    pieces = split_pieces(read_text(os.path.join(folder, f"{lang.lower()}.md")))
    records = state.get(lang, {}).get("sections", [])
    if len(pieces) == len(records) and any(p.strip() for p in pieces):
        return pieces, records
    return [], []


class Report:
    def __init__(self, lang):
        self.lang = lang
        self.fresh = self.done = 0
        self.failed = []          # (номер куска, заголовок, проблемы)
        self.warned = []
        self.pending = []         # не переведены в этот раз (лимит, --section)
        self.stopped = ""


def translate_language(lang, ru_text, ask, *, folder=GUIDE_DIR, force=False, only=None, attempts=ATTEMPTS,
                       log=print, icons=None, batch=MAX_BATCH_CHARS):
    """Перевести guide/ru.md на язык lang в guide/<lang>.md. ask — Asker (запрос к модели). Возвращает Report."""
    report = Report(lang)
    state = load_state(folder)
    pieces = split_pieces(ru_text)
    total = len(pieces)
    terms, templates = window_terms(lang)
    titans = titan_names(lang)
    glossaries = [Glossary(piece, lang, terms, templates, titans) for piece in pieces]
    hashes = [piece_hash(piece, g) for piece, g in zip(pieces, glossaries)]
    titles = [piece_title(piece) for piece in pieces]

    old_pieces, old_records = _old_translation(folder, lang, state)
    by_hash = {rec.get("hash"): p for p, rec in zip(old_pieces, old_records) if rec.get("hash")}
    # прежний перевод раздела (русский раздел с тех пор поменялся) — лучше, чем ничего; «own» — такой перевод уже ждёт замены
    by_title = {rec.get("ru"): p for p, rec in zip(old_pieces, old_records) if rec.get("hash") or rec.get("own")}
    en_pieces, en_records = _old_translation(folder, "EN", state) if lang != "EN" else ([], [])
    en_by_title = {rec.get("ru"): p for p, rec in zip(en_pieces, en_records) if rec.get("hash")}

    result, records, todo, kept = [], [], [], {}
    for i, piece in enumerate(pieces):
        wanted = only is None or i in only
        reuse = None if force and wanted else by_hash.get(hashes[i])
        if reuse is not None:
            result.append(reuse)
            records.append({"ru": titles[i], "hash": hashes[i]})
            report.fresh += 1
            continue
        own = by_title.get(titles[i])                   # пока нет перевода: прежний свой, английский или русский текст
        english = en_by_title.get(titles[i])
        result.append(own or english or piece)
        kept[i] = "прежний перевод" if own else "английский текст" if english else "русский текст"
        records.append({"ru": titles[i], "hash": None, "own": bool(own)})
        (todo if wanted else report.pending).append(i)

    saved = ["".join(old_pieces), old_records]

    def save():
        """Записать файл и состояние, если что-то поменялось. Файла ещё не было и ничего не переведено — не создавать."""
        text = "".join(result)
        if (not report.done and not old_pieces) or [text, records] == saved:
            return
        state[lang] = {"sections": records}
        write_text(os.path.join(folder, f"{lang.lower()}.md"), text)
        save_state(folder, state)
        saved[:] = [text, [dict(r) for r in records]]

    name = f"{lang} ({LANG_NAMES.get(lang, lang)})"
    if not todo:
        log(f"[ПЕРЕВОД] {name}: всё уже переведено ({report.fresh} из {total}).")
        save()
        return report
    batches = make_batches(todo, pieces, batch)
    log(f"[ПЕРЕВОД] {name}: перевожу {len(todo)} из {total} (уже переведено: {report.fresh}), запросов — "
        f"{len(batches)}. Ответ — обычно 1–5 мин; нет ответа {say_time(REQUEST_TIMEOUT_S)} — спрошу снова.")
    finished = set()

    def what(i):
        return titles[i] or "вступление"

    def answered():
        seconds = getattr(ask, "seconds", 0)
        return f" (ответ за {say_time(seconds)})" if seconds >= 1 else ""

    def accept(i, text, problems):
        result[i] = text
        records[i] = {"ru": titles[i], "hash": hashes[i]}
        report.done += 1
        finished.add(i)
        if problems:
            report.warned.append((i, what(i), problems))

    def single(i, feedback=None):
        text, problems = translate_piece(ask, pieces[i], lang, i, total, glossaries[i], attempts, log, feedback)
        if text is None:
            finished.add(i)
            report.failed.append((i, what(i), problems))
            log(f"[ПЕРЕВОД]    не получилось: в файле пока {kept[i]}.")
            return
        accept(i, text, problems)
        log(f"[ПЕРЕВОД]    готово{answered()}, сохранено.")
        save()

    try:
        for number, group in enumerate(batches, start=1):
            if len(group) == 1:
                log(f"[ПЕРЕВОД]  {number}/{len(batches)}: {group[0]}. {what(group[0])}")
                single(group[0])
                continue
            log(f"[ПЕРЕВОД]  {number}/{len(batches)}: одним запросом — "
                + ", ".join(f"{i}. {what(i)}" for i in group))
            good, bad = translate_batch(ask, pieces, group, lang, total, glossaries)
            for i in group:
                if i in good:
                    accept(i, *good[i])
            if good:
                log(f"[ПЕРЕВОД]    готово {len(good)} из {len(group)}{answered()}, сохранено.")
                save()
            for i in group:
                if i in bad:
                    shown = "; ".join(bad[i][:2]) + (f" и ещё {len(bad[i]) - 2}" if len(bad[i]) > 2 else "")
                    log(f"[ПЕРЕВОД]    {i}. {what(i)}: не прошёл проверку ({shown}) — перевожу его отдельно.")
                    single(i, feedback=bad[i])
    except Stop as exc:
        report.stopped = str(exc)
        report.pending += [i for i in todo if i not in finished]
        save()
        return report
    save()
    full = "".join(result)
    for problem in gr.problems(full, icons if icons is not None else icon_names()):
        log(f"[ПЕРЕВОД] {name}: в файле {problem}")
    return report


# ── Проверка готовых переводов (--check) ────────────────────────────────────
def check_language(lang, ru_text, *, folder=GUIDE_DIR, log=print):
    """Без запросов: какие разделы guide/<lang>.md переведены с нынешнего ru.md и не сломана ли в них разметка.
    True — всё в порядке."""
    state = load_state(folder)
    path = os.path.join(folder, f"{lang.lower()}.md")
    text = read_text(path)
    name = f"{lang} ({LANG_NAMES.get(lang, lang)})"
    if not text.strip():
        log(f"[ПРОВЕРКА] {name}: перевода нет (окно покажет английский или русский текст).")
        return False
    pieces = split_pieces(ru_text)
    terms, templates = window_terms(lang)
    titans = titan_names(lang)
    old_pieces, old_records = _old_translation(folder, lang, state)
    by_hash = {rec.get("hash"): p for p, rec in zip(old_pieces, old_records) if rec.get("hash")}
    fresh, stale, bad = 0, [], []
    for i, piece in enumerate(pieces):
        glossary = Glossary(piece, lang, terms, templates, titans)
        translated = by_hash.get(piece_hash(piece, glossary))
        if translated is None:
            stale.append(i)
            continue
        fresh += 1
        errors, warnings = check(frame(piece)[1], frame(translated)[1], lang, glossary)
        if errors or warnings:
            bad.append((i, piece_title(piece) or "вступление", errors, warnings))
    log(f"[ПРОВЕРКА] {name}: переведено с нынешнего ru.md {fresh} из {len(pieces)}"
        + (f"; надо перевести (новые или изменённые): {', '.join(map(str, stale))}" if stale else ""))
    for i, what, errors, warnings in bad:
        for problem in errors:
            log(f"[ПРОВЕРКА]   {i}. {what}: ошибка — {problem}")
        for problem in warnings:
            log(f"[ПРОВЕРКА]   {i}. {what}: замечание — {problem}")
    problems = gr.problems(text, icon_names())
    for problem in problems:
        log(f"[ПРОВЕРКА]   в файле {problem}")
    return not stale and not problems and not any(errors for _, _, errors, _ in bad)


# ── Запуск ───────────────────────────────────────────────────────────────────
def target_langs(names):
    """Коды из командной строки или из ответа на вопрос translate_guide.bat: «en, de» и «EN DE» — одно и то же."""
    langs = [code for code in i18n.LANGUAGES if code != SOURCE_LANG]
    chosen = [name.upper() for name in re.split(r"[\s,;.]+", " ".join(names or [])) if name]
    if not chosen:
        return langs
    unknown = [code for code in chosen if code not in langs]
    if unknown:
        raise SystemExit(f"[ПЕРЕВОД] Не знаю языков: {', '.join(unknown)}. Можно: {', '.join(langs)}")
    return [code for code in langs if code in chosen]       # английский — первым: он запасной для остальных


def summary(reports, log=print):
    log("")
    log("[ПЕРЕВОД] Итог:")
    for r in reports:
        line = f"  {r.lang}: переведено сейчас {r.done}, уже было {r.fresh}"
        if r.failed:
            line += f", не получилось {len(r.failed)} (разделы {', '.join(str(i) for i, _, _ in r.failed)})"
        if r.pending:
            line += f", ждут следующего запуска {len(r.pending)}"
        log(line)
        for i, what, problems in r.failed:
            log(f"    {i}. {what}: " + "; ".join(problems[:3]))
        for i, what, problems in r.warned:
            log(f"    {i}. {what} (переведено, но проверь): " + "; ".join(problems[:3]))
    stopped = next((r.stopped for r in reports if r.stopped), "")
    if stopped:
        log(f"[ПЕРЕВОД] Остановился: {stopped}")
    elif any(r.failed for r in reports):
        log("[ПЕРЕВОД] Запусти скрипт ещё раз — он попробует перевести только то, что не получилось.")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Перевод guide/ru.md на другие языки окна программы через Gemini.")
    parser.add_argument("langs", nargs="*", help="коды языков (EN DE ...), по умолчанию — все")
    parser.add_argument("--check", action="store_true", help="ничего не переводить, только проверить готовые переводы")
    parser.add_argument("--force", action="store_true", help="перевести заново все разделы")
    parser.add_argument("--section", type=int, action="append", help="перевести заново только этот раздел (0 — вступление)")
    parser.add_argument("--model", default=MODEL, help=f"модель Gemini (по умолчанию {MODEL})")
    parser.add_argument("--pause", type=float, default=PAUSE_S, help=f"секунд между запросами (по умолчанию {PAUSE_S})")
    parser.add_argument("--batch", type=int, default=MAX_BATCH_CHARS,
                        help=f"разделов в одном запросе — пока текст не длиннее N знаков (по умолчанию {MAX_BATCH_CHARS}; "
                             "0 — каждый раздел своим запросом)")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ru_text = read_text(os.path.join(GUIDE_DIR, f"{SOURCE_LANG.lower()}.md"))
    if not ru_text.strip():
        raise SystemExit(f"[ПЕРЕВОД] Нет файла {GUIDE_DIR}/ru.md. Запускай скрипт из папки бота.")
    langs = target_langs(args.langs)
    if args.check:
        ok = [check_language(lang, ru_text) for lang in langs]
        return 0 if all(ok) else 1
    log = lambda text: print(text, flush=True)          # noqa: E731
    try:
        key, source = choose_key(log=log)
        note = api_key()[2] if source and source.startswith("переменная") else ""
        gemini = Gemini(args.model, key, source)
        asker = Asker(gemini, log, pause=args.pause)
    except Stop as exc:
        log(f"[ПЕРЕВОД] Не могу начать: {exc}")
        return 1
    log(f"[ПЕРЕВОД] Ключ {gemini.key_hint} ({gemini.key_var})." + (f" Внимание: {note}." if note else ""))
    log(f"[ПЕРЕВОД] Модель {gemini.model}, библиотека google-genai {gemini.version}; ответа жду не дольше "
        f"{say_time(REQUEST_TIMEOUT_S)}, пауза между запросами {say_time(args.pause)}.")
    reports = []
    try:
        for lang in langs:
            only = set(args.section) if args.section else None
            report = translate_language(lang, ru_text, asker, force=args.force or bool(only), only=only, log=log,
                                        batch=args.batch)
            reports.append(report)
            if report.stopped:
                break
    except KeyboardInterrupt:
        log("\n[ПЕРЕВОД] Остановлено (Ctrl+C). Готовые разделы сохранены — следующий запуск продолжит.")
    summary(reports, log)
    log(f"[ПЕРЕВОД] Запросов к Gemini: {asker.requests}.")
    return 0 if reports and not any(r.failed or r.stopped for r in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
