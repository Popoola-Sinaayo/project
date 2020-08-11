from django.db import models
from django import forms
# Create your models here.
class Website(models.Model):
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    Email = models.CharField(max_length=64)
    Gender = models.CharField(max_length=20)
    Comment = models.CharField(max_length=1000)
    Date = models.CharField(max_length=20)
    def __str__(self):
        return f" Name: {self.FirstName} {self.LastName}, \n Email: {self.Email} \n Gender: {self.Gender} \n Comment: {self.Comment}, \n  Date registered: {self.Date}"
class Users(models.Model):
    UserName = models.CharField(max_length=30)
    Password = models.CharField(max_length=40)
    app = models.ManyToManyField(Website, blank=True, related_name="User")
    def __str__(self):
        return f" UserName is {self.UserName} "
class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
class Subscribe0(models.Model):
    Email = models.CharField(max_length=200)
    def __str__(self):
        return self.Email
