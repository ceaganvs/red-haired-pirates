"""
Form definitions for the Red-Haired Pirates crew application system.

This module contains Django forms for handling crew member signups
with Bootstrap styling and custom validation.
"""

from django import forms
from .models import CrewMember


class CrewSignupForm(forms.ModelForm):
    """
    Form for new crew member applications.
    
    This ModelForm provides a user-friendly interface for submitting
    applications to join the Red Hair Pirates. Includes Bootstrap
    styling and custom placeholders for better UX.
    
    Meta:
        model: CrewMember model
        fields: All user-facing fields for the application
        widgets: Custom Bootstrap-styled input widgets
        labels: User-friendly field labels
    """
    
    class Meta:
        model = CrewMember
        fields = ['name', 'email', 'age', 'hometown', 'role', 'skills', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '18'}),
            'hometown': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Where are you from?'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'What are you good at? Any special abilities?'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us why you want to sail with the Red Hair Pirates...'}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'age': 'Age',
            'hometown': 'Hometown',
            'role': 'Preferred Role',
            'skills': 'Your Skills',
            'reason': 'Why Join Us?',
        }
