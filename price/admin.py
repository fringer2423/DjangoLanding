from django.contrib import admin
from .models import PriceTable, PriceCard


@admin.register(PriceCard)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['pc_value', 'pc_description']


@admin.register(PriceTable)
class TableAdmin(admin.ModelAdmin):
    list_display = ['pt_title', 'pt_old_price', 'pt_new_price']
