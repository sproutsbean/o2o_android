import unittest
from com.ea.pages import operate_analysis_report_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""运营分析报表"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    start_date = '2018-01-01'
    end_date = '2018-01-31'
    apply_amount = '24,503.00'
    approve_amount = '21,063.00'
    fangkuan_amount = '21,063.00'
    before_loan_apply_amount = '14,456.00'

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

    def test_after_loan(self):
        u"""运营分析报表->业务运营分析（贷后数据）"""
        casename = sys._getframe().f_code.co_name
        try:
            afterloanpage = operate_analysis_report_page.AfterLoan(self.webdriver)
            url = afterloanpage.get_url()
            self.webdriver.get(url)
            afterloanpage.input_loan_date_start(self.start_date)
            afterloanpage.input_loan_date_end(self.end_date)
            afterloanpage.click_search_button()
            time.sleep(3)
            afterloanpage.page_down()
            time.sleep(1)
            assert self.apply_amount == afterloanpage.get_apply_amount()
            assert self.approve_amount == afterloanpage.get_approve_amount()
            assert self.fangkuan_amount == afterloanpage.get_fangkuan_amount()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_before_loan(self):
        u"""运营分析报表->业务运营分析（贷前数据）"""
        casename = sys._getframe().f_code.co_name
        try:
            beforeloanpage = operate_analysis_report_page.BeforeLoan(self.webdriver)
            url = beforeloanpage.get_url()
            self.webdriver.get(url)
            beforeloanpage.input_loan_date_start(self.start_date)
            beforeloanpage.input_loan_date_end(self.end_date)
            beforeloanpage.click_search_button()
            time.sleep(5)
            beforeloanpage.page_down()
            time.sleep(1)
            assert self.before_loan_apply_amount == beforeloanpage.get_apply_amount()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
