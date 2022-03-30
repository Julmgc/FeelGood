from rest_framework.test import APITestCase
from users.models import User


class CategoryViewTest(APITestCase):
    token_admin: str
    category_data = {
        "name": "Perfume"
    }

    def setUp(self) -> None:
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
        User.objects.create_user(**admin_data, **user_data)

        self.token_admin = self.client.post(
            '/api/login/', admin_data, format="json").json()["token"]

    def test_create_new_category_success_201(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)

        response = self.client.post(
            '/api/category/', self.category_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(output['name'], self.category_data['name'])
        self.assertIn('id', output)

    def test_create_new_category_bad_request_400(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)

        response = self.client.post('/api/category/', {}, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('name', output)

    def test_list_categories_200(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)

        response = self.client.get("/api/category/", format="json")

        self.assertEqual(response.status_code, 200)

    def test_list_categories_with_no_token_401(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token ")

        response = self.client.get("/api/category/", format="json")
        output = response.json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            output, {'detail': 'Invalid token header. No credentials provided.'})

    def get_only_one_category_200(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin)

        response = self.client.post(
            '/api/category/', self.category_data, format='json')
        output = response.json()

        response = self.client.get(f'/api/category/{output["id"]}')
        get = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(output['name'], get['name'])
        self.assertEqual(output['id'], get['id'])
