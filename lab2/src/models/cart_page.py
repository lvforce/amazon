from .base import Base
from lab2.src.utils.locators import AmazonCartPage


class CartManager(Base):

    def processed_to_checkout(self):
        self.find_element(AmazonCartPage.CHECKOUT).click()

