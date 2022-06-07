from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PostModel
from movie.models import MovieModel
from django.http import HttpResponse



#게시물 작성 페이지
#화면 보여 주기(영화 제목 + html 파일)
@login_required
def show_post(request, id):
    user = request.user.is_authenticated
    if user:
        title = MovieModel.objects.get(id=id)['title']
        return render(request, 'post/post.html', {'title': title})


#사용자 입력값 DB 저장
#로그인 확인 -> 영화 제목, 평점 입력값, 코멘트 입력값 불러 오기 -> db저장
@login_required
def write_post(request):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            score = request.POST.get("score", "")
            comment = request.POST.get("comment", "")

            PM = PostModel()
            PM.title =
            PM.score = score
            PM.comment = comment
            PM.save()

            return redirect('//'+str(id))



#마이 페이지
#화면 보여 주기(영화제목, 평점, 작성일)
@login_required
def show_list(request):
    if request.method == 'GET':
        user = request.user.is_authenticated   # 사용자가 로그인이 되어 있는지 확인하기
        if user:
            all_post = PostModel.objects.all(author=user).order_by('-created_at')
            return render(request,'post/mypage.html', {'posts': all_post})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in/')




