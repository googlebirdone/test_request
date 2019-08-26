from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.search_page import SearchPage
from appium_po.page.base_page import BasePage


class ChoosePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # if "新增手势切换、指标设置功能" in self.driver.page_source:
        #     width = self.driver.get_window_size()["width"]
        #     height = self.driver.get_window_size()["height"]
        #     self.driver.swipe(width/2, height/2, width/2, height*0.6)
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "snb_tip_text")))
        self.driver.implicitly_wait(5)
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        if "新增手势切换、指标设置功能" in self.driver.page_source:
            self.driver.tap([(width/2, height/2)])

    def goto_search(self):
        self.driver.find_element(By.ID, "action_search").click()
        return SearchPage(self.driver)

    def get_type(self, name):
        if name in self.driver.page_source:
            return True
        else:
            return False



