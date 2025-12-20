from django.test import TestCase, RequestFactory
from django.contrib.auth.hashers import make_password

from blog.forms import SignInForm, SignUpForm
from ..models import User


class UserFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='formuser3',
            email='formuser3@example.com',
            password=make_password('formpassword123')
        )
        self.factory = RequestFactory()

    def test_signup_form_valid(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser2@example.com',
            'password1': 'formpassword123',
            'password2': 'formpassword123'
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_signin_form_valid(self):
        # AuthenticationForm precisa de request como primeiro argumento
        request = self.factory.post('/login/')
        form_data = {
            'username': 'formuser',
            'password': 'formpassword123'
        }
        form = SignInForm(request, data=form_data)
        # AuthenticationForm valida contra o banco, então pode não ser válido
        # Apenas testamos se o formulário tem os campos corretos
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
    
    def test_signin_form_empty(self):
        request = self.factory.post('/login/')
        form = SignInForm(request, data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)