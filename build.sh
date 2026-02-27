#!/usr/bin/env bash
# build.sh - Script para Render

echo "===== INICIANDO BUILD ====="
set -o errexit  # Salir si hay error

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones
python manage.py migrate

echo "===== BUILD COMPLETADO ====="