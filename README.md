label
=====

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "label" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'label',
    ]

2. Run ``python manage.py makemigrations``:

3. Run ``python manage.py migrate`` to create the models.

4. Create your model:

    from django.db import models
    from label.models import LabelMixin, ContentMixin

    class Article(LabelMixin, ContentMixin):
        pass

5. Create an object:

    article = Article.objects.create()

6. Add labels:

    article.labels.create(
        language='de',
        label="Hallo, Welt!"
    )

    article.labels.create(
        language='en',
        label="Hello, World!"
    )

7. Contents work the same way:

    article.contents.create(
        language='en',
        content="Hello, World!"
    )

8. Call ```label``` or ```content``` to retrieve the label or content for the current locale:

    from django.utils import translation
    translation.activate('de')
    assert article.label == 'Hello, World!'

9. Admin inlines are provided. Check out ```example.web```.
