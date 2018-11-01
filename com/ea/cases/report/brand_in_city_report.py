import unittest
from com.ea.pages import brand_in_city_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""按省区各品牌投放城市"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    start_date = '2018-01-01'
    end_date = '2018-01-31'
    count = '294'

    @classmethod
    def setUpClass(cls):
        cls.webdriver = tools.get_chrome_driver()
        web_login.login(cls.webdriver)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.webdriver.quit()

    def test_brand_in_city(self):
        u"""按省区各品牌投放城市"""
        casename = sys._getframe().f_code.co_name
        try:
            brandincitypage = brand_in_city_page.BrandInCityPage(self.webdriver)
            url = brandincitypage.get_url()
            self.webdriver.get(url)
            brandincitypage.input_loan_date_start(self.start_date)
            brandincitypage.input_loan_date_end(self.end_date)
            brandincitypage.click_search_button()
            time.sleep(5)
            brandincitypage.page_down()
            time.sleep(1)
            assert self.count == brandincitypage.get_count()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
