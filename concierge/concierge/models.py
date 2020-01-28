from django.db.models import Model, CharField, IntegerField, DateTimeField, OneToOneField, DO_NOTHING, ForeignKey
from django.utils import timezone

MAX_NAME_LENGTH = 80


class Person(Model):
    name = CharField(max_length=MAX_NAME_LENGTH)

    def __str__(self):
        return '%s' % (self.name)


class Apartment(Model):
    number = IntegerField()


class Key(Model):
    apartment = OneToOneField(
        Apartment,
        on_delete=DO_NOTHING
    )


class KeyTransfer(Model):
    key_out_date = DateTimeField(null=True)
    key_in_date = DateTimeField(default=timezone.now)
    person_id = ForeignKey(Person, on_delete=DO_NOTHING)
    key_id = ForeignKey(Key, on_delete=DO_NOTHING)
