from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

admin.site.register(StatusCrm)


@admin.register(Order)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['order_data', 'order_name', 'order_phone', 'order_status']


@admin.register(CommentCrm)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_dt', 'comment_binding', 'comment_text']
