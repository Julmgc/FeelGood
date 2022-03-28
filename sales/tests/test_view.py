from rest_framework.test import APITestCase

class SaleViewTest(APITestCase):
    token_admin: str
    token_client: str

    def setUp(self):
        admin_data = {
            "email":"admin@gmail.com",
             "password":"12345678",
             "first_name":"Teste",
             "last_name":"Resto",
             "cpf": "12345678901",
             "birthdate":"2000-01-01",
             "is_seller":False,
             "is_admin":True
        }
        client_data = {
            "email":"client@gmail.com",
             "password":"12345678",
             "first_name":"Teste",
             "last_name":"Resto",
             "cpf": "12345678901",
             "birthdate":"2000-01-01",
             "is_seller":False,
             "is_admin":False
        }


        admin =  self.client.post("/api/register/",admin_data, format="json")
        client = self.client.post("/api/register/",client_data, format="json")
        self.token_admin = self.client.post(
            "/api/login/", { "email":"admin@gmail.com",
             "password":"12345678"}, format="json").json()["token"]
        self.token_client = self.client.post(
            "/api/login/", { "email":"client@gmail.com",
             "password":"12345678"}, format="json").json()["token"]

    def test_create_sale_201(self):
        data = {
            "discount_percentage": 5.0,
            "initial_datetime": "2022-09-05 06:00:55.099000",
            "final_datetime": "2022-09-05 06:00:55.099000"
        }        
        
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        response = self.client.post('/api/sale/', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("initial_datetime", response.data)
        self.assertIn("final_datetime", response.data)
        self.assertIn("is_active", response.data)
        self.assertEqual(response.data['discount_percentage'], 5.0)

    def test_create_sale_403(self):
        data = {
            "discount_percentage": 5.0,
            "initial_datetime": "2022-09-05 06:00",
            "final_datetime": "2022-09-05 06:00"
        }

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_client)
        response = self.client.post('/api/sale/', data)

        self.assertEqual(response.status_code, 403)

    def test_create_sale_without_token_401(self):
        data = {
            "discount_percentage": 5.0,
            "initial_datetime": "2022-09-05 06:00",
            "final_datetime": "2022-09-05 06:00"
        }

        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post('/api/sale/', data)

        self.assertEqual(response.status_code, 401)

    def test_create_sale_incorret_fields_400(self):
        data = {
            "discount_percentage": 5.0,
            "initial_datetime": "2022-09-05 06:00",
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)
        response = self.client.post('/api/sale/', data)

        self.assertEqual(response.status_code, 400)
