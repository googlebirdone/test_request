from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium_po.page.choose_page import *
from appium_po.page.search_page import *


class HomePage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        # if self.wait_element_appear(By.ID, "image_cancel"):
        #     self.driver.find_element(By.ID, "image_cancel").click()
        # else:
        self.wait_element_appear(By.ID, "user_profile_icon")

    def wait_element_appear(self, method, name):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((method, name))
        )
        if name in self.driver.page_source:
            return True
        else:
            return False

    def goto_search(self):
        self.wait_element_appear(By.XPATH, "//*[contains(@resource-id, 'home_search')]")
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'home_search')]").click()
        return SearchPage(self.driver)

    def goto_own_add(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='自选']").click()   #"snb_tip_text"
        return ChoosePage(self.driver)
