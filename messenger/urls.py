from django.urls import path

from . import views

urlpatterns = [
    path('addhospital/', views.addHospital, name='add_hospital'),
    path('chatlist/', views.chatList, name='chat_list'),
    path('chatdetails/', views.chatDetails, name='chat_details'),
    path('registernewchat/', views.registerNewChat, name='registered_new_chat'),
    path('getmodelist/', views.getModeList, name='get_mode_list'),
]
