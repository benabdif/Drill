from django.urls import path
from . import views



urlpatterns = [
    path('', views.members, name='members'),
    # path('rigs/', views.rig_list, name='rig-list'),
    path('timeline1/', views.rig_timeline1, name='rig_timeline'),
    path('projects/', views.project_list, name='project_list'),
    path('create_rig_info/', views.create_rig_info, name='create_rig_info'),
    path('view_rig_info/', views.view_rig_info, name='view_rig_info'),
    


    # path('raw-sql/', views.raw_sql_query_view, name='raw_sql_query_view'),
    # path('custom-sql/', views.custom_sql_query_view, name='custom_sql_query_view'),
    
    

]
