from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod

# Time to wait for element visibility or clickability
WAIT_TIME = 10


class BasePage(object):
    """Base page object with methods representing selenium interactions with some arbitrary web page"""

    def __init__(self, driver):
        """Initializes the page object"""
        self.driver = driver
        self.wait_time = WAIT_TIME
        self._verify_page()

    @abstractmethod
    def _verify_page(self):
        """Verifies that we landed on the expected page"""
        return

    def wait_for_element_visibility(self, locator_mode, locator):
        """Get element after verifying that it is visible

        Args:
            locator_mode: str, type of the strategy to locate an element (id, name, xpath, css)
            locator: str, locator of the element

        Raises: Exception

        Returns: element

        """
        element = None
        if locator_mode == 'id':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.visibility_of_element_located((By.ID, locator)))
        elif locator_mode == 'name':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.visibility_of_element_located((By.NAME, locator)))
        elif locator_mode == 'xpath':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.visibility_of_element_located((By.XPATH, locator)))
        elif locator_mode == 'css':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            raise Exception("Unsupported locator strategy: {0}.".format(locator_mode))

        return element

    def wait_until_element_clickable(self, locator_mode, locator):
        """Get element after verifying that it is clickable

        Args:
            locator_mode: str, type of the strategy to locate an element (id, name, xpath, css)
            locator: str, locator of the element

        Raises: Exception

        Returns: element

        """
        element = None
        if locator_mode == 'id':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.element_to_be_clickable((By.ID, locator)))
        elif locator_mode == 'name':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.element_to_be_clickable((By.NAME, locator)))
        elif locator_mode == 'xpath':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.element_to_be_clickable((By.XPATH, locator)))
        elif locator_mode == 'css':
            element = WebDriverWait(self.driver, self.wait_time). \
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        else:
            raise Exception("Unsupported locator strategy: {0}.".format(locator_mode))

        return element

    def find_element(self, locator_mode, locator):
        """Finds an element by specified locator

        Args:
            locator_mode: str, type of the strategy to locate an element (id, name, xpath, css)
            locator: str, locator of the element

        Raises: Exception

        Returns: element

        """
        element = None
        if locator_mode == 'id':
            element = self.driver.find_element_by_id(locator)
        elif locator_mode == 'name':
            element = self.driver.find_element_by_name(locator)
        elif locator_mode == 'xpath':
            element = self.driver.find_element_by_xpath(locator)
        elif locator_mode == 'css':
            element = self.driver.find_element_by_css_selector(locator)
        else:
            raise Exception("Unsupported locator strategy: {0}.".format(locator_mode))

        return element

    def fill_out_field(self, locator_mode, locator, text):
        """Clears out text field and then fills it out

        Args:
            locator_mode: str, type of the strategy to locate an element (id, name, xpath, css)
            locator: str, locator of the element
            text: str, text to enter into textfield
        """
        self.find_element(locator_mode, locator).clear()
        self.find_element(locator_mode, locator).send_keys(text)

    def click(self, locator_mode, locator):
        """Clicks on element

        Args:
            locator_mode: str, type of the strategy to locate an element (id, name, xpath, css)
            locator: str, locator of the element

        """
        self.wait_until_element_clickable(locator_mode, locator).click()


class IncorrectPageException(Exception):
    """This exception is raised when incorrect page is instantiated."""