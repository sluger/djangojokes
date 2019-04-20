from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'jokes/index.html')

def jokes(request):
    return render(request, 'jokes/jokes.html')
