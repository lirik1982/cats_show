from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

payload = {
                'email': 'test@test.com',
                'username': 'test_user',
                'password': 'test_password',
        }


class TestCats(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_cat(self):
        #TODO
        assert True
