from django.test import TestCase
from sales.models import Sale
from products.models import Product
from course_link.models import CourseLink
from category.models import Category
from datetime import date, datetime
import pytz


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.discount_percentage = 0.05
        cls.is_active = True
        cls.initial_datetime = datetime(
            2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)
        cls.final_datetime = datetime(
           2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)

        cls.sale = Sale.objects.create(
            discount_percentage=cls.discount_percentage,
            is_active=cls.is_active,
            initial_datetime=cls.initial_datetime,
            final_datetime=cls.final_datetime

        )

        cls.name = 'vidro'
        cls.description = "Glass water bottle"
        cls.price_client = 10.6
        cls.price_seller = 6.5
        cls.quantity = 10
        cls.expiration_date = datetime.now()

        cls.product = Product.objects.create(
            name=cls.name,
            description=cls.description,
            price_client=cls.price_client,
            price_seller=cls.price_seller,
            quantity=cls.quantity,
            expiration_date=cls.expiration_date,
            sale=cls.sale
        )

    def test_product_field(self):
        self.assertIsInstance(self.product.description, str)
        self.assertEqual(self.product.description, self.description)

        self.assertIsInstance(self.product.price_client, float)
        self.assertEqual(self.product.price_client, self.price_client)

        self.assertIsInstance(self.product.quantity, int)
        self.assertEqual(self.product.quantity, self.quantity)

        self.assertIsInstance(self.product.sale, Sale)
        self.assertEqual(self.product.sale.is_active, self.is_active)
