
from django.test import TestCase
from sales.models import Sale
from django.utils.timezone import now, timedelta

from product_reviews.models import ProductReview
from users.models import User
from products.models import Product
from address.models import Address


class ProductReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            'email': 'teste@email.com',
            'password': '1234',
            'first_name': 'Nome',
            'last_name': 'Sobre Nome',
            'cpf': '12345678901',
            'birthdate': '2000-01-01',
        }

        cls.address_data = {
            'street': 'Rua teste',
            'cep': '123456789',
            'house_number': 123,
            'city': 'Cidade',
            'district': 'Bairro',
            'state': 'RS',
            'country': 'Brasil',
        }

        cls.sale_data = {
            'discount_percentage': 0.1,
            'initial_datetime': now().date(),
            'final_datetime': now().date() + timedelta(days=10)
        }

        cls.product_data = {
            'name': 'Produto',
            'description': 'Descrição',
            'price_client': 10.00,
            'price_seller': 8.00,
            'quantity': 100,
            'expiration_date': '2030-01-01'
        }

        cls.address = Address.objects.create(**cls.address_data)
        cls.user = User.objects.create(**cls.user_data, address=cls.address)
        cls.sale = Sale.objects.create(**cls.sale_data)
        cls.product = Product.objects.create(**cls.product_data, sale=cls.sale)

        cls.comment = "Good product",
        cls.score = 3.9

        cls.product_review = ProductReview.objects.create(
            user=cls.user,
            product=cls.product,
            comment=cls.comment,
            score=cls.score
        )

        def test_product_review_fields(self):
            self.assertIsInstance(self.product_review.comment, str)
            self.assertEqual(self.product_review.comment, self.comment)

            self.assertIsInstance(self.product_review.score, float)
            self.assertEqual(self.product_review.score, self.score)

            self.assertIsInstance(self.product_review.user, User)
            self.assertEqual(self.product_review.user.email,
                             self.user_data['email'])

            self.assertIsInstance(self.product_review.product, Product)
            self.assertEqual(self.product_review.product.name,
                             self.product_data['name'])
