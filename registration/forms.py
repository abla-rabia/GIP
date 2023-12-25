from django import forms
from .models import Participant

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'discord_id', 'organization', 'phone_number', 'how_did_you_hear', 'motivation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-field1', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'custom-field1', 'placeholder': 'Email', 'required': True}),
            'discord_id': forms.TextInput(attrs={'class': 'custom-field1', 'placeholder': 'Discord ID', 'required': True}),
            'organization': forms.TextInput(attrs={'class': 'custom-field1', 'placeholder': 'Organization', 'required': True}),
            'phone_number': forms.TextInput(attrs={'class': 'custom-field1', 'placeholder': 'Phone Number', 'required': True}),
            'how_did_you_hear': forms.TextInput(attrs={'class': 'custom-field1', 'placeholder': 'How did you hear?', 'required': True}),
            'motivation': forms.Textarea(attrs={'class': 'custom-field', 'placeholder': 'Motivation', 'required': True,'rows': 5, 'style': 'height: 70px;'}),
        }
