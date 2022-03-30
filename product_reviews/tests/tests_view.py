from rest_framework.test import APITestCase
from users.models import User

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


        product_data_1 = {
            "name": "produto1",
            "description": "descrição do 1",
            "price_client": 100.00,
            "price_seller": 80.00,
            "quantity": 100,
            "expiration_date": "2024-01-01",
            "course_links": ["http://asdu.com", ],
            "categories": ["teste", "categoria 1"]
        }

        product_data_2 = {
            "name": "produto2",
            "description": "descrição do 1",
            "price_client": 100.00,
            "price_seller": 80.00,
            "quantity": 100,
            "expiration_date": "2024-01-01",
            "course_links": ["http://asdu.com", ],
            "categories": ["teste", "categoria 1"]
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        created_product_1 =  self.client.post('/api/products/', product_data_1, format="json")
        product_1_id = created_product_1.data['id']
        self.product = self.client.get('/api/products/'+created_product_1.data["id"]+"/", format="json")
        created_product_2 =  self.client.post('/api/products/', product_data_2, format="json")
        self.product_2 = self.client.get('/api/products/'+created_product_2.data["id"]+"/", format="json")
        
        self.product_review_data = {
            "comment": "Good product",
            "score": 4.0,
            "product": self.product.data["id"]
        }
        self.product2_review_data = {
            "comment": "Good product",
            "score": 4.0,
            "product": self.product_2.data["id"]
        }

        self.payment_data = {
            "payment_method": "credit",
            "card_number": "12345678123456",
            "cardholders_name": "Teste Resto",
            "card_expiration_date": "2122-04-01",
            "cvv": 456
        }

        # CREATE PAYMENT
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response_payment_creation = self.client.post('/api/payment/', self.payment_data)
        response_payment_creation_id = response_payment_creation.data["id"]

#         payment_id = response_payment_creation.data['id']
#   id = self.client.post(
#             '/api/products/', self.product_data, format="json").json()["id"]
        transaction_data = {
            "payment": {"id": response_payment_creation_id},
            "products": [{"id": self.product.data["id"], "quantity": 10}]
        }

        # CREATE TRANSACTION
        response_payment_creation = self.client.post('/api/transaction/', transaction_data)

    def test_create_product_review_201(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller)
        response = self.client.post('/api/productReview/', self.product_review_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("comment", response.data)
        self.assertIn("score", response.data)    

    def test_create_product_review_product_not_bought400(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller)
        response = self.client.post('/api/productReview/', self.self.product2_review_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("id", response.data)
        self.assertIn("comment", response.data)
        self.assertIn("score", response.data)    

    def test_create_productReview_admin_403(self):

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_admin)
        response = self.client.post('/api/productReview/', self.product_review_data)

        self.assertEqual(response.status_code, 403)

    def test_create_product_review_without_token_401(self):

        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post('/api/productReview/', self.product_review_data)

        self.assertEqual(response.status_code, 401)

    def test_create_product_review_incorret_fields_400(self):
        product_review_data = {
            "comment": "Good product",
            "score": 4.0,
            "user": self.create_client
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/productReview/', product_review_data)
        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(output, {'detail': "You can only review a product you have bought."})


    def test_list_product_reviews_200(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/productReview/', self.product_review_data)

        response= self.client.get("/api/productReview/", format="json")
        output = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(output), 1)
 
    def test_return_product_review_by_id_200(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/productReview/', self.product_review_data, format='json').json()
        id = response['id']
        response= self.client.get(f'/api/productReview/{id}/',format="json")
        output = response.json()
        self.assertEqual(response.status_code, 200)
        
       
    def test_patch_product_review_200(self):
 
        patch_product_review_data = {
            "comment": "Super good product",
            "score": 1.0
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/productReview/', self.product_review_data, format='json').json()
        id = response['id']
        patch_review = self.client.patch(f'/api/productReview/{id}/', patch_product_review_data, format='json')
        output = patch_review.json()
        self.assertEqual(output["comment"], patch_product_review_data["comment"])
        self.assertEqual(patch_review.status_code, 200)
       


 