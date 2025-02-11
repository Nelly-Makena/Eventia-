from django import forms
from .models import EventOrganizer, Event

class EventOrganizerForm(forms.ModelForm):
    class Meta:
        model = EventOrganizer
        fields = ['phone', 'email', 'organization_name',  'bio', 'website', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }




class EventListingForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'location_type', 'price', 'event_type', 'organizer']

        # Optional: Customize widgets (e.g., date picker, file input styling)
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'event_picture': forms.ClearableFileInput(attrs={'multiple': False}),  # Disable multiple uploads
        }
