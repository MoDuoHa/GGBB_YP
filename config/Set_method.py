from selenium.webdriver.common.by import By
from selenium import webdriver
from GGBB_YP.base.base_page import BasePage


class Set_method(BasePage):
    driver = None

    @classmethod  # ���÷�������Ϊ�༶��������ֱ�����������ü��ɣ�����Ҫʵ����
    def get_webdriver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            # cls.driver.maximize_window()
            # cls.driver.get('http://8.136.104.56:8082/#/login')
            cls.driver.implicitly_wait(15)
        return cls.driver

    def login(self):
        self.driver.find_element_by_xpath('')
        self.driver.find_element_by_xpath()
