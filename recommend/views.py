from django.shortcuts import render
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from surprise import SVD, Dataset, accuracy, Reader
from surprise.model_selection import train_test_split

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

#### item_based_filtering ####
movie_ratings = pd.merge(ratings, movies, on='movieId')

user_title = movie_ratings.pivot_table('rating', index='title', columns='userId')
user_title = user_title.fillna(0)

item_based_collab = cosine_similarity(user_title, user_title)
item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)

#### latent_based_filtering ####
reader = Reader(rating_scale=(1.0, 5.0))
data = Dataset.load_from_df(df=ratings[['userId', 'movieId', 'rating']], reader=reader)

train, test = train_test_split(data, test_size=0.25, shuffle=True, random_state=23)

algo = SVD(n_factors=50, n_epochs=20, random_state=23)
algo.fit(trainset=train)

pred = algo.test(testset=test)
accuracy.rmse(predictions=pred)


def item_based_filtering(movie):
    # 주어질 영화 중 cosine-similarity 값이 가장 큰 순으로 20번째까지 변수에 저장
    movie_list = item_based_collab[movie].sort_values(ascending=False)[1:20]

    return movie_list.index

# m = item_based_filtering('Dark Knight, The (2008)')
# for i in m:
#     print(i)


def latent_factor_filtering(user_id, movie_id):
    pred = algo.predict('user_id', 'movie_id')
    print(pred)

    preds = []
    for i in ratings['movieId'].unique():
        pred = algo.predict('10', i)
        preds.append((pred.est, pred.iid))
    preds.sort(reverse=True)

    user_like = []
    for i in range(len(preds)):
        user_like.append(preds[i][1])

    return user_like

# print(latent_factor_filtering(10, 200))