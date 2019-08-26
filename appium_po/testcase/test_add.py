"""
func : 股票自选测试
"""
from selenium.webdriver.common.by import By
from appium_po.page.driver_xueqiu import XueQiu
from appium_po.page.home_page import HomePage
from appium_po.page.search_page import SearchPage


class TestAdd:
    def setup_method(self):
        self.add = HomePage()
        # self.own = SearchPage()

    def teardown_method(self):
        pass

    def test_success(self):
        status = self.add.goto_own_add().goto_search().search("阿里").select(0).add_code("BABA").\
            goto_own_page().get_type("BABA")
        assert status == True

    def test_added(self):
        text = self.add.goto_own_add().goto_search().search("阿里").select(0).get_status("BABA")
        assert text == "已添加"

    def test_deleted(self):
        text = self.add.goto_own_add().goto_search().search("阿里").select(0).get_status("BABA")
        assert text == "加自选"
