from django.contrib import admin

from concierge.models import Person, Apartment, Key, KeyTransfer

admin.site.register(Person)
admin.site.register(Apartment)
admin.site.register(Key)
admin.site.register(KeyTransfer)
