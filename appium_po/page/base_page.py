from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium_po.page.driver_xueqiu import XueQiu


class BasePage(XueQiu):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_appear(self, method, name):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((method, name))
        )
        if name in self.driver.page_source:
            return True
        else:
            return False


