from django.contrib import admin
from .models import Broadcast, BroadcastList


# Register your models here.
@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    pass


@admin.register(BroadcastList)
class BroadcastListAdmin(admin.ModelAdmin):
    pass
