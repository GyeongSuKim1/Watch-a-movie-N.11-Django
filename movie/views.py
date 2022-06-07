from django.shortcuts import render, redirect
from movie.models import Movie


def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        for movie in movies:
            print(f'무비들 ->{movie.tag.all()}')
            movie.tags = list(movie.tag.all())

        return render(request, 'movie/home.html', {'movies' : movies})

    elif request.method == 'POST':
        return render(request, 'movie/detail.html')



def detail(request, id):
    if request.method == 'GET':
        selected_movie = Movie.objects.get(id=id)
        print(selected_movie)

        recommend = Movie.objects.all()
        for movie in recommend:
            movie.tags = list(movie.tag.all())
            print(f'추천영화 리스트입니당->>>>{movie}')

        content = {
            'selected' : selected_movie,
            'movies' : movie,
            'recommend' : recommend,
        }

        return render(request, 'movie/detail.html', content)


    elif request.method == 'POST':
        return render(request, 'movie/detail.html')
