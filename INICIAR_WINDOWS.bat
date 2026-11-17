@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Instalando dependencias da interface web (se necessario)...
py -m pip install -r requirements.txt
if errorlevel 1 (
    echo Falha na instalacao. Verifique se Python e py estao disponiveis.
    pause
    exit /b 1
)
py -m streamlit run app.py
pause
