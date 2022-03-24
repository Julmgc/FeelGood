from django.test import TestCase
from sales.models import Sale
from products.models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.discount_percentage = 0.05
        cls.is_active = True
        cls.initial_datetime = "2022/04/01"
        cls.final_datetime = "2022/04/02"
       

        cls.sale = Sale.objects.create_user(
           discount_percentage = cls.discount_percentage ,
           is_active = cls.is_active,
           initial_datetime = cls.initial_datetime ,
           final_datetime = cls.final_datetime 

        )

        cls.name = 'vidro'
        cls.description = "Glass water bottle"
        cls.price_client = 10
        cls.price_seller = 6
        cls.quantity = 10
        cls.expiration_date = "2023/04/02"

        cls.product = Product.objects.create(
            name = cls.name ,
            description=cls.description,
            price_client=cls.price_client,
            price_seller=cls.price_seller,
            quantity=cls.quantity,
            expiration_date =cls.expiration_date,
            sale_id=cls.sale
        )

    def test_product_field(self):
        self.assertIsInstance(self.product.description, str)
        self.assertEqual(self.product.description, self.description)

        self.assertIsInstance(self.product.price, float)
        self.assertEqual(self.product.price, self.price)

        self.assertIsInstance(self.product.quantity, int)
        self.assertEqual(self.product.quantity, self.quantity)

        self.assertIsInstance(self.product.sale_id, Sale)
        self.assertEqual(self.product.sale_id.is_active, self.is_active)