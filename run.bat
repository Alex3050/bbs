@echo off
python manage.py runserver_plus --cert server.crt 127.0.0.1:8000
exit