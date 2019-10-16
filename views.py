
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def home(request):
    return render(request, 'logowanie.html')

def show_number(request):
    return render(request, 'base.html')

def show_number2(request):
    return render(request, 'logowanie.html')

def show_number3(request):
    return render(request, 'rejestracja.html')

def show_number4(request):
    return render(request, 'browar.html')

def show_number5(request):
    return render(request, 'hurtownik.html')

def show_number6(request):
    return render(request, 'dystrybutor.html')

def show_number7(request):
    return render(request, 'detalista.html')

def show_number8(request):
    return render(request, 'window_game.html')

def show_number9(request):
    return render(request, 'admin.html')


