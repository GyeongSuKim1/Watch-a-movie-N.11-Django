from django.shortcuts import render, redirect
from .models import PostModel
from django.http import HttpResponse

def show_list(request):
    if request.method == 'GET':
        user = request.user.is_authenticated   # 사용자가 로그인이 되어 있는지 확인하기
        if user:
            all_post = PostModel.objects.all(author=user).order_by('-created_at')
            return render(request,'post/mypage.html', {'posts': all_post})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in/')




