from telnetlib import EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Opps Can\'t find element by locator {locator}')

    def get_page(self):
        self.browser.implicitly_wait(3)
        self.browser.maximize_window()
        return self.browser.get(self.url)
