from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from clients.models import Client

class ClientTests(APITestCase):
    def test_create_client(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/api/clients/', {'client_name': 'Test Client'})
        self.assertEqual(response.status_code, 201)
