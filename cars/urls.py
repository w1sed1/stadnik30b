from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'), # Головна сторінка
    path('<int:pk>/', views.car_detail, name='car_detail'), # Сторінка одного авто
    path('<int:pk>/book/', views.book_car, name='book_car'), # Сторінка бронювання
]