from django.urls import path
from pacientes.views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('login_error/', login_error, name='login_error'),
    path('mi_perfil/', view_profile, name='view_profile'),
    path('mis_turnos/', listar_turnos, name="listar_turnos"),
    path('mis_vacunas/', listar_vacunas, name="listar_vacunas"),
    path('mis_solicitudes/', listar_solicitudes, name="listar_solicitudes"),
    path('inicio_pacientes/', inicio_pacientes, name='inicio_pacientes'),
]