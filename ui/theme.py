"""Дизайн-токены нового интерфейса (задача 15): цвета, шрифты, размеры, стихии и титаны.

Источник — design/theme.py и макеты в design/mockups. Отличия от design/theme.py:
- титаны записаны внутренними именами (как в assets/ и i18n.py: "angus", "araji"), а не русскими;
- смешанная комната — "mix" (как в bot_data/rules/mix.yml), "mixed" оставлен как второе имя;
- названия стихий берутся из i18n.py (elem_earth, ...), русских строк здесь нет;
- добавлены цвета, которые в design/README.md записаны прямо в тексте (кнопка «Удалить все», поле с ошибкой).

Tkinter не умеет полупрозрачные цвета (rgba), поэтому все «подкрашенные» фоны уже смешаны с фоном.
Новый оттенок — через blend(), а не hex руками в виджете.
Модуль без Tk: его можно импортировать в тестах в облаке.
"""
import base64
import io
import unicodedata
from pathlib import Path

import titans


def blend(fg: str, bg: str, alpha: float) -> str:
    """Смешать цвет fg поверх bg с прозрачностью alpha (0..1). Возвращает #RRGGBB."""
    f = [int(fg[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i:i + 2], 16) for i in (1, 3, 5)]
    mixed = [round(bb + (ff - bb) * alpha) for ff, bb in zip(f, b)]
    return "#{:02X}{:02X}{:02X}".format(*mixed)


# ── Базовые цвета ────────────────────────────────────────────────────────────
COLORS = {
    # фоны (от самого тёмного к светлому)
    "bg_primary": "#12131A",      # фон окна, сайдбар, консоль
    "bg_surface": "#1B1D26",      # карточки, панели, шапка списков, футер
    "bg_elevated": "#242734",     # поля ввода, второстепенные кнопки, строки списков
    # рамки
    "border": "#2E3244",          # обычная рамка 1px
    "border_strong": "#3A3F55",   # контурные кнопки, трек выключенного тумблера
    "border_focus": "#4A5068",    # выбранный фильтр, пунктир «добавить»
    # текст
    "text": "#E8EAF0",            # основной
    "text_secondary": "#A9AFC2",  # подписи полей, неактивные пункты
    "text_muted": "#8A90A6",      # подсказки, время в логе (не светлее!)
    # зелёный — ТОЛЬКО старт и сохранение
    "green": "#3B8E26",           # большая кнопка «Начать фарм» (текст 19px bold), столбики графика
    "green_button": "#2F7A1E",    # кнопки «Сохранить …» с мелким текстом (контраст белого 5.3:1)
    "green_hover": "#4AA52F",
    # синий — выбранное и активное
    "blue": "#2979FF",            # тумблер ВКЛ, прогресс-бар титанита, рамка выделенного
    "blue_button": "#1F6FEB",     # синие кнопки с текстом и выбранный сегмент (контраст 4.6:1)
    "blue_text": "#6EA8FF",       # синие ссылки и иконки на тёмном фоне
    # статусы
    "success": "#4ADE80",
    "warning": "#FACC15",
    "danger": "#EF4444",          # рамки, иконки, точки
    "danger_text": "#F87171",     # красный ТЕКСТ (на #EF4444 мелкий текст плохо читается)
    "danger_button": "#DC2626",   # опасная кнопка в диалоге («Удалить все»), текст белый
    "gold": "#F5C542",            # «золотые правила», блок доната
    "sos_bg": "#302129",          # фон док-плеера в состоянии SOS
    "white": "#FFFFFF",
    "guide_text": "#C9CEDB",      # абзацы руководства (макет 06_guide): между text и text_secondary
}

# ── Подкрашенные фоны (rgba из макетов, уже смешанные) ───────────────────────
TINTS = {
    # активный пункт сайдбара: rgba(41,121,255,.16) + рамка rgba(41,121,255,.45) на #12131A
    "nav_active_bg": blend(COLORS["blue"], COLORS["bg_primary"], 0.16),
    "nav_active_border": blend(COLORS["blue"], COLORS["bg_primary"], 0.45),
    # выделенная строка/карточка на поверхности
    "blue_on_surface": blend(COLORS["blue"], COLORS["bg_surface"], 0.16),
    # выбранный титан в пикере / выбранный враг
    "green_on_surface": blend(COLORS["green"], COLORS["bg_surface"], 0.14),
    # плашка-подсказка «Как это работает» (вкладка Авто-тактика)
    "info_banner_bg": "#182033",
    "info_banner_border": blend(COLORS["blue"], COLORS["bg_primary"], 0.35),
    # бейджи статусов на #242734
    "success_badge_bg": blend(COLORS["success"], COLORS["bg_elevated"], 0.14),
    "warning_badge_bg": blend(COLORS["warning"], COLORS["bg_elevated"], 0.14),
    "danger_badge_bg": blend(COLORS["danger"], COLORS["bg_elevated"], 0.18),
    # подложка иконки в диалоге подтверждения (экран 8): rgba(239,68,68,.16) и rgba(250,204,21,.14) на #1B1D26
    "danger_on_surface": blend(COLORS["danger"], COLORS["bg_surface"], 0.16),
    "warning_on_surface": blend(COLORS["warning"], COLORS["bg_surface"], 0.14),
    "blue_icon_bg": blend(COLORS["blue"], COLORS["bg_surface"], 0.16),
    "gold_on_surface": blend(COLORS["gold"], COLORS["bg_surface"], 0.16),
    # поле ввода с ошибкой и недоступное (экран 8)
    "field_error_bg": "#2A1F27",
    "field_disabled_bg": "#1F2129",
    # наведение на кнопки (в макетах не нарисовано: чуть светлее фона кнопки)
    "hover_elevated": blend(COLORS["white"], COLORS["bg_elevated"], 0.06),
    "hover_surface": blend(COLORS["white"], COLORS["bg_surface"], 0.05),
    "hover_primary": blend(COLORS["white"], COLORS["bg_primary"], 0.05),
    "hover_blue": blend(COLORS["white"], COLORS["blue_button"], 0.12),
    "hover_green_button": blend(COLORS["white"], COLORS["green_button"], 0.10),
    "hover_danger_button": blend(COLORS["white"], COLORS["danger_button"], 0.10),
    # плашки руководства (макет 06_guide): «Готово» — rgba(59,142,38,.12) и рамка .45 на #1B1D26; «Внимание» — так же жёлтым
    "done_bg": blend(COLORS["green"], COLORS["bg_surface"], 0.12),
    "done_border": blend(COLORS["green"], COLORS["bg_surface"], 0.45),
    "warning_banner_bg": blend(COLORS["warning"], COLORS["bg_surface"], 0.08),
    "warning_banner_border": blend(COLORS["warning"], COLORS["bg_surface"], 0.40),
}

# ── Стихии ───────────────────────────────────────────────────────────────────
# color — рамки аватарок, иконки, заголовки колонок
# text  — если стихия пишется ТЕКСТОМ мелким шрифтом (у «Смешанной» основной цвет темноват)
# tint  — фон аватарки/бейджа (16% цвета поверх карточки #1B1D26)
# Название стихии — i18n.py, ключ elem_<стихия> (без значка: ui.theme.plain_text)
ELEMENTS = {
    "earth": {"color": "#52B788", "text": "#52B788", "icon": "leaf"},
    "water": {"color": "#00B4D8", "text": "#00B4D8", "icon": "droplet"},
    "fire": {"color": "#F77F00", "text": "#F77F00", "icon": "flame"},
    "light": {"color": "#E9C46A", "text": "#E9C46A", "icon": "sun"},
    "dark": {"color": "#A3A8C3", "text": "#A3A8C3", "icon": "moon"},
    # «Смешанная» — это тип КОМНАТЫ, а не стихия титана
    "mix": {"color": "#9D4EDD", "text": "#BF8CF0", "icon": "swords"},
}
for _el in ELEMENTS.values():
    _el["tint"] = blend(_el["color"], COLORS["bg_surface"], 0.16)
ELEMENTS["mixed"] = ELEMENTS["mix"]

# Титан без стихии (новый, которого ещё нет в TITANS): серая рамка
UNKNOWN_ELEMENT = {"color": COLORS["border_strong"], "text": COLORS["text_secondary"], "icon": "user",
                   "tint": COLORS["bg_elevated"]}

# Титаны — из titans.py (задача 16: новый титан — одна строка там и картинки). Имена — внутренние, как картинки
# в assets/ и ключи titan_<имя> в i18n.py.
# Стихии титанов (кого можно в комнату стихии): земля, вода, огонь, свет, тьма; эларитовые Паллант, Орм и Алекто
# встают и в комнату своей стихии, поэтому они здесь
TITANS = {element: titans.of_element(element) for element in titans.ELEMENTS}
TITAN_ELEMENT = {name: el for el, names in TITANS.items() for name in names}

# Эларитовые титаны (ответ пользователя 22.10.2026, шаг 3). Метида — только эларит: её ставят лишь в смешанную комнату.
# Цвет — как у смешанной комнаты (другой комнаты у неё нет), значок — кристалл. Название — i18n.py, elem_elarite
ELARITE_ONLY = titans.elarite_only()
ELEMENTS["elarite"] = {**ELEMENTS["mix"], "icon": "gem"}
TITAN_ELEMENT.update({name: "elarite" for name in ELARITE_ONLY})

# Новые титаны (задача 16): картинка есть, а строки в titans.py нет — стихия неизвестна (серая рамка, UNKNOWN_ELEMENT).
# Ваш ответ 26.10.2026: такие встают только в смешанную комнату, в «Собери состав» — своей строкой «Новые титаны»
NEW_TITANS = titans.unknown()

# Группы в окне выбора и в списках (ваш ответ 25.10.2026): порядок внутри — позиция в игре 1…5
TITAN_GROUPS = {element: titans.group(element) for element in titans.ELEMENTS + (titans.ELARITE,)}
if NEW_TITANS:
    TITAN_GROUPS["new"] = list(NEW_TITANS)
# Порядок в паке, как ставит игра: место 1, 2, … (на экране игры место 1 — справа)
GAME_SLOT_ORDER = titans.slot_order()
# Все титаны по группам, одним списком (колонки списков: каждая группа с новой колонки)
GROUPED_TITANS = [name for names in TITAN_GROUPS.values() for name in names]


def game_order(team):
    """Пак в порядке игры: место 1, 2, … Неизвестные титаны — в конце, в прежнем порядке."""
    team = list(team)
    known = [t for t in GAME_SLOT_ORDER if t in team]
    return known + [t for t in team if t not in GAME_SLOT_ORDER]


def grouped(names):
    """Титаны по группам и позициям (для списков). Неизвестные — в конце."""
    names = list(names)
    return [t for t in GROUPED_TITANS if t in names] + [t for t in names if t not in GROUPED_TITANS]


def screen_order(team):
    """Пак слева направо, как на экране игры (место 1 — справа). Только для показа: в файлах порядок прежний."""
    return list(reversed(game_order(team)))


def room_titans(room):
    """Кого можно поставить в комнату: в комнату земли, воды и огня — только титанов этой стихии,
    в смешанную — всех, и Метиду, и новых титанов без стихии. Комната неизвестна — всех."""
    if room in ("earth", "water", "fire"):
        return list(TITANS[room])
    return [name for names in TITANS.values() for name in names] + ELARITE_ONLY + NEW_TITANS


# Цвета тегов журнала
LOG_TAGS = {
    "СИСТЕМА": "#5BC0EB",
    "GUI": COLORS["text_muted"],
    "БОЙ": COLORS["success"],
    "ПЕРЕХВАТ": COLORS["warning"],
    "ОШИБКА": COLORS["danger_text"],
    "SOS": COLORS["danger_text"],
    "ML": "#BF8CF0",
}

# Журнал нового окна (шаг 3): бот пишет свои теги ([ТАКТИКА], [НАВИГАЦИЯ] ...), поэтому тег красится цветом своей
# «таблетки» (ui/log_lines.py): бои — зелёным, правила — жёлтым (как [ПЕРЕХВАТ] в макете), система — голубым, ошибки — красным.
# Строки самого окна ([GUI]) — серым, время в начале строки — серым
LOG_CATEGORY_COLORS = {
    "fights": LOG_TAGS["БОЙ"],
    "rules": LOG_TAGS["ПЕРЕХВАТ"],
    "system": LOG_TAGS["СИСТЕМА"],
    "errors": LOG_TAGS["ОШИБКА"],
    "gui": LOG_TAGS["GUI"],
}

# «Правила и перехваты» (шаг 5в, макет 03c): значки в строке правила — (цвет текста, подложка на фоне строки bg_elevated).
# Тип правила (ваш ответ 4.2): ЛЕЧЕНИЕ, СКИП, ХП, ВРАГИ, ЭНЕРГИЯ; действие без пака: «Спросить вас», «Пропустить комнату»
_SKIP_TEXT = "#C3C8D6"
RULE_TAG_COLORS = {
    "heal": (COLORS["success"], blend(COLORS["success"], COLORS["bg_elevated"], 0.14)),
    "skip": (_SKIP_TEXT, blend(COLORS["text_secondary"], COLORS["bg_elevated"], 0.14)),
    "hp": (COLORS["warning"], blend(COLORS["warning"], COLORS["bg_elevated"], 0.14)),
    "enemies": (COLORS["danger_text"], blend(COLORS["danger"], COLORS["bg_elevated"], 0.16)),
    "energy": (COLORS["blue_text"], blend(COLORS["blue"], COLORS["bg_elevated"], 0.16)),
}
RULE_ACTION_COLORS = {
    "ask": RULE_TAG_COLORS["hp"],
    "skip": RULE_TAG_COLORS["skip"],
}
RULE_DIM = 0.45   # выключенное правило бледное (макет: opacity 0.45), но не удалено


def rule_room_badge(room):
    """Значок стихии в строке правила: (цвет текста, подложка на фоне строки)."""
    style = ELEMENTS.get(room, UNKNOWN_ELEMENT)
    return style["text"], blend(style["color"], COLORS["bg_elevated"], 0.18 if room == "mix" else 0.16)


# Иконки в списках руководства «- :имя: пункт» — по очереди этими цветами (макет 06_guide: синий, зелёный, голубой, жёлтый)
GUIDE_LIST_ICON_COLORS = (COLORS["blue_text"], COLORS["success"], "#5BC0EB", COLORS["warning"])

# Цвет текста элементов CustomTkinter по умолчанию (тёмная тема): у лёгких элементов (ui/light.py), если цвет не задан
CTK_TEXT = "#DCE4EE"

# Иконки ui/icons, которых нет в design/icons: нарисованы по контуру Lucide тем же размером (ui/icons/__init__.py)
EXTRA_ICONS = {"minimize-2", "minus"}

# Цель сессии на главной: значок и его цвет (кристалл титанита — фиолетовый, как в макете 01_main)
GOAL_ICONS = {
    "titanite": ("gem", "#9D4EDD"),
    "rooms": ("door-open", COLORS["blue_text"]),
    "floors": ("layers", COLORS["blue_text"]),
    "time": ("gauge", COLORS["blue_text"]),
}

# «Статистика» (шаг 6, макет 05_stats): значок плитки и его цвет (цифры белые, цвет только у значка)
STAT_TILES = {
    "titanite": ("gem", COLORS["success"]),
    "today": ("calendar", COLORS["success"]),
    "potions": ("flask-conical", ELEMENTS["mix"]["text"]),
    "rooms": ("door-open", LOG_TAGS["СИСТЕМА"]),
    "floors": ("layers", LOG_TAGS["СИСТЕМА"]),
}
# «О программе» (шаг 7, макет 07_about): цвет квадрата у кнопок прямых переводов (оранжевый — как у огня, фиолетовый — как у смешанной)
DONATE_COLORS = {
    "boosty": ELEMENTS["fire"]["color"],
    "yoomoney": ELEMENTS["mix"]["color"],
}
# График титанита: столбики зелёные; выбран один — он ярче, остальные бледнее, под ним синеватая колонка
CHART_COLORS = {
    "bar": COLORS["green"],
    "bar_hover": COLORS["green_hover"],
    "bar_dim": blend(COLORS["green"], COLORS["bg_surface"], 0.35),
    "column": blend(COLORS["blue"], COLORS["bg_surface"], 0.10),
    "grid": COLORS["border"],
    "axis": COLORS["text_muted"],
    "label": COLORS["text_secondary"],
    "label_selected": COLORS["text"],
    "plate": COLORS["bg_elevated"],
    "plate_border": COLORS["border_strong"],
}

# ── Шрифты ───────────────────────────────────────────────────────────────────
# Roboto идёт вместе с CustomTkinter. Моноширинный: Consolas (есть в Windows).
# Размер — в пикселях, как в макетах; CustomTkinter сам увеличивает его под масштаб Windows.
FONT_FAMILY = "Roboto"
MONO_FAMILY = "Consolas"
FONTS = {
    "page_title": (FONT_FAMILY, 18, "bold"),   # заголовок в шапке
    "app_name": (FONT_FAMILY, 22, "bold"),     # название программы в карточке «О программе»
    "about_text": (FONT_FAMILY, 16),           # описание под названием в «О программе»
    "section": (FONT_FAMILY, 15, "bold"),      # заголовок карточки/раздела
    "card_title": (FONT_FAMILY, 14, "bold"),
    "dialog_title": (FONT_FAMILY, 16, "bold"),
    "body": (FONT_FAMILY, 14),
    "body_bold": (FONT_FAMILY, 14, "bold"),
    "button": (FONT_FAMILY, 13),
    "button_bold": (FONT_FAMILY, 13, "bold"),
    "text": (FONT_FAMILY, 13),                 # текст диалогов и уведомлений
    "label": (FONT_FAMILY, 12),                # подписи полей, подсказки
    "label_bold": (FONT_FAMILY, 12, "bold"),
    "small": (FONT_FAMILY, 11),
    "small_bold": (FONT_FAMILY, 11, "bold"),   # «ОБЫЧНОЕ», «РАЗДЕЛ 1»
    "cta": (FONT_FAMILY, 19, "bold"),          # «Начать фарм»
    "kpi": (MONO_FAMILY, 26),                  # большие цифры
    "mono": (MONO_FAMILY, 12),                 # журнал
    "mono_field": (MONO_FAMILY, 14),           # числа в полях ввода
    "version": (MONO_FAMILY, 10),              # «v1.6.1» под логотипом в полоске
    # руководство (шаг 10.0, макет 06_guide)
    "guide_title": (FONT_FAMILY, 22, "bold"),  # заголовок «#» вверху
    "guide_heading": (FONT_FAMILY, 20, "bold"),  # заголовок раздела «##»
    "guide_code": (MONO_FAMILY, 13),           # `команда` внутри абзаца
    "toc_number": (MONO_FAMILY, 11),           # номер раздела в кружке оглавления
}

# ── Размеры ──────────────────────────────────────────────────────────────────
SIZES = {
    "window": (1100, 720),        # размер по умолчанию, если экран позволяет
    "window_min": (1000, 620),    # меньше не даём; не влезло — прокрутка внутри
    "rail_width": 64,             # полоска навигации с иконками
    "rail_button": 44,            # кнопка в полоске (иконка 20)
    "header_height": 56,
    "header_button": 34,          # иконки-кнопки в шапке
    "footer_height": 64,          # футер «Сохранить настройки» в мастере правил
    "content_padding": 24,
    "gap_xs": 6, "gap_s": 8, "gap_m": 12, "gap_l": 16, "gap_xl": 24,
    "radius_card": 10,
    "radius_dialog": 12,
    "radius_control": 6,
    "radius_chip": 15,            # фильтры-«таблетки» высотой 30
    "control_height": 36,         # поля ввода, выпадающие списки, обычные кнопки
    "button_height_footer": 38,
    "cta_height": 62,
    "chip_height": 30,
    "avatar": 36,                 # мини-аватар титана, рамка 2px цветом стихии
    "avatar_small": 26,
    "avatar_border": 2,
    "icon": 18,                   # иконка в кнопке
    "icon_nav": 20,
    "hud_height": 60,             # док-плеер под окном scrcpy (макет)
    "hud_height_tall": 100,       # док-плеер на деле: выше макета, 4 строки (ваш ответ после проверки шага 4)
    "toast_height": 44,
    "toast_ms": 4000,             # уведомление видно 4 с
    "tooltip_delay_ms": 400,
}

# ── Картинки титанов для оболочки ────────────────────────────────────────────
# Только для окна программы: бот их не читает (титанов для слотов он ищет в корне assets/, а не в папках).
# Имя файла — внутреннее имя титана: assets/icons/angus.png. Нет картинки — в квадрате две буквы имени.
# Сначала папка (заменили картинку — видно сразу, без пересборки assets_db.py), потом assets_db.py (шаг 8: в собранном
# .exe папки может не быть). pack_assets.py кладёт в него картинку с ключом «путь от assets/ через /»: icons/angus.png.
TITAN_ICON_DIRS = (
    Path("assets") / "icons",                                       # запуск из папки проекта (start.bat)
    Path(__file__).resolve().parent.parent / "assets" / "icons",    # рядом с кодом (и в собранном .exe)
)
TITAN_ICON_EXTS = (".png", ".webp", ".jpg")
TITAN_ICON_DB_EXTS = (".png", ".jpg")                               # pack_assets.py берёт только их
TITAN_ICON_DB_PREFIX = "db:"                                        # ключ картинки из assets_db.py: «db:icons/angus.png»
_ICON_DB = None                                                     # ASSETS из assets_db.py, читается один раз


def element_of(titan):
    """Стихия титана ("earth", ...) или None, если титана нет в TITANS (новый титан)."""
    return TITAN_ELEMENT.get(titan)


def element_style(element):
    """Цвета стихии (color, text, tint, icon). Неизвестная стихия — серый стиль."""
    return ELEMENTS.get(element, UNKNOWN_ELEMENT)


def titan_icon_path(titan, dirs=TITAN_ICON_DIRS):
    """Путь к картинке титана для оболочки или None, если её в папке ещё нет."""
    for folder in dirs:
        for ext in TITAN_ICON_EXTS:
            path = Path(folder) / f"{titan}{ext}"
            if path.is_file():
                return path
    return None


def _icon_db():
    """ASSETS из assets_db.py ({«icons/angus.png»: картинка в base64}) или {}, если файла нет. Файл большой (в нём все
    картинки бота), поэтому читается один раз и только когда в папке картинки титана не нашлось."""
    global _ICON_DB
    if _ICON_DB is None:
        try:
            from assets_db import ASSETS
        except Exception:      # файла нет (обычный случай при запуске из исходников) или он повреждён
            ASSETS = {}
        _ICON_DB = ASSETS if isinstance(ASSETS, dict) else {}
    return _ICON_DB


def titan_icon_source(titan, dirs=TITAN_ICON_DIRS):
    """Откуда взять картинку титана: (ключ, отметка) или None, если её нет ни в папке, ни в assets_db.py.
    Ключ — путь к файлу или «db:icons/имя.png»; отметка — время изменения файла (заменённая картинка перечитается),
    у картинки из assets_db.py — 0. Саму картинку открывает open_titan_icon(ключ)."""
    path = titan_icon_path(titan, dirs)
    if path is not None:
        return str(path), path.stat().st_mtime
    db = _icon_db()
    for ext in TITAN_ICON_DB_EXTS:
        for name in (f"icons/{titan}{ext}", f"icons\\{titan}{ext}"):
            if name in db:
                return TITAN_ICON_DB_PREFIX + name, 0
    return None


def open_titan_icon(key):
    """Картинка PIL по ключу из titan_icon_source. Не читается (битый файл или base64) — исключение, его ловит окно:
    в квадрате тогда две буквы имени."""
    from PIL import Image
    if key.startswith(TITAN_ICON_DB_PREFIX):
        # как у бота (vision.get_image_data): в assets_db.py картинка лежит в base64
        return Image.open(io.BytesIO(base64.b64decode(_icon_db()[key[len(TITAN_ICON_DB_PREFIX):]])))
    return Image.open(key)


def plain_text(text):
    """Убрать значки-эмодзи в начале надписи из i18n.py: «🌿 Земля» → «Земля», «⚔️ Смешанная» → «Смешанная».
    В новом интерфейсе эмодзи нет (Tkinter в Windows рисует их плохо), а надписи с ними в i18n.py остались от старого окна.
    Конец надписи не трогаем: там бывают нужные стрелки («Открыть →»)."""
    start = 0
    while start < len(text) and (unicodedata.category(text[start])[0] in "SCZ" or text[start] in "️‍"):
        start += 1
    return text[start:].rstrip()


def initials(name):
    """Две буквы имени для квадрата титана, пока нет картинки: «Араджи» → «Ар», «amon» → «Am»."""
    letters = [ch for ch in plain_text(name) if ch.isalnum()]
    if not letters:
        return "?"
    return (letters[0].upper() + "".join(letters[1:2]).lower())
