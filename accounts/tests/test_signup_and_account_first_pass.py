from django.test import TestCase
from accounts.forms import UserRegisterForm
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpTests(TestCase):

    def test_signup_view(self):
        response = self.client.post('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post('/accounts/signup/')
        form = UserRegisterForm({'username': 'test',
                                 'email': 'john@john.com',
                                 'password1': 'XD78xd87!',
                                 'password2': 'XD78xd87!'})
        self.assertTrue(form.is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)


class AccountsTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user({'username': 'johnjohn',
                                              'email': 'john@john.com',
                                              'password1': 'XD78xd87!',
                                              'password2': 'XD78xd87!'})
        test_user.save()

    def test_user_can_login(self):
        """A user should be able to log in with username and password"""

    def test_user_can_logout(self):
        """A user should be able to log out"""

    def test_user_can_change_password(self):
        """A user should be able to change password"""

    def test_user_can_reset_password(self):
        """A user should be able to reset password using email"""
