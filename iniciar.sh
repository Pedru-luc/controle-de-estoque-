#!/bin/bash

clear

echo "╔════════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                                ║"
echo "║                    🚀 SISTEMA DE CONTROLE DE ESTOQUE 🚀                       ║"
echo "║                                                                                ║"
echo "╚════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "📋 Verificando dependências..."

if ! python -c "import flask" 2>/dev/null; then
    echo "⚠️  Flask não está instalado!"
    echo "📦 Instalando dependências..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Erro ao instalar dependências!"
        exit 1
    fi
    echo "✅ Dependências instaladas com sucesso!"
else
    echo "✅ Dependências já estão instaladas!"
fi

echo ""
echo "🚀 Iniciando servidor Flask..."
echo ""
echo "📌 O servidor está rodando em: http://localhost:5000"
echo "📝 Abra o arquivo 'index.html' no navegador para acessar a interface"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

python app.py
