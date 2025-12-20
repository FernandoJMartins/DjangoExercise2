from django.test import TestCase
from ..models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='asdasd@gmail.com',
            password='securepassword123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertIsNotNone(self.user.id)
    
    def test_user_unique_username(self):
        with self.assertRaises(Exception):
            User.objects.create(username='testuser')
    
    def test_user_unique_email(self):
        with self.assertRaises(Exception):
            User.objects.create(
                username='anotheruser',
                email='asdasd@gmail.com',
                password='anotherpassword123'
            )
    

    def test_user_is_empty(self):
        User.objects.all().delete()
        users = User.objects.all()
        self.assertEqual(users.count(), 0)
        