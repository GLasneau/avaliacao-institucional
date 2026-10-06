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

    # A ForeignKey fica aqui, na Avaliacao, e nao no Aluno, porque um mesmo
    # aluno faz varias avaliacoes ao longo do semestre. Em uma relacao 1:N a
    # referencia mora no lado que se repete: cada linha de Avaliacao guarda
    # o aluno dela, e o Aluno continua unico na tabela dele.
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes')

        # Mesma logica do lado da Disciplina: uma disciplina recebe varias
    # avaliacoes, uma de cada aluno que a cursa. Por isso a referencia fica
    # na Avaliacao, que e o lado "muitos" da relacao.
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