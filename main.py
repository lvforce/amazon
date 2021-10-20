from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def search_amazon(item):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.amazon.com')
    driver.find_element_by_id('twotabsearchtextbox').send_keys(item)
    driver.find_element_by_id("nav-search-submit-text").click()
    time.sleep(3)

search_amazon('iphone 13')