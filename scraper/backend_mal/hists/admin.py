from django.contrib import admin
from .models import AnimeScoreHist, AnimeMembersHist


# Register your models here.


# Register your models here.
@admin.register(AnimeScoreHist)
class AnimeScoreHistAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimeMembersHist)
class AnimeMembersHistAdmin(admin.ModelAdmin):
    pass
