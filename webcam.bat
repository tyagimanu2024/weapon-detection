@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
start "" cmd /c "python -m uvicorn app.main:app --reload"
timeout /t 3 /nobreak >nul
start "" "http://127.0.0.1:8000/webcam"