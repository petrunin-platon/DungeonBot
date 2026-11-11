# stats_manager.py
import json
import os
import yaml
import time
from datetime import datetime, timedelta
import data_paths
import safe_files

PROFILE_FILE = "profile.yml"

# Кэш для хранения сдвига времени (читаем диск 1 раз)
_RESET_SHIFT_CACHE = None

def get_reset_shift():
    """Читает из профиля час сброса дня по местному времени с использованием кэширования."""
    global _RESET_SHIFT_CACHE
    if _RESET_SHIFT_CACHE is not None:
        return _RESET_SHIFT_CACHE

    shift = 5
    if os.path.exists(PROFILE_FILE):
        try:
            with open(PROFILE_FILE, 'r', encoding='utf-8') as f:
                profile = yaml.safe_load(f) or {}
                shift = int(profile.get("settings", {}).get("reset_hour", 5))
        except Exception:
            pass
            
    _RESET_SHIFT_CACHE = shift
    return shift

def get_game_datetime():
    """Возвращает объект datetime со сдвигом игрового времени."""
    return datetime.now() - timedelta(hours=get_reset_shift())

def get_game_date():
    """Возвращает строковую игровую дату."""
    return get_game_datetime().strftime("%Y-%m-%d")

def empty_stats():
    """Пустая статистика: всё по нулям, дней нет."""
    return {"total_titanite": 0, "total_rooms": 0, "total_floors": 0, "total_potions": 0, "daily": {}}


def load_stats():
    """Загружает статистику из файла с защитой от блокировок диска и повреждения JSON."""
    stats_file = data_paths.stats_file()
    if not os.path.exists(stats_file):
        return empty_stats()

    max_retries = 5
    retry_delay = 0.5  # Пауза в полсекунды между попытками

    for attempt in range(max_retries):
        try:
            with open(stats_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "total_potions" not in data:
                    data["total_potions"] = 0
                return data
                
        except json.JSONDecodeError as e:
            # Файл прочитался, но внутри мусор или пустота. Начинаем заново, а испорченный файл не теряем (задача 18,
            # шаг 6: раньше следующая комната записывала новую статистику поверх, и вся история пропадала)
            kept = keep_broken_file(stats_file)
            where = f" Испорченный файл сохранён: {kept}." if kept else ""
            print(f"[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден. Начинаем новую статистику. ({e}){where}")
            return empty_stats()
            
        except OSError:
            # Файл заблокирован антивирусом, OneDrive или другой программой
            if attempt < max_retries - 1:
                print(f"[СТАТИСТИКА] Доступ к stats.json заблокирован. Попытка {attempt + 1}/{max_retries} через {retry_delay} сек...")
                time.sleep(retry_delay)
            else:
                print(f"[СТАТИСТИКА] КРИТИЧЕСКАЯ ОШИБКА: Не удалось получить доступ к stats.json после {max_retries} попыток! Защита от потери данных.")
                raise  # Пробрасываем ошибку выше, чтобы принудительно остановить бота и спасти файл

def keep_broken_file(path):
    """Испорченный файл — рядом под именем <имя>.broken_<время>. Возвращает новое имя или None, если не вышло."""
    target = f"{path}.broken_{datetime.now():%Y-%m-%d_%H-%M-%S}"
    try:
        os.replace(path, target)
        return target
    except OSError:
        return None


def save_stats(stats):
    """Сохраняет структуру во временный файл, затем атомарно перезаписывает основной (с повтором, если файл занят)."""
    safe_files.write_text(data_paths.stats_file(), json.dumps(stats, indent=4, ensure_ascii=False))


# Метрики, которые не удалось записать (файл занят, диск недоступен): допишутся со следующей записью (задача 18, шаг 6)
_UNSAVED = []

def add_metric(metric, amount=1, date_str=None, is_bot=False):
    """Добавляет одно значение к счётчикам (ручная корректировка во вкладке «Статистика»)."""
    add_metrics_bulk({metric: amount}, date_str=date_str, is_bot=is_bot)

def add_metrics_bulk(metrics_dict, date_str=None, is_bot=False):
    """
    Пакетное добавление метрик. Сводит чтение/запись файла к одной транзакции.
    Принимает словарь, например: {"rooms": 1, "titanite": 12, "potions": 50}
    """
    if not metrics_dict:
        return

    if not date_str:
        date_str = get_game_date()
    batch = _UNSAVED + [(metrics_dict, date_str, is_bot)]
    try:
        stats = load_stats()
        for metrics, day, bot in batch:
            _apply(stats, metrics, day, bot)
        save_stats(stats)
    except OSError as e:
        # Раньше ошибка записи роняла бота сразу после боя. Теперь — строка в журнал и запись в следующий раз
        _UNSAVED[:] = batch
        print(f"[СТАТИСТИКА] Не удалось записать stats.json ({e}). Допишу со следующей комнатой.")
        return
    if len(batch) > 1:
        print(f"[СТАТИСТИКА] stats.json снова записывается: дописал {len(batch) - 1} пропущенных записей.")
    _UNSAVED.clear()


def _apply(stats, metrics_dict, date_str, is_bot):
    """Прибавить метрики дня к статистике (в памяти)."""
    if date_str not in stats["daily"]:
        stats["daily"][date_str] = {"titanite": 0, "rooms": 0, "floors": 0, "potions": 0}

    for metric, amount in metrics_dict.items():
        # Глобальные счетчики
        global_key = f"total_{metric}"
        if global_key in stats:
            stats[global_key] += amount
        elif global_key == "total_potions": 
            stats[global_key] = amount
        elif metric == "potions": # Защита, если ключа total_potions не было в старых базах
            stats["total_potions"] = amount

        # Дневные счетчики
        if metric in stats["daily"][date_str]:
            stats["daily"][date_str][metric] += amount
        else:
            stats["daily"][date_str][metric] = amount

        # Неизменяемый базис бота
        if is_bot:
            bot_key = f"bot_{metric}"
            if bot_key in stats["daily"][date_str]:
                stats["daily"][date_str][bot_key] += amount
            else:
                stats["daily"][date_str][bot_key] = amount

def reset_stats():
    """Полностью обнуляет базу данных статистики."""
    save_stats(empty_stats())