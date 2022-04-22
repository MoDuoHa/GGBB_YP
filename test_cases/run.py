#coding:utf-8
#生成测试报告allure测试报告
#1.安装allure-pytest
#2.下载一个commandline包
#3.配置环境变量
import os
import pytest


if __name__ == '__main__':
    #执行测试用例获得测试数据
    pytest.main(['-s','test_case_function.py','--alluredir','./allure-results'])
    #生成测试报告，找的测试户籍 生成测试报告的目录

    os.system('allure generate  ./allure-results -o ./reports --clean')
   #小型的测试框架,关键字驱动,数据驱动,yaml,pytest/unittest
   #日志,特殊元素,下拉框,ifram,数据库,断言