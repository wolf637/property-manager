from tests.UI.page_objects import UI_map
from tests.UI.page_objects.UI_map import BASE_URL
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
        self.driver.get(BASE_URL)
        homepage = HomePage(self.driver)
        loginpage = homepage.login()
        time.sleep(10)
        loginpage.login()





