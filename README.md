# Install pip
> python3 -m pip install --user pygame
> python3 -m pip install --user matplotlib
> python3 -m pip install --user plotly
> python3 -m pip install --user requests
> python3 -m venv ll_env
### Linux/Mac OS
> source ll_env/bin/activate
>### Windows
> ll_env/Scripts/activate.bat
### Install Django inside activated env
> pip install django
>### Creating a Project in Django
> django-admin startproject learning_log
### Create the Database
> python manage.py migrate
### Viewing the Project
> python manage.py runserver
# Starting an app inside a Django project
> python manage.py startapp learning_logs
# Make migrations for app
> python manage.py makemigrations learning_logs
> python manage.py migrate
# Setting up a Superuser
> python manage.py createsuperuser