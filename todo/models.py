from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    completed = models.BooleanField(default=False)