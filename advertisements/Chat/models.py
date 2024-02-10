from django.db import models
from core.models import User
# Create your models here.

class chat(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_chat=models.TextField()
    system_chat=models.TextField()

    