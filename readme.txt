Запуск приложения
=================
uwsgi --http :8000 --enable-threads --thunder-lock --wsgi-file main.py

или

gunicorn main:application
