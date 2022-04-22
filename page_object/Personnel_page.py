# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from GGBB_YP.base.base_page import BasePage

class Personnel(BasePage):
    #核心元素

    url = 'http://127.0.0.1:8888/yp/#/basic'

    #增加
    z1 = (By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]/div[1]')
    #姓名
    z2 = (By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/form/div[1]/div/div/input')
    #身份证号码
    z3 = (By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/form/div[2]/div/div/input')
    #出生日期
    #z4 = (By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/form/div[4]/div/div/div/div')
    #工作信息
    z5=(By.XPATH,'//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[4]')
    #管理类别
    z6=(By.XPATH,'//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div')
    #其他
    z9=(By.XPATH,'/html/body/div[40]/ul[2]/li[5]')
    #人员管理状态
    z7=(By.XPATH,'//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div')
    #现职人员
    z10=(By.XPATH,'/html/body/div[41]/ul[2]/li[1]')
    #保存
    z8=(By.XPATH,'//*[@id="app"]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/i')


    #断言
    z11=(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[4]/div/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/span')

    z12=(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[4]/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/label/span/input')
    z13=(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]/div[2]/span')
    z14=(By.XPATH,'/html/body/div[40]/div[2]/div/div/div/div/div[3]/button[2]')
    #人员新增
    def added(self,name,carid,data,num,num2):

        self.login2('admin','123')
        self.visit()
        self.click(self.z1)
        self.input_(self.z2,name)
        self.input_(self.z3,carid)
        #self.input_(self.z4,data)
        self.click(self.z5)
        self.click(self.z6)
        self.click(self.z9)
        self.click(self.z7)
        self.click(self.z10)

        self.click(self.z8)

        if self.text(self.z11) == name:
            return True
        else:
            return False
    #人员删除
    def perdele(self):
        self.visit()
        self.click(self.z12)
        self.click(self.z13)
        self.sleep(1)
        self.click(self.z14)
#调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Personnel(driver)
    print(lp.added('李丽','365122199101010125','2020.02',1,2))
    lp.perdele()







