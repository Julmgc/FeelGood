from django.test import TestCase
from django.utils.timezone import now, timedelta

from address.models import Address
from orders.models import Order
from users.models import User
from sales.models import Sale
from products.models import Product
from payment.models import Payment
from transactions.models import Transaction


class OrderModelTest(TestCase):
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

        cls.payment_data = {
            'payment_method': 'credit',
            'card_number': '12345678',
            'cardholders_name': 'Teste de Model',
            'card_expiration_date': '2100-01-01',
            'cvv': 123,
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

        cls.order_data = {
            'quantity': 1,
        }

        cls.address = Address.objects.create(**cls.address_data)
        cls.user = User.objects.create(**cls.user_data, address=cls.address)
        cls.sale = Sale.objects.create(**cls.sale_data)
        cls.product = Product.objects.create(**cls.product_data, sale=cls.sale)
        cls.payment = Payment.objects.create(**cls.payment_data, customer=cls.user)
        cls.transaction = Transaction.objects.create(payment=cls.payment, user=cls.user)
        cls.order = Order.objects.create(
            product=cls.product,
            transaction=cls.transaction,
            sale=cls.sale,
            **cls.order_data
        )

        def test_order_fields(self):
            self.assertIsInstance(self.order.quantity, int)
            self.assertEqual(self.order.quantity, self.order_data['quantity'])

            self.assertIsInstance(self.order.product, Product)
            self.assertEqual(self.order.product.name, self.product_data['name'])

            self.assertIsInstance(self.order.transaction, Transaction)

            self.assertIsInstance(self.order.sale, Sale)
            self.assertEqual(self.order.sale.discount_percentage,
                             self.sale_data['discount_percentage'])

