from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return render(request, 'generator/index.html', {'password': 'jkw39b9o8'})


def password(request):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    length = int(request.GET.get('length'))
    the_password = ''
    if request.GET.get('uppercase'):
        characters += characters.upper()
    if request.GET.get('numbers'):
        characters += '1234567890'
    if request.GET.get('special'):
        characters += '!@#$%^&*()_'
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'about/about.html')
