@echo off
REM Quantum Browser - Dependency Installer
REM This script installs the required Python packages

echo.
echo ================================================
echo    QUANTUM BROWSER - SETUP
echo    Installing dependencies...
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo Python found!
echo.

REM Get the directory where this batch file is located
set BROWSER_DIR=%~dp0

REM Install required packages
echo Installing required packages (PyQt5 and PyQtWebEngine)...
echo This may take a few minutes...
echo.

pip install -r "%BROWSER_DIR%requirements.txt"

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo.
    echo Try running this command manually:
    echo pip install PyQt5 PyQtWebEngine
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================
echo    Installation Complete!
echo ================================================
echo.
echo You can now run the browser with: run-browser.bat
echo.
pause
