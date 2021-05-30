from django import forms
from django.forms import fields
from . import models
from django.contrib.auth.forms import UserCreationForm
class comlaint(forms.ModelForm):
    class Meta:
       model=models.complaints
       fields=['name','Eid','department','mobile','subject','comlaint'] 
       widgets={
           'name':forms.TextInput(attrs={'placeholder':'FullName'}),
           'department':forms.TextInput(attrs={'placeholder':'Department'}),
           'Eid':forms.TextInput(attrs={'placeholder':'Employee Id'}),
           'mobile':forms.TextInput(attrs={'placeholder':'Mobile'}),
           'subject':forms.TextInput(attrs={'placeholder':'Complait Type'}),
           'comlaint':forms.Textarea(attrs={'placeholder':'Write Complaints','rows':5,'cols':20}),
       }
class userForm(forms.ModelForm):
    class Meta:
        model=models.UserDetail
        fields=['fullname','emp_id','department','joining','desigination']

class AttendenceForm(forms.ModelForm):
    class Meta:
        model=models.Attendence
        fields=['emp_id','fullname','date','PAL','workinghour','timein','timeout']
        widgets={
           #'fullname':forms.TextInput(attrs={'disabled':'True'}),
           #'emp_id':forms.TextInput(attrs={'disabled':'True'}),
           #'date':forms.TextInput(attrs={'disabled':'True'}),
           'PAL':forms.TextInput(attrs={'list':'pallist'}),
        }