from django.test import TestCase
from payment.models import Payment

from address.models import Address
from users.models import User

class PaymentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:


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
            'contry': 'Brasil',
        }

        cls.payment_method = 'credit'
        cls.card_number = '130120323123'
        cls.cardholders_name = 'User'
        cls.card_expiration_date = "2024-08-03"
        cls.cvv = '123'
        cls.is_active = True
      
        cls.address = Address.objects.create(**cls.address_data)
        cls.user = User.objects.create(**cls.user_data, address=cls.address)
        cls.payment = Payment.objects.create(
            payment_method = cls.payment_method,
            card_number = cls.card_number,
            cardholders_name = cls.cardholders_name,
            card_expiration_date = cls.card_expiration_date,
            cvv = cls.cvv,
            costumer = cls.user  
        )   

    def test_payment_fields(self):
        self.assertIsInstance(self.payment.payment_method, str)
        self.assertEqual(self.payment.payment_method, self.payment_method)
        
        self.assertIsInstance(self.payment.card_number, str)
        self.assertEqual(self.payment.card_number, self.card_number)
        
        self.assertIsInstance(self.payment.cardholders_name, str)
        self.assertEqual(self.payment.cardholders_name, self.cardholders_name)
        
        self.assertIsInstance(self.payment.card_expiration_date, str)
        self.assertEqual(self.payment.card_expiration_date, self.card_expiration_date)
        
        self.assertIsInstance(self.payment.cvv, str)
        self.assertEqual(self.payment.cvv, self.cvv)
        
        self.assertIsInstance(self.payment.is_active, bool)
        self.assertEqual(self.payment.is_active, self.is_active)

        self.assertIsInstance(self.payment.user, User)
        self.assertEqual(self.payment.user.email, self.user_data['email'])