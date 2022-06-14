from django.shortcuts import render, redirect
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from movie.models import Movie, Taste, Tag
from django.db.models import Max


movies = pd.read_csv('recommend/movies.csv')
ratings = pd.read_csv('recommend/ratings.csv')

### item_based_filtering ####
movie_ratings = pd.merge(ratings, movies, on='movieId')

user_title = movie_ratings.pivot_table('rating', index='title', columns='userId')
user_title = user_title.fillna(0)

item_based_collab = cosine_similarity(user_title, user_title)
item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)


def item_based_filtering(movie):
    movie_list = item_based_collab[movie].sort_values(ascending=False)[1:21]
    print(f'아이템 협업 필터링 결과값 : {movie_list.index}')
    return movie_list.index


def taste(request):
    print(f'request.GET{request.GET}')
    print(f'request.POST{request.POST}')
    user = request.user
    choice = request.POST.get('title')
    print(f'{user}의 choice: {choice}')
    scores = []
    tags = Tag.objects.all()
    for tag in tags:
        max_score = tag.movies.all().aggregate(score=Max('score'))
        movie = tag.movies.filter(score=max_score["score"])[0]
        scores.append(movie)  # 태그별 가장 높은 평점의 영화들을 리스트함
        max_score = set(scores)

    if request.method == 'GET':
        user_taste = Taste.objects.all().values_list('user_id', flat=True)
        if request.user.id in user_taste:
            return redirect('/')
        else:
            return render(request, 'recommend/taste.html',{'movies':max_score})
    elif request.method == 'POST':
        for key, value in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue
            
            elif key == "title":
                title = Movie.objects.get(id=value).title
                a = item_based_filtering(title)
                for i in a:
                    movies = Movie.objects.get(title=i)
                    movies.tags = ", ".join(list(movies.tag.all().values_list('tag', flat=True)))
                    max_score.add(movies)
                print(max_score)

            Taste.objects.create(user=user, movie_id=choice)
            return render(request, 'movie/home.html', {'movies': max_score, 'tag_all': tags})
        return render(request, 'recommend/taste.html', {'error': '에러메세지', 'movies': max_score, 'tag_all': tags})

def refresh(request):
    movie = Movie.objects.filter(score__gt=3.5).order_by('?')[:20]
    return render(request, 'recommend/taste.html', {'movies': movie})
