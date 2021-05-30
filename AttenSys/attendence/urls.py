from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('sign_in_form/',views.sign_in),
    path('check/',views.admin),
    path('addUser/',views.AddUser),
    path('more/',views.AddMoreUser),
    path('removeUser/',views.DisplayUser),
    path('deleteUser/',views.RemoveUser),
    path('takeattendence/',views.TakeAttendence),
    path('saveAtten/',views.SaveAttendence),
    path('dataEdit/',views.DataEdit),
    path('SavedataEdit/',views.SaveDataEdit),
    path('summary/',views.summary),
    path('complaint/',views.complaint),
    path('cmpform/',views.complaintForm),
    path('userLogout/',views.UserLogOut),
]