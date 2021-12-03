from .base import Base
import time
from lab2.src.utils.locators import AmazonStartPage


class AmazonBaseManager(Base):

    def search_item(self, item):
        self.find_element(AmazonStartPage.INPUT_BAR).send_keys(item)
        self.find_element(AmazonStartPage.SEARCH_BUTTON).click()
        time.sleep(3)

    @staticmethod
    def is_browser_alive(browser):
        try:
            if browser.current_url:
                return True
        except:
            return False



