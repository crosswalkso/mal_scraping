from django.urls import path
from . import views

urlpatterns = [
    path("", views.Sources.as_view()),
    path("<int:source_pk>/animes", views.SourceAnimes.as_view()),
]
