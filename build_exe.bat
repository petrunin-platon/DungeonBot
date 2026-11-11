@echo off
:: Сборка .exe (задача 15, шаг 9). Готовая программа — dist\HeroWarsBot\HeroWarsBot.exe, открывает новое окно.
:: Запускать из папки проекта двойным щелчком. Перед сборкой нужен свежий assets_db.py: python pack_assets.py.
chcp 65001 >nul
cd /d "%~dp0"

echo [СБОРКА] Сборка HeroWarsBot.exe...

IF NOT EXIST "venv\Scripts\activate.bat" (
    echo [СБОРКА] Нет папки venv. Сначала один раз запустите start.bat: он поставит библиотеки.
    pause
    exit /b 1
)
call venv\Scripts\activate.bat

IF NOT EXIST "assets_db.py" (
    echo [СБОРКА] Нет файла assets_db.py: без него в .exe не будет картинок бота.
    echo [СБОРКА] Соберите его командой: python pack_assets.py
    echo [СБОРКА] Потом запустите build_exe.bat снова.
    pause
    exit /b 1
)

python -m PyInstaller --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [СБОРКА] PyInstaller не установлен. Ставлю библиотеки для сборки из requirements-build.txt...
    pip install -r requirements-build.txt
)

:: Сборка стирает папку dist\HeroWarsBot. Ваши настройки и данные из неё (profile.yml, bot_data) на время
:: сборки переносятся в build_keep и потом возвращаются на место.
set OUT=dist\HeroWarsBot
set KEEP=build_keep
IF EXIST "%KEEP%" (
    echo [СБОРКА] Осталась папка %KEEP% от прошлой сборки: в ней ваши profile.yml и bot_data.
    echo [СБОРКА] Перенесите их в %OUT% или удалите %KEEP%, потом запустите build_exe.bat снова.
    pause
    exit /b 1
)
IF EXIST "%OUT%\profile.yml" (
    mkdir "%KEEP%" 2>nul
    move "%OUT%\profile.yml" "%KEEP%\" >nul
)
IF EXIST "%OUT%\bot_data" (
    mkdir "%KEEP%" 2>nul
    move "%OUT%\bot_data" "%KEEP%\" >nul
)

:: Рядом с HeroWarsBot.exe — только папка _internal (библиотеки, руководство, иконки); profile.yml и bot_data
:: программа создаёт рядом с .exe сама. Руководство ищется в _internal (ui/guide_renderer.guide_dir).
:: Раньше было --contents-directory . — все ~50 файлов рядом с .exe (27.10.2026: так понятнее игрокам, ваша просьба).
:: ui\icons — иконки окна, guide — руководство (шаг 10, с картинками).
:: Папку assets в .exe НЕ кладём (09.11.2026): все картинки бота и картинки титанов для окна (ключи icons/имя.png)
:: уже лежат в assets_db.py, а папки assets на ПК после pack_assets.py может и не быть - тогда сборка падала.
:: --hidden-import assets_db - сборщик точно возьмёт assets_db.py, даже если найти его в коде сам не сумеет.
:: PIL._tkinter_finder — без него картинки в окне не рисуются (проверка шага 9: окно падало на первой иконке).
python -m PyInstaller --noconfirm --clean --onedir --windowed --name "HeroWarsBot" ^
    --hidden-import main --hidden-import assets_db --hidden-import PIL._tkinter_finder ^
    --add-data "guide;guide" ^
    --add-data "ui/icons;ui/icons" ^
    gui.py
set BUILD_ERROR=%ERRORLEVEL%

:: Правила по умолчанию (rules\) — рядом с .exe, если папка есть: бот копирует их в bot_data\rules при первом запуске
IF "%BUILD_ERROR%"=="0" IF EXIST "rules" xcopy /E /I /Y "rules" "%OUT%\rules" >nul

IF NOT EXIST "%OUT%" mkdir "%OUT%"
IF EXIST "%KEEP%\profile.yml" move "%KEEP%\profile.yml" "%OUT%\" >nul
IF EXIST "%KEEP%\bot_data" move "%KEEP%\bot_data" "%OUT%\" >nul
rmdir "%KEEP%" 2>nul

echo.
IF "%BUILD_ERROR%"=="0" (
    echo [СБОРКА] Готово: %OUT%\HeroWarsBot.exe
) ELSE (
    echo [СБОРКА] Сборка не удалась, сообщение об ошибке — выше.
)
pause
