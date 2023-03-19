from django.urls import path
from . import views
from animes import views as a_views

urlpatterns = [
    path("", views.Seasons.as_view()),
    path("<int:season_pk>/", views.SeasonDetail.as_view()),
    path("<int:season_pk>/animes", a_views.Animes.as_view()),
]
