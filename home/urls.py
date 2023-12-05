from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name  = "home"),
    path("login/", login_view, name = "login" ),
    path("register/", register_view, name = "register" ),
]

