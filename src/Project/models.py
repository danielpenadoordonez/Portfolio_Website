from django.db import models

# Create your models here.
class Project(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    languages = models.ManyToManyField("Programming_Language")
    frameworks = models.ManyToManyField("Framework", blank=True)
    tools = models.ManyToManyField("Tool", blank=True)
    o_Systems = models.ManyToManyField("Operating_System")
    github_Link = models.URLField()

    def __str__(self) -> str:
        return self.name

class Technologies(models.Model):
    code = models.CharField(primary_key=True,max_length=15)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Programming_Language(Technologies):
    image = models.ImageField(upload_to='images/languages/', default=None)

class Framework(Technologies):
    version = models.CharField(max_length=20)

class Tool(Technologies):
    pass

class Operating_System(Technologies):
    pass

#Additional Models 
class Project_Images(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images/projects", default=None)

    def __str__(self) -> str:
        return self.title