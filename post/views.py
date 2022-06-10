from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PostModel
from movie.models import Movie
from django.contrib import messages



# 게시물 작성 페이지
# @login_required
def show_post(request, id):
    user = request.user
    if user:
        if request.method == 'GET':
        # 사용자가 이미 작성했는지 확인
            try:
                existed_post = PostModel.objects.get(author_id=user.id, title_id=id)
                print(existed_post)
                return render(request, 'post/post.html')
            except:
                movie = Movie.objects.get(id=id)
                return render(request, 'post/post.html', {'movie': movie})
    # 게시글 작성
        elif request.method == 'POST':
            score = request.POST.get("myRange", "")
            comment = request.POST.get("comment", "")
            current_movie = Movie.objects.get(id=id)
            user = request.user
    # 게시글 저장
            PM = PostModel()
            PM.title = current_movie
            PM.score = score
            PM.content = comment
            PM.author_id = user.id
            PM.save()
            return redirect('/mypage')



# 마이 페이지
# 화면 보여 주기(영화제목, 평점, 작성일)
def show_list(request):
    if request.method == 'GET':
        user = request.user   # 사용자가 로그인이 되어 있는지 확인하기
        if user.is_authenticated:
            all_post = PostModel.objects.filter(author_id=user.id).order_by('-created_at')
            return render(request, 'post/mypage.html', {'username': user, 'posts': all_post})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')



# 게시물 삭제
def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return redirect('/mypage')
