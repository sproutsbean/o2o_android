import unittest
from com.ea.pages import loan_approve_report_page
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
    expect_xinzeng_zhengxin_tibao = '932'
    expect_zhengxin_jieshu_xinzeng = '862'
    expect_neishen_xintijiao = '837'
    expect_neishen_jieshu_xinzeng = '729'
    expect_yinhang_songshen_xinzeng = '620'
    bank_neishen_xintijiao = '657'
    bank_neishen_jieshu_xinzeng = '653'

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

    def test_loan_approve_by_agencies(self):
        u"""贷款审批报表->贷款审批经办机构统计"""
        casename = sys._getframe().f_code.co_name
        try:
            agenciespage = loan_approve_report_page.LoanAprroveByAgencies(self.webdriver)
            url = agenciespage.get_url()
            self.webdriver.get(url)
            agenciespage.input_loan_date_start(self.start_date)
            agenciespage.input_loan_date_end(self.end_date)
            agenciespage.click_search_button()
            time.sleep(3)
            agenciespage.page_down()
            time.sleep(1)
            assert self.expect_xinzeng_zhengxin_tibao == agenciespage.get_xinzeng_zhengxin_tibao()
            assert self.expect_zhengxin_jieshu_xinzeng == agenciespage.get_zhengxin_jieshu_xinzeng()
            assert self.expect_neishen_xintijiao == agenciespage.get_neishen_xintijiao()
            assert self.expect_neishen_jieshu_xinzeng == agenciespage.get_neishen_jieshu_xinzeng()
            assert self.expect_yinhang_songshen_xinzeng == agenciespage.get_yinhang_songshen_xinzeng()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_approve_by_loanmanager(self):
        u"""贷款审批报表->贷款审批贷前信贷经理统计"""
        casename = sys._getframe().f_code.co_name
        try:
            managerpage = loan_approve_report_page.LoanAprroveByManager(self.webdriver)
            url = managerpage.get_url()
            self.webdriver.get(url)
            managerpage.input_loan_date_start(self.start_date)
            managerpage.input_loan_date_end(self.end_date)
            managerpage.click_search_button()
            time.sleep(5)
            managerpage.page_down()
            time.sleep(1)
            assert self.expect_xinzeng_zhengxin_tibao == managerpage.get_xinzeng_zhengxin_tibao()
            assert self.expect_zhengxin_jieshu_xinzeng == managerpage.get_zhengxin_jieshu_xinzeng()
            assert self.expect_neishen_xintijiao == managerpage.get_neishen_xintijiao()
            assert self.expect_neishen_jieshu_xinzeng == managerpage.get_neishen_jieshu_xinzeng()
            assert self.expect_yinhang_songshen_xinzeng == managerpage.get_yinhang_songshen_xinzeng()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_approve_by_province(self):
        u"""贷款审批报表->贷款审批省区统计"""
        casename = sys._getframe().f_code.co_name
        try:
            provincepage = loan_approve_report_page.LoanAprroveByProvince(self.webdriver)
            url = provincepage.get_url()
            self.webdriver.get(url)
            provincepage.input_loan_date_start(self.start_date)
            provincepage.input_loan_date_end(self.end_date)
            provincepage.click_search_button()
            time.sleep(5)
            provincepage.page_down()
            time.sleep(1)
            assert self.expect_xinzeng_zhengxin_tibao == provincepage.get_xinzeng_zhengxin_tibao()
            assert self.expect_zhengxin_jieshu_xinzeng == provincepage.get_zhengxin_jieshu_xinzeng()
            assert self.expect_neishen_xintijiao == provincepage.get_neishen_xintijiao()
            assert self.expect_neishen_jieshu_xinzeng == provincepage.get_neishen_jieshu_xinzeng()
            assert self.expect_yinhang_songshen_xinzeng == provincepage.get_yinhang_songshen_xinzeng()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    def test_loan_approve_by_bank(self):
        u"""贷款审批报表->贷款审批银行统计"""
        casename = sys._getframe().f_code.co_name
        try:
            bankpage = loan_approve_report_page.LoanAprroveByBank(self.webdriver)
            url = bankpage.get_url()
            self.webdriver.get(url)
            bankpage.input_loan_date_start(self.start_date)
            bankpage.input_loan_date_end(self.end_date)
            bankpage.click_search_button()
            time.sleep(5)
            bankpage.page_down()
            time.sleep(1)
            assert self.expect_xinzeng_zhengxin_tibao == bankpage.get_xinzeng_zhengxin_tibao()
            assert self.expect_zhengxin_jieshu_xinzeng == bankpage.get_zhengxin_jieshu_xinzeng()
            assert self.bank_neishen_xintijiao == bankpage.get_neishen_xintijiao()
            assert self.bank_neishen_jieshu_xinzeng == bankpage.get_neishen_jieshu_xinzeng()
            assert self.expect_yinhang_songshen_xinzeng == bankpage.get_yinhang_songshen_xinzeng()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
