from django.db import models
from django.contrib.auth.models import User

class EventOrganizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    organization_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, help_text="City or Region")

    def __str__(self):
        return self.organization_name


class Event(models.Model):
    EVENT_TYPE = (
        ('Free', 'Free'),
        ('Paid', 'Paid'),
    )

    LOCATION_TYPE = (
        ('Online', 'Online'),
        ('Physical', 'Physical'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    location_type = models.CharField(max_length=10, choices=LOCATION_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE)
    organizer = models.ForeignKey('EventOrganizer', on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return self.title

