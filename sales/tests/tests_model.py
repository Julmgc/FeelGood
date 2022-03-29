from datetime import date, datetime
from django.test import TestCase
from sales.models import Sale
from django.utils import timezone

class SaleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.discount_percentage = 0.05
        cls.is_active = True
        cls.initial_datetime = datetime.strptime(
            '07/28/2022 18:54:55.099000', '%m/%d/%Y %H:%M:%S.%f').date()
        cls.final_datetime = datetime.strptime(
            '07/29/2022 18:54:55.099000', '%m/%d/%Y %H:%M:%S.%f').date()

        cls.sale = Sale.objects.create(
            discount_percentage=cls.discount_percentage,
            is_active=cls.is_active,
            initial_datetime=cls.initial_datetime,
            final_datetime=cls.final_datetime
        )

    def test_sale_field(self):
        self.assertIsInstance(self.sale.discount_percentage, float)
        self.assertEqual(self.sale.discount_percentage,
                         self.discount_percentage)

        self.assertIsInstance(self.sale.is_active, bool)
        self.assertEqual(self.sale.is_active, self.sale.is_active)

        self.assertIsInstance(self.sale.initial_datetime, date)
        self.assertEqual(self.sale.initial_datetime, self.initial_datetime)

        self.assertIsInstance(self.sale.final_datetime, date)
        self.assertEqual(self.sale.final_datetime, self.final_datetime)
