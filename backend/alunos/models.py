from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    ra = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.ra})"