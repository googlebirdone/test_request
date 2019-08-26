from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword):
        self.driver.find_element(By.ID, "search_input_text").send_keys(keyword)
        return self

    def select(self, index):
        self.driver.find_elements(By.ID, "name")[index].click()
        return self

    def goto_own_page(self):
        from appium_po.page.choose_page import ChoosePage
        self.driver.find_element(By.ID, "action_close").click()
        return ChoosePage(self.driver)

    def add_code(self, stock_type):
        text = self.get_status(stock_type)
        if text == "加自选":
            self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'stockCode') and "
                                               "@text='%s']/../../..//*[contains"
                                               "(@resource-id, 'follow_btn')]" % stock_type).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.ID, "md_buttonDefaultNegative")))
        if "下次再说" in self.driver.page_source:
            self.driver.find_element(By.ID, "md_buttonDefaultNegative").click()

        return self

    def delete_code(self, stock_type):
        text = self.get_status(stock_type)
        if text == "已添加":
            self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'stockCode') and "
                                               "@text='%s']/../../..//*[contains"
                                               "(@resource-id, 'follow_btn')]" % stock_type).click()
        return self

    def get_status(self, stock_type):
        text = self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'stockCode') and "
                                                  "@text='%s']/../../..//*[contains"
                                                  "(@resource-id, 'follow_btn')]" % stock_type).text
        return text







