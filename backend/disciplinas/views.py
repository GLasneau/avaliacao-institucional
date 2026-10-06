from django.http import JsonResponse

from .models import Disciplina


def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return JsonResponse(list(disciplinas.values()), safe=False)
