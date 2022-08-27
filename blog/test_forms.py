from django.test import TestCase
from .forms import ShareForm

# Create your tests here.

class TestShareForm(TestCase):

    def test_title_is_required(self):
        form = ShareForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ShareForm()
        self.assertEqual(form.Meta.fields, ["title", "featured_image", "description", "attractions"])
