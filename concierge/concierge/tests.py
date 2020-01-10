from django.test import TestCase

from concierge.models import Key, Apartment


class KeyModelTests(TestCase):

    def test_key_model_creation_positive_case(self):
        apartment = Apartment(number=2)
        apartment.save()
        key = Key(apartment=apartment)
        # self.assertEqual(key.apartment.number, 2)
        key.save()

        keys = Key.objects.all()
        self.assertEqual(keys[0].apartment.number, 2)
        self.assertEqual(keys[0].id, 1)
        self.assertEqual(len(keys), 1)
