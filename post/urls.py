from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('detail/post/<int:id>/', views.show_post, name='show-post'),
    path('mypage/', views.show_list, name='show-list'),
    path('mypage/delete/<int:id>/', views.delete_post, name='delete-post'),
]
