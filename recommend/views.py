from django.shortcuts import render, redirect
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from movie.models import Movie, Taste, Tag
from django.http.response import JsonResponse
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
    if request.method == 'POST':
        user = request.user
        movies = []
        print(f'request.POST.items(): {request.POST.items}')

        choice = request.POST.get('title')
        print()

        movie_list = []
        tags = Tag.objects.all()
        for tag in tags:
            max_score = tag.movies.all().aggregate(score=Max('score'))
            movie = tag.movies.filter(score=max_score["score"])[0]
            movie_list.append(movie)  # 태그별 가장 높은 평점의 영화들을 리스트함

        for key, value in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue

            elif choice is None:
                return render(request, 'recommend/taste.html', {'error':'에러메세지','movies': movie_list})

            elif choice is not None:
                a = item_based_filtering(movie.title)
                for i in a:
                    movie = Movie.objects.get(title=i)
                    movie.tags = ", ".join(list(movie.tag.all().values_list('tag', flat=True)))
                    movies.append(movie)
                    Taste.objects.create(user=user, movie_id=choice)
                return render(request, 'movie/home.html', {'movies': movies})

