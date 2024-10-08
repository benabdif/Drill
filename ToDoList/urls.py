# tasks/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='apps'),
    path('Das/', views.dashboard, name='dashboard'),
   
    path('add_task/', views.add_task, name='add_task'),
    path('add_group_workshop/', views.add_group_workshop, name='add_group_workshop'),
    path('main/', views.main_page, name='main'),
    path('Dash_3/', views.Dash_3, name='Dash_3'),
    path('createTaske/', views.createTask, name='createTaske'),
    # path('myaddTask/', views.myaddTask, name='myaddTask'),
]
