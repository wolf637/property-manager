from tests.UI.page_objects import UI_map

from .page_objects.homepage import HomePage
from .base import TestClassBase
import time

class TestLogin(TestClassBase):


    def test_signup(self):
        # If user logged in => log her out

        # Sign up

        # Assert that logged in
        pass

    def test_login(self):

        # If user logged in => log her out

        # Log in with credentials of existing user

        # Make sure user logged in

        homepage = HomePage(self.driver)
        print("Home url: {}".format(self.driver.current_url))
        loginpage = homepage.login()
        loginpage.login()

    def test_logout(self):

        pass

    def test_invalid_credentials(self):

        pass




