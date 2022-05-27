from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

admin.site.register(StatusCrm)


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ['comment_dt', 'comment_text']
    readonly_fields = ['comment_dt']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_status', 'order_data', 'order_name', 'order_phone']
    list_display_links = ['id', 'order_name']
    search_fields = ['id', 'order_data', 'order_name', 'order_phone']
    list_filter = ['order_status']
    list_editable = ['order_status', 'order_phone']
    list_per_page = 10
    list_max_show_all = 100
    fields = ['id', 'order_status', 'order_data', 'order_name', 'order_phone']
    readonly_fields = ['id', 'order_data']
    inlines = [Comment]


@admin.register(CommentCrm)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_dt', 'comment_binding', 'comment_text']
