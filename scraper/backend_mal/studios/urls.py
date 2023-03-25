from django.urls import path
from . import views

urlpatterns = [
    path("list", views.Studios.as_view()),
    path("<int:studio_pk>/animes", views.StudioAnimes.as_view()),
]
