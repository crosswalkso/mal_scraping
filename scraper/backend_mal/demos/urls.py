from django.urls import path
from . import views

urlpatterns = [
    path("", views.Demos.as_view()),
    path("<int:demo_pk>/animes", views.DemoAnimes.as_view()),
]
