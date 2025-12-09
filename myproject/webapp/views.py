"""
View functions for the Red Hair Pirates web application.

This module contains all the view functions that handle HTTP requests
and render templates for the crew management system.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CrewMember
from .forms import CrewSignupForm


def home(request):
    """
    Renders the home page with Shanks biography and features.
    
    Args:
        request: HttpRequest object.
        
    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'webapp/home.html')


def about(request):
    """
    Renders the about page with detailed Shanks biography.
    
    Args:
        request: HttpRequest object.
        
    Returns:
        HttpResponse: Rendered about page template.
    """
    return render(request, 'webapp/about.html')


def contact(request):
    """
    Renders the contact page with contact information.
    
    Args:
        request: HttpRequest object.
        
    Returns:
        HttpResponse: Rendered contact page template.
    """
    return render(request, 'webapp/contact.html')


def join_crew(request):
    """
    Handles crew member signup form submission and display.
    
    Processes POST requests to save new crew member applications.
    Displays the signup form for GET requests.
    
    Args:
        request: HttpRequest object containing form data if POST.
        
    Returns:
        HttpResponse: Rendered join crew page with form or redirect to crew list.
    """
    if request.method == 'POST':
        form = CrewSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome aboard! Your application has been received.')
            return redirect('crew_list')
    else:
        form = CrewSignupForm()
    
    return render(request, 'webapp/join_crew.html', {'form': form})


def crew_list(request):
    """
    Displays a list of all crew members who have joined.
    
    Args:
        request: HttpRequest object.
        
    Returns:
        HttpResponse: Rendered crew list page with all crew members.
    """
    members = CrewMember.objects.all()
    return render(request, 'webapp/crew_list.html', {'members': members})
