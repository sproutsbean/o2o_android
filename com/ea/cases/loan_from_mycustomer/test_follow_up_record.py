#!usr/bin/env python  
# -*- coding:utf-8 -*-
"""
@author:user 
@file: test_zhongduandai_changjia.py 
@time: 2018/03/05 
"""
from com.ea.common import tools
import unittest
import os
import sys
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_page import MenuPage
from com.ea.pages.my_customer_page import MyCustomerPage


class MyTestCase(unittest.TestCase):
    u"""流通贷-厂家-共享"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path

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
        cls.driver.quit()

    # @unittest.skip("skip")
    def test_follow_up_record(self):
        """跟进记录"""
        casename = sys._getframe().f_code.co_name
        record = "自动化跟进记录" + tools.get_chinese()
        try:
            tools.login(self.driver)
            menupage = MenuPage(self.driver)
            menupage.click_me_page()
            mycustomerpage = MyCustomerPage(self.driver)
            mycustomerpage.click_my_customer()
            mycustomerpage.click_first_customer()
            mycustomerpage.click_follow_up_record()
            mycustomerpage.click_add_record()
            mycustomerpage.select_follow_up_type()
            mycustomerpage.input_record(record)
            mycustomerpage.click_save_button()
            assert record == mycustomerpage.get_follow_up_record_result(record)
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
