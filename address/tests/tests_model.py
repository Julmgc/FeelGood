from django.test import TestCase
from address.models import Address

class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.street = 'street'
        cls.cep = '00000-000'
        cls.house_number = '123'
        cls.city = 'city'
        cls.district = 'district'
        cls.state = 'SP'
        cls.country = 'Brasil'

        cls.address = Address.objects.create(
            street = cls.street,
            cep = cls.cep,
            house_number = cls.house_number,
            city = cls.city,
            district = cls.district,
            state = cls.state,
            country = cls.country,
        )

    def test_address_fields(self):
        self.assertIsInstance(self.address.street, str)
        self.assertEqual(self.address.street, self.street)
        
        self.assertIsInstance(self.address.cep, str)
        self.assertEqual(self.address.cep, self.cep)
        
        self.assertIsInstance(self.address.house_number, str)
        self.assertEqual(self.address.house_number, self.house_number)
        
        self.assertIsInstance(self.address.city, str)
        self.assertEqual(self.address.city, self.city)
        
        self.assertIsInstance(self.address.district, str)
        self.assertEqual(self.address.district, self.district)
        
        self.assertIsInstance(self.address.state, str)
        self.assertEqual(self.address.state, self.state)
        
        self.assertIsInstance(self.address.country, str)
        self.assertEqual(self.address.country, self.country)
