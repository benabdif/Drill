from django.urls import path
from . import views
# from TRS_DRE2.views import rig_schedule *******



urlpatterns = [
    path('home2/', views.members2, name='members2'),
    # path('rigs/', views.rig_list, name='rig-list'),
    path('r/', views.project_timeline, name='project_timeline'), 
    path('home3/', views.rig_schedule, name='project_timeline'), 
    path('sql/', views.sql_file, name='sql_file'), 
    path('rr/', views.rig_schedule1, name='rig_schedule'), 



    # path('rigs/', rig_schedule, name='rig-schedule'),   *******


    

]
