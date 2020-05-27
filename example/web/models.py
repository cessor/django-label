from label.models import LabelMixin, ContentMixin
from django.db import models


class Article(LabelMixin, ContentMixin):
    created = models.DateTimeField(
        auto_now_add=True
    )
