from unicodedata import name
from django.urls import path
from .views import about_View, add_View

urlpatterns = [
    path('', about_View, name="about"),
    path('add/', add_View, name="add")
]