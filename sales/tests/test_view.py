from rest_framework.test import APITestCase

from users.models import User


class SaleViewTest(APITestCase):
    token_admin: str
  

    def setUp(self):
        User.objects.create_user(
            email='admin@gmail.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            cpf="12345678901",
            birthdate="2000-01-01",
            is_seller=False,
            is_admin=True,
        )


        self.token_admin = self.client.post(
            "/api/login/", {'email': 'admin@gmail.com', 'password': '12345678'}, format="json").json()["token"]

    def test_create_sale_201(self):
        data = {
            "discount_percentage": 5.0,
            "initial_datetime": "07/28/2022 18:54:55.099000",
            "final_datetime": "07/29/2022 18:54:55.099000"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin)
        response = self.client.post('/api/payment/', data)

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("initial_datetime", response.data)
        self.assertIn("final_datetime", response.data)
        self.assertIn("is_active", response.data)
        self.assertEqual(response.data['discount_percentage'], 5.0)

    def test_create_sale_403(self):
        data = {
            "payment_method": "credit",
            "card_number": "12345678123456",
            "cardholders_name": "Teste Resto",
            "card_expiring_date": "2122-04-01",
            "cvv": 456
        }

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_seller)
        response = self.client.post('/api/payment/', data)

        self.assertEqual(response.status_code, 403)

    def test_create_sale_without_token_401(self):
        data = {
            "payment_method": "credit",
            "card_number": "12345678123456",
            "cardholders_name": "Teste Resto",
            "card_expiring_date": "2122-04-01",
            "cvv": 456
        }

        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post('/api/payment/', data)

        self.assertEqual(response.status_code, 401)

    def test_create_sale_incorret_fields_400(self):
        data = {
            "payment_method": "credit",
            "card_number": "12345678123456"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer)
        response = self.client.post('/api/payment/', data)

        self.assertEqual(response.status_code, 400)
