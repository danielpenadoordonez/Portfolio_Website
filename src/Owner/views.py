from django.shortcuts import render
from django.http import HttpRequest

#Home Page
def home_Page_View(request:HttpRequest, *args, **kwargs):
    return render(request, 'Owner/home.html', {})