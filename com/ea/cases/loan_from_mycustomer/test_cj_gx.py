#!usr/bin/env python  
# -*- coding:utf-8 -*-
"""
@author:user 
@file: test_zhongduandai_changjia.py 
@time: 2018/03/05 
"""
from com.ea.common import tools
from com.ea.common.cardname import cardname
from com.ea.common.cardnumber import IdCardNumber
import unittest
import time
import os
import sys
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_page import MenuPage
from com.ea.pages import approve_page
from com.ea.common import web_login
from com.ea.pages.zhengxin_page import ZhengxinPage


class MyTestCase(unittest.TestCase):
    u"""流通贷-厂家-共享"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    cardNo = IdCardNumber.getRandomIdNumber(1)[0]
    fullname, first_name, second_name, full_english_name, first_english_name, last_english_name = cardname.get_names()
    phoneNo = cardname.createPhone()
    accountid = tools.get_random_string()
    zx_no = tools.get_zx_no()
    loan_no = None
    dakuandanhao = None
    loan_type = "流通贷-厂家"
    operate_mode = "共享模式"
    marry_status = "已婚"
    bank_name = "浦发广州分行"
    sd_customer_name = ""
    print("姓名:" + fullname)
    print("身份证:" + cardNo + "\n")

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        # cls.webdriver = tools.get_chrome_driver()

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.login_activity)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    # @unittest.skip("skip")
    def test_a_zhengxin_apply(self):
        """申请征信"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import zhengxin
        zhengxin.zhengxin_apply_from_mycustomer(self.driver, self.cardNo, self.first_name, self.second_name, self.first_english_name, self.last_english_name, self.phoneNo, self.bank_name, self.screenshot_path, casename)

    # @unittest.skip("skip")
    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        zx_no = tools.get_zx_no_by_cardno(self.cardNo)
        # zx_no = "O2OZX-1807-00879"
        casename = sys._getframe().f_code.co_name
        from com.ea.common import zhengxin
        zhengxin.zhengxin_approve(self.driver, zx_no, self.screenshot_path, casename)

    # @unittest.skip("skip")
    def test_c_loan_apply(self):
        """申请贷款"""
        casename = sys._getframe().f_code.co_name
        print("申请贷款用例开始")
        print("使用的身份证号是:", self.cardNo)
        loan_amount = "500000"
        channel_name = "深圳"
        from com.ea.pages.my_customer_page import MyCustomerPage
        from com.ea.common import add_customer
        try:
            mycustomerpage = MyCustomerPage(self.driver)
            tools.login(self.driver)
            add_customer.add_customer(self.driver, self.first_name, self.second_name, self.first_english_name, self.last_english_name, self.cardNo, self.phoneNo)
            mycustomerpage.click_customer_name(self.fullname)
            mycustomerpage.click_archives()
            mycustomerpage.click_loan_apply()
            mycustomerpage.select_loan_type(self.loan_type)
            mycustomerpage.click_next_button()
            mycustomerpage.select_marry_status(self.marry_status)
            mycustomerpage.click_next_button()
            if self.marry_status == "已婚":
                pcard_no = IdCardNumber.getRandomIdNumber(1)[0]
                pfullname, pfirst_name, psecond_name, pfull_english_name, pfirst_english_name, plast_english_name = cardname.get_names()
                pphone_no = cardname.createPhone()
                mycustomerpage.input_pfirst_name(pfirst_name)
                mycustomerpage.input_psecond_name(psecond_name)
                mycustomerpage.input_pfirst_english_name(pfirst_english_name)
                mycustomerpage.input_plast_english_name(plast_english_name)
                mycustomerpage.input_pcard_no(pcard_no)
                mycustomerpage.click_card_expire_date()
                mycustomerpage.input_pphone_no(pphone_no)
                mycustomerpage.click_next_button()
            mycustomerpage.input_loan_amount(loan_amount)
            mycustomerpage.select_operate_mode(self.operate_mode)
            mycustomerpage.input_channel_name(channel_name)
            if self.loan_type == "终端贷":
                mycustomerpage.input_sd_customer_name(self.sd_customer_name)
            mycustomerpage.click_save_button()
            time.sleep(3)
            loan_no = tools.get_loan_no_by_cardno(self.cardNo)
            mycustomerpage.click_loan_no(loan_no)
            mycustomerpage.select_fuqizhengxin_report()

            mycustomerpage.click_name(self.first_name + self.second_name)
            mycustomerpage.click_zhengxin_apply()
            mycustomerpage.click_zhengxin_bank_option()
            mycustomerpage.click_zhengxin_bank_name(self.bank_name)
            mycustomerpage.click_save_button()
            mycustomerpage.click_shenfenzhengfuyinjian()
            time.sleep(4)
            mycustomerpage.click_shouchishouquanshu()
            time.sleep(4)
            mycustomerpage.click_zhengxinshouquanshu()
            time.sleep(4)
            mycustomerpage.click_disanfangshujuchaxunshouquanshu()
            time.sleep(4)
            mycustomerpage.click_shouchishenfenzheng()
            time.sleep(4)
            mycustomerpage.click_kehuhukouben()
            time.sleep(4)
            mycustomerpage.click_zxbgsysqsm()
            time.sleep(4)
            mycustomerpage.click_sxsqyxs()
            time.sleep(4)
            mycustomerpage.click_jkryyytmywlfj()
            time.sleep(4)
            mycustomerpage.click_save_button()
            mycustomerpage.click_radio_button()
            mycustomerpage.click_guanlian_button()
            mycustomerpage.click_confirm_button()
            assert "审核中" == mycustomerpage.get_zx_status_by_name(self.first_name + self.second_name)
            if self.marry_status == "已婚":
                mycustomerpage.click_name(pfullname)
                mycustomerpage.click_zhengxin_apply()
                mycustomerpage.click_zhengxin_bank_option()
                mycustomerpage.click_zhengxin_bank_name(self.bank_name)
                mycustomerpage.click_save_button()
                mycustomerpage.click_shenfenzhengfuyinjian()
                time.sleep(4)
                mycustomerpage.click_shouchishouquanshu()
                time.sleep(4)
                mycustomerpage.click_zhengxinshouquanshu()
                time.sleep(4)
                mycustomerpage.click_disanfangshujuchaxunshouquanshu()
                time.sleep(4)
                mycustomerpage.click_shouchishenfenzheng()
                time.sleep(4)
                mycustomerpage.click_kehuhukouben()
                time.sleep(4)
                mycustomerpage.click_zxbgsysqsm()
                time.sleep(4)
                mycustomerpage.click_sxsqyxs()
                time.sleep(4)
                mycustomerpage.click_jkryyytmywlfj()
                time.sleep(4)
                mycustomerpage.click_save_button()
                mycustomerpage.click_radio_button()
                mycustomerpage.click_guanlian_button()
                mycustomerpage.click_confirm_button()
                assert "审核中" == mycustomerpage.get_zx_status_by_name(pfullname)
                partner_zx_no = tools.get_zx_no_by_cardno(pcard_no)
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
