from django import forms
from .models import EventOrganizer, Event

class EventOrganizerForm(forms.ModelForm):
    class Meta:
        model = EventOrganizer
        fields = ['phone', 'email', 'organization_name', 'profile_picture', 'bio', 'website', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }