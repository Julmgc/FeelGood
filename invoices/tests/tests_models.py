from trace import Trace
from django.test import TestCase
from address.models import Address
from transactions.models import Transaction
from users.models import User
from payment.models import Payment
from invoices.models import Invoice


class InvoiceModelTest(TestCase):
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

        cls.payment_method = "debit",
        cls.card_number = "1234567812345678",
        cls.cardholders_name = "MARIANA F SOUZA",
        cls.card_expiring_date = "2028-02-01",
        cls.cvv = 200

        cls.payment = Payment.objects.create(
            payment_method=cls.payment_method,
            card_number=cls.card_number,
            cardholders_name=cls.cardholders_name,
            card_expiring_date=cls.card_expiring_date,
            cvv=cls.cvv,
            customer=cls.user
        )

        cls.amount = 10.5

        cls.transaction = Transaction.objects.create(
            amount=cls.amount,
            user=cls.user,
            payment=cls.payment
        )

        cls.number = "12325214563222211144477788899966633355511142"

        cls.invoice = Invoice.objects.create(
            number=cls.number,
            transaction=cls.transaction
        )

    def test_invoice_fields(self):
        self.assertIsInstance(self.invoice.number, str)
        self.assertEqual(self.invoice.number, self.number)

        self.assertIsInstance(self.invoice.transaction, Transaction)
        self.assertEqual(self.invoice.transaction.amount, self.amount)
