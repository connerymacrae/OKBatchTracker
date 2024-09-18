from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.forms import UserRegisterForm


class TestSignupView(TestCase):

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.view_name, 'signup')

    def test_signup_url_reverse_resolves_from_name(self):
        url = reverse('signup')
        self.assertEqual(url, '/accounts/signup/')

    def test_signup_view_gets_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html',
                                "View returned incorrect template template")
        # ensure each field is correctly rendered:
        for field_name, field in UserRegisterForm().fields.items():
            # if a label is not specified, django converts _ to space and capitalizes the first letter
            label = field.label or field_name.title().replace('_', ' ')
            # the label should be rendered in the response
            self.assertContains(response, f'<label for="id_{field_name}">{label}:</label>')

    def test_signup_view_shows_errors_for_invalid_form(self):
        """Only testing one invalid form, as form tests are covered elsewhere"""
        invalid_form = UserRegisterForm(data={
            'username': 'test-invalid',
            'email': ''
        })
        self.assertFalse(invalid_form.is_valid())
        response = self.client.post(reverse('signup'), data=invalid_form.data)
        self.assertEqual(response.status_code, 200, "should return the same page")
        self.assertContains(response, 'This field is required.')
        self.assertTemplateUsed(response, 'registration/signup.html')
        # should not create an object:
        self.assertFalse(get_user_model().objects.filter(username='test-invalid').exists())

    def test_signup_view_creates_user_for_valid_form(self):
        valid_form = UserRegisterForm(data={
            'username': 'test-valid',
            'email': 'test@example.com',
            'password1': '123ABCabc!',
            'password2': '123ABCabc!'})
        self.assertTrue(valid_form.is_valid())
        response = self.client.post(reverse('signup'), data=valid_form.data)
        self.assertEqual(response.status_code, 302, "should redirect to login")
        follow_on_response = self.client.get(response.url)
        self.assertEqual(follow_on_response.status_code, 200)
        self.assertTemplateUsed(follow_on_response, 'registration/login.html', "Should redirect to login")
        self.assertEqual(get_user_model().objects.filter(username='test-valid').count(), 1)
