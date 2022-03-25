from django.test import TestCase
from users.models import User
from transactions.models import Transaction
from datetime import datetime
from payment.models import Payment
from address.models import Address


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.is_admin = True
        cls.is_seller = False
        cls.email = "ju98@gmail.com"
        cls.password = "1234"
        cls.first_name = "Julia"
        cls.last_name = "Matos"

        cls.address_data = {
            'street': 'Rua teste',
            'cep': '123456789',
            'house_number': 123,
            'city': 'Cidade',
            'district': 'Bairro',
            'state': 'RS',
            'country': 'Brasil',
        }

        cls.address = Address.objects.create(**cls.address_data)

        cls.user = User.objects.create_user(
            is_admin=cls.is_admin,
            is_seller=cls.is_seller,
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            address=cls.address
        )

        cls.payment_method = 'credit'
        cls.card_number = '130120323123'
        cls.cardholders_name = 'User'
        cls.card_expiration_date = "2024-08-03"
        cls.cvv = '123'
        cls.is_active = True

        cls.payment = Payment.objects.create(
            payment_method = cls.payment_method,
            card_number = cls.card_number,
            cardholders_name = cls.cardholders_name,
            card_expiration_date = cls.card_expiration_date,
            cvv = cls.cvv,
            customer = cls.user  
        )   

        cls.amount = 10.5

        cls.transaction = Transaction.objects.create(
            amount=cls.amount,
            user=cls.user,
            payment=cls.payment
        )

    def test_transaction_field(self):
   


        self.assertIsInstance(self.transaction.amount, float)
        self.assertEqual(self.transaction.amount, self.amount)

        self.assertIsInstance(self.transaction.user, User)
        self.assertEqual(self.transaction.user.email, self.email)

        self.assertIsInstance(self.transaction.payment, Payment)
        self.assertEqual(self.transaction.payment.cvv, self.cvv)
