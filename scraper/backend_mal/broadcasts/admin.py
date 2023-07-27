from django.contrib import admin
from .models import Broadcast, BroadcastList
from django.db.models.functions import Lower


# Register your models here.
@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    pass


@admin.register(BroadcastList)
class BroadcastListAdmin(admin.ModelAdmin):
    list_display = (
        "broadcast",
        "anime",
    )
    list_filter = ("broadcast",)
