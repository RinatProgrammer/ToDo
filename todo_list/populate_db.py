import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import MyModel

MyModel.objects.create(field1='value1', field2='value2')
MyModel.objects.create(field1='value3', field2='value4')

print("Data loaded successfully")
