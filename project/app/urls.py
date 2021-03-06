from django.urls import path
from . import views
from django_email_verification import urls as mail_urls
urlpatterns = [
path("Confirm", views.Confirm, name="email"),
path("", views.homepage, name="homepage"),
path("login", views.login, name="login"),
path("loginsuccess", views.loginsuccess, name="loginsuccess"),
path("Subscribe", views.Subscribe, name="Subscribe"),
path("Sign_Up", views.Sign_Up, name="Sign_Up"),
path("Confirm2", views.Confirm2, name="Confirm2"),
path("Developer", views.Developer, name="Developer"),
path("web0", views.web0, name="web0"),
path("web1", views.web1, name="web1"),
path("web3", views.web3, name="web3"),
path("web4", views.web4, name="web4"),
path("web5", views.web5, name="web5"),
path("web6", views.web6, name="web6"),
path("web7", views.web7, name="web7"),
path("web8", views.web8, name="web8"),
path("web9", views.web9, name="web9"),
path("web10", views.web10, name="web10"),
path("index", views.index, name="index"),
path("login", views.login, name="login"),
path("test", views.test, name="test"),
path("User", views.User, name="User"),
path("User_0", views.User_0, name="User_0"),
path("get_name", views.get_name, name="get_name")
]
