from django.urls import path
from . import views

urlpatterns = [
    path('crear/empresa/', views.crear_empresa, name='crear_empresa'),
    path('crear/cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear/recarga/', views.crear_recarga, name='crear_recarga'),
    path('buscar/recarga/', views.buscar_recarga, name='buscar_recarga'),
]