from django.db import models
from django.contrib.auth.models import User

class complaints(models.Model):
    name=models.CharField(max_length=20)
    Eid=models.CharField(max_length=8)
    department=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    subject=models.CharField(max_length=200)
    comlaint=models.CharField(max_length=500)
class UserDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    fullname=models.CharField(max_length=20,null=True)
    emp_id=models.CharField(max_length=7,null=True)
    department=models.CharField(max_length=20,null=True)
    joining=models.DateField(null=True)
    desigination=models.CharField(max_length=15,null=True)
    date=models.DateField(null=True)
    PA=models.CharField(max_length=5,null=True)
    timein=models.CharField(max_length=10,null=True)
    timeout=models.CharField(max_length=10,null=True)
    workingHour=models.CharField(max_length=3,null=True)
    leave=models.CharField(max_length=10,null=True)
class Attendence(models.Model):
    emp_id=models.CharField(max_length=7,primary_key=True)
    fullname=models.CharField(max_length=20)
    date=models.DateField(null=True)
    PAL=models.CharField(max_length=10)
    timein=models.CharField(max_length=10,null=True)
    timeout=models.CharField(max_length=10,null=True)
    workinghour=models.CharField(max_length=10,null=True)