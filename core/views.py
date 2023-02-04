from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Rota para a index
def index(request):
    return render(request, 'index.html')