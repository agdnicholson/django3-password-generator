from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.POST.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.POST.get('special'):
        characters.extend('!@£$%^&*()/?.>,<][}{|')
    if request.POST.get('numbers'):
        characters.extend('0123456789')
    length = int(request.POST.get('length', 12))
    password = ''
    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : password})