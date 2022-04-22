#conding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium import  webdriver
from time import sleep

class BasePage:
    #构造函数
    def __init__(self,driver):
        self.driver = driver
        #self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        #self.driver.maximize_window()


    #访问url
    def visit(self):
        self.driver.get(self.url)

    #元素定位
    def locator(self,loc):
        ele = WebDriverWait(self.driver,10).until(lambda x:x.find_element(*loc))
        self.driver.execute_script("arguments[0].style.border=\'3px solid red\'", ele)
        return ele
        #return self.driver.find_element(*loc)

    #输入
    def input_(self,loc,txt):
        self.locator(loc).send_keys(txt)

    #点击
    def click(self,loc):
        self.locator(loc).click()

    #文本
    def text(self,loc):
        return self.locator(loc).text

    def sleep(self,s):
        sleep(s)

    #查找数据库

   #iframe表格进入
    def iframe_in(self,loc):
       self.driver.switch_to.frame(self.locator(loc))

    #iframe表格退出
    def iframe_out(self):
       self.driver.switch_to.default_content()

    #下拉框
    def drop(self,ele,num):
        from selenium.webdriver.support.select import Select
        # 实例化一个select类的对象
        selector = Select(self.locator(ele))
        selector.select_by_index(num)

    def login2(self,user,pwd):
        self.driver.get('http://127.0.0.1:8888/yp')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/form/div[1]/div/div/input').send_keys(
            user)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/form/div[2]/div/div/input').send_keys(
            pwd)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/form/div[3]/div').click()
        time.sleep(1)

    def js(self):
        js = """
                    var date = document.querySelectorAll('.ivu-form-item:nth-of-type(5) .ivu-input-with-suffix');
                    date.readOnly = false;
                    date.value = arguments[0];
                 """
        self.driver.execute_script(js, "2022.01")

    #断言
    def Assert(self,a,b):
     try:
        if self.text(a) == b:
            return True
        else:
            return False
     except Exception as e:
         print(e)
         return False



