# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_lista, name='producto_lista'),
    path('nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('editar/<int:pk>/', views.producto_editar, name='producto_editar'),
    path('eliminar/<int:pk>/', views.producto_eliminar, name='producto_eliminar'),
]
