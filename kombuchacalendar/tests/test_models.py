from kombuchacalendar.models import Batch
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


def set_up_test_user():
    test_user = User.objects.create_user({'username': 'johnjohn',
                                          'email': 'john@john.com',
                                          'password1': 'XD78xd87!',
                                          'password2': 'XD78xd87!'})
    test_user.save()
    return test_user


class BatchModelTest(TestCase):
    test_user = None

    @classmethod
    def setUpTestData(cls):
        cls.test_user = set_up_test_user()
        cls.test_batch = Batch.objects.create(brewer=cls.test_user,
                                              name='Test Batch',
                                              description='This is a test description.',
                                              date_brewed=timezone.now(),
                                              starter_type='k',
                                              archive=False,)

    def test_starter_type_verbose(self):
        self.assertEqual(self.test_batch.starter_type_verbose(), 'Kombucha')

    def test_date_brewed_format(self):
        current_date = timezone.now().strftime('%b %-d, %Y')
        self.assertEqual(self.test_batch.date_brewed_display, current_date)

    def test_get_absolute_url(self):
        self.assertEqual(self.test_batch.get_absolute_url(), '/kombuchacalendar/batch/1/')

    def test_str(self):
        expected_batch_name = f'{self.test_batch.name}({self.test_batch.get_starter_type_display()}):{self.test_batch.date_brewed_display}'
        self.assertEqual(str(self.test_batch), expected_batch_name)
