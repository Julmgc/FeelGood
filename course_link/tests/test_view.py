from rest_framework.test import APITestCase

class CourseLinkViewTest(APITestCase):
    def setUp(self):
        user_admin ={
            "email": "jose@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": False,
            "is_admin": True,
            'cpf':'12345678912',
            'birthdate':'30/11/1987'
        }

        user_seller ={
            "email": "joseano@bol.com",
            "password": "12345678",
            "first_name": "Jose",
            "last_name": "Gaspar",
            "is_seller": True,
            "is_admin": False,
            'cpf':'12345678912',
            'birthdate':'30/11/1987'
        }

        response = self.client.post('/api/register/',user_admin, format='json')
        response = self.client.post('/api/register/',user_seller, format='json')

    def test_create_course_link_sucess_201(self):
        login_admin = {
            "email": "jose@bol.com",
            "password": "12345678"
            }
        token = self.client.post("/api/login/",login_admin, format="json").json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        course ={
            'link':'https://sintasebem.com.br'
        }

        response= self.client.post("/api/course/",course, format="json")
        output = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(output["link"], course["link"])
    
    def test_create_course_link_no_permission_403(self):
        login_admin = {
            "email": "joseano@bol.com",
            "password": "12345678"
            }
        token = self.client.post("/api/login/",login_admin, format="json").json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        course ={
            'link':'https://sintasebem.com.br'
        }

        response= self.client.post("/api/course/",course, format="json")
        output = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(output, {'detail': 'You do not have permission to perform this action.'})
    
    def test_create_course_link_no_token_401(self):
  
        course ={
            'link':'https://sintasebem.com.br'
        }

        response= self.client.post("/api/course/",course, format="json")
        output = response.json()
        self.assertEqual(response.status_code, 401)
        self.assertEqual(output, {'detail': 'Authentication credentials were not provided.'})
    
    def test_list_course_admin_200(self):

        login_admin = {
            "email": "jose@bol.com",
            "password": "12345678"
            }
        token = self.client.post("/api/login/",login_admin, format="json").json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        course ={
            'link':'https://sintasebem.com.br'
        }

        response= self.client.post("/api/course/",course, format="json")
        output = response.json()

    
        self.client.credentials()
     
     
        response= self.client.get("/api/course/", format="json")
        output = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(output), 1)
    
    def test_list_course_one_admin_200(self):

        login_admin = {
            "email": "jose@bol.com",
            "password": "12345678"
            }
        token = self.client.post("/api/login/",login_admin, format="json").json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        course ={
            'link':'https://sintasebem.com.br'
        }

        response= self.client.post("/api/course/",course, format="json")
        output = response.json()
        
        id = output['id']

        self.client.credentials()
     
        response= self.client.get(f"/api/course/{id}/", format="json")
        output = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(output['link'], course['link'])