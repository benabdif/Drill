from django.urls import path
from . import views

urlpatterns = [
    path('f/', views.project_timeline, name='project_timeline'),

]
