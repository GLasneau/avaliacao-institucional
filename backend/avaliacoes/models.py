from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from alunos.models import Aluno
from disciplinas.models import Disciplina


class Avaliacao(models.Model):
    PENDENTE = 'PENDENTE'
    RESPONDIDA = 'RESPONDIDA'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (RESPONDIDA, 'Respondida'),
    ]

   
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes')

    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')

    nota = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comentario = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} ({self.status})"