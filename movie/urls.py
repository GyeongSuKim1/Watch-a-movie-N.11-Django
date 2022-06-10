from django.urls import path
from movie import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
