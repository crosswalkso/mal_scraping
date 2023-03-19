from django.urls import path
from . import views

urlpatterns = [
    path("", views.Genres.as_view()),
    path("<int:pk>", views.GenreDetail.as_view()),
    path("<int:genre_pk>/animes", views.GenreAnimes.as_view()),
]
