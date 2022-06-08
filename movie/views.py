from django.shortcuts import render
from movie.models import Movie


def home(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('?')[:20] # 랜덤으로 상위 20개 지정

        for movie in movies:
            movie.tags = ", " .join(list(movie.tag.all().values_list('tag', flat=True)))    # 태그
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")         # movie.tags 는 변수일 뿐. 다만, list안의 movie.tag랑 중복되면 error 발생
            print(movie.tag.all())                                                 # 쿼리셋으로 출력됨
            print(list(movie.tag.all()))                                 # 처음 버전 # 리스트 형식 [<Tag: Horror>]
            print(list(movie.tag.all().values_list()))                             # values_list : (id, 'Horror') 처럼 value 값을 다 보여줌 / 현재Tag에 tag만 있어서 2개밖에 안나옴
            print(list(movie.tag.all().values_list('tag')))                        # values_list : 클래스 안에 있는 value값 중에 (title/image등에서) 'tag'값만
            print(list(movie.tag.all().values_list('tag', flat=True)))              # flat : ()를 빼주어 값만 보여줌
            print(", ".join(list(movie.tag.all().values_list('tag', flat=True))))   # join : list -> str & ", "을 더해줌
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        return render(request, 'movie/home.html', {'movies': movies})

    elif request.method == 'POST':
        return render(request, 'movie/detail.html')



def detail(request, id):
    if request.method == 'GET':
        selected_movie = Movie.objects.get(id=id)
        selected_movie.tags = ", ".join(list(selected_movie.tag.all().values_list('tag', flat=True))) # 태그
        # print(f'(상단에 있는)선택한 영화 상세보기 : {selected_movie}')

        recommend = Movie.objects.all()
        if selected_movie in recommend:
            recommend = Movie.objects.exclude(id=selected_movie.id).order_by('?')[:10] # 태그
            # '추천' 안에 '선택한 영화'가 있다면 -> id값 중복을 제외. 정렬은 무작위로. 상위 20개 값을 지정 => 'recommend'
            # print(f'(하단에 있는)선택영화와 추천영화가 같다면 제외하고 보여주기!{recommend}')
            for movie in recommend:
                movie.tags = ", ".join(list(movie.tag.all().values_list('tag', flat=True)))
                # print(f'추천 영화의 태그 !->{movie.tags}')

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
    





