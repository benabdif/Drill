from django.urls import path
from . import views



urlpatterns = [
    # path('', views.members, name='members'),
    # path('rigs/', views.rig_list, name='rig-list'),
    path('timeline1/', views.rig_timeline1, name='rig_timeline'),
    # path('timeline1/<int:pk>/', views.rig_timeline1, name='rig_timeline'),
    path('timeline1/<int:pk>/', views.getMyinfo, name='rig_timeline'),

    path('projects/', views.project_list, name='project_list'),
    path('create_rig_info/', views.create_rig_info, name='create_rig_info'),
    path('view_rig_info/', views.view_rig_info, name='view_rig_info'),
    path('save-note/', views.save_note, name='save_note'),


    # new
    path('get-pre-construction-data/', views.get_pre_construction_data, name='get_pre_construction_data'),
    path("get-well-construction-info/<int:pk>/", views.get_Well_Construction_Info, name="get-well-construction-info"),
    path("get_Rig_Construction_Info/<int:pk>/", views.get_Rig_Construction_Info, name="get_Rig_Construction_Info"),
    path("get_Pre_Construction_Info/<int:pk>/", views.get_Pre_Construction_Info, name="get_Pre_Construction_Info"),
    path("get_Construction_Department/<int:pk>/", views.get_Construction_Department, name="get_Construction_Department"),
    path("get_Cellar/<int:pk>/", views.get_Cellar, name="get_Cellar"),
    path("get_HDPE_Installation/<int:pk>/", views.get_HDPE_Installation, name="get_HDPE_Installation"),
    path("Get_Rig_Move/<int:pk>/", views.Get_Rig_Move, name="Get_Rig_Move"),
   
]
