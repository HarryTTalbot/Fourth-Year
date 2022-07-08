#!/bin/sh
# Entrypoint for the Django Dockerfile
# NOTE: On Windows, make sure the line endings for this are in LF (otherwise the container won't be able to run this)
export KUMON_DEVELOPMENT=0

echo "Creating backend API migrations..."
python manage.py makemigrations backend_api

echo "Migrating database..."
python manage.py migrate

echo "Running server..."
python manage.py runserver '0.0.0.0:8000'
