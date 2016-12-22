import unittest

from django.test import TestCase
from selenium import webdriver


# functional tests
class NewVistitorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_browsers_homepage(self):
        """
        Sally visits Nomad Emergency for the first time takes a look.
        """
        # She notices the title
        self.browser.get('http://localhost:8000')
        self.assertIn('Nomad Emergency', self.browser.title)

        # She notices a map
        self.fail('Unfinished test case')

        # She notices a Signup or Login link (TBD)

# Unit Tests
class HomePageTest(TestCase):
    def test_root_url_renders_maps_index_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'maps/index.html')

    def test_maps_root_url_renders_maps_index_view(self):
        response = self.client.get('/map/')
        self.assertTemplateUsed(response, 'maps/index.html')


if __name__ == '__main__':
    unittest.main()
