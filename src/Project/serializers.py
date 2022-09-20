from rest_framework import serializers
from .models import Project, Technologies, Programming_Language, Framework, Tool, Project_Images

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'code',
            'name',
            'date_Registered',
            'description',
            'languages',
            'frameworks',
            'tools',
            'github_Link'
        )

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = (
            'code',
            'name',
            'description',
            'image',
            'version'
        )

class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Images
        fields = (
            'imgCode',
            'project',
            'title',
            'description',
            'image'
        )