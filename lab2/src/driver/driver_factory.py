from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from .singleton import singleton


@singleton
class DriverFactory:
    def __init__(self, browser):
        self.browser = browser
        self.driver = None

    def get_driver_instance(self):
        if self.browser == "firefox":
            self.driver = webdriver.Firefox(GeckoDriverManager().install())
        elif self.browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            print('Unsupported driver!')

        return self.driver




