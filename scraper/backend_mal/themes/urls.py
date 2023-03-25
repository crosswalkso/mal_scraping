from django.urls import path
from . import views

urlpatterns = [
    path("list", views.Themes.as_view()),
    path("<int:theme_pk>/animes", views.ThemeAnimes.as_view()),
]
