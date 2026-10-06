from django.http import JsonResponse

from .models import Avaliacao


def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return JsonResponse(list(avaliacoes.values()), safe=False)


def listar_pendentes(request):
    pendentes = Avaliacao.objects.filter(status=Avaliacao.PENDENTE)
    return JsonResponse(list(pendentes.values()), safe=False)
