from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "forum"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register, name="register"),
    path("login",views.signin,name='signin')
]