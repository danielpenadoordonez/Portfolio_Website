from django.urls import path, include
from .views import ProjectAPIView, TechnologyAPIView, ProjectImagesAPIView

urlpatterns = [
    path('projects/', ProjectAPIView.as_view(), name="project-list"),
    path('technologies/', TechnologyAPIView.as_view(), name="tech-list"),
    path('proj-images/', ProjectImagesAPIView.as_view(), name="proj-images")
]