"""
View functions for the Red-Haired Pirates web application.

This module handles all HTTP requests and renders templates
for displaying information about Shanks and managing crew applications.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CrewMember
from .forms import CrewSignupForm


def home(request):
    """
    Display the home page with information about Shanks.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered home.html template
    """
    return render(request, 'webapp/home.html')


def about(request):
    """
    Display the biography page with Shanks' backstory.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered about.html template
    """
    return render(request, 'webapp/about.html')


def contact(request):
    """
    Display the contact page.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered contact.html template
    """
    return render(request, 'webapp/contact.html')


def join_crew(request):
    """
    Handle crew member signup form submission and display.
    
    Process POST requests to save new crew applications and
    display the signup form on GET requests.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered join_crew.html template with form or redirect to crew list
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
    Display a list of all crew member applications.
    
    Retrieves all CrewMember objects from the database and displays
    them in a grid layout.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered crew_list.html template with all crew members
    """
    members = CrewMember.objects.all()
    return render(request, 'webapp/crew_list.html', {'members': members})
