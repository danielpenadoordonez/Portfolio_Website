from django.shortcuts import render
from django.http import HttpRequest, Http404
from .services import PageServices
import json
import logging

API_SERVICE = PageServices()

#Home Page
def home_Page_View(request:HttpRequest, *args, **kwargs):
    return render(request, 'Pages/home.html', {})

#About Page
def about_View(request:HttpRequest, *args, **kwargs):
    data = None
    #Objects that the API requires
    objects = ['owner', 'degrees', 'certs', 'jobs']
    try:
        #Get the data from the API
        data = API_SERVICE.get_Owner_Info(objects=objects)
    except Http404:
        data = {'status' : '404'}
    except json.JSONDecodeError:
        data = {'status' : 'no data'}

    return render(request, 'Pages/about.html', data)

#Page with all projects
def all_Projects_View(request:HttpRequest, *args, **kwargs):
    data = None
    try:
        #Get the data from the API
        data = API_SERVICE.get_All_Projects()
    except Http404:
        data = {'status' : '404'}
    except json.JSONDecodeError:
        data = {'status' : 'no data'}
    return render(request, 'Pages/allProjects.html', data)

def project_View(request:HttpRequest, project:str, *args, **kwargs):
    data = None
    try:
        #Get the data from the API
        data = API_SERVICE.get_Project(project)
    except Http404:
        data = {'status' : '404'}
    except json.JSONDecodeError:
        data = {'status' : 'no data'}
    return render(request, 'Pages/project.html', data)
