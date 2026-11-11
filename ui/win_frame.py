"""Рамка окна в Windows (задача 15, шаг 6а.1): тёмный заголовок без «спрятать окно и вернуть».

CustomTkinter сам красил заголовок в тёмный, но для этого прятал окно (withdraw), вызывал update() и через 5 мс
возвращал окно «как было». Окно, которое показали в этот миг, пропадало, а захват мыши оставался у невидимого окна —
программа переставала отвечать на щелчки. Теперь CustomTkinter заголовок не трогает (`widgets.AppWindow`,
`_deactivate_windows_window_header_manipulation`), а красим мы: одним вызовом после показа окна, без withdraw и update.

Шаг 6а.2: у главного окна заголовок и рамку Windows убираем совсем (`captionless_style`, `strip_caption`): стили WS_CAPTION
и WS_THICKFRAME снимаются, WS_SYSMENU и WS_MINIMIZEBOX остаются — кнопка на панели задач сворачивает окно, работает Alt+F4.
Не overrideredirect: у такого окна нет кнопки на панели задач, а iconify падает (на этом держится мини-бар шага 4).

Шаг 6а.3 (дополнение): у привязанных окон (transient: подтверждения, «Собери состав», SOS) Tk 8.6 до версии 8.6.14 ставит
расширенный стиль WS_EX_DLGMODALFRAME — объёмную рамку диалога в 2 px (белая и светло-серая полоса сверху и слева,
светло-серая и серая снизу и справа). Заголовок он не требует, поэтому оставался после снятия WS_CAPTION: это и была белая
полоса внутри серой рамки на скриншоте пользователя. Теперь strip_caption снимает и объёмные рамки (`flat_ex_style`).

Сессия 11б: окно без заголовка двигают и меняют ему размер только через Windows (drag_window, set_window_rect), а не
wm geometry Tk: Tk не знает, что заголовок сняли, и менял размер такого окна дважды. Окно программы появляется из-под
«плаща» (cloak), а не через прозрачность -alpha.

Вне Windows функции ничего не делают. Модуль без Tk: окно сюда приходит только своим номером.
"""
import sys

WS_CAPTION = 0x00C00000      # заголовок вместе с тонкой рамкой (WS_BORDER | WS_DLGFRAME)
WS_THICKFRAME = 0x00040000   # рамка, за которую окно растягивают
WS_SYSMENU = 0x00080000
WS_MINIMIZEBOX = 0x00020000
GWL_STYLE = -16
GWL_EXSTYLE = -20
WS_EX_DLGMODALFRAME = 0x00000001   # объёмная рамка диалога (Tk ставит её привязанным окнам)
WS_EX_WINDOWEDGE = 0x00000100      # выпуклый край
WS_EX_CLIENTEDGE = 0x00000200      # вдавленный край
WS_EX_STATICEDGE = 0x00020000      # тонкий вдавленный край
EDGE_EX_STYLES = WS_EX_DLGMODALFRAME | WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE | WS_EX_STATICEDGE
# SWP_NOSIZE | SWP_NOMOVE | SWP_NOZORDER | SWP_NOACTIVATE | SWP_FRAMECHANGED
SWP_FRAME_ONLY = 0x0001 | 0x0002 | 0x0004 | 0x0010 | 0x0020
DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1 = 19


WM_NCLBUTTONDOWN = 0x00A1
HTCAPTION = 2
SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_NOZORDER = 0x0004
SWP_NOACTIVATE = 0x0010
DWMWA_CLOAK = 13              # окно «под плащом»: Windows его рисует, но на экран не выводит (Windows 8 и новее)


def windows_available():
    return sys.platform == "win32"


def _point_lparam(point):
    return ((point.y & 0xFFFF) << 16) | (point.x & 0xFFFF)


def drag_window(hwnd):
    """Отдать перетаскивание окна Windows, как за настоящий заголовок (сессия 11: окно тащат мышью — никаких следов):
    Windows сама ведёт окно за мышью и двигает его готовую картинку, окну не нужно перерисовываться на каждый сдвиг.

    Только PostMessage — «записка» в очередь окна, функция сразу возвращается. С SendMessage перетаскивание шло бы
    внутри этого вызова, а Tk в это время звал бы обработчики Python (часы, события) из-под вызова ctypes — Python 3.13
    на этом аварийно закрывает программу («PyEval_RestoreThread: the function must be called with the GIL held»;
    так и было у пользователя 26.10.2026). Записку Tk достаёт уже своим обычным циклом, как щелчок по заголовку.
    Кнопку отпустили — Windows забирает это отпускание себе; Tk узнаёт, что кнопка отпущена, при следующем движении мыши.
    Перед запиской окно Tk не двигаем (сессия 11б): wm geometry у окна без заголовка дважды меняет его размер
    (см. set_window_rect) — это и были 3 с фриза и следы, стоило взять окно за шапку.
    True — записку отправили; False — вне Windows или не вышло (тогда двигает Tk, как раньше)."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        user32 = ctypes.WinDLL("user32")
        user32.ReleaseCapture.restype = wintypes.BOOL
        post = user32.PostMessageW
        post.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
        post.restype = wintypes.BOOL
        point = wintypes.POINT()
        user32.GetCursorPos(ctypes.byref(point))
        user32.ReleaseCapture()              # мышь держит виджет шапки (Tk), а вести её должна Windows
        return bool(post(hwnd, WM_NCLBUTTONDOWN, HTCAPTION, _point_lparam(point)))
    except Exception:
        return False


def set_window_rect(hwnd, x=None, y=None, width=None, height=None):
    """Поставить окно без заголовка на место и задать размер — сразу Windows, без Tk (сессия 11б). Tk не знает, что
    заголовок и рамку мы сняли (strip_caption): на wm geometry он прибавляет к размеру их высоту и ширину, а потом
    убирает лишнюю высоту вторым изменением — окно дважды меняло размер (и становилось на 16 px шире), и всё окно
    раскладывалось и перерисовывалось заново. Об изменении Tk узнаёт сам, как о перетаскивании мышью.
    Размеры — в настоящих пикселях; без x и y — только размер, без width и height — только место. True — получилось.
    SetWindowPos только отправляет окну сообщения о новом месте (своего цикла Windows не крутит, как SendMessage
    у перетаскивания), а Tk во время обработчика Python их только запоминает — так же снимается рамка (strip_caption)."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        user = ctypes.WinDLL("user32")
        user.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                      ctypes.c_int, ctypes.c_uint]
        user.SetWindowPos.restype = wintypes.BOOL
        flags = SWP_NOZORDER | SWP_NOACTIVATE
        if width is None or height is None:
            flags |= SWP_NOSIZE
            width = height = 0
        if x is None or y is None:
            flags |= SWP_NOMOVE
            x = y = 0
        return bool(user.SetWindowPos(hwnd, None, int(x), int(y), int(width), int(height), flags))
    except Exception:
        return False


def cloak(hwnd, on=True):
    """Спрятать окно «под плащ» (DWMWA_CLOAK) или снять его. Окно под плащом для Windows видимое — его элементы
    рисуются как обычно, — но на экран не выводится. Так окно программы появляется уже нарисованным (сессия 11б), без
    прозрачности -alpha: её Tk не снимает никогда, и окно навсегда оставалось «полупрозрачным» (WS_EX_LAYERED) —
    такое окно Windows перерисовывает медленнее. True — получилось; False — не Windows или Windows 7."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        set_attribute = ctypes.WinDLL("dwmapi").DwmSetWindowAttribute
        set_attribute.argtypes = [wintypes.HWND, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
        set_attribute.restype = ctypes.c_long
        value = ctypes.c_int(1 if on else 0)
        return set_attribute(hwnd, DWMWA_CLOAK, ctypes.byref(value), ctypes.sizeof(value)) == 0
    except Exception:
        return False


TK_FRAME_CLASS = "TkTopLevel"   # класс рамки окна Tk в Windows (TK_WIN_TOPLEVEL_CLASS_NAME в исходниках Tk)


def frame_hwnd(window):
    """Номер рамки окна (то, что видит Windows): родитель внутреннего окна Tk, как делает CustomTkinter.
    Только если это правда рамка Tk (класс TkTopLevel): пока окно ни разу не показывали, рамки у него ещё нет, и
    родитель внутреннего окна — рабочий стол Windows; снимать заголовок и скруглять углы надо не ему (сессия 11б).
    Вне Windows, без рамки и при ошибке — None."""
    if not windows_available():
        return None
    try:
        import ctypes
        from ctypes import wintypes
        user = ctypes.WinDLL("user32")
        user.GetParent.argtypes = [wintypes.HWND]
        user.GetParent.restype = wintypes.HWND
        user.GetClassNameW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        user.GetClassNameW.restype = ctypes.c_int
        parent = user.GetParent(window.winfo_id())
        if not parent:
            return None
        name = ctypes.create_unicode_buffer(64)
        user.GetClassNameW(parent, name, 64)
        return parent if name.value == TK_FRAME_CLASS else None
    except Exception:
        return None


def dark_title(hwnd):
    """Тёмный заголовок окна. Сначала атрибут 20 (Windows 10 20H1 и новее), не вышло — 19. True — получилось."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        set_attribute = ctypes.WinDLL("dwmapi").DwmSetWindowAttribute
        set_attribute.argtypes = [wintypes.HWND, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
        set_attribute.restype = ctypes.c_long
        value = ctypes.c_int(1)
        for attribute in (DWMWA_USE_IMMERSIVE_DARK_MODE, DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1):
            if set_attribute(hwnd, attribute, ctypes.byref(value), ctypes.sizeof(value)) == 0:
                return True
    except Exception:
        pass
    return False


def paint_title_dark(window):
    """Покрасить заголовок окна Tk в тёмный. Звать один раз после показа окна. Ошибки не бросает."""
    return dark_title(frame_hwnd(window))


def captionless_style(style):
    """Стиль окна без заголовка и рамки; системное меню и «свернуть» остаются (панель задач, Alt+F4)."""
    return (style & ~(WS_CAPTION | WS_THICKFRAME)) | WS_SYSMENU | WS_MINIMIZEBOX


def flat_ex_style(ex_style):
    """Расширенный стиль окна без объёмных рамок (WS_EX_DLGMODALFRAME и других): остальное как было."""
    return ex_style & ~EDGE_EX_STYLES


def _signed(value):
    return value - (1 << 32) if value >= (1 << 31) else value


def strip_caption(hwnd):
    """Убрать у окна заголовок, рамку и объёмные края. Стиль уже такой, как нужно, — ничего не делает (иначе окно
    перерисовывалось бы). Возвращает True, если стиль поменяли."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        user = ctypes.WinDLL("user32", use_last_error=True)
        user.GetWindowLongW.argtypes = [wintypes.HWND, ctypes.c_int]
        user.GetWindowLongW.restype = ctypes.c_long
        user.SetWindowLongW.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_long]
        user.SetWindowLongW.restype = ctypes.c_long
        user.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                      ctypes.c_int, ctypes.c_uint]
        user.SetWindowPos.restype = wintypes.BOOL
        old = user.GetWindowLongW(hwnd, GWL_STYLE) & 0xFFFFFFFF
        old_ex = user.GetWindowLongW(hwnd, GWL_EXSTYLE) & 0xFFFFFFFF
        new, new_ex = captionless_style(old), flat_ex_style(old_ex)
        if new == old and new_ex == old_ex:
            return False
        if new != old:
            user.SetWindowLongW(hwnd, GWL_STYLE, _signed(new))
        if new_ex != old_ex:
            user.SetWindowLongW(hwnd, GWL_EXSTYLE, _signed(new_ex))
        user.SetWindowPos(hwnd, None, 0, 0, 0, 0, SWP_FRAME_ONLY)
        return True
    except Exception:
        return False


DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWCP_DONOTROUND = 1
DWMWCP_ROUND = 2


def round_corners(hwnd, on=True):
    """Скруглить углы окна без рамки средствами Windows 11 (DwmSetWindowAttribute 33). True — получилось;
    False — не Windows или Windows 10 (там атрибута нет): тогда углы режет region_corners."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        set_attribute = ctypes.WinDLL("dwmapi").DwmSetWindowAttribute
        set_attribute.argtypes = [wintypes.HWND, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
        set_attribute.restype = ctypes.c_long
        value = ctypes.c_int(DWMWCP_ROUND if on else DWMWCP_DONOTROUND)
        return set_attribute(hwnd, DWMWA_WINDOW_CORNER_PREFERENCE, ctypes.byref(value), ctypes.sizeof(value)) == 0
    except Exception:
        return False


DWMWA_BORDER_COLOR = 34


def colorref(color):
    """'#RRGGBB' → число COLORREF Windows (0x00BBGGRR)."""
    color = color.lstrip("#")
    return int(color[4:6] + color[2:4] + color[0:2], 16)


def border_color(hwnd, color):
    """Цвет тонкой рамки, которую Windows 11 рисует вокруг окна со скруглёнными углами (по умолчанию белая или цвета
    акцента — это и была «толстая белая обводка»). True — получилось; False — не Windows 11: там рамки нет."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        set_attribute = ctypes.WinDLL("dwmapi").DwmSetWindowAttribute
        set_attribute.argtypes = [wintypes.HWND, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
        set_attribute.restype = ctypes.c_long
        value = ctypes.c_uint(colorref(color))
        return set_attribute(hwnd, DWMWA_BORDER_COLOR, ctypes.byref(value), ctypes.sizeof(value)) == 0
    except Exception:
        return False


def region_corners(hwnd, width, height, radius):
    """Запасной способ для Windows 10: вырезать окну скруглённую область. radius = 0 — вернуть прямоугольное окно
    (развёрнутое на весь экран). Размеры и радиус — в настоящих пикселях."""
    if not windows_available() or not hwnd:
        return False
    try:
        import ctypes
        from ctypes import wintypes
        gdi, user = ctypes.WinDLL("gdi32"), ctypes.WinDLL("user32")
        user.SetWindowRgn.argtypes = [wintypes.HWND, wintypes.HRGN, wintypes.BOOL]
        gdi.CreateRoundRectRgn.argtypes = [ctypes.c_int] * 6
        gdi.CreateRoundRectRgn.restype = wintypes.HRGN
        if radius <= 0:
            return bool(user.SetWindowRgn(hwnd, None, True))
        region = gdi.CreateRoundRectRgn(0, 0, width + 1, height + 1, radius * 2, radius * 2)
        return bool(user.SetWindowRgn(hwnd, region, True))   # область после этого принадлежит Windows
    except Exception:
        return False

