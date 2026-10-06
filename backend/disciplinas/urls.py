from django.urls import path

from . import views

urlpatterns = [
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
]
