from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
#from .forms import OwnerForm
from .models import Owner, Degree, Certificate, Work_Experience
from .serializers import OwnerSerializer, DegreeSerializer, CertificateSerializer, WorkExperienceSerializer
from rest_framework import viewsets

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = Work_Experience.objects.all()
    serializer_class = WorkExperienceSerializer

