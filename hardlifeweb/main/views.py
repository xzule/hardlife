from django.shortcuts import render, redirect
from .forms import SignUpForm
import logging

def home(request):
    return render(request, 'main/index.html')

def logout(request):
    return render(request, 'main/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            logging.error('Form is not valid. Errors: %s', form.errors)
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})
