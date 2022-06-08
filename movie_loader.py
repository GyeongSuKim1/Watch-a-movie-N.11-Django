import json

with open('movies.json', 'r') as f:
    movies = json.load(f)


new_list = []
for movie in movies:

