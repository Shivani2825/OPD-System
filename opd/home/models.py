from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=500)
    speciality=models.CharField(max_length=400)
    def __str__(self):
        return self.name+'-'+ self.speciality

    

class Patient(models.Model):
    doctor=models.OneToOneField(Doctor, on_delete=models.CASCADE)
    name=models.CharField(max_length=500,blank=True)
    age=models.PositiveBigIntegerField()

    def __str__(self):
        return self.name

    
    

