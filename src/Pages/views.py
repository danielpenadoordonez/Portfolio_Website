from django.shortcuts import render
from django.http import HttpRequest, Http404
from .services import PageServices
import json

API_SERVICE = PageServices()

#Home Page
def home_Page_View(request:HttpRequest, *args, **kwargs):
    return render(request, 'Pages/home.html', {})

def about_View(request:HttpRequest, *args, **kwargs):
    data = None
    #Objects that the API requires
    objects = ['owner', 'degrees', 'certs', 'jobs']
    try:
        #Get the data from the API
        data = API_SERVICE.get_Owner_Info(objects=objects)
    except Http404:
        data = {'status', '404'}

    #context = data
    return render(request, 'Pages/about.html', data)
