# gui.py
import sys

# =====================================================================
# ЖИЗНЕННО ВАЖНО: АППАРАТНЫЙ ФИКС DPI WINDOWS
# ДОЛЖЕН БЫТЬ ДО ИМПОРТА ЛЮБЫХ БИБЛИОТЕК
# =====================================================================
if sys.platform == "win32":
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass
# =====================================================================

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# ИНТЕЛЛЕКТУАЛЬНЫЙ РОУТИНГ ДЛЯ .EXE (FORK PATTERN)
if "--bot-mode" in sys.argv:
    import main
    sys.exit(0)

if __name__ == "__main__":
    # Окно программы (задача 15) — ui/app.py: и в start.bat / python gui.py, и в собранном .exe.
    # Старое окно удалено на шаге 9 (решение пользователя 25.10.2026), оно есть в истории git.
    from ui.app import run
    run()
