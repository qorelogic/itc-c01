#!/bin/bash

virtualenv --python=/usr/bin/python3 venv
. venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations todos users
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

deactivate
