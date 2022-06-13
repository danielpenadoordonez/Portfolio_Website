from email.policy import default
from django.db import models

# Create your models here.
class Owner(models.Model):
    idCode = models.CharField(max_length=12, unique=True, default=None)
    userName = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField()
    skills = models.JSONField(default=None)