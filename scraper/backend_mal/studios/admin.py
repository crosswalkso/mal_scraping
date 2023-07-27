from django.contrib import admin
from .models import Studio, AnimeStudios
from django.db.models.functions import Lower

# Register your models here.


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimeStudios)
class AnimeStudiosAdmin(admin.ModelAdmin):
    list_display = (
        "studio",
        "anime",
    )
    list_filter = ("studio",)
