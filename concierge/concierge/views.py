from http import HTTPStatus

from django.core import serializers
from django.core.serializers import SerializerDoesNotExist
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import FormView

from concierge import models
from concierge.forms import KeyTransferForm


def health_check(request):
    return HttpResponse("Healthcheck - OK")


def index(request):
    return HttpResponse(render_to_string('index.html', {'title': 'concierge'}))


def key_transfer_created(request):
    return HttpResponse('Key transfer was created')


def api_serializer(request, object_type, object_id):
    try:
        model = getattr(models, object_type.capitalize())
        return HttpResponse(
            serializers.serialize(format=request.GET['format'],
                                  queryset=[model.objects.get(id=object_id)]
                                  )
        )
    except (AttributeError,
            SerializerDoesNotExist,
            models.Person.DoesNotExist,
            models.Key.DoesNotExist,
            models.Apartment.DoesNotExist,
            ):
        return HttpResponse(status=HTTPStatus.NOT_FOUND)


class KeyTransferView(FormView):
    template_name = 'key_transfer_form.html'
    form_class = KeyTransferForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save_key_transfer()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse(status=HTTPStatus.BAD_REQUEST)
