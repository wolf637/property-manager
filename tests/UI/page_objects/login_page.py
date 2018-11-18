from .pagebase import BasePage, IncorrectPageException
from . import UI_map
import time

class LoginPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def _verify_page(self):
        """Verifies that we landed on the expected page"""
        try:
            self.wait_for_element_visibility('css', UI_map.LOGIN['email_textfield'])
            self.wait_for_element_visibility('css', UI_map.LOGIN['password_textfield'])
        except:
            raise IncorrectPageException

    def login(self):

        self.fill_out_field('css', UI_map.LOGIN['email_textfield'], 'alexvolkov.jobsearch@gmail.com')
        self.fill_out_field('css', UI_map.LOGIN['password_textfield'], '123')
        self.click('css', UI_map.LOGIN['login_button'])

        return

    def logout(self):

        self.click('css', UI_map.LOGIN['logout_button'])


    def is_logged_out(self):

        self.wait_for_element_visibility('css', UI_map.HOME['signup_button'])
        self.wait_for_element_visibility('css', UI_map.HOME['login_button'])

        return True