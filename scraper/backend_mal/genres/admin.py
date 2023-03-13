from django.contrib import admin
from .models import Genre, AnimeGenres

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimeGenres)
class AnimeGenresAdmin(admin.ModelAdmin):
    pass
