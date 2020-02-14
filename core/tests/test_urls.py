from django.test import SimpleTestCase
from core.views import index, product, about
from django.urls import resolve, reverse


class Test_Urls(SimpleTestCase):

    def test_index_resolves(self):
        url = reverse('core:index')
        self.assertEquals(resolve(url).func, index)

    def test_index_resolves(self):
        url = reverse('core:product')
        self.assertEquals(resolve(url).func, index)

    def test_index_resolves(self):
        url = reverse('core:about')
        self.assertEquals(resolve(url).func, about)
