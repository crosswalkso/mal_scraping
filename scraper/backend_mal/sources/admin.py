from django.contrib import admin
from .models import Source, SourceList

# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(SourceList)
class SourceListAdmin(admin.ModelAdmin):
    pass
