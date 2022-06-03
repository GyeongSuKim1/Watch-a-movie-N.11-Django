from django.shortcuts import render


def home(request):
    
    return render(request, 'movie/home.html')


def detail(request):
    return render(request, 'movie/detail.html')