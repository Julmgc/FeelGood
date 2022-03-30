from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from users.models import User


class AddressViewTest(APITestCase):
    token_seller: str

    def setUp(self):
        self.create_seller = User.objects.create_user(
            email="jose@bol.com",
            password="12345678",
            first_name="Jose",
            last_name="Gaspar",
            is_seller=True,
            is_admin=False,
            cpf='12345678912',
            birthdate='30/11/1987'
        )

        self.token_seller = self.client.post(
            "/api/login/", {'email': 'jose@bol.com', 'password': '12345678'}, format="json").json()["token"]

        self.address_data = {
            "street": "Rua das Flores",
            "cep": "20755-170",
            "house_number": "255",
            "city": "Rio De Janeiro",
            "district": "Copa",
            "state": "RJ",
            "country": "Brasil",
        }

    def test_create_new_address_success_200(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_seller)

        response = self.client.put(
            '/api/address/', self.address_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(output['street'], self.address_data['street'])
        self.assertEqual(output['cep'], self.address_data['cep'])
        self.assertEqual(output['city'], self.address_data['city'])
        self.assertIn('id', output)
        self.assertNotIn('passowrd', output)

    def test_create_new_address_wrong_key_400(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_seller)

        address_wrong_data = {
            "street": "Rua das Flores",
            "cep": "20755-170",
            "house_number": "255",
            "city": "Rio De Janeiro",
            "district": "Copa",
            "state": "RJ"
        }

        response = self.client.put(
            '/api/address/', address_wrong_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("country", output)

    def test_create_address_no_token(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token ")

        response = self.client.put(
            '/api/address/', self.address_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            output, {'detail': 'Invalid token header. No credentials provided.'})

    def test_update_new_address_success_200(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_seller)

        id = self.client.put(
            '/api/address/', self.address_data, format='json').json()["id"]

        response = self.client.patch(
            f'/api/address/{id}/', self.address_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(output['street'], self.address_data['street'])
        self.assertEqual(output['cep'], self.address_data['cep'])
        self.assertEqual(output['city'], self.address_data['city'])
        self.assertIn('id', output)
        self.assertNotIn('passowrd', output)

    def test_update_address_no_token(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_seller)

        id = self.client.put(
            '/api/address/', self.address_data, format='json').json()["id"]

        self.client.credentials(
            HTTP_AUTHORIZATION="Token ")

        response = self.client.patch(
            f'/api/address/{id}/', self.address_data, format='json')
        output = response.json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            output, {'detail': 'Invalid token header. No credentials provided.'})
