from django.contrib import admin
from .models import EventOrganizer, Event  # Import your models

# Register your models
admin.site.register(EventOrganizer)
admin.site.register(Event)

