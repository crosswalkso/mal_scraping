from django.contrib import admin
from .models import AnimeScoreHist, AnimeMembersHist

# Register your models here.


# Register your models here.
@admin.register(AnimeScoreHist)
class AnimeScoreHistAdmin(admin.ModelAdmin):
    list_display = (
        "d_date",
        "anime",
        "score",
    )
    list_filter = ("anime__title",)
    search_fields = ("d_date",)
    ordering = (
        "anime_id",
        "d_date",
    )


@admin.register(AnimeMembersHist)
class AnimeMembersHistAdmin(admin.ModelAdmin):
    list_display = (
        "d_date",
        "anime",
        "members",
    )
    list_filter = ("anime__title",)
    search_fields = ("d_date",)
    ordering = (
        "anime_id",
        "d_date",
    )
