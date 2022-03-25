from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class UserViewTest(APITestCase):
    def setUp(self):
        user_data ={
            "email": "jose@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": True,
            "is_admin": False,
            'cpf':'12345678912',
            'birthdate':'30/11/1987'
        }

        response = self.client.post('/api/register/',user_data, format='json')

    def test_create_new_user_success_201(self):
        user_data ={
            "email": "joselinda@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": True,
            "is_admin": False,
            'cpf':'12345678913',
            'birthdate':'30/11/1985'
        }

        response = self.client.post('/api/register/',user_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(output['first_name'],user_data['first_name'])
        self.assertEqual(output['is_seller'],user_data['is_seller'])
        self.assertEqual(output['is_admin'],user_data['is_admin'])
        self.assertIn('uuid',output)
        self.assertNotIn('passowrd',output)
    
    def test_create_new_user_duplicate_email_400(self):
        user_data ={
            "email": "jose@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": True,
            "is_admin": False,
            'cpf':'12345678916',
            'birthdate':'30/11/1985'
        }

     
        response = self.client.post('/api/register/',user_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(output, {'email': ["user with this email already exists."]}) 

       
    
    def test_create_new_user_wrong_key_400(self):

        user_wrong_data ={
            "email": "joao@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "is_admin": False
        }

     

        response = self.client.post('/api/register/',user_wrong_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("is_seller", output) 

           
    def test_login_sucess_200(self):
     
        login_user_data= {
            "email": "jose@bol.com",
            "password": "12345678",
        }
        response = self.client.post("/api/login/",login_user_data, format="json")
        output = response.json()

        self.assertEqual(response.status_code,200)
        self.assertIn('token',output)

    def test_login_credential_errada_401(self):
        login_user_invalid_data= {
            "email": "josi@bol.com",
            "password": "12345678",
        }

        response = self.client.post("/api/login/",login_user_invalid_data, format="json")
        self.assertEqual(response.status_code, 401)

        try:
            output = response.json()
            self.assertNotIn("token", output)
        except TypeError:
            pass
    
    def test_login_wrong_key_400(self):
        login_user_wrong_data= {
            "username": "josi@bol.com",
            "password": "12345678",
        }

        response = self.client.post("/api/login/",login_user_wrong_data, format="json")
        output = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIn("email", output)

    def test_list_users_admin_200(self):
        user_data_admin ={
            "email": "jo@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": False,
            "is_admin": True,
            'cpf':'12345678913',
            'birthdate':'30/11/1986'
        }

        response = self.client.post('/api/register/',user_data_admin, format='json').json()

        login_admin = {
            "email": "jo@bol.com",
            "password": "12345678"
            }
        token = self.client.post("/api/login/",login_admin, format="json").json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        response= self.client.get("/api/register/", format="json")
        output = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(output), 2)
        self.assertEqual(output[1]["email"], user_data_admin["email"])
    
    def test_list_users_no_token(self):
        response = self.client.get("/api/register/", format="json")
        output = response.json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(output, {'detail': 'Authentication credentials were not provided.'})
    
    def test_list_users_no_admin(self):
        login_user_data= {
            "email": "jose@bol.com",
            "password": "12345678",
        }

        token = self.client.post("/api/login/",login_user_data, format="json").json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        response = self.client.get("/api/register/", format="json")
        output = response.json()

        self.assertEqual(response.status_code, 403)
        self.assertEqual(output, {'detail': 'You do not have permission to perform this action.'})

