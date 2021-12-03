from selenium.webdriver.common.by import By


class AmazonStartPage:
    INPUT_BAR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
    ITEM = 'iphone 13'


class AmazonSelectPage:
    ITEM = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div['
                      '2]/div/div/div[1]/h2/a')
    ADD_MORE_BUTTON = (By.XPATH, '//*[@id="a-autoid-0-announce"]')
    SELECT_MORE = (By.XPATH, '//*[@id="quantity_1"]')
    ADD_TO_CART = (By.XPATH, '//*[@id="add-to-cart-button"]')
    CART = (By.XPATH, '//*[@id="nav-cart"]')
    CART_CHECK = (By.XPATH, '//*[@id="nav-cart-count"]')


class AmazonCartPage:
    ADD_BUTTON = (By.XPATH, '//*[@id="a-autoid-0-announce"]')
    CHECKOUT = (By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[2]/div/form/div/div/span/span/input')