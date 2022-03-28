from rest_framework.test import APITestCase

from users.models import User


class PaymentViewTest(APITestCase):
    token_seller: str
    token_buyer: str

    def setUp(self):
        User.objects.create_user(
            email='seller@email.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            cpf="12345678901",
            birthdate="2000-01-01",
            is_seller=True,
            is_admin=False,
        )
        User.objects.create_user(
            email='buyer@email.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            is_seller=False,
            is_admin=False,
        )

        self.token_seller = self.client.post(
            "/api/login/", {'email': 'seller@email.com', 'password': '12345678'}, format="json").json()["token"]
        self.token_buyer = self.client.post(
            "/api/login/", {'email': 'buyer@email.com', 'password': '12345678'}, format="json").json()["token"]

    def test_create_paymentinfo_buyer_201(self):
        data = {
            "payment_method": "credit",
            "card_number": "12345678123456",
            "cardholders_name": "Teste Resto",
            "card_expiration_date": "2122-04-01",
            "cvv": 456
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer)
        response = self.client.post('/api/payment/', data)

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("customer", response.data)
        self.assertIn("is_active", response.data)
        self.assertEqual(response.data['card_number_info'], "**********3456")
        self.assertNotIn("card_number", response.data)

    def test_create_paymentinfo_seller_403(self):
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

    def test_create_paymentinfo_without_token_401(self):
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

    def test_create_payment_incorret_fields_400(self):
        data = {
            "payment_method": "credit",
            "card_number": "12345678123456"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer)
        response = self.client.post('/api/payment/', data)

        self.assertEqual(response.status_code, 400)
