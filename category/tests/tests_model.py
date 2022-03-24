from django.test import TestCase
from category.models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.name = 'Perfumaria'

        cls.category = Category.objects.create(
            name = cls.name
        )

    
    def test_category_field(self):
        self.assertIsInstance(self.category.name, str)
        self.assertEqual(self.category.name, self.name)
