@echo off
:loop
echo Lancement de main.py...
python main.py
if %errorlevel% neq 0 (
    echo Le programme a plante. Relancement dans 5 secondes...
    timeout /t 5 /nobreak
    goto loop
)
echo Le programme s'est termine avec succes.
pause
