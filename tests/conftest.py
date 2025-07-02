import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url_home = 'https://www.saucedemo.com/'
url_products = 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def open_sauce_demo():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.get(url_home)
    yield driver
    driver.quit()

@pytest.fixture()
def login_open_sauce_demo(open_sauce_demo):
    driver = open_sauce_demo
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == url_products, 'Pagina de produtos não apresentada'
    yield driver