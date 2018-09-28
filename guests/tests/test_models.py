from django.test import TestCase
from guests.models import Guest

TEST_FIRST_NAME = 'John'
TEST_LAST_NAME = 'Doe'
TEST_EMAIL = 'john.doe@gmail.com'
TEST_PHONE = '1234567890'
FIRST_NAME_MAX_LENGTH = 80
LAST_NAME_MAX_LENGTH = 80


class GuestModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.guest = Guest.objects.create(first_name=TEST_FIRST_NAME,
                             last_name=TEST_LAST_NAME,
                             email=TEST_EMAIL,
                             phone=TEST_PHONE)

    def test_first_name(self):
        self.assertEquals(self.guest.first_name, TEST_FIRST_NAME)

    def test_first_name_max_length(self):
        max_length = self.guest._meta.get_field('first_name').max_length
        self.assertEquals(max_length, FIRST_NAME_MAX_LENGTH)


    def test_last_name(self):
        self.assertEquals(self.guest.last_name, TEST_LAST_NAME)

    def test_last_name_max_length(self):
        max_length = self.guest._meta.get_field('last_name').max_length
        self.assertEquals(max_length, LAST_NAME_MAX_LENGTH)

    def test_email(self):
        self.assertEquals(self.guest.email, TEST_EMAIL)

    def test_phone(self):
        self.assertEquals(self.guest.phone, TEST_PHONE)


    def test_string_representation(self):
        expected_str = f'{TEST_LAST_NAME}, {TEST_FIRST_NAME}'
        self.assertEquals(str(self.guest), expected_str)