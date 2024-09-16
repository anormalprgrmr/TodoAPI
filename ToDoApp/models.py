from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
class CustomUser(AbstractUser):
    TelID = models.CharField(max_length=20)

class Todo(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    todoName = models.CharField(max_length=50)
    todoDescription = models.TextField()
    isDone = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
