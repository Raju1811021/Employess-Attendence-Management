from django.contrib import admin
from . import models

admin.site.register(models.complaints)
admin.site.register(models.UserDetail)
admin.site.register(models.Attendence)