from django.db import models

# Create your models here.
class Owner(models.Model):
    userName = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50)
    skills:list = list()