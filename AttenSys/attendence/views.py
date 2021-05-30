from django.db.models.base import ModelState
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from . import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required
#TEMP
#@login_required(login_url='http://localhost:8000/')
def admin(request):
    userData=models.UserDetail.objects.all()
    return render(request,'attendence/staff.html',{'userData':userData})
#HOME PAGE
def home(request):
    form=forms.comlaint()
    return render(request,'attendence/home.html',{'form':form})

#LOGIN FORM
def sign_in(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            passw=form.cleaned_data['password']
            user=authenticate(request,username=uname,password=passw)
            if user:
                login(request,user)
                if user.is_superuser:
                    return render(request,'attendence/adminpage.html',{'data':request.user})
                else:
                    data=models.UserDetail.objects.get(user=request.user.id)
                    DATE=datetime.datetime.today()
                    return render(request,'attendence/staff.html',{'data':data,'date':DATE})
            else:
                return render(request,'attendence/sign_in_form.html',{'form':form})
    else:
        form=AuthenticationForm()
    return render(request,'attendence/sign_in_form.html',{'form':form})

#Add User
@login_required(login_url='http://localhost:8000/')
def AddUser(request):
    if(request.method=='GET'):
        user=UserCreationForm()
        return render(request,'attendence/admin_operation.html',{'data':request.user,'form':user})
    else:
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            detailForm=forms.userForm()
            return render(request,'attendence/addMoreUser.html',{'form':detailForm,'data':request.user,'uname':fm.cleaned_data['username']})
        else:
            return render(request,'attendence/admin_operation.html',{'form':fm,'data':request.user})

@login_required(login_url='http://localhost:8000/')
def AddMoreUser(request):
    if request.method=='POST':
        fm=forms.userForm(request.POST)
        if fm.is_valid():
            userData=models.UserDetail()
            Man=User.objects.get(username=request.GET['name'])
            userData.fullname=fm.cleaned_data['fullname']
            userData.joining=fm.cleaned_data['joining']
            userData.emp_id=fm.cleaned_data['emp_id']
            userData.desigination=fm.cleaned_data['desigination']
            userData.department=fm.cleaned_data['department']
            userData.user=Man
            userData.save()
            messages.success(request,"User Registration Successfull")
            return render(request,'attendence/addMoreUser.html',{'form':fm,'data':request.user})
 
@login_required(login_url='http://localhost:8000/')
def DisplayUser(request):
    userData=models.UserDetail.objects.all()
    return render(request,'attendence/removeUser.html',{'userData':userData})
@login_required(login_url='http://localhost:8000/')
def RemoveUser(request):
    userData=models.UserDetail.objects.get(id=request.GET['user'])
    User.objects.get(username=userData.user).delete()
    userData.delete()
    return HttpResponseRedirect('http://localhost:8000/Attendence/removeUser/')

@login_required(login_url='http://localhost:8000/')
def TakeAttendence(request):
    if request.method=='GET':
        tm=datetime.datetime.now()
        today=f"{tm.year}-{tm.month}-{tm.day}"
        attendenceModel=models.Attendence.objects.filter(date=today)
        if bool(attendenceModel)==False:
            attendence1=models.Attendence()
            userDetailmodel=models.UserDetail.objects.all()
            for i in userDetailmodel:
                attendence1.date=today
                attendence1.fullname=i.fullname
                attendence1.emp_id=i.emp_id
                attendence1.save()
        attendenceModel=models.Attendence.objects.all()
        formobj=[]
        for obj in attendenceModel:
            formobj.append(forms.AttendenceForm(initial={'emp_id':obj.emp_id,'fullname':obj.fullname,'date':obj.date,'PAL':obj.PAL,'timein':obj.timein,'timeout':obj.timeout,'workinghour':obj.workinghour}))
        return render(request,'attendence/takeattendence.html',{'userData':formobj})
@login_required(login_url='http://localhost:8000/')
def SaveAttendence(request):
    if(request.method=='POST'):
        data=forms.AttendenceForm(request.POST)
        fm=models.Attendence()
        #if data.is_valid():
        fm.emp_id=data.data['emp_id']
        fm.fullname=data.data['fullname']
        fm.PAL=data.data['PAL']
        fm.date=data.data['date']
        fm.timein=data.data['timein']
        fm.timeout=data.data['timeout']
        fm.workinghour=data.data['workinghour']
        fm.save()
        d=datetime.datetime.today()
        messages.success(request,f"Saved at {d}")
        return render(request,'attendence/takeattendence.html')
    return render(request,'attendence/takeattendence.html')

@login_required(login_url='http://localhost:8000/')
def DataEdit(request):
    if request.method=='GET':
        return render(request,'attendence/dataEdit.html',{'check':True})
    elif request.method=='POST':
        data=models.UserDetail.objects.get(emp_id=request.POST['un'])
        form=forms.userForm({'emp_id':data.emp_id,'fullname':data.fullname,'department':data.department,'desigination':data.desigination,'joining':data.joining})
        return render(request,'attendence/dataEdit.html',{'check':False,'check2':True,'form':form})

@login_required(login_url='http://localhost:8000/')
def SaveDataEdit(request):
    if request.method=='POST':
        form=forms.userForm(request.POST)
        emp=request.POST['fullname']
        dataForm=models.UserDetail()
        if form.is_valid():
            dataForm.fullname=form.cleaned_data['fullname']
            dataForm.emp_id=form.cleaned_data['emp_id']
            dataForm.joining=form.cleaned_data['joining']
            dataForm.desigination=form.cleaned_data['desigination']
            dataForm.department=form.cleaned_data['department']
            dataForm.save()
            messages.success(request,'Empoyees Updation Succssfully')
            return render(request,'attendence/dataEdit.html',{'check':False,'check2':True,'form':form})

@login_required(login_url='http://localhost:8000/')
def summary(request):
    data=models.Attendence.objects.all()
    return render(request,'attendence/summary.html',{'data':data})
@login_required(login_url='http://localhost:8000/')
def complaint(request):
    data=models.complaints.objects.all()
    return render(request,'attendence/coplaints.html',{'data':data})
def complaintForm(request):
    fm=forms.comlaint(request.POST)
    if fm.is_valid():
        fm.save()
        messages.success(request,'Complaint Submitted')
        return render(request,'attendence/home.html',{'form':fm})
    return render(request,'attendence/home.html',{'form':fm})
@login_required(login_url='http://localhost:8000/')
def UserLogOut(request):
    logout(request)
    fm=forms.comlaint(request.POST)
    return render(request,'attendence/home.html',{'form':fm})
