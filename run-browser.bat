@echo off
REM Quantum Browser Launcher
REM Launch the standalone Quantum Browser application

echo.
echo ================================================
echo    QUANTUM BROWSER
echo    Starting application...
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo Please run install-dependencies.bat first.
    echo.
    pause
    exit /b 1
)

REM Get the directory where this batch file is located
set BROWSER_DIR=%~dp0

REM Launch the browser
echo Launching Quantum Browser...
echo.

python "%BROWSER_DIR%quantum_browser.py"

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to launch browser!
    echo.
    echo Make sure you have installed dependencies by running:
    echo install-dependencies.bat
    echo.
    pause
    exit /b 1
)
