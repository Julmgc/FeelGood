from rest_framework.test import APITestCase

class CategoryViewTest(APITestCase):
    def setUp(self) -> None:
        category_data = {
            "name": "Perfume"
        }

        response = self.client.post('/api/category/', category_data, format='json')
    
    def test_create_new_category_success_201(self):
        category_data = {
            "name": "Perfume"
        }
        
        response = self.client.post('/api/category/', category_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(output['name'], category_data['name'])
        self.assertIn('id', output)
    
    def test_create_new_category_bad_request_400(self):
        category_data = {
            
        }
        response = self.client.post('/api/category/', category_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn(output, 'name')

    def test_list_categories_200(self):
        user_data_admin ={
            "email": "jo@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": False,
            "is_admin": False,
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
        
        response= self.client.get("/api/category/", format="json")
        
        self.assertEqual(response.status_code, 200)

    def test_list_categories_with_no_token_401(self):
        response = self.client.get("/api/category/", format="json")
        output = response.json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(output, {'detail': 'Authentication credentials were not provided.'})

    def get_only_one_category_200(self):
        category_data = {
            "name": "Perfume"
        }
        
        response = self.client.post('/api/category/', category_data, format='json')
        output = response.json()

        response = self.client.get(f'/api/category/{output["id"]}')
        get = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(output['name'], get['name'])
        self.assertEqual(output['id'], get['id'])
    
    def get_non_existing_category_404(self):
        ...