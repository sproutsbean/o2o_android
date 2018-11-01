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
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_page import MenuPage
from com.ea.pages.zhengxin_page import ZhengxinPage


class MyTestCase(unittest.TestCase):
    u""""""
    # screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    screenshot_path = gl.screenshot_path
    pic_path = gl.test_pic_path
    cardNo = IdCardNumber.getRandomIdNumber(1)[0]
    fullname, first_name, second_name, full_english_name, first_english_name, last_english_name = cardname.get_names()
    phoneNo = cardname.createPhone()
    accountid = tools.get_random_string()
    zx_no = tools.get_zx_no()

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        tools.login(cls.driver)
        cls.menupage = MenuPage(cls.driver)
        cls.zhengxinpage = ZhengxinPage(cls.driver)
        # applyer_acount = tools.get_zhuanyuan_acount()
        # 粤东(xianhui.ling),粤西(feng.yun),山东(wenhui.zhang),重庆(ling.cheng)

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.homepage_activity)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def test_a_zhengxin_apply(self):
        """申请征信"""
        print("申请征信用例开始")
        print("使用的身份证号是:", self.cardNo)
        self.menupage.click_personal_zhengxin_query()
        self.zhengxinpage.click_apply_button()
        print(self.cardNo)
        self.zhengxinpage.send_cardno(self.cardNo)
        self.zhengxinpage.click_next_button()
        self.zhengxinpage.send_first_name(self.first_name)
        self.zhengxinpage.send_second_name(self.second_name)
        self.zhengxinpage.send_first_english_name(self.first_english_name)
        self.zhengxinpage.send_second_english_name(self.last_english_name)
        self.zhengxinpage.click_card_expire_date()
        self.zhengxinpage.click_confirm_button()
        self.zhengxinpage.send_phoneno(self.phoneNo)
        self.zhengxinpage.click_next_button()
        time.sleep(2)
        self.zhengxinpage.click_customer_type_option()
        self.zhengxinpage.click_customer_type_value()
        self.zhengxinpage.click_loan_manager_option()
        self.zhengxinpage.send_loan_manager_editview("李")
        time.sleep(1)
        self.zhengxinpage.click_loan_manager_name()
        self.zhengxinpage.click_platform_option()
        self.zhengxinpage.send_platform_editview("深圳")
        time.sleep(2)
        self.zhengxinpage.click_platform_name()
        self.zhengxinpage.click_zhengxin_bank_option()
        self.zhengxinpage.click_zhengxin_bank_name()
        time.sleep(1)
        self.zhengxinpage.click_save_button()
        self.zhengxinpage.click_danhao_option()
        self.zhengxinpage.click_zhengxin_attachment()
        self.zhengxinpage.click_upload_attachment_button()
        self.zhengxinpage.click_shenfenzhengfuyinjian()
        time.sleep(4)
        self.zhengxinpage.click_shouchishouquanshu()
        time.sleep(4)
        self.zhengxinpage.click_zhengxinshouquanshu()
        time.sleep(4)
        self.zhengxinpage.click_disanfangshujuchaxunshouquanshu()
        time.sleep(4)
        self.zhengxinpage.click_shouchishenfenzheng()
        time.sleep(4)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.zhengxinpage.click_start_flowing_button()
        self.zhengxinpage.click_confirm_button()

    def test_b_zhengxin_approve(self):
        zx_no = tools.get_zx_no_by_cardno(self.cardNo)
        from com.ea.pages import approve_page
        pubapprovepage = approve_page.ApprovePubPage(self.driver)
        zhengxinapprovepage = approve_page.ZhengxinApprovePage(self.driver)
        self.menupage.click_approve_page()
        pubapprovepage.click_todo_first_row(zx_no)
        zhengxinapprovepage.click_my_approve()


if __name__ == '__main__':
    unittest.main()
