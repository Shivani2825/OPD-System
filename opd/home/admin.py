from django.contrib import admin

from .models import Doctor, Patient
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['id','name','speciality']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','doctor','name','age']



