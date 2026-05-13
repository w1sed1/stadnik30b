from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('book/<int:pk>/', views.book_car, name='book_car'),
]