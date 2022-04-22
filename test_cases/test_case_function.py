#测试用例的设计
from time import sleep
from selenium import webdriver
from GGBB_YP.page_object.Login_page import LoginPage
from GGBB_YP.page_object.index_page import IndexPages
from ddt import ddt, file_data , data, unpack
import pytest
from GGBB_YP.config.yamlload import loadyaml


class TestCase():
    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPages(cls.driver)


    def tearDownClass(cls) -> None:
        cls.driver.quit()


    @pytest.mark.parametrize('udata',loadyaml('../data/user.yaml'))
    def test_1_login(self,udata):
        assert self.lp.login(udata['username'],udata['password'])
        sleep(1)


    @pytest.mark.parametrize('utxt',loadyaml('../data/test.yaml'))
    def test_2_search(self,utxt):
        assert self.ip.search(utxt['txt'])
        sleep(1)

if __name__ == '__main__':
    pytest.main()


