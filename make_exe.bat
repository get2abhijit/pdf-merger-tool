@echo off
setlocal

REM Usage: make_exe.bat your_script.py

if "%~1"=="" (
    echo Usage: make_exe.bat your_script.py
    exit /b 1
)

REM Ensure pip is available
python -m ensurepip

REM Install PyInstaller if not present
python -m pip install --upgrade pip
python -m pip install pyinstaller

REM Build the executable
pyinstaller --onefile "%~1"

echo.
echo Executable created in the dist folder.
echo.

endlocal