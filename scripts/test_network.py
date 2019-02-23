import os,sys
sys.path.append(os.getcwd())
from appium import webdriver
from time import  sleep
from base.base_driver import init_driver
from page.network_page import NetworkPage
class TestNetwork:
    def setup(self):
        self.driver =init_driver()
        self.network_page=NetworkPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_mobile_network_2g(self):
        # 更多
        self.network_page.click_more()
        # 移动网络
        self.network_page.click_network()
        # 首选网络类型
        self.network_page.click_first_network()
        # 2G
        self.network_page.click_2g()

        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_mobile_network_3g(self):
        # 更多
        self.network_page.click_more()
        # 移动网络
        self.network_page.click_network()
        # 首选网络类型
        self.network_page.click_first_network()
        # 3G
        self.network_page.click_3g()

        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()




