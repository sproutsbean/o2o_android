import unittest
from com.ea.pages import channel_business_count_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""渠道业务统计"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    start_date = '2018-01-01'
    end_date = '2018-01-31'
    expect_count = '323'
    business_count = '128'
    loan_count = '4610.00'

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

    def test_by_channel_agent(self):
        u"""渠道业务统计->按渠道经办人统计(总部)"""
        casename = sys._getframe().f_code.co_name
        try:
            channelagentpage = channel_business_count_page.ChannelAgent(self.webdriver)
            url = channelagentpage.get_url()
            self.webdriver.get(url)
            channelagentpage.input_loan_date_start(self.start_date)
            channelagentpage.input_loan_date_end(self.end_date)
            channelagentpage.click_search_button()
            time.sleep(3)
            channelagentpage.page_down()
            time.sleep(1)
            assert self.expect_count == channelagentpage.get_count()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_by_channel(self):
        u"""渠道业务统计->按渠道统计（管理层）"""
        casename = sys._getframe().f_code.co_name
        try:
            channelpage = channel_business_count_page.Channel(self.webdriver)
            url = channelpage.get_url()
            self.webdriver.get(url)
            channelpage.input_loan_date_start(self.start_date)
            channelpage.input_loan_date_end(self.end_date)
            channelpage.click_search_button()
            time.sleep(5)
            channelpage.page_down()
            time.sleep(1)
            assert self.business_count == channelpage.get_business_count()
            assert self.loan_count == channelpage.get_loan_count()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
