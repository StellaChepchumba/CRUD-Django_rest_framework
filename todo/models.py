from django.db import models

class Todo(models.Model):
        title = models.CharField(max_length=255)
        description= models.TextField()
        deadline = models.DateTimeField()
        isCompleted= models.BooleanField(default=False)


# Create your models here.
