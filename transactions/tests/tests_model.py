from django.test import TestCase
from users.models import User
from transactions.models import Transaction
from datetime import datetime
# from payments.models import Payment

class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.is_admin = True
        cls.is_seller = False
        cls.email = "ju98@gmail.com"
        cls.password = "1234"
        cls.first_name = "Julia"
        cls.last_name = "Matos"
        
        cls.user = User.objects.create_user(
            is_admin=cls.is_admin,
            is_seller=cls.is_seller,
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name
        )
        
        cls.payment_method="debit",
        cls.card_number="1234567812345678",
        cls.cardholders_name="MARIANA F SOUZA",
        cls.card_expiring_date="2028-02-01",
        cls.cvv=200
        
        # cls.payment = Payment.objects.create(
        #     payment_method=cls.payment_method,
        #     card_number=cls.card_number,
        #     cardholders_name=cls.cardholders_name,
        #     card_expiring_date=cls.card_expiring_date,
        #     cvv=cls.cvv
        #     customer=cls.user
        # )


        cls.amount = 10.5


        cls.transaction = Transaction.objects.create(
            amount = cls.amount ,
            user=cls.user,
            # payment=cls.payment
        )

    def test_transaction_field(self):
        self.assertIsInstance(self.product.description, str)
        self.assertEqual(self.product.description, self.description)

        self.assertIsInstance(self.transaction.created_at, datetime)

        self.assertIsInstance(self.transaction.amount, float)
        self.assertEqual(self.transaction.amount, self.amount)

        self.assertIsInstance(self.transaction.user, User)
        self.assertEqual(self.transaction.user.email, self.email)

        # self.assertIsInstance(self.transaction.payment, Payment)
        # self.assertEqual(self.transaction.payment.cvv, self.cvv)        