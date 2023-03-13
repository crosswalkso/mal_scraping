from django.contrib import admin
from .models import Theme, ThemeList

# Register your models here.


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(ThemeList)
class ThemeListAdmin(admin.ModelAdmin):
    pass
