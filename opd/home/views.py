from django.shortcuts import render
from .models import Doctor,Patient
from django.contrib import messages

def index(request):
    data=Doctor.objects.all()
    return render(request,'index.html',{'data':data})

def book(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        did=request.POST['doctor']
        if Patient.objects.filter(doctor_id=did).exists():
            messages.error(request,"Already Exists")
            data=Doctor.objects.all()
            return render(request,'index.html',{'data':data})
        else:
            doctor=Doctor.objects.get(id=did)
            appoint=Patient.objects.create(name=name,age=age,doctor=doctor)
            appoint.save()
            messages.success(request,"Appointment Added")
            data=Doctor.objects.all()
            return render(request,'index.html',{'data':data})
    else:
        data=Doctor.objects.all()
        return render(request,'index.html',{'data':data})