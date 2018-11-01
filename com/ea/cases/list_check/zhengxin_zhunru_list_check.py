#!usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
from com.ea.common import tools
from com.ea.resource import globalparameter as gl
from com.ea.pages import menu_page, zhengxin_zhunru_list_page
import os
import sys
import time


class MyTestCase(unittest.TestCase):
    u"""征信注入页面所有选项检查"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])

    def setUp(self):
        tools.del_pics(self.screenshot_path)
        self.driver = tools.getAppiumDriver()
        self.driver.start_activity(gl.packagename, gl.login_activity)
        self.menupage = menu_page.MenuPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_zhengxin_zhunru_list_check(self):
        u"""征信准入页面所有选项检查"""
        casename = sys._getframe().f_code.co_name
        try:
            listpage = zhengxin_zhunru_list_page.ZhengxinZhunruListPage(self.driver)
            tools.login(self.driver)
            self.menupage.click_zhengxinzhunru()
            listpage.click_first_row()
            listpage.click_zhengxin_zhunru_liucheng()
            self.assertTrue(tools.have_element(self.driver, "审核记录", 10))
            self.driver.back()
            listpage.click_daikuan_yaosu()
            self.assertTrue(tools.have_element(self.driver, "贷款基本资料", 10))
            self.driver.back()
            listpage.click_jiekuanren_jiben_xinxi()
            self.assertTrue(tools.have_element(self.driver, "证件类型", 10))
            self.driver.back()
            listpage.click_jiekuanren_peiou_xinxi()
            self.assertTrue(tools.have_element(self.driver, "配偶姓名", 10))
            self.driver.back()
            listpage.click_fuqishuangfang_zhengxin_report_xinxi()
            self.assertTrue(tools.have_element(self.driver, "银行征信报告时间", 10))
            self.driver.back()
            listpage.click_jiekuanren_zhengxin_fujian()
            self.assertTrue(tools.have_element(self.driver, "附件列表", 10))
            self.driver.back()
            listpage.click_peiou_zhengxin_fujian()
            self.assertTrue(tools.have_element(self.driver, "附件列表", 10))
            self.driver.back()
            listpage.click_qiye_zhengxin_baogao_xinxi()
            self.assertTrue(tools.have_element(self.driver, "企业征信报告日期", 10))
            self.driver.back()
            listpage.click_qiye_zhengxin_fujian_xinxi()
            self.assertTrue(tools.have_element(self.driver, "企业征信附件信息", 10))
            self.driver.back()
            listpage.click_buchong_zhengxin_fujian_xinxi()
            self.assertTrue(tools.have_element(self.driver, "附件列表", 10))
            self.driver.back()
            listpage.click_qita_fujian_xinxi()
            self.assertTrue(tools.have_element(self.driver, "附件列表", 10))
            self.driver.back()
            time.sleep(2)
            listpage.swipe("up")
            listpage.click_fuqi_shuangfang_daikuan_jilu()
            self.assertTrue(tools.have_element(self.driver, "贷款类型", 10))
            self.driver.back()
            listpage.click_fuqi_shuangfang_daichang_shuju()
            self.assertTrue(tools.have_element(self.driver, "未查到相应信息", 3))
            self.driver.back()
            listpage.click_fuqi_shuangfang_yuqi_shuju()
            self.assertTrue(tools.have_element(self.driver, "未查到相应信息", 3))
            self.driver.back()
            listpage.click_daichang_yuqi_xinxi()
            self.assertTrue(tools.have_element(self.driver, "未查到相应信息", 3))
            self.driver.back()
            listpage.click_fuqi_shuangfang_danbao_daikuan_xinxi()
            self.assertTrue(tools.have_element(self.driver, "未查到相应信息", 3))
            self.driver.back()
            listpage.click_danbaoren_xiangqing()
            self.assertTrue(tools.have_element(self.driver, "未查到相应信息", 3))
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
