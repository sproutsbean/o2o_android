#!usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
from com.ea.common import tools
from com.ea.resource import globalparameter as gl
from com.ea.pages import menu_page, platform_caiwu_list_page
import os
import sys
import time


class MyTestCase(unittest.TestCase):
    u"""平台财务审核页面所有选项检查"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])

    def setUp(self):
        tools.del_pics(self.screenshot_path)
        self.driver = tools.getAppiumDriver()
        self.driver.start_activity(gl.packagename, gl.login_activity)
        self.menupage = menu_page.MenuPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_platform_caiwu_list_check(self):
        u"""平台财务审核页面所有选项检查"""
        casename = sys._getframe().f_code.co_name
        try:
            listpage = platform_caiwu_list_page.PlatformCaiwuListPage(self.driver)
            tools.login(self.driver)
            self.menupage.click_platform_caiwu_approve()
            status = listpage.get_first_row_status()
            listpage.click_first_row()
            if status != "新建":
                listpage.click_shenheliucheng()
                self.assertTrue(tools.have_element(self.driver, "审核记录", 10))
                self.driver.back()
            listpage.click_daikuan_jiben_ziliao()
            self.assertTrue(tools.have_element(self.driver, "贷款类型", 10))
            self.driver.back()
            marry_status = listpage.click_jiekuanren_jiben_xinxi()
            self.assertTrue(tools.have_element(self.driver, "借款人姓", 10))
            self.driver.back()
            if marry_status == "已婚":
                listpage.click_jiekuanren_peiou_xinxi()
                self.assertTrue(tools.have_element(self.driver, "配偶姓", 10))
                self.driver.back()
            listpage.click_kehu_zichan_xinxi()
            self.assertTrue(tools.have_element(self.driver, "自有房产", 10))
            self.driver.back()
            listpage.click_sd_xitong_jiaoyi_jilu_huizongbiao()
            self.assertTrue(tools.have_element(self.driver, "提货金额", 10))
            self.driver.back()
            listpage.click_caiwu_shenhe_sd_xinxi()
            if status == "流程中":
                self.assertTrue(tools.have_element(self.driver, "未查到相应信息", 10))
            elif status == "流程结束":
                self.assertTrue(tools.have_element(self.driver, "提货金额", 10))
            self.driver.back()
            listpage.click_caiwu_shenhe_jilu()
            self.assertTrue(tools.have_element(self.driver, "客户年销售额", 10))
            self.driver.back()
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
