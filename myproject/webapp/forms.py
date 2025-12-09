"""
Forms for the Red Hair Pirates crew management system.

This module defines the Django forms used for crew member registration
and data validation.
"""

from django import forms
from .models import CrewMember


class CrewSignupForm(forms.ModelForm):
    """
    Form for new crew members to sign up and join the Red Hair Pirates.
    
    This ModelForm provides a user-friendly interface for collecting
    crew member information with proper validation and Bootstrap styling.
    
    Attributes:
        model: CrewMember model that this form is based on.
        fields: List of model fields to include in the form.
        widgets: Custom widget configurations for form fields.
        labels: User-friendly labels for each form field.
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
