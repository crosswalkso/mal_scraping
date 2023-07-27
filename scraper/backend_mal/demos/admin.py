from django.contrib import admin
from .models import Demo, DemoList
from django.db.models.functions import Lower


# Register your models here.
@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass


@admin.register(DemoList)
class DemoListAdmin(admin.ModelAdmin):
    list_display = (
        "demo",
        "anime",
    )
    list_filter = ("demo",)
