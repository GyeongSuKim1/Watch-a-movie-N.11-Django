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


# Create your views here.

def sign_up_view(request):
	if request.method == 'GET':
		return render(request, 'user/signup.html')

	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		password2 = request.POST.get('password2', None)

		if password != password2:
			return render(request, 'user/signup.html')
		else:
			exist_user = get_user_model().objects.filter(username=username)
			if exist_user:
				return render(request, 'user/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
			else:
				UserModel.objects.create_user(username=username, password=password)
				return redirect('/sign-in')  # 회원가입이 완료되었으므로 로그인 페이지로 이동


def sign_in_view(request):
	return render(request, 'user/signin.html')