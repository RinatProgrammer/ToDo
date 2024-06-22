# todo/apps.py
from django.apps import AppConfig
from django.db.models import BigAutoField

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
