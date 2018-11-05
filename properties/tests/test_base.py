from django.test import TestCase
from django.contrib.auth.models import User
from properties.models import Property
from .settings import *
from django.test import Client

class PropertyBaseTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.admin = User.objects.create_user(username=TEST_ADMIN_USERNAME, password=TEST_ADMIN_PASSWORD)
        cls.property = Property.objects.create(
            user=cls.admin,
            name=TEST_PROPERTY_NAME,
            picture=TEST_PICTURE)
        cls.client = Client()
        cls.client.login(username=TEST_ADMIN_USERNAME, password=TEST_ADMIN_PASSWORD)


    def login(self):
        self.client.login(username=TEST_ADMIN_USERNAME, password=TEST_ADMIN_PASSWORD)