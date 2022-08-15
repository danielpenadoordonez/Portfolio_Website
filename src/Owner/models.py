from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Owner(models.Model):
    idCode = models.CharField(max_length=12, unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField()
    skills = models.JSONField()
    github_Account = models.URLField()
    linkedin_Profile = models.URLField()

    def __str__(self) -> str:
        return f"{self.name} {self.lastName}"

class Degree(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=60)
    description = models.TextField()
    institution = models.CharField(max_length=60)
    file = models.FileField(upload_to="docs/degrees", max_length=100, blank=True)
    image = models.ImageField(upload_to='images/degrees', blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.title} at {self.institution}"

class Certificate(Degree):
    cert_Link = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.title} granted by {self.institution}"

class Work_Experience(models.Model):
    code = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    description = models.TextField()
    start_Date = models.DateField(auto_now=False)
    quit_Date = models.DateField(auto_now=False, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.position} at {self.company}"
