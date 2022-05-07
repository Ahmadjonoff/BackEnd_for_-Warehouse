from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(Statistika)
class StatsAdmin(ModelAdmin):
    list_display = ['mahsulot', 'client', 'miqdor', 'sana']
    search_fields = ['mahsulot', 'client', 'miqdor', 'sana', 'id']