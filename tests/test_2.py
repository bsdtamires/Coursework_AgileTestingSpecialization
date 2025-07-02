from selenium.webdriver.common.by import By
from conftest import url_products

class Test2:
    products_title = 'Products'

    def test_login(self,open_sauce_demo):
        driver = open_sauce_demo
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        driver.find_element(By.ID,'password').send_keys('secret_sauce')
        driver.find_element(By.ID,'login-button').click()
        assert driver.current_url == url_products, 'Página de produtos não apresentada'
        assert driver.find_element(By.CLASS_NAME,'title').text == self.products_title, 'Título não encontrado'