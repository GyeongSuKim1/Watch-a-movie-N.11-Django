from django.urls import path
from movie import views


app_name = 'movie'
urlpatterns = [
    path('home/', views.home),
    path('detail/', views.detail),
]
