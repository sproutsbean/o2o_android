import unittest
from com.ea.pages import fangkuan_taizhang_report_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""贷款审批报表"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    start_date = '2018-01-01'
    end_date = '2018-01-31'
    count = '531'
    loan_count = '13,225.00'

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

    def test_loan_code_fangkuan_taizhang(self):
        u"""放款台账->贷款单放款台帐报表"""
        casename = sys._getframe().f_code.co_name
        try:
            loancodepage = fangkuan_taizhang_report_page.LoanCode(self.webdriver)
            url = loancodepage.get_url()
            self.webdriver.get(url)
            loancodepage.input_loan_date_start(self.start_date)
            loancodepage.input_loan_date_end(self.end_date)
            loancodepage.click_search_button()
            time.sleep(3)
            loancodepage.page_down()
            time.sleep(1)
            assert self.count == loancodepage.get_count()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_liutongdai_fangkuan_taizhang(self):
        u"""放款台账->流通贷放款台账查询"""
        casename = sys._getframe().f_code.co_name
        try:
            liutongdaipage = fangkuan_taizhang_report_page.LiutongdaiPage(self.webdriver)
            url = liutongdaipage.get_url()
            self.webdriver.get(url)
            liutongdaipage.input_loan_date_start(self.start_date)
            liutongdaipage.input_loan_date_end(self.end_date)
            liutongdaipage.click_search_button()
            time.sleep(5)
            liutongdaipage.page_down()
            time.sleep(1)
            assert self.loan_count == liutongdaipage.get_loan_count()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
