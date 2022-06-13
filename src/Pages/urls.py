from django.urls import path
from .views import home_Page_View, about_View

urlpatterns = [
    path('', home_Page_View, name="home-page"),
    path('about/', about_View, name="about-page"),
    path('home/', home_Page_View, name="home-page")
]