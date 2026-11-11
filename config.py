import os

import titans

CONFIG = {
    "angus_manual_control": False,  # задача 12: земля автобоем, ручная ульта — переключателем в окне
    "debug_mode": False,  
    # Динамически получаем язык из процесса GUI (по умолчанию RU, если переменной нет)
    "game_language": os.environ.get("HEROWARS_LANG", "RU")
}

# Лимиты для остановки бота (если 0 - лимит отключен)
LIMITS = {
    "max_time_minutes": 0,      # Остановиться через X минут
    "max_rooms": 0,             # Количество комнат (0 = бесконечно)
    "max_floors": 0,            # Количество этажей (0 = бесконечно)
    "target_titanite": 120      # Остановиться, собрав X титанита
}

# Титаны — в titans.py (задача 16): новый титан — одна строка там и картинки.
# Все титаны с записью в titans.py (титанов для слотов team_manager берёт из картинок, а не отсюда)
ALL_ACTIVE_TITANS = titans.known()

# 13 возможных врагов в подземелье (земля без Палланта, вода без Тидуса и Орма, огонь без Ашерона и Алекто):
# пометка enemy=True в titans.py
ENEMY_TITANS = titans.enemies()

CONFIDENCE_THRESHOLD = 0.8

# Файл-флаг для управления мягкой паузой бота
PAUSE_FLAG_FILE = "pause.flag"

# Системный заголовок окна трансляции (scrcpy / эмулятор)
GAME_WINDOW_TITLE = "HeroWarsBot_Arena"

# Версия программы (показывается в окне программы)
APP_VERSION = "2.0.0"

# Репозиторий программы на GitHub («владелец/имя»). Бот переехал в другой репозиторий — поменяйте только эту строку
# (01.11.2026, задача 19: переезд из petrunin-platon/HeroWarsBot в petrunin-platon/DungeonBot):
# от неё берутся кнопка «GitHub проекта» и «Проверить обновления» (страница релизов) в окне «О программе»
GITHUB_REPO = "petrunin-platon/DungeonBot"

# Почта автора: кнопка «Написать автору», строка Email в «О программе» и «Отправить лог автору» на главной
AUTHOR_EMAIL = "petrunin.platon@gmail.com"
