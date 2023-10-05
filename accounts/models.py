from django.db import models

# Create your models here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})