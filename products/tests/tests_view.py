from rest_framework.test import APITestCase

from users.models import User


class UserViewTest(APITestCase):
    token_admin: str
    token_buyer: str

    product_data = {
        "name": "produto1",
        "description": "descrição do 1",
        "price_client": 100.00,
        "price_seller": 80.00,
        "quantity": 100,
        "expiration_date": "2024-01-01",
        "course_links": ["http://asdu.com", ],
        "categories": ["teste", "categoria 1"]
    }

    def setUp(self):
        user_data = {
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": False,
            'cpf': '12345678912',
            'birthdate': '30/11/1987'
        }
        admin_data = {
            "email": "adm@mail.com",
            "password": "1234",
            "is_admin": True
        }
        buyer_data = {
            "email": "buyer@mail.com",
            "password": "1234",
            "is_admin": False
        }

        User.objects.create_user(**admin_data, **user_data)
        User.objects.create_user(**buyer_data, **user_data)

        self.token_admin = self.client.post(
            '/api/login/', admin_data, format="json").json()["token"]
        self.token_buyer = self.client.post(
            '/api/login/', buyer_data, format="json").json()["token"]

    def test_create_corret_product_201(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        response = self.client.post('/api/products/', self.product_data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("is_active", response.data)
        self.assertEqual(len(response.data['course_links']), 1)
        self.assertEqual(len(response.data['categories']), 2)

    def test_only_admin_can_create_403(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer)
        response = self.client.post('/api/products/', self.product_data)

        self.assertEqual(response.status_code, 403)

    def test_anyone_can_get_200(self):

        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)

    def test_wrong_fields_creation_400(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        wrong_fields = {**self.product_data}
        wrong_fields.pop("description")
        response = self.client.post('/api/products/', wrong_fields)

        self.assertEqual(response.status_code, 400)

    def test_update_correct_200(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        id = self.client.post(
            '/api/products/', self.product_data, format="json").json()["id"]

        update = {"description": "novo texto"}
        response = self.client.patch(f'/api/products/{id}/', update)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['description'], "novo texto")
