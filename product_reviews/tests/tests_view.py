from itertools import product
from rest_framework.test import APITestCase
from sales.models import Sale
from users.models import User
from products.models import Product
from datetime import  datetime
import pytz

class productReviewViewTest(APITestCase):
    token_seller: str
    token_client: str
    token_admin: str

    def setUp(self):
        self.create_admin = User.objects.create_user(
            email='seller@email.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            cpf="12345678901",
            birthdate="2000-01-01",
            is_seller=True,
            is_admin=False,
        )
        self.create_client = User.objects.create_user(
            email='client@email.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            is_seller=False,
            is_admin=False,
        )

        self.create_seller = User.objects.create_user(
            email='admin@email.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            is_seller=False,
            is_admin=True,
        )

        self.token_admin = self.client.post(
            "/api/login/", {'email': 'admin@email.com', 'password': '12345678'}, format="json").json()["token"]
        self.token_seller = self.client.post(
            "/api/login/", {'email': 'seller@email.com', 'password': '12345678'}, format="json").json()["token"]
        self.token_client = self.client.post(
            "/api/login/", {'email': 'client@email.com', 'password': '12345678'}, format="json").json()["token"]


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
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        created_product =  self.client.post('/api/products/', product_data, format="json")
        self.product = self.client.get('/api/products/'+created_product.data["id"]+"/", format="json")
        
    def test_create_product_review_201(self):
        product_review_data = {
            "comment": "Good product",
            "score": 4.0,
            "product": self.product.data["id"]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/productReview/', product_review_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("comment", response.data)
        self.assertIn("score", response.data)
    

    def test_create_productReview_admin_403(self):
        data = {
            "comment": "Good product",
            "score": 4.0,
            "user": self.create_admin,
            "product": self.product.data["id"]
        }

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_admin)
        response = self.client.post('/api/productReview/', data)

        self.assertEqual(response.status_code, 403)

    def test_create_product_review_without_token_401(self):
        data = {
            "comment": "Good product",
            "score": 4.0,
            "user": self.create_seller,
            "product": self.product.data["id"]
        }

        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post('/api/productReview/', data)

        self.assertEqual(response.status_code, 401)

    def test_create_product_review_incorret_fields_400(self):
        data = {
            "comment": "Good product",
            "score": 4.0,
            "user": self.create_client
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/productReview/', data)

        self.assertEqual(response.status_code, 400)

