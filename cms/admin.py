from django.contrib import admin
from .models import CmsSlider


@admin.register(CmsSlider)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['cms_title', 'cms_text', 'cms_img', 'cms_css']
