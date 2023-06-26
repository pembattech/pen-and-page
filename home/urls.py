from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name  = "home"),
    path("addblog/", add_blog, name = "addblog"),
    path("login/", login_view, name = "login" ),
    path("register/", register_view, name = "register" ),
    path("logout/", logout_view, name = "logout" ),
    path("blog_detail/<slug>", blog_detail, name = "blog_detail" ),
]
