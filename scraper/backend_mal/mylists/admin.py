from django.contrib import admin
from .models import Mylist


# Register your models here.
@admin.register(Mylist)
class MyListAdmin(admin.ModelAdmin):
    pass
