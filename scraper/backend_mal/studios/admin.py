from django.contrib import admin
from .models import Studio, AnimeStudios

# Register your models here.


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimeStudios)
class AnimeStudiosAdmin(admin.ModelAdmin):
    pass
