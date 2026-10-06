from django.urls import path

from . import views

urlpatterns = [
    path('avaliacoes/', views.listar_avaliacoes, name='listar_avaliacoes'),
    path('avaliacoes/pendentes/', views.listar_pendentes, name='listar_pendentes'),
]
