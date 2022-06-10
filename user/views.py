from django.shortcuts import render, redirect
# 내가 가지고 있는 앱, 나의 위치와 동일한 models 중에 UserModel 을 가져 오겠다 는 뜻
from .models import UserModel
#  화면에 글자를 띄울때 사용. (로그인이 성공한다면 로그인 성공이라는 메세지를 출력할 예정)
from django.http import HttpResponse
# 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib.auth import get_user_model
# 사용자 auth 기능
from django.contrib import auth
# 로그인의 여부만 검증 해 주는 기능
from django.contrib.auth.decorators import login_required
from movie.models import Movie, Taste


# Create your views here.

def sign_up_view(request):
	if request.method == 'GET':  # GET 메소드 로 오청이 들어 올 경우
		user = request.user.is_authenticated  # 로그인 된 사용자가 요청하는지 검사
		if user:  # 로그인이 되어있다면
			return redirect('/')
		else:  # 로그인이 되어있지 않다면
			return render(request, 'user/signup.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		password2 = request.POST.get('password2', None)

		if len(str(username)) <= 6:
			return render(request, 'user/signup.html', {'error': '아이디를 6자리 이상 입력해주세요'})
		if len(str(password)) <= 6:
			return render(request, 'user/signup.html', {'error': '패스워드 6자리 이상 입력해주세요'})
		if password != password2:
			return render(request, 'user/signup.html', {'error': '패스워드를 확인 해 주세요!'})
		else:
			if username == '' or password == '':
				return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수 값 입니다'})
			exist_user = get_user_model().objects.filter(username=username)
			if exist_user:
				return render(request, 'user/signup.html', {'error': '사용자가 존재합니다.'})
			else:
				UserModel.objects.create_user(username=username, password=password)
				return redirect('/sign-in')




def sign_in_view(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
		if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
			auth.login(request, me)
			return redirect('/')
		else:  # 로그인 실패하면 다시 로그인 페이지를 보여주기
			return render(request, 'user/signin.html', {'error': '아이디 혹은 패스워드를 확인 해 주세요'})  # 로그인 실패
	elif request.method == 'GET':
		user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
		if user:  # 로그인이 되어 있다면
			return redirect('/')
		else:  # 로그인이 되어 있지 않다면
			return render(request, 'user/signin.html')


@login_required
def logout(request):
	auth.logout(request)
	return redirect('/')