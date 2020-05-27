from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import translation
from label.models import Label, Content
from web.models import Article


class LabelTests(TestCase):

    def test_labels_for_a_language_must_be_unique(self):

        article = Article.objects.create()

        Label.objects.create(
            content_object=article,
            label="Hallo, Welt!",
            language="de"
        )

        Label.objects.create(
            content_object=article,
            label="Hello, World!",
            language="en"
        )

        with self.assertRaises(IntegrityError):
            # Language and object must be unique!
            Label.objects.create(
                content_object=article,
                label="Hello, Deviation!",
                language="en"
            )

    def test_labels(self):

        article = Article.objects.create()

        Label.objects.create(
            content_object=article,
            label="Hallo, Welt!",
            language="de"
        )

        Label.objects.create(
            content_object=article,
            label="Hello, World!",
            language="en"
        )

        self.assertEqual(
            article.labels.count(),
            2
        )

        self.assertEqual(
            article.labels.get(language='de').label,
            'Hallo, Welt!'
        )

        self.assertEqual(
            article.labels.get(language='en').label,
            'Hello, World!'
        )

    def test_label_returns_current_language(self):

        article = Article.objects.create()

        Label.objects.create(
            content_object=article,
            label="Hallo, Welt!",
            language="de"
        )

        Label.objects.create(
            content_object=article,
            label="Hello, World!",
            language="en"
        )

        translation.activate('de')
        self.assertEqual(
            article.label,
            'Hallo, Welt!'
        )

        translation.activate('en')
        self.assertEqual(
            article.label,
            'Hello, World!'
        )


class ContentTests(TestCase):

    def test_contents(self):

        article = Article.objects.create()

        Content.objects.create(
            content_object=article,
            content="Hallo, Welt!",
            language="de"
        )

        Content.objects.create(
            content_object=article,
            content="Hello, World!",
            language="en"
        )

        self.assertEqual(
            article.contents.count(),
            2
        )

        self.assertEqual(
            article.contents.get(language='de').content,
            'Hallo, Welt!'
        )

        self.assertEqual(
            article.contents.get(language='en').content,
            'Hello, World!'
        )

    def test_content_returns_the_current_language(self):

        article = Article.objects.create()

        Content.objects.create(
            content_object=article,
            content="Hallo, Welt!",
            language="de"
        )

        Content.objects.create(
            content_object=article,
            content="Hello, World!",
            language="en"
        )

        self.assertEqual(
            article.contents.count(),
            2
        )

        translation.activate('de')
        self.assertEqual(
            article.content,
            'Hallo, Welt!'
        )

        translation.activate('en')
        self.assertEqual(
            article.content,
            'Hello, World!'
        )
