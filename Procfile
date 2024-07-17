web: gunicorn chat_app.asgi:application --host 0.0.0.0 --port $PORT
web: python manage.py migrate && gunicorn chat_app.asgi