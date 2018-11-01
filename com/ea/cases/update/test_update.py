#!usr/bin/env python  
# -*- coding:utf-8 -*-
"""
@author:user 
@file: test_zhongduandai_changjia.py 
@time: 2018/03/05 
"""
from com.ea.common import tools
from com.ea.common.cardname import cardname
import unittest
import os
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_page import MenuPage
import time
import sys
import arrow
from com.ea.pages import zhengxin_page

logger = tools.create_logger()


class MyTestCase(unittest.TestCase):
    u"""修改征信信息用例"""
    logger.info(str(arrow.now()))
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    driver = None

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.login_activity)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    # @unittest.skip("skip")
    def test_update_zhengxin_xinxi(self):
        """修改征信信息"""
        casename = sys._getframe().f_code.co_name
        logger.info("修改征信信息用例开始")
        driver = self.driver
        screenshot_path = self.screenshot_path
        try:
            tools.login(driver)
            menupage = MenuPage(driver)
            zhengxinpage = zhengxin_page.ZhengxinPage(driver)
            menupage.click_personal_zhengxin_query()
            zhengxinpage.click_filter_button()
            zhengxinpage.select_danju_zhuangtai("新建")
            zhengxinpage.click_search_button()
            no = zhengxinpage.get_first_row_no()
            logger.info("修改的征信单号是:" + no)
            zhengxinpage.click_first_row()
            """修改征信基本资料"""
            zhengxinpage.click_zhengxin_jiben_ziliao()
            kehu_leixing = zhengxinpage.get_kehu_leixing()
            after_kehu_leixing = None
            if kehu_leixing == "借款人":
                after_kehu_leixing = "配偶"
                zhengxinpage.click_kehu_leixing(after_kehu_leixing)
            if kehu_leixing == "配偶":
                after_kehu_leixing = "借款人"
                zhengxinpage.click_kehu_leixing(after_kehu_leixing)
            zhengxin_bank = zhengxinpage.get_zhengxin_bank_name()
            zhengxinpage.click_zhengxin_bank_option()
            time.sleep(1)
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            if zhengxin_bank == "怡亚通":
                self.driver.swipe(x / 2, y * 12 / 15, x / 2, y * 13 / 15, 2000)
            else:
                self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
            zhengxinpage.click_confirm_button()
            zhengxinpage.click_save_button()
            zhengxinpage.click_zhengxin_jiben_ziliao()
            actul_kehu_leixing = zhengxinpage.get_kehu_leixing()
            after_zhengxin_bank = zhengxinpage.get_zhengxin_bank_name()
            logger.info("修改前客户类型为:" + kehu_leixing + "    修改后客户类型为:" + actul_kehu_leixing)
            logger.info("修改前征信银行为:" + zhengxin_bank + "    修改后征信银行为:" + after_zhengxin_bank)
            self.assertNotEqual(kehu_leixing, actul_kehu_leixing)
            self.assertNotEqual(zhengxin_bank, after_zhengxin_bank)
            driver.back()
            """修改客户信息"""
            zhengxinpage.click_kehu_xinxi()
            p_first_english_name = zhengxinpage.get_first_english_name()
            p_last_english_name = zhengxinpage.get_last_english_name()
            p_phone = zhengxinpage.get_phone()
            p_date = zhengxinpage.get_date()
            zhengxinpage.click_edit_button()
            zhengxinpage.input_first_english_name(tools.create_random_english())
            zhengxinpage.input_last_english_name(tools.create_random_english())
            zhengxinpage.input_phone(cardname.createPhone())
            zhengxinpage.click_zhengjian_daoqiri()
            time.sleep(1)
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
            zhengxinpage.click_confirm_button()
            zhengxinpage.click_save_button()
            a_first_english_name = zhengxinpage.get_first_english_name()
            a_last_english_name = zhengxinpage.get_last_english_name()
            a_phone = zhengxinpage.get_phone()
            a_date = zhengxinpage.get_date()
            logger.info("修改前客户姓拼音为:" + p_first_english_name + "    修改后客户姓拼音为:" + a_first_english_name)
            logger.info("修改前客户名拼音为:" + p_last_english_name + "    修改后客户名拼音为:" + a_last_english_name)
            logger.info("修改前证件到期日为:" + p_date + "    修改后证件到期日为:" + a_date)
            logger.info("修改前电话号码为:" + p_phone + "    修改后电话号码为:" + a_phone)
            self.assertNotEqual(p_first_english_name, a_first_english_name)
            self.assertNotEqual(p_last_english_name, a_last_english_name)
            self.assertNotEqual(p_date, a_date)
            self.assertNotEqual(p_phone, a_phone)
            logger.info("修改征信信息用例结束")
        except Exception as e:
            tools.screenshot(driver, screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
