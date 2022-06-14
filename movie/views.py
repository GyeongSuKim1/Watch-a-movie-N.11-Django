from django.shortcuts import render
from movie.models import Movie,Tag


def home(request):
    if request.method == 'GET':
        scores = Movie.objects.filter(score__gt=2.9).order_by('?')[:100]
        # 변수score = Movie의 score가 2.9보다 큰 값을 필터링 > 랜덤 정렬된 총 99개의 값
        for movie in scores:
            movie.tags = ", " .join(list(movie.tag.all().values_list('tag', flat=True)))
        # 영화들을 for 반복문을 돌려주고, 변수를 이용해 movie.tag(Movie.tag)의 value값을 찾아 movie에 담고 랜더링해준다.
        
        tag_all = Tag.objects.all()

        return render(request, 'movie/home.html', {'movies': scores, 'tag_all': tag_all})

    elif request.method == 'POST':
        tag_all = Tag.objects.all()
        return render(request, 'movie/detail.html', {'tag_all': tag_all})


def detail(request, id):
    if request.method == 'GET':
        tag_all = Tag.objects.all()
        selected_movie = Movie.objects.get(id=id)
        selected_movie.tags = ", ".join(list(selected_movie.tag.all().values_list('tag', flat=True)))
        # (상단에 있는) 선택 영화의 정보와 태그
        movie_list = []
        recommend = Movie.objects.all()
        # 추천 영화
        if selected_movie in recommend:
            recommend = Movie.objects.exclude(id=selected_movie.id).order_by('?')[:10]
            # '추천' 안에 '선택한 영화'가 있다면 -> id값이 중복을 제외 정렬은 무작위로 하여 상위 10개 값
            # print(f'(하단에 있는)선택 영화와 추천 영화가 같다면 제외하고 보여주기!{recommend}')
            for movie in recommend:
                movie_list.append(movie)

            content = {
                'selected' : selected_movie,
                'movies' : movie_list,
                'recommend' : recommend,
                'tag_all': tag_all,
            }
            return render(request, 'movie/detail.html', content)
        else:
            return render(request, 'movie/detail.html')

    elif request.method == 'POST':
        return render(request, 'post/post.html')


#검색 기능
def search(request):
    if request.method == 'POST':
        context = dict()
        input = request.POST.get("search", "")

        movies = Movie.objects.filter(title__icontains=input)
        context['movies'] = movies
        print(context)
        return render(request, 'movie/search.html', context)


# 화면 상단 tag값 나오는 nav 바
def tagging(request, name):
    if request.method == 'GET':
        tag_all = Tag.objects.all()

        tag = Tag.objects.get(tag=name)
        max_score = tag.movies.filter(tag=tag.id)

        return render(request, 'movie/home.html', {'movies': max_score,'tag_all': tag_all, 'tag': tag})




