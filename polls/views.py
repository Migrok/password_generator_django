import random

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'polls/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()<>'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'polls/password.html', {'password': thepassword})

def inf(request):
    return render(request, 'polls/inf.html')
