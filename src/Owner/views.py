from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
#from .forms import OwnerForm
from .models import Owner, Degree, Certificate, Work_Experience
from .serializers import OwnerSerializer, DegreeSerializer, CertificateSerializer, WorkExperienceSerializer
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class OwnerAPIView(APIView):
    """
      API that displays the owner information
    """

    def get(self, request, format=None):
        #Dictionary with the query parameters and their values
        params:dict = request.query_params
        #Parameter validation
        if("owner_id" not in params.keys() or "format" not in params.keys()):
            return JsonResponse({"detail" : "params required"}, safe=False, status=404)

        #Get the owner id value from the query parameter and validate that it is correct
        owner_ID = params.get("owner_id")
        if owner_ID != "118200576":
            raise Http404

        owner = Owner.objects.get(idCode=owner_ID)
        ownerSerializer = OwnerSerializer(owner)
        return Response(ownerSerializer.data, status=200)


class DegreeAPIView(APIView):
    """
       API that diplays all the degrees with their information
    """

    def get(self, request, format=None):
        #Query parameters
        params:dict = request.query_params
        if("format" not in params.keys()):
            return JsonResponse({"detail" : "params required"}, safe=False, status=404)

        degrees = Degree.objects.all()
        degreeSerializer = DegreeSerializer(degrees, many=True)
        return Response(degreeSerializer.data, status=200)


class CertificateAPIView(APIView):
    """
      API that displays Certificates
    """

    def get(self, request, format=None):
        #Query parameters
        params:dict = request.query_params
        if("format" not in params.keys()):
            return JsonResponse({"detail" : "params required"}, safe=False, status=404)

        certs = Certificate.objects.all()
        certSerializer = CertificateSerializer(certs, many=True)
        return Response(certSerializer.data, status=200)


class WorkAPIView(APIView):
    """
    API that displays job information
    """
    
    def get(self, request, format=None):
        #Query parameters
        params:dict = request.query_params
        if("format" not in params.keys()):
            return JsonResponse({"detail" : "params required"}, safe=False, status=404)

        jobs = Work_Experience.objects.all()
        jobsSerializer = WorkExperienceSerializer(jobs, many=True)
        return Response(jobsSerializer.data, status=200)
