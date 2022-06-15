from django.contrib import admin
from .models import Owner, Degree, Certificate, Work_Experience

# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass

@admin.register(Work_Experience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass

