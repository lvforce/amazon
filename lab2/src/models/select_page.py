from .base import Base
from lab2.src.utils.locators import AmazonSelectPage


class AmazonSelectManager(Base):

    def select_item(self):
        self.find_element(AmazonSelectPage.ITEM).click()

    def select_more_item(self):
        self.find_element(AmazonSelectPage.ADD_MORE_BUTTON).click()

    def add_more(self):
        self.find_element(AmazonSelectPage.SELECT_MORE).click()

    def add_to_cart(self):
        self.find_element(AmazonSelectPage.ADD_TO_CART).click()

    def get_cart(self):
        self.find_element(AmazonSelectPage.CART).click()

    def check_cart_has_product(self):
        cart = self.find_element(AmazonSelectPage.CART_CHECK)
        return cart.text
