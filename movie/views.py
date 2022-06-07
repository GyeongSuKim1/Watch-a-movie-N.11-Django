from django.shortcuts import render, redirect
from movie.models import Movie


def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        for movie in movies:
            print(movie)
            print(f'무비들 ->{movie.tag.all()}')
            movie.tags = list(movie.tag.all())
        return render(request, 'movie/home.html', {'movies' : movies})

    elif request.method == 'POST':
        return render(request, 'movie/detail.html')



def detail(request, id):
    if request.method == 'GET':
        selected_movie = Movie.objects.get(id=id)
        print(selected_movie)



        content = {
            'selected': selected_movie
        }

        return render(request, 'movie/detail.html', content)

