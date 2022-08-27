"""Create test for views.py"""

from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """
    Class to test views.py
    """
    def test_get_paginated_list(self):
        """
        Method to test whether the homepage can be displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        """
        Method to test whether the about page can be displayed
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
