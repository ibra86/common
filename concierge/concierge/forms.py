from django import forms

from concierge.models import Person, Key, KeyTransfer, MAX_NAME_LENGTH


class PersonForm(forms.Form):
    person_name = forms.CharField(max_length=MAX_NAME_LENGTH)

    def save_person(self):
        name = self.cleaned_data.get('person_name')
        person = Person(name=name)
        person.save()


class KeyTransferForm(forms.Form):
    person_name = forms.CharField()
    key_id = forms.IntegerField()

    def save_key_transfer(self):
        key = Key.objects.get(id=int(self.data['key_id']))
        person = Person.objects.get(name=self.data['person_name'])

        transfer_object = KeyTransfer(key_id=key, person_id=person)
        transfer_object.save()
