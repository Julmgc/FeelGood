from django.test import TestCase
from payment.models import Payment


class PaymentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.payment_method = 'credit'
        cls.card_number = '130120323123'
        cls.cardholders_name = 'User'
        cls.card_expiration_date = '01/24'
        cls.cvv = '123'
        cls.is_active = True
        # cls.costumer_id = 

        cls.payment = Payment.objects.create(
            payment_method = cls.payment_method,
            card_number = cls.card_number,
            cardholders_name = cls.cardholders_name,
            card_expiration_date = cls.card_expiration_date,
            cvv = cls.cvv,
            # costumer_id = cls.costumer_id  
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

        # self.assertIsInstance(self.)