from django.test import TestCase
from ..models import User


#TESTE VIEWS

class ListUserViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='user1',
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user1.username)

    def test_list_users_empty(self):
        User.objects.all().delete()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '[]')

    