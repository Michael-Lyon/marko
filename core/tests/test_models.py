from django.test import TestCase
from core.models import Item


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(title='Chicken', description='Broiler chicken')
        Item.objects.create(
            title='Goats', description='Christmas goat kgcljhhvc kjfjs slH')

    def test_title_label(self):
        item1 = Item.objects.get(id=1)
        field_label = item1._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        item = Item.objects.get(id=2)
        field_label = item._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_lenght(self):
        item = Item.objects.get(id=1)
        field_lenght = item._meta.get_field('title').max_length
        self.assertEquals(field_lenght, 100)

    def title_and_description(self):
        item = Item.objects.get(id=1)
        expected_name = f'{self.item.title}, {self.item.description}'
        self.assertEquals(expected_name, str(item))
