from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import UserModel


def sign_up_view(request):
	if request.method == 'GET':
		user = request.user.is_authenticated
		if user:
			return redirect('/')
		else:
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

		me = auth.authenticate(request, username=username, password=password)
		if me is not None:
			auth.login(request, me)
			return redirect('/taste/')
		else:
			return render(request, 'user/signin.html', {'error': '아이디 혹은 패스워드를 확인 해 주세요'})

	elif request.method == 'GET':
		user = request.user.is_authenticated
		if user:
			return redirect('/')
		else:
			return render(request, 'user/signin.html')


@login_required
def logout(request):
	auth.logout(request)
	return redirect('/')
