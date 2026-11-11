# win_focus.py
# Какая клавиша опущена и какое окно Windows сейчас активно (задача 18, шаг 2).
# Общее для бота (Ctrl+Q, Ctrl+Shift+Q — main.py) и окна программы (F9, F10 — ui/hotkeys.py): горячие клавиши
# срабатывают, только когда активно окно игры или окно программы. Раньше бот ловил Ctrl+Q в любой программе, а это
# «выйти» в Telegram Desktop (Ctrl+Q) и в браузерах (Ctrl+Shift+Q).
# Без Tk и OpenCV. Вне Windows функции key_down / foreground_is не работают (их и не зовут); focus_allowed — проверяется тестами.
import os

_USER32 = None


def _user32():
    """Своя копия user32 с правильными типами (номер окна 64-битный). Своя — чтобы не менять ctypes.windll.user32:
    им пользуется pygetwindow, и чужие типы могли бы его сломать."""
    global _USER32
    if _USER32 is None:
        import ctypes
        from ctypes import wintypes
        user32 = ctypes.WinDLL("user32")
        user32.GetAsyncKeyState.argtypes = [ctypes.c_int]
        user32.GetAsyncKeyState.restype = ctypes.c_short
        user32.GetForegroundWindow.argtypes = []
        user32.GetForegroundWindow.restype = wintypes.HWND
        user32.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        user32.GetWindowThreadProcessId.restype = wintypes.DWORD
        user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
        user32.GetWindowTextLengthW.restype = ctypes.c_int
        user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        user32.GetWindowTextW.restype = ctypes.c_int
        _USER32 = user32
    return _USER32


def key_down(vk):
    """Клавиша опущена прямо сейчас (старший бит GetAsyncKeyState)."""
    return _user32().GetAsyncKeyState(vk) & 0x8000


def focus_allowed(owner_pid, title, game_title, pids):
    """Активное окно — «наше»: принадлежит одному из процессов pids (окно программы, его диалоги) или в его заголовке
    game_title (окно игры scrcpy)."""
    return owner_pid in pids or game_title in (title or "")


def foreground_is(game_title, pids=None):
    """Активно окно игры (в заголовке game_title) или окно одного из процессов pids (по умолчанию — этого процесса)."""
    import ctypes
    from ctypes import wintypes
    user32 = _user32()
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        return False
    owner = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(owner))
    length = user32.GetWindowTextLengthW(hwnd)
    title = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, title, length + 1)
    return focus_allowed(owner.value, title.value, game_title, tuple(pids or (os.getpid(),)))
