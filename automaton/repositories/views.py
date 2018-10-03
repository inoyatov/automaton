from django.http import HttpResponse
from django.http import Http404

from django.views.decorators.csrf import csrf_exempt

from automaton.celery import pull

from .models import Repositories


@csrf_exempt
def push_notifications(request, repository_name):
    if request.method == 'GET':
        raise Http404

    repository = Repositories.objects.get(name=repository_name)
    pull(repository.path)

    return HttpResponse("Accepted", status=202)
