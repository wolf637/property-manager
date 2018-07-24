from .pagebase import BasePage, IncorrectPageException
from . import UI_map
from .UI_map import BASE_URL
from .login_page import LoginPage

class HomePage(BasePage):


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def _verify_page(self):
        """Verifies that we landed on the expected page"""
        try:
            print("Base URL: {}".format(BASE_URL))
            self.wait_for_element_visibility('css', UI_map.HOME['welcome_h1'])

        except:
            raise IncorrectPageException

    def home(self):
        print("Base URL: {}".format(BASE_URL))
        self.driver.get(BASE_URL)

    def login(self):
        self.click('css', UI_map.HOME['login_button'])
        return LoginPage(self.driver)