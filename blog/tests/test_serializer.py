from django.test import TestCase

from ..models import User
from ..serializers import UserSerializer



class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='serializeruser',
            email='asidjoijio@gmail.com',
            password='serializerpassword123'
        )

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data['username'], 'serializeruser')
        self.assertEqual(data['email'], 'asidjoijio@gmail.com')
        
    def test_user_serializer_empty(self):
        User.objects.all().delete()
        users = User.objects.all()
        self.assertEqual(users.count(), 0)

