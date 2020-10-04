from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.


def home (request):
    return render(request, 'generator/home.html')

def about (request):
    return render(request, 'generator/about.html')

def passw (request):

    context = {'pass':''}

    characters = list('abcdefghiklmnopqrtuvwaxy')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#%^&*'))
    
    
    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))

    for x in range(length):
        context['pass'] += random.choice(characters)


    return render(request, 'generator/passw.html', context)