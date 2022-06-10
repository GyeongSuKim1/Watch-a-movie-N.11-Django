from django.urls import path
from . import views

urlpatterns = [
    path('detail/post/<int:id>/', views.show_post, name='show-post'),
    path('mypage/', views.show_list, name='show-list'),
    path('mypage/delete/<int:id>/', views.delete_post, name='delete-post'),
    path('detail/edit/<int:id>/', views.edit, name='edit'),
    path('detail/update/<int:id>', views.update, name='update'),
]
