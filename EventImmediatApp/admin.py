from django.contrib import admin
from .models import Events, EventsParticipants

# Register your models here.

admin.site.register(Events)
admin.site.register(EventsParticipants)