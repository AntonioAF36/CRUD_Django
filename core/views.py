from django.shortcuts import render


# Rota para a index
def index(request):
    return render(request, 'index.html')

