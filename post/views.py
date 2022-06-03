from django.shortcuts import render, redirect
from django.http import HttpResponse

def show_list(request):
    if request.method == 'GET':
        return render(request,'post/post.html')
