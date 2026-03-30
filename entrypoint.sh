#!/bin/sh

echo "等待数据库启动..."

while ! nc -z mall-db 3306; do
  sleep 1
done

echo "数据库已启动"
python manage.py makemigrations account
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn core.wsgi:application --bind 0.0.0.0:8000