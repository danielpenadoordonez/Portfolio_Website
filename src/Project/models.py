from email.policy import default
from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    languages = models.ManyToManyField("Programming_Language")
    frameworks = models.ManyToManyField("Framework", blank=True)
    tools = models.ManyToManyField("Tool", blank=True)
    o_Systems = models.ManyToManyField("Operating_System")
    github_Link = models.URLField(default=None)

class Programming_Language(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default=None)

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

#Additional Models 
class Project_Images(models.Model):
    pass