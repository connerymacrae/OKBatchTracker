from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase

from accounts.forms import UserRegisterForm


class UserRegisterFormTest(TestCase):
    good_data = {
        'username': 'test',
        'email': 'test@example.com',
        'password1': '123ABCabc!',
        'password2': '123ABCabc!'
    }

    def test_valid_data_passes(self):
        form = UserRegisterForm(data=self.good_data)
        self.assertTrue(form.is_valid())

    def test_form_creates_object(self):
        form = UserRegisterForm(data=self.good_data)
        form.is_valid()
        form.save()
        user = get_user_model().objects.get(username=self.good_data['username'])
        assert user.email == self.good_data['email']
        # test password by getting the user through login with u/n and password, assert same user:
        authenticated_user = authenticate(username=self.good_data['username'], password=self.good_data['password1'])
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(user.pk, authenticated_user.pk)

    def test_all_fields_required(self):
        for field in self.good_data.keys():
            bad_data = {**self.good_data}
            bad_data.pop(field)
            form = UserRegisterForm(data=bad_data)
            self.assertFalse(form.is_valid())
            self.assertIn(field, form.errors)
            self.assertIn('required', form.errors[field][0])

    def test_email_validation(self):
        """Not strictly necessary because this is a built-in field provided by Django,
        but this gives some examples for the range of unit tests you would put in, especially
        if you had any custom validation, like a birthday and min age, etc.
        """
        for bad_email in [
            'no_at_sign',
            'notld@somewhere',
            '@nousername.com',
            'toolong'*50 + '@example.com',
        ]:
            bad_data = {**self.good_data, 'email': bad_email}
            form = UserRegisterForm(data=bad_data)
            self.assertFalse(form.is_valid())
            self.assertIn('email', form.errors)
            self.assertIn('Enter a valid email address.', form.errors['email'][0])
