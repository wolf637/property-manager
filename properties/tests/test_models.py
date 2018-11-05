from django.test import TestCase
from django.contrib.auth.models import User
from properties.models import Property

TEST_PROPERTY_NAME = 'test_property_name'
TEST_PROPERTY_NAME_MAX_LENGTH = 80
TEST_ADMIN_USERNAME = 'test_property_admin'
TEST_ADMIN_PASSWORD = 'test_password'
TEST_PICTURE = 'test_image.png'

class GuestModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.admin = User.objects.create_user(username=TEST_ADMIN_USERNAME, password=TEST_ADMIN_PASSWORD)
        cls.property = Property.objects.create(
            user=cls.admin,
            name=TEST_PROPERTY_NAME,
            picture=TEST_PICTURE
        )

    def test_property_name(self):
        self.assertEquals(self.property.name, TEST_PROPERTY_NAME)

    def test_name_max_length(self):
        max_length = self.property._meta.get_field('name').max_length
        self.assertEquals(max_length, TEST_PROPERTY_NAME_MAX_LENGTH)

    def test_picture(self):
        self.assertEquals(self.property.picture, TEST_PICTURE)

    def test_string_representation(self):
        self.assertEquals(str(self.property), TEST_PROPERTY_NAME)