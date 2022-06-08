from django.shortcuts import render
from movie.models import Movie


def home(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('?') # 랜덤으로 보여주기

        for movie in movies:
            print(f'무비들 ->{movie.tag.all()}')
            movie.tags = list(movie.tag.all()) # 태그 넣어주기

        return render(request, 'movie/home.html', {'movies' : movies})

    elif request.method == 'POST':
        return render(request, 'movie/detail.html')



def detail(request, id):
    if request.method == 'GET':
        selected_movie = Movie.objects.get(id=id)
        print(f'선택한 영화 : {selected_movie}')
        recommend = Movie.objects.order_by('?')

        if selected_movie in recommend:
            print('오우!!')
            recommend = Movie.objects.exclude(id=selected_movie.id)
            print(f'선택영화와 추천영화가 같다면 제외하고 보여주기!{recommend}')

            for movie in recommend:
                movie.tags = list(movie.tag.all())
                print(f'추천영화 리스트 들!->{movie}')

            content = {
                'selected' : selected_movie,
                'movies' : movie,
                'recommend' : recommend,
            }
            return render(request, 'movie/detail.html', content)
        else:
            return render(request, 'movie/detail.html')


    elif request.method == 'POST':
        return render(request, 'movie/detail.html')
