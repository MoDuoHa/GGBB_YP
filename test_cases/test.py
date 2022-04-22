from selenium import webdriver

class test:
    def list(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        js_value = "document.getElementById('ivu-select-selection').value='{}'".format("2020-09-18")
        self.driver.execute_script(js_value)
        self.driver.quit()



        pass
