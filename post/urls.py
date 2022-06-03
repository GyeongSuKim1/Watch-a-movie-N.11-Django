from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('mypage/', views.show_list, name='show-list'),
]
