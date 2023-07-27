from django.contrib import admin
from .models import Theme, ThemeList
from django.db.models.functions import Lower

# Register your models here.


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(ThemeList)
class ThemeListAdmin(admin.ModelAdmin):
    list_display = (
        "theme",
        "anime",
    )
    list_filter = ("theme",)
