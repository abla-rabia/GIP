from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm


#participant registration
def register_participant(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("hellllo")

    else: 
            form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def welcomeView(request):
    return render(request, 'home.html')