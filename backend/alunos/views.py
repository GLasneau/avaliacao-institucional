from django.http import JsonResponse

from .models import Aluno


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return JsonResponse(list(alunos.values()), safe=False)
