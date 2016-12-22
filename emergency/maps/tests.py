import unittest

from django.test import TestCase
from selenium import webdriver

from .models import Facility


# functional tests
class NewVistitorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_browsers_homepage(self):
        """
        Sally visits Nomad Emergency for the first time takes a look.
        """
        # She notices the website name in the page title in the nav
        self.browser.get('http://localhost:8000')
        self.assertIn('Nomad Emergency', self.browser.title)
        nav_title = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertEqual('Nomad Emergency', nav_title)

        # She notices a Signup or Login link (TBD)
        signup = self.browser.find_element_by_link_text('Sign Up')
        self.assertIsNotNone(signup)

        # She sees a full screen map
        browser_map = self.browser.find_element_by_id('map')
        self.assertIsNotNone(browser_map)
        self.fail('check full screen')


# Unit Tests
class HomePageTest(TestCase):
    def test_root_url_renders_maps_index_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'maps/index.html')

    def test_maps_root_url_renders_maps_index_view(self):
        response = self.client.get('/map/')
        self.assertTemplateUsed(response, 'maps/index.html')

class NewFacilityTest(TestCase):
    def test_new_facility_renders_correct_template(self):
        response = self.client.get('/facility/new')
        self.assertTemplateUsed(response, 'maps/new.html')

class FacilityDetailPageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.facility = Facility.objects.create(
            name='test_name', address='123 main street',
            country='China'
        )

    def test_facility_detail_renders_correct_template(self):
        response = self.client.get('/facility/1')
        self.assertTemplateUsed(response, 'maps/show_facility.html')

    def test_facility_detail_finds_correct_facility(self):
        response = self.client.get('/facility/1')
        self.assertEqual(response.context['facility'], self.facility)




if __name__ == '__main__':
    unittest.main()
