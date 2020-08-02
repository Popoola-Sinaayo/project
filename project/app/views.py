import http.client
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Website, User
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm

# Create your views here.

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
    Users = User.objects.all()
    if User.objects.get(UserName=UserName) and User.objects.get(Password=Password):
        return render(request, 'app/loginsucces.html', context)
    else:
        return render(request, 'app/login.html', context)
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
    user = get_user_model().objects.create(username=username, password=password, email=email)
    sendConfirm(user)
    return render (request, 'app/sent.html')
