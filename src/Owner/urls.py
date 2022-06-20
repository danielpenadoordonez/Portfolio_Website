from django.urls import path, include
from .views import OwnerViewSet, DegreeViewSet, CertificateViewSet, WorkExperienceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'owner', OwnerViewSet)
router.register(r'degree', DegreeViewSet)
router.register(r'certs', CertificateViewSet)
router.register(r'works', WorkExperienceViewSet)

#http://localhost:8000/api/owner/?format=json
#For viewing in JSON format

urlpatterns = [
    path('', include(router.urls)),
]