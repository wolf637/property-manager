from tests.UI.page_objects import UI_map

from .page_objects.homepage import HomePage
from .base import TestClassBase
import time

class TestLogin(TestClassBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.homepage = HomePage(cls.driver)

    def test_signup(self):
        # If user logged in => log her out

        # Sign up

        # Assert that logged in
        pass

    def test_login(self):

        # If user logged in => log her out

        # Log in with credentials of existing user

        # Make sure user logged in
        loginpage = self.homepage.login()
        loginpage.login()
        loginpage.logout()

    def test_logout(self):
        loginpage = self.homepage.login()
        loginpage.login()
        loginpage.logout()

        assert loginpage.is_logged_out() == True

    def test_invalid_credentials(self):

        pass




