from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return render(request, 'password_generator/index.html')

def password(request):
    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('digit'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    if request.GET.get('upper'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    i = 0
    length = int(request.GET.get('length'))
    for i in range(length):
        password += random.choice(characters)
    return render(request, 'password_generator/password.html',
                  {'password': password})

def manual(request):
    return render(request, 'password_generator/manual.html')