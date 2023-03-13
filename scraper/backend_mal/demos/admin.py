from django.contrib import admin
from .models import Demo, DemoList


# Register your models here.
@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass


@admin.register(DemoList)
class DemoListAdmin(admin.ModelAdmin):
    pass
