from django.urls import path
from . import views
from animes import views as a_views

urlpatterns = [
    path("", views.Seasons.as_view()),
    path("<int:season_pk>", views.SeasonDetail.as_view()),
    path("<int:season_pk>/animes", views.SeasonAnimes.as_view()),
    path("<int:season_pk>/animes/<int:anime_pk>", views.SeasonAnimeDetail.as_view()),
    ##
    path(
        "<int:season_pk>/animes/genre/<int:genre_pk>",
        a_views.SeasonGenreAnimes.as_view(),
    ),
]
