from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_tweet, name='create'),
    path('edit/<int:id>/', views.edit_tweet, name='edit'),
    path('delete/<int:id>/', views.delete_tweet, name='delete'),
    path('register/', views.register, name='register'),
]
