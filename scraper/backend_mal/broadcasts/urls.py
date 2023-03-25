from django.urls import path
from . import views

urlpatterns = [
    path("", views.Broadcasts.as_view()),
    path("<int:broad_pk>", views.BroadcastDetail.as_view()),
    path("<int:broad_pk>/animes", views.BroadcastLists.as_view()),
]
