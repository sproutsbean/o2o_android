import unittest
from com.ea.pages import loan_balance_page
from com.ea.common import tools, web_login
from com.ea.resource import globalparameter as gl
import time
import os
import sys


class MyTestCase(unittest.TestCase):
    u"""贷款余额统计"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    day = '2018-01-01'
    fangkuan_jine = '2,781,640,000.00'
    bank_zhengchang_daikuan_yue = '0.00'
    bank_yuqi_daikuan_yue = '32,594,743.17'
    daichang_daikuan_jine = '185,602,011.94'
    daichang_daikuan_qianhuan_yue = '86,827,339.51'

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

    def test_loan_balance_by_agencies(self):
        u"""贷款余额统计->按经办机构统计"""
        casename = sys._getframe().f_code.co_name
        try:
            byagenciespage = loan_balance_page.LoanBalanceByAgencies(self.webdriver)
            url = byagenciespage.get_url()
            self.webdriver.get(url)
            byagenciespage.input_day(self.day)
            byagenciespage.click_search_button()
            time.sleep(10)
            byagenciespage.page_down()
            time.sleep(1)
            assert self.fangkuan_jine == byagenciespage.get_fangkuan_jine()
            assert self.bank_zhengchang_daikuan_yue == byagenciespage.get_bank_zhengchang_daikuan_yue()
            assert self.bank_yuqi_daikuan_yue == byagenciespage.get_bank_yuqi_daikuan_yue()
            assert self.daichang_daikuan_jine == byagenciespage.get_daichang_daikuan_jine()
            assert self.daichang_daikuan_qianhuan_yue == byagenciespage.get_daichang_daikuan_qianhuan_yue()
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
