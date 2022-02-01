from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hospital_manager/login.html'), name='logout'),
    path('home/', views.Home, name='home'),
    path('fetchdistributediv/', views.SendDistibuteDiv, name='distribute_div'),
    path('distributevaccine/', views.DistributVaccine, name='distribute_vacc'),
    path('assignvaccine/', views.AssigneVaccine, name='assign_vaccine'),
    path('fetchqueuediv/', views.SendQueueDiv, name='send_queue_div'),
    path('fetchuserdiv/', views.ViewUsers, name='send_user_div'),
    path('fetchhospitalsdiv/', views.ViewHospitals, name='send_hospital_div'),
    path('registerhospital/', views.registerHospitalFromFile, name='register_hos_from_file'),
    path('dailyreport/', views.generateDailyReport, name='daily_report'),
]
