from http import HTTPStatus

from django.core import serializers
from django.core.serializers import SerializerDoesNotExist
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import FormView, ListView, DetailView, TemplateView

from concierge import models
from concierge.forms import KeyTransferForm, PersonForm
from concierge.models import Person, Apartment, Key, KeyTransfer


def health_check(request):
    return HttpResponse("Healthcheck - OK")


# def index(request):
#     return HttpResponse(render_to_string('index.html', {'title': 'Concierge app'}))
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartment_objects'] = Apartment.objects.all()
        context['person_objects'] = Person.objects.all()
        context['key_objects'] = Key.objects.all()
        context['key_transfer_objects'] = KeyTransfer.objects.all()
        return context


def key_transfer_created(request):
    return HttpResponse('Key transfer was created')


def form_accepted(request):
    return HttpResponse('Form successfully accepted')


def api_serializer(request, object_type, object_id):
    try:
        model = getattr(models, object_type.capitalize())
        return HttpResponse(
            content=serializers.serialize(format=request.GET.get('format', 'json'),
                                          queryset=[model.objects.get(id=object_id)]
                                          ),
            content_type="application/json"
        )
    except (AttributeError,
            SerializerDoesNotExist,
            models.Person.DoesNotExist,
            models.Key.DoesNotExist,
            models.Apartment.DoesNotExist,
            ):
        return HttpResponse(status=HTTPStatus.NOT_FOUND)


class PersonFormView(FormView):
    template_name = 'person_form.html'
    form_class = PersonForm
    success_url = '/form-accepted/'

    def form_valid(self, form):
        form.save_person()
        return super().form_valid(form)


class PersonListView(ListView):
    template_name = "person_list.html"
    context_object_name = 'persons'
    model = Person
    paginate_by = 10  # if pagination is desired


class PersonDetailView(DetailView):
    template_name = "person_detail.html"
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class KeyTransferView(FormView):
    template_name = 'key_transfer_form.html'
    form_class = KeyTransferForm
    success_url = '/form-accepted/'

    def form_valid(self, form):
        form.save_key_transfer()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse(status=HTTPStatus.BAD_REQUEST)
