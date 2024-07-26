# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('Das/', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('add_group_workshop/', views.add_group_workshop, name='add_group_workshop'),
    path('main/', views.main_page, name='main'),
    
]
