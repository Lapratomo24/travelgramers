"""Create test for forms.py"""

from django.test import TestCase
from .forms import ShareForm

# Create your tests here.


class TestShareForm(TestCase):
    """
    Class to test forms.py
    """
    def test_title_is_required(self):
        """
        Method to test error message when title is empty
        """
        form = ShareForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Method to test whether the fields displayed to users are as defined
        """
        form = ShareForm()
        self.assertEqual(
            form.Meta.fields, [
                "title", "featured_image", "description", "attractions"])
