from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('post/detail/', views.show_list, name='show-list'),
]
