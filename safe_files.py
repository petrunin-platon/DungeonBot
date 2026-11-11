# safe_files.py
# Надёжная запись файлов бота и окна программы (задача 18, шаги 6–7): сначала во временный файл рядом, потом замена
# настоящего (os.replace) — файл никогда не остаётся записанным наполовину.
# В Windows замена не удаётся, если файл в этот миг держит другая программа (антивирус проверяет новый файл,
# OneDrive/Яндекс.Диск синхронизирует папку, окно программы читает статистику): PermissionError. Раньше бот на этом падал
# сразу после боя. Теперь замена повторяется REPLACE_TRIES раз через REPLACE_PAUSE_S; не вышло — ошибка у вызывающего
# (он решает, писать ли строку в журнал или идти дальше).
# Без OpenCV и Tk, при импорте ничего не делает. Проверяется тестами (tests/test_safe_files.py).
import os
import time

REPLACE_TRIES = 5
REPLACE_PAUSE_S = 0.2


def replace(tmp, path, tries=REPLACE_TRIES, pause=REPLACE_PAUSE_S, sleep=time.sleep):
    """os.replace(tmp, path) с повтором, пока файл занят другой программой."""
    for attempt in range(tries):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == tries - 1:
                raise
            sleep(pause)


def write_text(path, text, encoding="utf-8", sleep=time.sleep):
    """Записать текст в файл целиком: временный файл <path>.tmp и замена (с повтором). Папку создаёт сама."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding=encoding) as f:
        f.write(text)
    replace(tmp, path, sleep=sleep)
