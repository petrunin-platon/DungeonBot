@echo off
:: Перевод руководства guide\ru.md на другие языки окна программы через Gemini (translate_guide.py, шаг 10.16).
:: Запускать из папки проекта двойным щелчком: спросит, на какие языки перевести (Enter — на все).
:: Можно и сразу с языками из cmd: translate_guide.bat EN DE. Проверить готовые переводы без запросов: translate_guide.bat --check
chcp 65001 >nul
cd /d "%~dp0"

IF EXIST "venv\Scripts\activate.bat" call venv\Scripts\activate.bat

:: Двойной щелчок (языки не указаны) — спросить, какие языки перевести
set "LANGS=%*"
IF "%~1"=="" (
    echo [ПЕРЕВОД] Русское руководство guide\ru.md переведу на языки:
    echo     EN - английский     UK - украинский     KK - казахский      DE - немецкий
    echo     ES - испанский      FR - французский    PL - польский       PT - португальский
    echo     TR - турецкий       ZH - китайский      KO - корейский      JA - японский
    echo.
    set /p "LANGS=Какой язык перевести? Коды через пробел, например EN DE. Просто Enter - все языки: "
)

python -c "import google.genai" >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ПЕРЕВОД] Ставлю библиотеку google-genai для Gemini...
    pip install google-genai==2.33.0
)

:: Ключ Gemini спросит сам translate_guide.py: покажет сохранённые ключи (файл gemini_keys.txt) и даст вставить новый

python translate_guide.py %LANGS%
pause
