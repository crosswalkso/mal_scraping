# season/animes와 겹쳐서 잠시 보류
from django.urls import path
from . import views

urlpatterns = [
    path("list", views.HomeAnimes.as_view()),
    # path("<int:anime_pk>", views.AnimeDetails.as_view()),
]
