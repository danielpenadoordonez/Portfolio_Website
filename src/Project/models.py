from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    languages:list = list()
    frameworks:list = list()
    tools:list = list()
    o_Systems:list = list()

class Programming_Language(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class Framework(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class Tool(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class Operating_System(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()