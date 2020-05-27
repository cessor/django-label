from django.contrib.contenttypes.admin import (GenericTabularInline,
                                               GenericStackedInline)
from django.conf import settings
from django.contrib import admin
from . import models


class LabelInline(GenericTabularInline):
    model = models.Label
    max_num = len(settings.LANGUAGES)
    min_num = 0
    extra = 1


class ContentInline(GenericStackedInline):
    model = models.Content
    max_num = len(settings.LANGUAGES)
    min_num = 0
    extra = 1
