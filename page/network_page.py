from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):
    # 更多
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 移动网络
    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    # 首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2G
    g2_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3G
    g3_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        self.driver = driver
        BaseAction.__init__(self,driver) # 父类的初始化方法

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.find_element1(self.more_button).click()
        self.click(self.more_button)

    def click_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.find_element1(self.network_button).click()
        self.click(self.network_button)

    def click_first_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.find_element1(self.first_network_button).click()
        self.click(self.first_network_button)

    def click_2g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        # self.find_element1(self.g2_button).click()
        self.click(self.g2_button)

    def click_3g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        # self.find_element1(self.g3_button).click()
        self.click(self.g3_button)

    # 自定义一个 find_element方法
    def find_element1(self, clo):
        return self.driver.find_element(clo[0], clo[1])
