from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/animes/", include("animes.urls")),
    path("api/v1/seasons/", include("seasons.urls")),
    path("api/v1/genres/", include("genres.urls")),
    path("api/v1/broadcasts/", include("broadcasts.urls")),
    path("api/v1/demos/", include("demos.urls")),
    path("api/v1/sources/", include("sources.urls")),
    path("api/v1/studios/", include("studios.urls")),
    path("api/v1/themes/", include("themes.urls")),
    path("api/v1/mylists/", include("mylists.urls")),
    path("api/v1/users/", include("users.urls")),
]
