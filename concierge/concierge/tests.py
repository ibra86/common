import json
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from tastypie.test import ResourceTestCaseMixin

from concierge.forms import PersonForm
from concierge.models import Key, Apartment, Person, KeyTransfer


class ModelTests(TestCase):

    def setUp(self):
        person = Person.objects.create(name='AA')
        apartment = Apartment.objects.create(number=2)
        key = Key.objects.create(apartment=apartment)
        KeyTransfer.objects.create(person_id=person, key_id=key)

        self.keys = Key.objects.all()
        self.key_transfers = KeyTransfer.objects.all()

    def test_key_model_creation_positive_case(self):
        self.assertEqual(self.keys.last().apartment.number, 2)

    def test_key_transfer_model_creation_positive_case(self):
        self.assertEqual(self.key_transfers.first().person_id.name, 'AA')


class PersonViewTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(name='AAAAAAAAA')

    def test_person_form_view(self):
        # go to /person-form
        response = self.client.get(reverse('person-form'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # create valid form
        form = PersonForm(data={"person_name": "BB"})
        self.assertTrue(form.is_valid())

        # submit form and save to db
        submit = self.client.post(path=reverse('person-form'), data=form.data)
        self.assertTrue(submit.url, reverse('form-accepted'))
        self.assertTrue(Person.objects.last().name, "BB")

    def test_person_list_view(self):
        response = self.client.get(reverse('person-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.name)

    def test_person_detail_view(self):
        number_last_person = len(Person.objects.all())
        response = self.client.get(reverse('person-detail', args=[number_last_person]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.name)


class ApiSerializerTest(ResourceTestCaseMixin, TestCase):

    def test_api(self):
        Person.objects.create(name='AA')

        url = reverse('api-serializer', args=['person', '1'])
        url = f'{url}?format=json'
        response = self.api_client.get(url, format='json')
        self.assertValidJSONResponse(response)

        response_list = response.content.decode('utf-8')
        response_list = json.loads(response_list)
        self.assertEqual(response_list[0].get('fields').get('name'), Person.objects.last().name)
