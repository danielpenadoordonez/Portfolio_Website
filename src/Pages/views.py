from django.shortcuts import render
from django.http import HttpRequest

#Home Page
def home_Page_View(request:HttpRequest, *args, **kwargs):
    return render(request, 'Pages/home.html', {})

def about_View(request:HttpRequest, *args, **kwargs):
    context = {}
    return render(request, 'Pages/about.html', context)
