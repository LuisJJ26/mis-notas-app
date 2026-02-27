#!/usr/bin/env bash
# build.sh

echo "===== INICIANDO BUILD ====="
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones
python manage.py migrate

# Crear superusuario si no existe
echo "===== CREANDO SUPERUSUARIO ====="
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123cambiar')
    print('Superusuario creado exitosamente')
else:
    print('Superusuario ya existe')
EOF

echo "===== BUILD COMPLETADO ====="