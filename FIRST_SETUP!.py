
# Workshop_RoomsMgt

# ls
# cd env
# virtualenv -p python3 env
# (source activate)
# source env/bin/activate
# pip install django
# django-admin version
# (env) pm1990@pm1990-Lenovo-Z51-70:~/env/bin$ django-admin startproject coderslab .


# pdb.set_trace() - UZYWAĆ !!!
# source env/bin/activate

# psql -h hostname -U username -W -d databasename
#
# psql -h localhost -U postgres -W

# psql -h localhost -d football -U postgres -f football.sql   - import z sql do db.

# Migracja baz danch do Django:
# https://docs.djangoproject.com/en/1.11/howto/legacy-databases/
# https://docs.djangoproject.com/en/1.11/ref/django-admin/#inspectdb


# Podstawowe Komendy:
# pip install django
# django-admin version
# python -m django --version
# django-admin startproject / runserver / startapp / makemigrations / migrate
# django-admin startproject <nazwa-projektu> <ścieżka-do-projektu>   or django-admin startproject coderslab .
#
#
# python manage.py runserver or python manage.py runserver <numer-portu>
# python manage.py runserver <ip>:<port>
# python manage.py startapp <nazwa-aplikacji>  --> python manage.py startapp edu
#
# python manage.py migrate / makemigrations

# class Product(models.Model):
# name = models.CharField(max_length=64)
# content = models.TextField()
# score = models.SmallIntegerField()
# price = models.DecimalField(max_digits=5, decimal_places=2)
# wants_spam = models.BooleanField()
# available_from = models.DateTimeField()
# visits = models.IntegerField()
#
# (null=True/False)  & (default=0) & max_length=64
# LIGHTSABERS = (
#     (1, "Red"),
#     (2, "Blue"),
#     (3, "Green"),
#     (4, "Purple")
# )
# saber = models.IntegerField(choices=LIGHTSABERS)
#
# (db_index=True) - to pole będzie indexem bazy danych
# primary_key=True - klucz główny
# python manage.py shell



