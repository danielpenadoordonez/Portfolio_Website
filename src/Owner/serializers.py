from rest_framework import serializers
from .models import Owner, Degree, Certificate, Work_Experience

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = (
            'idCode',
            'name',
            'lastName',
            'email',
            'description',
            'skills',
            'github_Account',
            'linkedin_Profile'
        )

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = (
            'code',
            'title',
            'description',
            'institution',
            'file',
            'image',
            'owner'
        )

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            'code',
            'title',
            'description',
            'institution',
            'file',
            'image',
            'owner',
            'cert_Link'
        )

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Experience
        fields = (
            'code',
            'position',
            'company',
            'description',
            'start_Date',
            'quit_Date',
            'owner'
        )