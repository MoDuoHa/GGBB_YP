
from selenium import webdriver
from selenium.webdriver.common.by import By
from GGBB_YP.base.base_page import BasePage

class LoginPage(BasePage):
    #核心元素

    url = 'http://47.110.70.19:8092/'
    user = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[1]/div/div/input')
    password = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/input')
    login_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div/button/span')
    text2 = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div')
    #核心业务流
    def login(self,username,pwd):
        self.visit()
        self.input_(self.user, username)
        self.input_(self.password, pwd)
        self.click(self.login_button)
        if self.text(self.text2) == '基本信息':
            return True
        else:
            return False


#调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = 'admin'
    password = '123'
    lp = LoginPage(driver)
    lp.login(username,password)







