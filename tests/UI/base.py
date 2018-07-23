from selenium import webdriver

WAIT_TIME = 10

class TestClassBase(object):

    @classmethod
    def setup_class(cls):
        "Runs once per class"
        cls.driver = webdriver.Chrome()


    @classmethod
    def teardown_class(cls):
        "Runs at end of class"
        cls.driver.quit()

