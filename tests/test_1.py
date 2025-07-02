from selenium.webdriver.common.by import By
from conftest import url_home

# url = 'https://www.saucedemo.com/'
# btn_login = (By.ID, 'login-button')
#
# driver = webdriver.Chrome()
# driver.get(url)
# driver.find_element(By.ID, 'login-button').click()
# error_msg_element = driver.find_element(By.CLASS_NAME, 'error-message-container')
# # assert driver.current_url == url, 'Pagina não encontrada'
# # assert error_msg_element.is_displayed(), 'Mensagem de erro não exibida!'
# # assert error_msg_element.text == 'Epic sadface: Username is required', 'Mensagem de erro não exibida'
#
# time.sleep(5)
# driver.quit()

class Test1:


    #POS CONDIÇÂO/TEARDOWN ------
    # @pytest.fixture
    # def close_browser(self,open_sauce_demo):
    #     #print('3')
    #     yield
    #     #print('4')
    #     driver = open_sauce_demo
    #     time.sleep(5)
    #     driver.quit()
    #------------

    #def test_click_login_button(self, open_sauce_demo, close_browser)
    #close_browser estava na anteriormente na chamada do metodo por conta
    #da segunda fixture não mais necessária

    # PASSOS DE TESTE
    def test_click_login_button(self, open_sauce_demo):
        #print('5')
        driver = open_sauce_demo
        driver.find_element(By.ID, 'login-button').click()
        error_msg_element = driver.find_element(By.CLASS_NAME, 'error-message-container')
        assert driver.current_url == url_home, 'Pagina não encontrada'
        assert error_msg_element.is_displayed(), 'Mensagem de erro não exibida!'
        assert error_msg_element.text == 'Epic sadface: Username is required', 'Mensagem de erro não exibida'

        #driver.save_screenshot('./prints/screenshot.png')
        #print('6')
    #-------