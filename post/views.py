from django.shortcuts import render, redirect
from .models import PostModel
from movie.models import Movie
from datetime import datetime


#게시물 작성 페이지
def show_post(request, id):
    user = request.user
    if user:
        if user.is_authenticated:      #로그인 검증
            if request.method == 'GET':

                #사용자가 이미 작성했는지 확인
                try:
                    existed_post = PostModel.objects.get(author_id=user.id, title_id=id)
                    print(existed_post)
                    return render(request, 'post/post.html')
                except:
                    movie = Movie.objects.get(id=id)
                    return render(request, 'post/post.html', {'movie': movie})

            #게시글 작성
            elif request.method == 'POST':
                score = request.POST.get("myRange", "")
                comment = request.POST.get("comment", "")

                current_movie = Movie.objects.get(id=id)
                user = request.user

                #게시글 저장
                PM = PostModel()
                PM.title = current_movie
                PM.score = score
                PM.content = comment
                PM.author_id = user.id

                PM.save()

                return redirect('/mypage')
        else:                       # 로그인이 되어 있지 않다면
            return redirect('/sign-in')


#마이 페이지
#화면 보여 주기(영화제목, 평점, 작성일)
def show_list(request):
    if request.method == 'GET':
        user = request.user

        if user.is_authenticated:      # 사용자가 로그인이 되어 있는지 확인하기
            all_post = PostModel.objects.filter(author_id=user.id).order_by('-created_at')
            return render(request,'post/mypage.html', {'username': user, 'posts': all_post})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')


#게시물 삭제
def delete_post(request,id):
    post = PostModel.objects.get(id=id)

    post.delete()
    return redirect('/mypage')

# 게시물 확인
def edit(request, id):
    article = PostModel.objects.get(id=id)
    movie = Movie.objects.get(id=article.title_id)

    context = {
        'article': article,
        'movie': movie,
    }

    return render(request, 'post/edit.html', context)


# 게시물 업데이트
def update(request, id):
    if request.method == 'POST':
        user = request.user

        article = PostModel.objects.get(id=id)
        movie = Movie.objects.get(id=article.title_id)

        if request.POST.get('myRange') == '1' or request.POST.get('myRange') == '2' or request.POST.get('myRange') == '3' or request.POST.get('myRange') == '4' or request.POST.get('myRange') == '5':
            range_1 = request.POST.get('myRange') + '.0'
        else:
            range_1 = request.POST.get('myRange')
        comment_1 = request.POST.get('comment')

        if str(article.score) == range_1 and article.content == comment_1:
            print(1)
            return render(request, 'post/edit.html', {'error': '내용 수정이 완료되지 않았습니다.', 'article': article, 'movie': movie})

        elif str(article.score) == range_1 and article.content != comment_1:
            print(2)
            article.content = comment_1
            article.created_at = datetime.now()

        elif str(article.score) != range_1 and article.content == comment_1:
            print(3)
            article.score = range_1
            article.created_at = datetime.now()

        elif str(article.score) != range_1 and article.content != comment_1:
            print(4)
            article.score = range_1
            article.content = comment_1
            article.created_at = datetime.now()

        article.save()
        all_post = PostModel.objects.filter(author_id=user.id).order_by('-created_at')

        return render(request, 'post/mypage.html', {'username': user, 'posts': all_post})