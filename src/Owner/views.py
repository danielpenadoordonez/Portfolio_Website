from django.shortcuts import render
from django.http import HttpRequest
from .forms import OwnerForm

#Home Page
def home_Page_View(request:HttpRequest, *args, **kwargs):
    return render(request, 'Owner/home.html', {})

def about_View(request:HttpRequest, *args, **kwargs):
    return render(request, 'Owner/about.html', {})

def add_View(request:HttpRequest, *args, **kwargs):
    owner_Form = OwnerForm()
    if request.method() == "POST":
        if owner_Form.is_valid():
            pass
    context = {
        "owner_form" : owner_Form
    }
    return render(request, 'Owner/add.html', context)