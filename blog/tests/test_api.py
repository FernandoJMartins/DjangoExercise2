from django.test import TestCase
from django.test import TestCase
# ...existing code...
# Remova esta linha:
# from django.urls import response

from ..models import User



class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='serializeruser',
            email='asidjoijio@gmail.com',
            password='serializerpassword123'
        )

    def test_user_list_items(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_user_item(self):
        self.user = User.objects.create(
            username='serializeruser2',
            email='aujsdhasiud@gmail.com',
            password='serializerpassword1234'
        )
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'serializeruser2')
        self.assertEqual(response.data['email'], 'aujsdhasiud@gmail.com')

    