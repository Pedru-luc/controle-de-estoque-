@echo off
chcp 65001 >nul
cls

echo ╔════════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                                ║
echo ║                    🚀 SISTEMA DE CONTROLE DE ESTOQUE 🚀                       ║
echo ║                                                                                ║
echo ╚════════════════════════════════════════════════════════════════════════════════╝

echo.
echo 📋 Verificando dependências...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Flask não está instalado!
    echo 📦 Instalando dependências...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Erro ao instalar dependências!
        pause
        exit /b 1
    )
    echo ✅ Dependências instaladas com sucesso!
) else (
    echo ✅ Dependências já estão instaladas!
)

echo.
echo 🚀 Iniciando servidor Flask...
echo.
echo 📌 O servidor está rodando em: http://localhost:5000
echo 📝 Abra o arquivo 'index.html' no navegador para acessar a interface
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

python app.py

pause
