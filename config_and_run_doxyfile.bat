@echo off

set "remotefile=.\ug_example\src\Ndigo_interface.h"
set "localfile=.\source\Ndigo_interface_DONT_USE.h"
set "search1=NDIGO_API "
set "replace1="

echo F | xcopy /f /y %remotefile% %localfile% > NUL

set "tempfile=.\source\tempfile.txt"
(for /f "delims=" %%i in (%localfile%) do (
    set "line=%%i"
    setlocal enabledelayedexpansion
    set "line=!line:%search1%=%replace1%!"
    echo(!line!
    endlocal
))>"%tempfile%"
del %localfile%
move %tempfile% %localfile% > NUL

doxygen

del %localfile%