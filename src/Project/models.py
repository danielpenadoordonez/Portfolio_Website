from django.db import models

# Create your models here.
class Project(models.Model):
    code = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=80)
    date_Registered = models.DateField(auto_now=True)
    description = models.TextField()
    languages = models.ManyToManyField("Programming_Language")
    frameworks = models.ManyToManyField("Framework", blank=True)
    tools = models.ManyToManyField("Tool", blank=True)
    github_Link = models.URLField()
    main_Image = models.ImageField(upload_to='images/languages/', default=None, null=True)

    def __str__(self) -> str:
        return self.name

class Technologies(models.Model):
    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/languages/', default=None, blank=True)
    version = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Programming_Language(Technologies):
    pass

class Framework(Technologies):
    pass

class Tool(Technologies):
    pass

#Additional Models 
class Project_Images(models.Model):
    imgCode = models.CharField(max_length=12, unique=True, primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/projects", default=None, blank=False)

    def __str__(self) -> str:
        return self.title