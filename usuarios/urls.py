from django.urls import path
from . import views

urlpatterns = [
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('panel_aprendiz/', views.panel_aprendiz, name='panel_aprendiz'),
    path('panel_bienestar/', views.panel_bienestar, name='panel_bienestar'),
]