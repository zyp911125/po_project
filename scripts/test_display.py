import os, sys

import pytest

sys.path.append(os.getcwd())
from appium import webdriver
from time import sleep
from base.base_driver import init_driver
from page.display_page import DisplayPage
from base.base_yaml import yaml_data_with_file


class TestDisplay:

    def data_with_key(key):
        return yaml_data_with_file("display_data")[key]

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def teardown(self):
        self.driver.quit()


    @pytest.mark.parametrize("content",data_with_key("test_mobile_display_input"))
    def test_mobile_display_input(self,content):
        # 点击显示
        self.display_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.click_text(content)
        # 点击返回
        self.display_page.click_back()

    @pytest.mark.parametrize("content", data_with_key("test_mobile_display_input1"))
    def test_mobile_display_input1(self,content):
        # 点击显示
        self.display_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
         # 输入文字
        self.display_page.click_text(content)
        # 点击返回
        self.display_page.click_back()
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
