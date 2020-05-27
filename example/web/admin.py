from django.conf import settings
from django.contrib import admin
from label.admin import LabelInline, ContentInline
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'label', 'content']
    inlines = (LabelInline, ContentInline)
