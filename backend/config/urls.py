from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("alunos.urls")),
    path("api/", include("disciplinas.urls")),
    path("api/", include("avaliacoes.urls")),
]
