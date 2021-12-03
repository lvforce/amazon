import time
from lab2.config import Config
from lab2.src.models.base_page import AmazonBaseManager
from lab2.src.models.select_page import AmazonSelectManager
from lab2.src.models.cart_page import CartManager


def test_amazon_page(browser):
    amazon_page = AmazonBaseManager(browser, 'https://www.amazon.com/')
    alive = amazon_page.is_browser_alive(browser)
    assert Config.IS_ALIVE == alive
    amazon_page.get_page()
    amazon_page.search_item('iphone 12')
    select = AmazonSelectManager(browser, browser.current_url)
    select.select_item()
    select.select_more_item()
    select.add_more()
    select.add_to_cart()
    cart = select.check_cart_has_product()
    assert Config.CART_ITEMS == cart
    time.sleep(2)
    select.get_cart()
    time.sleep(2)
    cart = CartManager(browser, browser.current_url)
    cart.processed_to_checkout()
    time.sleep(2)




