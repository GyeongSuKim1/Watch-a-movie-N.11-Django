from django.urls import path
from . import views


urlpatterns = [
    path('taste/', views.taste, name='taste'),
    path('refresh/', views.refresh, name='refresh'),
]
