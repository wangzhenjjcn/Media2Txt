@echo off

echo  install requirements ...
pip install -r %~dp0requirements.txt
echo install requirements finished!
echo  
echo to add PATH  ...
 
echo check PATH  ...
set "SCRIPT_DIR=%~dp0"
echo %PATH% | find /i "%SCRIPT_DIR%" > nul
if %errorlevel% equ 0 (
    echo exist!
) else (
    echo add...
    setx PATH "%PATH%;%SCRIPT_DIR%" /M
    echo added !
)

echo added PATH  
echo  
echo  
echo install finished
@pause
@pause
@pause
@pause
