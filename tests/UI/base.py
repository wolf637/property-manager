from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.UI.page_objects.UI_map import BASE_URL

WAIT_TIME = 10

class TestClassBase(object):

    @classmethod
    def setup_class(cls):
        "Runs once per class"
        # TODO Change path on server


        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # cls.driver = webdriver.Chrome('/Users/avolkov/Documents/05_Development/PMA/property_manager/tests/UI/drivers/mac/chromedriver')
        cls.driver = webdriver.Chrome('/home/pmadmin/property-manager-project/property-manager/tests/UI/drivers/linux/chromedriver')
        cls.driver.get(BASE_URL)

        # TODO common steps
        # Logout if logged in
        # Log in with test credentials


    @classmethod
    def teardown_class(cls):
        "Runs at end of class"
        cls.driver.quit()

