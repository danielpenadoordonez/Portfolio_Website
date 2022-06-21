from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
#from .forms import OwnerForm
from .models import Owner, Degree, Certificate, Work_Experience
from .serializers import OwnerSerializer, DegreeSerializer, CertificateSerializer, WorkExperienceSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# class OwnerViewSet(viewsets.ModelViewSet):
#     queryset = Owner.objects.all()
#     serializer_class = OwnerSerializer

@api_view(['GET'])
def owner_Api_View(request:HttpRequest):
    if request.method == "GET":
        owner = Owner.objects.all()
        serializer = OwnerSerializer(owner, many=True)
        #return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False, status=200)

@api_view(['GET'])
def degree_Api_View(request:HttpRequest):
    if request.method == "GET":
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        #return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False, status=200)

@api_view(['GET'])
def cert_Api_View(request:HttpRequest):
    if request.method == "GET":
        certs = Certificate.objects.all()
        serializer = CertificateSerializer(certs, many=True)
        #return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False, status=200)

@api_view(['GET'])
def work_Api_View(request:HttpRequest):
    if request.method == "GET":
        works = Work_Experience.objects.all()
        serializer = WorkExperienceSerializer(works, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
