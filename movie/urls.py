from django.urls import path
from movie import views


app_name = 'movie'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
