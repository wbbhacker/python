@echo off

:a
echo Enter the image folder path:
set /p input= 
python getImg.py %input%

pause
goto a
