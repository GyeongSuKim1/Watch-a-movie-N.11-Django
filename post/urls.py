from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('detail/post/<int:id>', views.show_post, name='show-post'),
    path('detail/post/<int:id>', views.write_post, name='write-post'),
    path('mypage/', views.show_list, name='show-list'),
]
