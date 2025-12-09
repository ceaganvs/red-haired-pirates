from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CrewMember
from .forms import CrewSignupForm


def home(request):
    return render(request, 'webapp/home.html')


def about(request):
    return render(request, 'webapp/about.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def join_crew(request):
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
    members = CrewMember.objects.all()
    return render(request, 'webapp/crew_list.html', {'members': members})
