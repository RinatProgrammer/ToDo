import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

application = get_wsgi_application()

print("Application:", application)  # Add this line