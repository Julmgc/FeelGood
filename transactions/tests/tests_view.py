from rest_framework.test import APITestCase

from users.models import User

class OrderViews(APITestCase):
    token_admin: str
    token_seller: str
    token_buyer: str
    id_products:str
    id_payment:str

    def setUp(self):

        User.objects.create_user(
            email='admin@email.com',
            password='12345678',
            first_name="Teste",
            last_name="Resto",
            cpf="12345678961",
            birthdate="2002-01-01",
            is_seller=False,
            is_admin=True,
        )
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
            cpf="12345678909",
            birthdate="2001-01-01",
            is_seller=False,
            is_admin=False,
        )

        self.token_admin = self.client.post(
            "/api/login/", {'email': 'admin@email.com', 'password': '12345678'}, format="json").json()["token"]
        self.token_seller = self.client.post(
            "/api/login/", {'email': 'seller@email.com', 'password': '12345678'}, format="json").json()["token"]
        self.token_buyer = self.client.post(
            "/api/login/", {'email': 'buyer@email.com', 'password': '12345678'}, format="json").json()["token"]

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
        response_product = self.client.post('/api/products/', product_data, format="json")
        self.id_products= response_product.data['id']

        self.client.credentials()

        data = {
            "payment_method": "credit",
            "card_number": "12345678123456",
            "cardholders_name": "Teste Resto",
            "card_expiration_date": "2122-04-01",
            "cvv": 456
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer)
        response_payment = self.client.post('/api/payment/', data,format="json")
        self.id_payment = response_payment.data['id']

        self.client.credentials()

    def test_create_transaction_sucess_201(self):
        data_transaction ={
            "payment": {"id":self.id_payment },
	        "products": [{"id":self.id_products , "quantity": 10}]
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer)
        response = self.client.post('/api/transaction/', data_transaction,format="json")
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("amount", response.data)
    
    def test_create_transaction_no_permission_403(self):
        data_transaction ={
            "payment": {"id":self.id_payment },
	        "products": [{"id":self.id_products , "quantity": 10}]
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        response = self.client.post('/api/transaction/', data_transaction,format="json")
        output = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(output, {'detail': 'You do not have permission to perform this action.'})
      
       

    
        

