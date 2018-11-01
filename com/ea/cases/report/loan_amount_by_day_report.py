import unittest
from com.ea.pages import loan_amount_by_day_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""按天统计放款量"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    day = '2018-06-01'
    yesterday_newcustomer_loanamount = '810.00'
    yesterday_loanamount = '2210.00'
    newcustomer_loanamount = '150.00'
    loanamount = '790.00'
    pre_month_newcustomer_loanamount = '3890.00'
    pre_month_loanamount = '14619.00'

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

    def test_loan_amount_by_day_by_loanmanager(self):
        u"""按天统计放款量->按信贷经理统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            managerpage = loan_amount_by_day_page.LoanAmountByDayByManager(self.webdriver)
            url = managerpage.get_url()
            self.webdriver.get(url)
            managerpage.input_day(self.day)
            managerpage.click_search_button()
            time.sleep(5)
            managerpage.page_down()
            time.sleep(1)
            assert self.yesterday_newcustomer_loanamount == managerpage.get_yesterday_newcustomer_loanamount()
            assert self.yesterday_loanamount == managerpage.get_yesterday_loanamount()
            assert self.newcustomer_loanamount == managerpage.get_newcustomer_loanamount()
            assert self.loanamount == managerpage.get_loanamount()
            assert self.pre_month_newcustomer_loanamount == managerpage.get_pre_month_newcustomer_loanamount()
            assert self.pre_month_loanamount == managerpage.get_pre_month_loanamount()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_amount_by_day_by_team(self):
        u"""按天统计放款量->按团队统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            teampage = loan_amount_by_day_page.LoanAmountByDayByTeam(self.webdriver)
            url = teampage.get_url()
            self.webdriver.get(url)
            teampage.input_day(self.day)
            teampage.click_search_button()
            time.sleep(5)
            teampage.page_down()
            time.sleep(1)
            assert self.yesterday_loanamount == teampage.get_yesterday_team_loanamount()
            assert self.loanamount == teampage.get_team_loanamount()
            assert self.newcustomer_loanamount == teampage.get_team_newcustomer_loanamount()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_amount_by_province(self):
        u"""按天统计放款量->按省区统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            provincepage = loan_amount_by_day_page.LoanAmountByDayByProvince(self.webdriver)
            url = provincepage.get_url()
            self.webdriver.get(url)
            provincepage.input_day(self.day)
            provincepage.click_search_button()
            time.sleep(5)
            provincepage.page_down()
            time.sleep(1)
            assert self.yesterday_newcustomer_loanamount == provincepage.get_yesterday_newcustomer_loanamount()
            assert self.yesterday_loanamount == provincepage.get_yesterday_loanamount()
            assert self.newcustomer_loanamount == provincepage.get_newcustomer_loanamount()
            assert self.loanamount == provincepage.get_loanamount()
            assert self.pre_month_newcustomer_loanamount == provincepage.get_pre_month_newcustomer_loanamount()
            assert self.pre_month_loanamount == provincepage.get_pre_month_loanamount()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
