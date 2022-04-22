'''

  index_page页面对象，实现搜索
'''
from selenium.webdriver.common.by import By
from selenium import webdriver
from GGBB_YP.base.base_page import BasePage
from GGBB_YP.page_object import  Login_page
from GGBB_YP.page_object.Login_page import LoginPage

class IndexPages(BasePage):

    #核心元素
    url = 'http://127.0.0.1:8888/yp/#/console'

    search_input=(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/input')
    search_button=(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
    search_Assert=(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[5]/div/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/span')


    #核心业务流
    def search(self,txt):

        self.visit()
        #self.login2('admin','123')
        self.sleep(1)
        self.input_(self.search_input,txt)
        self.click(self.search_button)
        self.sleep(2)
        if self.text(self.search_Assert) == txt:
            return True
        else:
            return False

if __name__ == '__main__':
    driver = webdriver.Chrome()

    txt = '毕润'
    ip = IndexPages(driver)
    ip.search(txt)

