from django.urls import path
from movie import views



urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('<str:name>/', views.tagging, name='tagging'),
]