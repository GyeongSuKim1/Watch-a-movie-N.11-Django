from django.urls import path
from movie import views


app_name = 'movie'
urlpatterns = [
    # path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
]
