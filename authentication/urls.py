from django.urls import path
from . import views

urlpatterns = [
    path('loginuser/', views.loginUser),
    path('registeruser/', views.registerUser),
    path('user/me/', views.getUserInfo),
    path('hospital/me/', views.getHospitalInfo),
    path('loginhospital/', views.loginHospital),
    path('registerhospital/', views.registerHospital),
    path('registervaccine/', views.registerForVaccine),
    path('updatevaccinenum/', views.updateVaccineNumber),
]
