# tasks/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('signup/', views.login_App, name='signup'),
    
]
