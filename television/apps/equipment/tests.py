from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Equipment
from rest_framework.authtoken.models import Token

User = get_user_model()

class EquipmentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test@example.com", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.equipment = Equipment.objects.create(name='Камера', status='Свободно')



    def test_get_equipment_list(self):
        response = self.client.get('/api/equipment/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_equipment(self):
        response = self.client.post('/api/equipment/', {'name': 'Микрофон', 'status': 'Свободно'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
