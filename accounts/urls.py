# tasks/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('login_app/', views.login_App, name='login_app'),
    path('signup_app/', views.signup_App, name='signup_app'),
    
]
