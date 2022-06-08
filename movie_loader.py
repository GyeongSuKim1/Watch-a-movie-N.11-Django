import json

tag_list = ['Adventure', 'Fantasy', 'Animation', 'Drama', 'Horror', 'Action', 'Comedy', 'History', 'Western', 'Thriller', 'Crime', 'Documentary', 'Science Fiction', 'Mystery', 'Music', 'Romance', 'Family', 'War', 'TV Movie']

with open('movies.json', 'r') as f:
    movies = json.load(f)


new_list = []
for movie in movies:
    new_data = {"model": "movie.movie"} #"app명.model명"
    if movie["tag"]:
        tags = movie["tag"].strip("[]").split(',')
        tag_int_list = []
        for tag in tags:
            tag_int = tag_list.index(tag.strip()) + 1 # 제일 처음 세는 값은 0이라 + 1
            tag_int_list.append(tag_int)
        movie['tag'] = tag_int_list

    else:
        movie["tag"] = []
    new_data["fields"] = movie
    new_list.append(new_data)

with open('movie_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
