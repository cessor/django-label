"""
 - Localized Model
 - Label
 - Content
 - LabelMixin
 - ContentMixin

# Max Length set to 10 tu support longest available
# language tag
# http://www.i18nguy.com/unicode/language-identifiers.html
"""
from django.conf import settings
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.db import models


class LocalizedModel(models.Model):
    language = models.CharField(
        choices=settings.LANGUAGES,
        max_length=10,
        null=False,
        blank=False
    )

    object_id = models.PositiveIntegerField()

    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE
    )

    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    class Meta:
        abstract = True


class Label(LocalizedModel):
    label = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.label

    class Meta:
        unique_together = ('object_id', 'language')
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')


class Content(LocalizedModel):
    content = models.TextField(
        null=False,
        blank=False
    )

    def __str__(self):
        return self.content

    class Meta:
        unique_together = ('object_id', 'language')
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')


class LabelMixin(models.Model):
    labels = GenericRelation(
        Label,
        related_query_name='labels'
    )

    @property
    def label(self):
        language = translation.get_language()
        return self.labels.get(language=language).label

    class Meta:
        abstract = True


class ContentMixin(models.Model):
    contents = GenericRelation(
        Content,
        related_query_name='contents'
    )

    @property
    def content(self):
        language = translation.get_language()
        return self.contents.get(language=language).content

    class Meta:
        abstract = True
