"""Все титаны в одном месте (задача 16): стихия, место в паке, лекарь, враг в подземелье и имя на языках окна.

Отсюда берут титанов бот (лекари — tactics.HEALERS, враги за дверью — config.ENEMY_TITANS), окно программы
(ui/theme.py: стихии, колонки «Собери состав», порядок в паке), Telegram (разбор пака из чата) и i18n.py (имена titan_<имя>).

Как добавить нового титана:
1. Картинки (имя файла — внутреннее имя титана латиницей, маленькими буквами, например newtitan):
   - assets/newtitan.png — титан в слотах и в сетке экрана выбора команды (по ней бот его ставит);
   - assets/res_newtitan.png — титан на окне результата (по ней бот читает ХП и энергию после боя);
   - assets/icons/newtitan.png — квадрат в окне программы (без неё — две буквы имени);
   - assets/enemy_newtitan.png — только если он бывает врагом в подземелье (и enemy=True ниже).
   Новые картинки git не видит (assets/ в .gitignore): git add -f assets/newtitan.png и т.д.
   Для собранного .exe — пересобрать assets_db.py (python pack_assets.py).
2. Одна строка в TITANS ниже. Без строки титан всё равно есть: бот ставит его в слоты, окно показывает его серым
   в строке «Новые титаны» (только для смешанной комнаты), имя — по названию файла.

Модуль без OpenCV и Tk: его можно импортировать в тестах в облаке. При импорте ничего не читает с диска.
"""
import os
import re
import sys

# Стихии комнат и титанов (как в bot_data/rules/<стихия>.yml и ui/theme.py)
ELEMENTS = ("earth", "water", "fire", "light", "dark")
# Эларит — титан без своей комнаты: ставится только в смешанную (Метида)
ELARITE = "elarite"
# Языки окна (i18n.LANGUAGES). Нет имени на языке — берётся имя на запасном языке, потом английское, потом русское
NAME_FALLBACK = {"UK": ("RU",), "KK": ("RU",)}


def titan(element, place, elarite=False, healer=0, enemy=False, **names):
    """Запись о титане.
    element — стихия: earth, water, fire, light, dark или elarite (только смешанная комната);
    place — (позиция в паке 1–5, очередь среди титанов этой позиции): так игра ставит пак, место 1 — справа на экране;
    elarite — эларитовый титан, который встаёт и в комнату своей стихии (в окне — в строке «Эларит»);
    healer — лекарь: номер в очереди лекарей (1 — лечит сильнее всех; бот берёт из равных по энергии того, кто раньше), 0 — не лечит;
    enemy — бывает врагом в подземелье (бот ищет его за дверью по картинке assets/enemy_<имя>.png);
    names — имя на языках окна: RU="Араджи", EN="Araji", ..."""
    return {"element": element, "place": tuple(place), "elarite": elarite, "healer": healer, "enemy": enemy,
            "names": names}


# Порядок строк — как в старом окне выбора по стихиям: в этом порядке бот ищет врагов, и так же их показывает окно.
# Позиции и очередь на позиции — ваш ответ 25.10.2026 (docs/plan_6a.md, шаг 6а.7).
# Лекари — ваш ответ на вопрос 2: сильно — Гиперион и Ияри, слабее — Авалон, Сигурд, Солярис, Паллант, Метида.
# Враги — 13 титанов подземелья: земля без Палланта, вода без Тидуса и Орма, огонь без Ашерона и Алекто.
TITANS = {
    # Земля
    "angus": titan("earth", place=(1, 6), enemy=True, RU="Ангус", EN="Angus", ZH="安格斯", KO="앵거스", JA="アンガス"),
    "avalon": titan("earth", place=(2, 4), healer=3, enemy=True, RU="Авалон", EN="Avalon", ZH="阿瓦隆", KO="아발론", JA="アバロン"),
    "eden": titan("earth", place=(4, 3), enemy=True, RU="Эдем", EN="Eden", UK="Едем", ES="Edén", ZH="伊甸", KO="에덴", JA="エデン"),
    "silva": titan("earth", place=(5, 3), enemy=True, RU="Сильва", EN="Sylva", UK="Сільва", ZH="希尔瓦", KO="실바", JA="シルバ"),
    "verdok": titan("earth", place=(3, 1), enemy=True, RU="Вердок", EN="Verdok", ZH="韦尔多克", KO="베르독", JA="ヴェルドク"),
    "pallant": titan("earth", place=(1, 2), elarite=True, healer=6, RU="Паллант", EN="Pallant", ZH="帕兰特", KO="팔란트", JA="パラント"),
    # Вода
    "hyperion": titan("water", place=(5, 1), healer=1, enemy=True, RU="Гиперион", EN="Hyperion", UK="Гіперіон", ZH="海伯利昂", KO="히페리온", JA="ヒペリオン"),
    "sigurd": titan("water", place=(1, 1), healer=4, enemy=True, RU="Сигурд", EN="Sigurd", UK="Сігурд", ZH="西格德", KO="시구르드", JA="シグルド"),
    "tidus": titan("water", place=(3, 3), RU="Тидус", EN="Tidus", UK="Тідус", ZH="泰特斯", KO="티두스", JA="タイダス"),
    "nova": titan("water", place=(2, 2), enemy=True, RU="Нова", EN="Nova", ZH="诺瓦", KO="노바", JA="ノヴァ"),
    "mairi": titan("water", place=(4, 1), enemy=True, RU="Маири", EN="Mairi", UK="Маїрі", ZH="迈里", KO="마이리", JA="マイリ"),
    "orm": titan("water", place=(3, 2), elarite=True, RU="Орм", EN="Orm", ZH="奥尔姆", KO="오름", JA="オルム"),
    # Огонь
    "araji": titan("fire", place=(3, 4), enemy=True, RU="Араджи", EN="Araji", UK="Араджі", ZH="阿拉吉", KO="아라지", JA="アラジ"),
    "ignis": titan("fire", place=(5, 2), enemy=True, RU="Игнис", EN="Ignis", UK="Ігніс", ZH="伊格尼斯", KO="이그니스", JA="イグニス"),
    "acheron": titan("fire", place=(4, 2), RU="Ашерона", EN="Acheron", UK="Ашерон", KK="Ашерон", ZH="阿刻戎", KO="아케론", JA="アケロン"),
    "vulcan": titan("fire", place=(2, 3), enemy=True, RU="Вулкан", EN="Vulcan", ZH="瓦尔坎", KO="불칸", JA="バルカン"),
    "moloch": titan("fire", place=(1, 5), enemy=True, RU="Молох", EN="Moloch", ZH="摩洛克", KO="몰록", JA="モロク"),
    "alecto": titan("fire", place=(2, 1), elarite=True, RU="Алекто", EN="Alecto", ZH="阿莱克托", KO="알렉토", JA="アレクト"),
    # Свет
    "rigel": titan("light", place=(1, 4), RU="Ригель", EN="Rigel", UK="Рігель", ZH="瑞格尔", KO="리겔", JA="リゲル"),
    "iyari": titan("light", place=(2, 5), healer=2, RU="Ияри", EN="Iyari", UK="Іярі", ZH="伊亚里", KO="이야리", JA="イヤリ"),
    "lumira": titan("light", place=(3, 5), RU="Люмира", EN="Lumira", UK="Люміра", ZH="卢米拉", KO="루미라", JA="ルミラ"),
    "solaris": titan("light", place=(4, 5), healer=5, RU="Солярис", EN="Solaris", UK="Соляріс", ZH="索拉里斯", KO="솔라리스", JA="ソラリス"),
    "amon": titan("light", place=(5, 4), RU="Амон", EN="Amon", ES="Amón", ZH="阿蒙", KO="아몬", JA="アモン"),
    # Тьма
    "mor": titan("dark", place=(2, 6), RU="Мор", EN="Mort", ZH="莫特", KO="모르트", JA="モート"),
    "tenebris": titan("dark", place=(5, 5), RU="Тенебрис", EN="Tenebris", UK="Тенебріс", ZH="泰内布里斯", KO="테네브리스", JA="テネブリス"),
    "brustar": titan("dark", place=(1, 3), RU="Брустар", EN="Brustar", ZH="布鲁斯塔", KO="브루스타", JA="ブルスター"),
    "umbra": titan("dark", place=(3, 6), RU="Умбра", EN="Umbra", ZH="乌姆布拉", KO="움브라", JA="ウンブラ"),
    "keros": titan("dark", place=(4, 6), RU="Керос", EN="Keros", ZH="凯罗斯", KO="케로스", JA="ケロス"),
    # Эларит: только в смешанную комнату
    "metida": titan("elarite", place=(4, 4), healer=7, RU="Метида", EN="Metis", UK="Метіда", FR="Métis", PL="Metyda", PT="Métis", ZH="墨提斯", KO="메티스", JA="メティス"),
}


# ── Списки для бота и окна ───────────────────────────────────────────────────
def known():
    """Титаны с записью в TITANS, в порядке строк."""
    return list(TITANS)


def of_element(element):
    """Кого можно в комнату этой стихии: титаны стихии и эларитовые этой стихии (Паллант — в земляную)."""
    return [name for name, t in TITANS.items() if t["element"] == element]


def elarite_only():
    """Титаны только для смешанной комнаты (Метида)."""
    return of_element(ELARITE)


def by_place(names):
    """Титаны в порядке игры: позиция 1…5, на одной позиции — по очереди. Неизвестные — в конце, в прежнем порядке."""
    names = list(names)
    placed = sorted((n for n in names if n in TITANS), key=lambda n: TITANS[n]["place"])
    return placed + [n for n in names if n not in TITANS]


def group(element):
    """Колонка окна выбора: титаны стихии без эларитовых, по позициям; ELARITE — все эларитовые (Паллант, Алекто, Орм, Метида)."""
    if element == ELARITE:
        return by_place(n for n, t in TITANS.items() if t["elarite"] or t["element"] == ELARITE)
    return by_place(n for n, t in TITANS.items() if t["element"] == element and not t["elarite"])


def slot_order():
    """Все титаны с записью в порядке игры (место 1, 2, …)."""
    return by_place(TITANS)


def healers():
    """Лекари по очереди: сначала те, кто лечит сильнее."""
    return tuple(sorted((n for n, t in TITANS.items() if t["healer"]), key=lambda n: TITANS[n]["healer"]))


def enemies():
    """Враги подземелья, в порядке строк (в нём бот их ищет и пишет в лог)."""
    return [n for n, t in TITANS.items() if t["enemy"]]


def name(titan_name, lang="RU"):
    """Имя титана на языке окна. Нет записи — по названию файла: newtitan → Newtitan."""
    names = TITANS.get(titan_name, {}).get("names", {})
    for code in (lang,) + NAME_FALLBACK.get(lang, ()) + ("EN", "RU"):
        if names.get(code):
            return names[code]
    return str(titan_name).capitalize()


def translation_keys(lang):
    """Имена всех титанов с записью для i18n.py: {"titan_araji": "Араджи", ...}."""
    return {f"titan_{n}": name(n, lang) for n in TITANS}


# ── Титаны по картинкам ──────────────────────────────────────────────────────
# Картинки в корне assets/, которые не титаны (кнопки, враги, значки и т.п.)
NOT_TITAN_PREFIXES = ("btn_", "res_", "enemy_", "icon_", "flag_", "badge_")
ICON_EXTS = (".png", ".webp", ".jpg")     # assets/icons/ (как ui/theme.TITAN_ICON_EXTS)
TITAN_NAME = re.compile(r"^[a-z0-9_]+$")  # внутреннее имя: латиница маленькими буквами, цифры, _


def _base_dir():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


ASSETS_DIR = os.path.join(_base_dir(), "assets")


def is_titan_picture(stem):
    """Картинка в корне assets/ (имя без расширения) — титан, а не кнопка или значок."""
    return bool(TITAN_NAME.match(stem)) and not stem.startswith(NOT_TITAN_PREFIXES)


def _files(folder, exts):
    try:
        entries = os.listdir(folder)
    except OSError:
        return set()
    stems = set()
    for f in entries:
        stem, ext = os.path.splitext(f)
        if ext.lower() in exts and os.path.isfile(os.path.join(folder, f)):
            stems.add(stem)
    return stems


def _db_keys():
    """Ключи картинок из assets_db.py ({«angus.png»: base64, «icons/angus.png»: ...}) или пусто, если файла нет."""
    try:
        from assets_db import ASSETS
    except Exception:      # файла нет (обычный случай при запуске из исходников) или он повреждён
        return ()
    return list(ASSETS) if isinstance(ASSETS, dict) else ()


def picture_titans(assets_dir=None, db_keys=None):
    """Титаны, у которых есть картинка: assets/<имя>.png (слоты) или assets/icons/<имя>.png (окно).
    assets_db.py читается, только если в папке assets/ нет картинок титанов (собранный .exe): он большой."""
    assets_dir = assets_dir or ASSETS_DIR
    names = {s for s in _files(assets_dir, (".png",)) if is_titan_picture(s)}
    from_disk = bool(names)
    names |= {s for s in _files(os.path.join(assets_dir, "icons"), ICON_EXTS) if TITAN_NAME.match(s)}
    if not from_disk:
        for key in (_db_keys() if db_keys is None else db_keys):
            key = key.replace("\\", "/")
            folder, _, file = key.rpartition("/")
            stem, ext = os.path.splitext(file)
            if folder == "" and ext.lower() == ".png" and is_titan_picture(stem):
                names.add(stem)
            elif folder == "icons" and ext.lower() in (".png", ".jpg") and TITAN_NAME.match(stem):
                names.add(stem)
    return names


def unknown(assets_dir=None, db_keys=None):
    """Титаны с картинкой, но без записи в TITANS (стихия неизвестна), по алфавиту."""
    return sorted(picture_titans(assets_dir, db_keys) - set(TITANS))


def all_titans(assets_dir=None, db_keys=None):
    """Все титаны: с записью (в порядке строк), потом новые по картинкам."""
    return known() + unknown(assets_dir, db_keys)
