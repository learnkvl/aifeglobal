#!/bin/bash

# Python setup
/usr/bin/python3.9 -m ensurepip --upgrade
/usr/bin/python3.9 -m pip install --upgrade pip
/usr/bin/python3.9 -m pip install -r requirements.txt

# Django setup
python3.9 manage.py collectstatic --noinput
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Create public directory and move static files into it
mkdir -p public/static
cp -r staticfiles/* public/static/
