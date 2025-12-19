# run_fix.py - Script para corrigir tudo automaticamente
import os
import sys

# Adiciona o diretório ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurações mínimas para rodar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeup.settings')

import django
django.setup()

from django.conf import settings

print("=" * 60)
print("CONFIGURAÇÃO ATUAL DO DJANGO")
print("=" * 60)
print(f"DEBUG: {settings.DEBUG}")
print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
print(f"INSTALLED_APPS: {settings.INSTALLED_APPS}")
print("=" * 60)

# Corrigir settings se necessário
settings_file = os.path.join(os.path.dirname(__file__), 'codeup', 'settings.py')

with open(settings_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Garantir que DEBUG seja True
if 'DEBUG = False' in content:
    content = content.replace('DEBUG = False', 'DEBUG = True')
    print("✅ DEBUG corrigido para True")
elif 'DEBUG=False' in content:
    content = content.replace('DEBUG=False', 'DEBUG=True')
    print("✅ DEBUG corrigido para True")

# Salvar correções
with open(settings_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Settings.py corrigido!")
print("\nAgora execute:")
print("python manage.py runserver")