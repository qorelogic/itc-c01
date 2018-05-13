#!/bin/bash

virtualenv --python=/usr/bin/python3 venv
. venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations users person movie
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

deactivate
