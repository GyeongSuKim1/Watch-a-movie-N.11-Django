from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PostModel
from movie.models import Movie




#게시물 작성 페이지

@login_required
def show_post(request, id):
    user = request.user.is_authenticated
    if user:

        if request.method == 'GET':
            movie = Movie.objects.get(id=id)
            return render(request, 'post/post.html', {'movie': movie})

        elif request.method == 'POST':
            score = request.POST.get("myRange", "")
            comment = request.POST.get("comment", "")
            current_movie = Movie.objects.get(id=id)
            user = request.user

            PM = PostModel()
            PM.title = current_movie
            PM.score = score
            PM.content = comment
            PM.author_id = user.id

            PM.save()

            return redirect('/mypage')



#마이 페이지
#화면 보여 주기(영화제목, 평점, 작성일)
@login_required
def show_list(request):
    if request.method == 'GET':
        user = request.user   # 사용자가 로그인이 되어 있는지 확인하기
        print(user)

        if user:
            all_post = PostModel.objects.filter(author_id=user.id).order_by('-created_at')
            return render(request,'post/mypage.html', {'username': user, 'posts': all_post})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in/')





