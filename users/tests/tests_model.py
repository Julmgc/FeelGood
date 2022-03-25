from django.test import TestCase
from users.models import User
from address.models import Address


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.first_name = 'User'
        cls.last_name = 'Last_name'
        cls.email = 'user@mail.com'
        cls.password = '1234'
        cls.cpf = '3333.333.333-33'
        cls.birthdate = '12/12/1980'
        cls.is_admin = False
        cls.is_seller = True
        cls.is_active = True

        cls.user = User.objects.create_user(
            first_name=cls.first_name,
            last_name=cls.last_name,
            email=cls.email,
            password=cls.password,
            cpf=cls.cpf,
            birthdate=cls.birthdate,
            is_admin=cls.is_admin,
            is_seller=cls.is_seller,
            is_active=cls.is_active,
            address_id=cls.address
        )

    def test_user_fields(self):
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, self.first_name)

        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, self.last_name)

        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, self.email)

        self.assertIsInstance(self.user.password, str)

        self.assertIsInstance(self.user.cpf, str)
        self.assertEqual(self.user.cpf, self.cpf)

        self.assertIsInstance(self.user.is_admin, bool)
        self.assertEqual(self.user.is_admin, self.is_admin)

        self.assertIsInstance(self.user.is_seller, bool)
        self.assertEqual(self.user.is_seller, self.is_seller)

        self.assertIsInstance(self.user.is_active, bool)
        self.assertEqual(self.user.is_active, self.is_active)

        self.assertIsInstance(self.user.address_id, Address)
        self.assertEqual(self.user.address_id.street, self.street)
