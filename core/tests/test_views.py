from django.test import TestCase
from django.urls import reverse


class Test_Views(TestCase):
    # Testing for that the views urls are correct
    def test_view_url_exists_at_desired_location_for_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_exists_at_desired_location_for_products(self):
        response = self.client.get('/product/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_exists_at_desired_location_for_about(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    # Test is the views are accessible through their name
    def test_view_url_accessible_by_name_index(self):
        response = self.client.get(reverse('core:index'))
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name_products(self):
        response = self.client.get(reverse('core:product'))
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name_about(self):
        response = self.client.get(reverse('core:about'))
        self.assertEquals(response.status_code, 200)

    # Test that vievs are using correct templates

    def test_view_correct_html_index(self):
        response = self.client.get(reverse('core:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_correct_html_products(self):
        response = self.client.get(reverse('core:product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_view_correct_html_about(self):
        response = self.client.get(reverse('core:about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
