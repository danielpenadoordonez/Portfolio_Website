from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
from .models import Project, Technologies, Programming_Language, Framework, Tool, Project_Images
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer, TechnologySerializer, ProjectImagesSerializer


class ProjectAPIView(APIView):
    """
    API for interacting with projects
    """

    def get(self, request, format=None):
        #Query parameters
        params:dict = request.query_params
        if "format" not in params.keys():
            return JsonResponse({"detail" : "format required"})

        #Check if projects are being requested by technology
        if "tech" in params.keys():
            tech_Requested = params.get("tech")

        #Check if a specific project is requested
        if "proj" in params.keys():
            proj_Id = params.get("proj")
            project_Requested = Project.objects.get(code=proj_Id)
            projectSerializer = ProjectSerializer(project_Requested)
            return Response(projectSerializer.data, status=200)

        projects = Project.objects.all()
        projectSerializer = ProjectSerializer(projects, many=True)
        return Response(projectSerializer.data, status=200)


class TechnologyAPIView(APIView):
    """
    API for interacting with Technology objects
    """

    def get(self, request, format=None):
        #Query parameters
        params:dict = request.query_params
        if "format" not in params.keys():
            return JsonResponse({"detail" : "format required"})

        technologies = Technologies.objects.all()
        techSerializer = TechnologySerializer(technologies, many=True)
        return Response(techSerializer.data, status=200)


class ProjectImagesAPIView(APIView):
    """
    API for interacting with Technology objects
    """

    def get(self, request, format=None):
        #Query parameters
        params:dict = request.query_params
        if "format" not in params.keys():
            return JsonResponse({"detail" : "format required"})
        #Validate that the proj parameter is specified
        if "proj" not in params.keys():
            return JsonResponse({"detail" : "no project specified"})

        #Get the id for the project
        projectId = params.get("proj")
        #Get the project from the DB
        #projectObj = Project.objects.get(code=projectId)
        #Get the images for the project
        images = Project_Images.objects.filter(project=projectId)
        imgSerializer = ProjectImagesSerializer(images, many=True)
        return Response(imgSerializer.data, status=200)
