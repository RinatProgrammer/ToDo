from django.core.management.base import BaseCommand
from myapp.models import MyModel

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        MyModel.objects.create(field1='value1', field2='value2')
        MyModel.objects.create(field1='value3', field2='value4')
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
