from django.contrib import admin
from .models import Anime
from .admin_filters import ScoreFilter


# Register your models here.


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        "season",
        "title",
        "start_date",
        "episodes",
        "duration",
        "members",
        "score",
    )
    search_fields = (
        # "season__season_name",
        "title",
    )
    list_filter = (
        "season",
        ScoreFilter,
    )
