from django.contrib import admin
from .models import Season


# Register your models here.
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass
