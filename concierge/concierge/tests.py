from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse


class StatusViewTest(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_data_from_api(self):
        response = self.client.get(reverse('pokemon'))

        self.assertIn(response.status_code, [200, 404])

        if response.status_code == 200:
            self.assertSetEqual(set(response.json().keys()), set(['name', 'url']))
