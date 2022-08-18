from django.shortcuts import render
from movie.models import Movie,Tag


def home(request):
    if request.method == 'GET':
        scores = Movie.objects.filter(score__gt=2.9).order_by('?')[:100]
        for movie in scores:
            movie.tags = ", " .join(list(movie.tag.all().values_list('tag', flat=True)))
        
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
        
        movie_list = []
        recommend = Movie.objects.all()
        
        if selected_movie in recommend:
            recommend = Movie.objects.exclude(id=selected_movie.id).order_by('?')[:10]
            
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
        
        return render(request, 'movie/search.html', context)


# 화면 상단 tag값 나오는 nav 바
def tagging(request, name):
    if request.method == 'GET':
        tag_all = Tag.objects.all()

        tag = Tag.objects.get(tag=name)
        max_score = tag.movies.filter(tag=tag.id)

        return render(request, 'movie/home.html', {'movies': max_score,'tag_all': tag_all, 'tag': tag})




