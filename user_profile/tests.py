import base64
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user_profile.models import User


class UserProfileTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser("admin@test.com", "Test@1234")
        User.objects.create_user("test@update", "Test@1234", name="Test User", bio="Test Bio")

    def setUp(self):
        self.headers = {
           'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(b'admin@test.com:Test@1234').decode("ascii")
        }

    def test_create_profile(self):
        url = reverse('user-list')
        data = {'email': 'test@gmail.com', 'name': 'Test User', 'bio': 'Test Bio'}
        response = self.client.post(url, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_body = json.loads(response.content)
        self.assertEqual(User.objects.filter(is_staff=False, id=response_body['id']).count(), 1)
        self.assertEqual(User.objects.get(is_staff=False, id=response_body['id']).name, 'Test User')
        self.assertEqual(User.objects.get(is_staff=False, id=response_body['id']).email, 'test@gmail.com')

    def test_update_profile(self):
        url = reverse('user-detail', args=(2,))
        data = {'email': 'test@gmail.com', 'name': 'Name Changed'}
        response = self.client.put(url, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_body = json.loads(response.content)
        self.assertEqual(User.objects.filter(is_staff=False, id=response_body['id']).count(), 1)
        self.assertEqual(User.objects.get(is_staff=False, id=response_body['id']).name, 'Name Changed')
        self.assertEqual(User.objects.get(is_staff=False, id=response_body['id']).email, 'test@gmail.com')

    def test_fetch_profile(self):
        url = reverse('user-list')
        response = self.client.get(url, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_body = json.loads(response.content)
        self.assertGreaterEqual(User.objects.filter(is_staff=False).count(), response_body['count'])
