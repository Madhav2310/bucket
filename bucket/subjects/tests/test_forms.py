from django.test import TestCase
from django.core.files import File

from subjects.constants import media_types
from subjects.forms import *
from subjects.models import Subject, Content


# TODO: Write tests for external api search forms

class BaseTestCase(object):
    def setUp(self):
        self.subject = Subject.objects.create(
            name="Test Subject",
            description="This is a test subject."
        )
        self.content = Content.objects.create(
            title="Test Content",
            url="abc.com",
            content_id="123456",
            type=media_types[2][0],
            image=File(file=b""),
            description="Test content description, this is.",
            tags=['Action', 'Comedy'],
            topics=['Strategy', 'Philosophy']
        )
        self.content.subject.add(self.subject)


class AddSubjectFormTestCase(BaseTestCase, TestCase):
    def test_add_subject_form(self):
        """Test add Subject form"""
        data = {'name':'Bar', 'description': 'This is another test subject.'}
        form = AddSubjectForm(data=data)
        form.save()
        subjects = Subject.objects.all()
        self.assertEqual(len(subjects), 2)
        new_subject = Subject.objects.get(slug='bar')
        self.assertTrue(new_subject.name, 'Bar')


class EditSubjectFormTestCase(BaseTestCase, TestCase):
    def test_edit_subject_form(self):
        """Test edit subject form"""
        data = {'name':'Bar Baz', 'description': 'This is another test subject'}
        form = EditSubjectForm(instance=self.subject, data=data)
        self.assertTrue(form.is_valid())
        form.save()
        subject = Subject.objects.get()
        self.assertEqual(subject.name, 'Bar Baz')
        self.assertEqual(subject.slug, 'bar-baz')


class AddContentFormTestCase(BaseTestCase, TestCase):
    def test_add_content_form(self):
        """Test add Content form"""
        data = {'title': 'FooTest', 'type': 'book', 'description': 'testing...',
                'url': 'www.bartest.com/foo/baz', 'tags': 'Crime Drama',
                'topics': 'Entertainment History'}
        form = AddContentForm(data=data)
        form.save()
        contents = Content.objects.all()
        self.assertEqual(len(contents), 2)
        new_content = Content.objects.get(slug='-footest')
        self.assertTrue(new_content.title, 'FooTest')


class EditContentFormTestCase(BaseTestCase, TestCase):
    def test_edit_content_form(self):
        """Test edit content form"""
        data = {'title': 'Foo Bar', 'type': 'movie', 'description': 'testing..',
                'url': 'www.bartest.com/foo/baz', 'tags': 'Crime Drama',
                'topics': 'Entertainment History'}
        form = EditContentForm(instance=self.content, data=data)
        self.assertTrue(form.is_valid())
        form.save()
        content = Content.objects.get()
        self.assertEqual(content.title, 'Foo Bar')
        self.assertEqual(content.slug, '123456-foo-bar')
