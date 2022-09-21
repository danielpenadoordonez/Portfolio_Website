from django.contrib import admin
from .models import Project, Technologies, Programming_Language, Framework, Tool, Project_Images

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Technologies)
class TechnologyAdmin(admin.ModelAdmin):
    pass

@admin.register(Programming_Language)
class ProgrammingLangAdmin(admin.ModelAdmin):
    pass

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass

@admin.register(Project_Images)
class ProjectImgAdmin(admin.ModelAdmin):
    pass
