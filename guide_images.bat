@echo off
:: Какие скриншоты нужны руководству и какие уже лежат в guide\images\ru и guide\images\en (guide_images.py, шаг 10.16).
:: Запускать из папки проекта двойным щелчком. Другие языки: guide_images.bat RU EN DE
chcp 65001 >nul
cd /d "%~dp0"

IF EXIST "venv\Scripts\activate.bat" call venv\Scripts\activate.bat

python guide_images.py %*
pause
