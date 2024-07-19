# from django.urls import path
# from . import views



# urlpatterns = [
   
#     path('', views.eHighlight_Re, name='eHighlight'),
    



# ]


from django.urls import path
from . import views
from django.urls import path
from .views import download_records_excel  # Adjust the import according to your view location


from .views import (
    eHighlightRecordListView,
    eHighlightRecordDetailView,
    eHighlightRecordCreateView,
    eHighlightRecordUpdateView,
    eHighlightRecordDeleteView,
 
)

urlpatterns = [
    path('', views.introduce, name='introduce'),


    path('num/', views.basec, name='basec'),
    path('recordlist', eHighlightRecordListView.as_view(), name='eHighlight_Record_list'),
    path('<int:pk>/', eHighlightRecordDetailView.as_view(), name='eHighlight_Record_detail'),
    path('new/', eHighlightRecordCreateView.as_view(), name='eHighlight_Record_new'),
    path('<int:pk>/edit/', eHighlightRecordUpdateView.as_view(), name='eHighlight_Record_edit'),
    path('<int:pk>/delete/', eHighlightRecordDeleteView.as_view(), name='eHighlight_Record_delete'),
    path('download_records_excel/', download_records_excel, name='download_records_excel'),
    path('total-cost/', views.total_cost_view, name='total_cost'),
    path('apps/', views.All_Apps, name='All_apps'),


    
]
