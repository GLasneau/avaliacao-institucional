from django.urls import path

from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos, name='listar_alunos'),
]
