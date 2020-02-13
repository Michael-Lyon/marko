from django.test import SimpleTestCase
from core.urls import index, product, about
from django.urls import resolve, reverse


class Test_Urls(SimpleTestCase):

    def test_index_resolves(self):
        url = reverse('index')
        print(url)
        # self.assertEquals(resolve(url).func, index, "Mtches")
