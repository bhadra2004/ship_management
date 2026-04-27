#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

# Load ship data from fixture
python manage.py loaddata management/fixtures/ships.json --verbosity=2

# Create superuser if DJANGO_ADMIN_PASSWORD is set
if [ -n "$DJANGO_ADMIN_PASSWORD" ]; then
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', '$DJANGO_ADMIN_PASSWORD')" | python manage.py shell
fi