from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class TestAuthorization(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_1_register(self):
        payload = {
                'email': 'test@test.com',
                'username': 'test_user',
                'password': 'test_password',
        }
        response = self.client.post('/auth/register/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_2_login(self):
        payload = {
                'email': 'test@test.com',
                'username': 'test_user',
                'password': 'test_password',
        }
        response = self.client.post('/auth/register/', data=payload, format='json')
        response = self.client.post('/auth/login/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["token"]}')

        response = self.client.get('/cats/ratetotal/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
