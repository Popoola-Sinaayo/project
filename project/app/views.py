import http.client
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Website, Users, Subscribe0
from . import forms
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from .forms import NameForm

# Create your views here.
"""send_mail(
         'DesignPro',
         'Hello from DesignPro',
         'Olusegunpopoola4real@gmail.com',
         ['mukailapopoola01@gmail.com'],
         fail_silently=False,
)"""
def Subscribe(request):
    if request.method == "POST":
        Email = request.POST["Email"]
        User = Subscribe0(Email=Email)
        subject = "Welcome to DesignPro"
        message = "Confirm Your Email Address"
        recipient = Email
        send_mail(
        subject, message, EMAIL_HOST_USER, [recipient], fail_silently = False
        )
        return render(request, 'app/success.html')
    return render(request, 'app/index.html')
def homepage(request):
    return render(request, 'app/homepage.html')
def login(request):
    return render(request, 'app/login2.html')
def loginsuccess(request):
    UserName = request.POST["UserName"]
    Password = request.POST["Password"]
    context = {
    "message": "Invalid Credentials",
    "UserName": UserName
    }
    if User.objects.get(UserName=UserName) and User.objects.get(Password=Password):
        return render(request, 'app/loginsucces.html', context)
    else:
        return render(request, 'app/login.html', context)
def Sign_Up(request):
    return render(request, "app/web2.html")
def web0(request):
    return render(request, 'app/web0.html')
def web1(request):
    return render(request, 'app/web1.html')

def web3(request):
    if request.method == "GET":
        return render(request, 'app/web2.html')
    context = {
    "meassage": "You Appear  To Have Left Out Some Fields Unfilled"
    }
    FirstName = request.POST["FirstName"]
    LastName = request.POST["LastName"]
    Email = request.POST["Email"]
    Gender = request.POST["Gender"]
    Comment = request.POST["Comment"]
    if FirstName == '' or LastName == '' or Email == '' or Gender == '' or Comment == '':
        context = {
        "message": "You Appear  To Have Left Out Some Fields Unfilled"
        }
        return render (request, 'app/web2.html', context)
    else:
        Users = Website(FirstName=FirstName, LastName=LastName, Email=Email, Gender=Gender, Comment=Comment)
        Users.save()
        return render(request, 'app/web3.html')
def web4(request):
    UserName = request.POST["UserName"]
    Password = request.POST["Password"]
    context = {
    "message": "Invalid Credentials",
    "UserName": UserName
    }
    Users = User.objects.all()
    if UserName == '' or Password == '':
        return render(request, 'app/web3.html', context)
    else:
        Users = User(UserName=UserName, Password=Password)
        Users.save()
        return render(request, 'app/web4.html', context)
def web9(request):
    UserName = request.POST["UserName"]
    Password = request.POST["Password"]
    context = {
    "message": "Invalid Credentials",
    "UserName": UserName
    }
    Users = User.objects.all()
    if User.objects.get(UserName=UserName) and User.objects.get(Password=Password):
        return render(request, 'app/web4.html', context)
    else:
        return render(request, 'app/web1.html', context)
def web5(request):
    return render(request, 'app/web5.html')
def web6(request):
    return render(request, 'app/web6.html')
def web7(request):
    return render(request, 'app/web7.html')
def web8(request):
    return render(request, 'app/web8.html')
def web9(request):
    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")
    headers = {}
def web10(request):
    return render(request, 'app/web10.html')
def index(request):
    return render(request, 'app/index.html')
def test(request):
    return render(request, 'app/test.html')
def Confirm(request):
    username = request.POST["Username"]
    password = request.POST["Password"]
    email = request.POST["Email"]
    User = get_user_model().objects.create(username=username, password=password, email=email)
    sendConfirm(user)
    return render (request, 'app/sent.html')
def Confirm2(request):
    UseS = request.POST["Email"]
    sendConfirm(UseS)
    return render(request, 'app/success.html')
def Developer(request):
    return render(request, 'app/developer.html')
def User(request):
    return render(request, 'app/User.html')
def User_0(request):
    FirstName = request.POST["FirstName"]
    LastName = request.POST["LastName"]
    Email = request.POST["Email"]
    Username = request.POST["Username"]
    Password = request.POST["Password"]
    User.objects.create(password=Password, username=Username, email=Email, first_name=FirstName, last_name=LastName)
    Use.save()
    return render(request, 'app/success.html')
def get_name(request):
    form = NameForm()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = NameForm()
    return render(request, 'app/testsform.html', {'form': form})
