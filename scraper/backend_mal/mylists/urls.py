from django.urls import path
from . import views

urlpatterns = [
    path("", views.Mylists.as_view()),
    path("<int:pk>", views.MylistDetail.as_view()),
    path("<int:pk>/animes/<int:anime_pk>", views.MylistToggle.as_view()),
]
