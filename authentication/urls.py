from django.urls import path
from . import views

urlpatterns = [
    path('loginuser/', views.loginUser),
    path('registeruser/', views.registerUser),
    path('getuserinfo/', views.getUserInfo),

    path('gethospitalinfo/', views.getHospitalInfo),
    path('loginhospital/', views.loginHospital),
    path('registerhospital/', views.registerHospital),
    path('registervaccine/', views.registerForVaccine),
    path('updatevaccinenum/', views.updateVaccineNumber),
]
