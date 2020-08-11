from django.contrib import admin
from django.contrib.auth.models import User
from .models import Website, Users
# Register your models here.

admin.site.register(Website)
admin.site.register(Users)
