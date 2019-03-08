# djangovue

Install python 3.x

Install Django 2.x

django-admin startproject djangovue


python3 manage.py runserver 8080

Change settings.py in the Django project

DATABASES = {
   # 'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   # }
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pythonProj',
        'USER': 'root',
        'PASSWORD': '00001134',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}


Create database ‘pythonProj’ in sqlworkbench


CREATE SCHEMA `pythonProj` ;


RUN:

python3 manage.py migrate

python3 manage.py createsuperuser

admin1
V0001134


python3 manage.py runserver 8081


pippip