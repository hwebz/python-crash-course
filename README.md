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
### Starting an app inside a Django project
> python manage.py startapp learning_logs
### Make migrations for app
> python manage.py makemigrations learning_logs
> python manage.py migrate
### Setting up a Superuser
> python manage.py createsuperuser
### Install bootstrap4 for django project
> pip install django-bootstrap4

### The Django Shell
> python3 manage.py shell
> from learning_logs.models import Topic
> Topic.objects.all()
> topics = Topic.objects.all()
> for topic in topics:
> print(topic.id, topic)
> t = Topic.objects.get(id=1)
> t.text
> t.entry_set.all()

## Deploy django web app to Heroku
### Psycopg package for manage database on Heroku
> pip install psycopg2==2.7.*
### django-heroku handle entire configuration our app needs to run properly on Heroku
> pip install django-heroku
### gunicorn pakcage provides a server capable of serving apps in a live env
> pip install gunicorn
### Create a requirements.txt file
> pip freeze > requirements.txt
### Create a runtime.txt file to store python version in 1 line
> python-3.6.9
### Making a Procfile to start process
> web: gunicorn learning_log.wsgi --log-file -