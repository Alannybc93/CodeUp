#!/bin/bash
# setup.sh - Script de configuração do ambiente

echo "🚀 Configurando ambiente CodeUp..."

# Criar virtual environment
python -m venv venv

# Ativar no Linux/Mac
# source venv/bin/activate

# Ativar no Windows PowerShell
# .\venv\Scripts\Activate.ps1

echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🔄 Aplicando migrações..."
python manage.py migrate

echo "👤 Criando superusuário..."
python manage.py createsuperuser

echo "✅ Setup completo! Execute: python manage.py runserver"
