from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import url_home


class Test3:
    products_title = 'Products'

    def test_logout(self,login_open_sauce_demo):
        driver = login_open_sauce_demo
        driver.find_element(By.ID,'react-burger-menu-btn').click()
        menu_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, 'react-burger-cross-btn')))
        assert menu_element.is_displayed(), 'Botão fechar menu não apresentado'
        assert driver.find_element(By.CLASS_NAME,'bm-menu').is_displayed(), 'Menu não apresentado'

        driver.find_element(By.ID,'logout_sidebar_link').click()
        assert driver.current_url == url_home, 'Logout não realizado'





