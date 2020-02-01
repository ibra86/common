from django.db.models import Model, CharField, IntegerField, DateTimeField, OneToOneField, DO_NOTHING, ForeignKey
from django.utils import timezone

MAX_NAME_LENGTH = 80


class Person(Model):
    name = CharField(max_length=MAX_NAME_LENGTH)

    def __str__(self):
        return self.name


class Apartment(Model):
    number = IntegerField()

    def __str__(self):
        return f'Apartment #{self.number}'


class Key(Model):
    apartment = OneToOneField(
        Apartment,
        on_delete=DO_NOTHING
    )

    def __str__(self):
        return f'Key from apartment #{self.apartment_id}'


class KeyTransfer(Model):
    key_out_date = DateTimeField(null=True)
    key_in_date = DateTimeField(default=timezone.now)
    person_id = ForeignKey(Person, on_delete=DO_NOTHING)
    key_id = ForeignKey(Key, on_delete=DO_NOTHING)

    def __str__(self):
        return f'Key from apartment #{self.key_id.apartment_id} transfered by person {self.person_id.name}'
