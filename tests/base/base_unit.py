from django.test import TestCase
from django.contrib.auth.models import User
from properties.models import Property
import tests.base.base_settings as base_settings
from django.test import Client

class BaseUnitTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.settings = base_settings
        cls.admin = User.objects.create_user(username=base_settings.TEST_ADMIN_USERNAME,
                                             password=base_settings.TEST_ADMIN_PASSWORD)
        cls.property = Property.objects.create(
            user=cls.admin,
            name=base_settings.TEST_PROPERTY_NAME,
            picture=base_settings.TEST_PICTURE)
        cls.client = Client()
        cls.client.login(username=base_settings.TEST_ADMIN_USERNAME, password=base_settings.TEST_ADMIN_PASSWORD)

    def login(self):
        self.client.login(username=base_settings.TEST_ADMIN_USERNAME,
                          password=base_settings.TEST_ADMIN_PASSWORD)

    def logout(self):
        self.client.logout()