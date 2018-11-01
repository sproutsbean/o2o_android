import unittest
from com.ea.pages import loan_amount_by_time_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""按时间区间统计放款量"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    start_date = '2018-01-01'
    end_date = '2018-01-31'
    fangkuanzongbishu = '531'
    fangkuanzongjine = '21063.00'
    xinkehufangkuanzongbishu = '292'
    xinkehufangkuanzongjine = '11553.00'
    bank_fangkuanzongjine = '21,063.00'
    bank_xinkehufangkuanzongjine = '11,553.00'

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

    def test_loan_amount_by_loanmanager(self):
        u"""按时间区间统计放款量->按信贷经理统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            managerpage = loan_amount_by_time_page.LoanAmountByManager(self.webdriver)
            url = managerpage.get_url()
            self.webdriver.get(url)
            managerpage.input_loan_date_start(self.start_date)
            managerpage.input_loan_date_end(self.end_date)
            managerpage.click_search_button()
            time.sleep(5)
            managerpage.page_down()
            time.sleep(1)
            assert self.fangkuanzongbishu == managerpage.get_fangkuanzongbishu()
            assert self.fangkuanzongjine == managerpage.get_fangkuanzongjine()
            assert self.xinkehufangkuanzongbishu == managerpage.get_xinkehufangkuanzongbishu()
            assert self.xinkehufangkuanzongjine == managerpage.get_xinkehufangkuanzongjine()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_amount_by_team(self):
        u"""按时间区间统计放款量->按团队统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            teampage = loan_amount_by_time_page.LoanAmountByTeam(self.webdriver)
            url = teampage.get_url()
            self.webdriver.get(url)
            teampage.input_loan_date_start(self.start_date)
            teampage.input_loan_date_end(self.end_date)
            teampage.click_search_button()
            time.sleep(5)
            teampage.page_down()
            time.sleep(1)
            assert self.fangkuanzongbishu == teampage.get_tuanduifangkuanzongbishu()
            assert self.fangkuanzongjine == teampage.get_tuanduifangkuanzongjine()
            assert self.xinkehufangkuanzongbishu == teampage.get_xinkehufangkuanzongbishu()
            assert self.xinkehufangkuanzongjine == teampage.get_xinkehufangkuanzongjine()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_amount_by_province(self):
        u"""按时间区间统计放款量->按省区统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            provincepage = loan_amount_by_time_page.LoanAmountByProvince(self.webdriver)
            url = provincepage.get_url()
            self.webdriver.get(url)
            provincepage.input_loan_date_start(self.start_date)
            provincepage.input_loan_date_end(self.end_date)
            provincepage.click_search_button()
            time.sleep(5)
            provincepage.page_down()
            time.sleep(1)
            assert self.fangkuanzongbishu == provincepage.get_fangkuanzongbishu()
            assert self.fangkuanzongjine == provincepage.get_fangkuanzongjine()
            assert self.xinkehufangkuanzongbishu == provincepage.get_xinkehufangkuanzongbishu()
            assert self.xinkehufangkuanzongjine == provincepage.get_xinkehufangkuanzongjine()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_amount_by_bank(self):
        u"""按时间区间统计放款量->按放款银行统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            bankpage = loan_amount_by_time_page.LoanAmountByBank(self.webdriver)
            url = bankpage.get_url()
            self.webdriver.get(url)
            bankpage.input_loan_date_start(self.start_date)
            bankpage.input_loan_date_end(self.end_date)
            bankpage.click_search_button()
            time.sleep(5)
            bankpage.page_down()
            time.sleep(1)
            assert self.fangkuanzongbishu == bankpage.get_fangkuanzongbishu()
            assert self.bank_fangkuanzongjine == bankpage.get_fangkuanzongjine()
            assert self.xinkehufangkuanzongbishu == bankpage.get_xinkehufangkuanzongbishu()
            assert self.bank_xinkehufangkuanzongjine == bankpage.get_xinkehufangkuanzongjine()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
