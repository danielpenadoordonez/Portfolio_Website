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
      Displays the owner information
    """

    def get(self, request, format=None):
        #Dictionary with the query parameters and their values
        params:dict = request.query_params
        if("owner_id" not in params.keys() or "format" not in params.keys()):
            return JsonResponse({"detail" : "params required"}, safe=False, status=404)

        #Get the owner id value from the query parameter and validate that it is correct
        owner_ID = params.get("owner_id")
        if owner_ID != "118200576":
            raise Http404

        owner = Owner.objects.get(idCode=owner_ID)
        serializer = OwnerSerializer(owner)
        return Response(serializer.data, status=200)



@api_view(['GET'])
def degree_Api_View(request:HttpRequest):
    if request.method == "GET":
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        #return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False, status=200)
