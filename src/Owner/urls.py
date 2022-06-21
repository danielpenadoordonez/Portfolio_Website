from django.urls import path, include
from .views import owner_Api_View, degree_Api_View, cert_Api_View, work_Api_View
from rest_framework import routers

# router = routers.DefaultRouter()
# #router.register(r'owner', owner_View)
# router.register(r'degree', DegreeViewSet)
# router.register(r'certs', CertificateViewSet)
# router.register(r'works', WorkExperienceViewSet)

#http://localhost:8000/api/owner/?format=json
#For viewing in JSON format

urlpatterns = [
    #path('', include(router.urls)),
    path('owner/', owner_Api_View),
    path('degrees/', degree_Api_View),
    path('certs/', cert_Api_View),
    path('works/', work_Api_View)
]