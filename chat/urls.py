from django.urls import path
from . import views


urlpatterns = [
    path("chat/", views.chat_home, name="chat_home"),
    path("chat/<str:group_id>/", views.user_chat, name="chat_group"),
]
