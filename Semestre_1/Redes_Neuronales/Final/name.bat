@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

rem Cambia al directorio donde está el script
cd /d "%~dp0"

rem === Renombrar archivos (en todas las subcarpetas) ===
for /r %%F in (*) do (
    set "oldname=%%~nxF"
    set "filepath=%%~dpF"
    call set "newname=%%oldname:ó=o%%"

    if not "!oldname!"=="!newname!" (
        echo [Archivo] Renombrando "!oldname!" → "!newname!"
        ren "%%F" "!newname!" >nul 2>&1
    )
)

rem === Renombrar carpetas (desde las más profundas hacia arriba) ===
for /f "delims=" %%D in ('dir /ad /b /s /o-n') do (
    set "folderpath=%%~dpD"
    set "foldername=%%~nxD"
    call set "newname=%%foldername:ó=o%%"

    if not "!foldername!"=="!newname!" (
        echo [Carpeta] Renombrando "!foldername!" → "!newname!"
        pushd "%%~dpD"
        ren "%%~nxD" "!newname!" >nul 2>&1
        popd
    )
)

endlocal
pause
