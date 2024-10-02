from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class TestAuthorization(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        User.objects.all().delete()

    def test_1_register(self):
        payload = {
            "user": {
                'email': 'test@test.com',
                'username': 'test_user',
                'password': 'test_password',
            }
        }
        response = self.client.post('/api/user/register/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)

    def test_2_login(self):
        payload = {
            "user": {
                'email': 'test@test.com',
                'username': 'test_user',
                'password': 'test_password',
            }
        }
        response = self.client.post('/api/user/register/', data=payload, format='json')
        response = self.client.post('/api/user/login/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["token"]}')

        response = self.client.get('/cats/ratetotal/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
