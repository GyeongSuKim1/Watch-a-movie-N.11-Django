from django.shortcuts import render
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from movie.models import Movie, Taste


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
        print(f'user:{user}')

        for key, value in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue
            else:
                Taste.objects.create(
                    user=user,
                    movie_id=value,
                )
                movies = []

                movie = Movie.objects.get(id=value)
                print(f'당신이 고른 선호하는 영화: {movie.title}')
                a = item_based_filtering(movie.title)
                for i in a:
                    movie = Movie.objects.get(title=i)
                    movie.tags = ", ".join(list(movie.tag.all().values_list('tag', flat=True)))
                    movies.append(movie)
                print(f'추천된 영화는 : {movies, type(movies)}')
            return render(request, 'movie/home.html', {'movies': movies})