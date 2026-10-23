@echo off
setlocal
title Sentinel Threat Intelligence Dashboard

where py >nul 2>&1
if errorlevel 1 goto :python_missing

py -3 -c "import sys" >nul 2>&1
if errorlevel 1 goto :python_missing

if not exist ".venv\Scripts\python.exe" (
    echo Creating a local Python environment...
    py -3 -m venv .venv
    if errorlevel 1 goto :setup_failed
)

call .venv\Scripts\activate.bat
echo Installing or checking required packages...
python -m pip install --disable-pip-version-check -r requirements.txt
if errorlevel 1 goto :setup_failed

echo.
echo Starting Sentinel at http://127.0.0.1:5000
start "" "http://127.0.0.1:5000"
python app.py
goto :end

:python_missing
echo.
echo Python is not installed correctly on this computer.
echo Install Python 3.10 or newer from https://www.python.org/downloads/
echo During installation, select "Add Python to PATH", then run this file again.
goto :end

:setup_failed
echo.
echo Setup failed. Check your Python installation and internet connection, then run this file again.

:end
pause
