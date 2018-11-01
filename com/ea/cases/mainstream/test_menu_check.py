#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: test_menu_check.py 
@time: 2018/03/01 
"""
from com.ea.common import tools
from com.ea.resource import globalparameter as gl
import os
import sys
import unittest
from com.ea.pages.menu_page import MenuPage
import time


class MyTestCase(unittest.TestCase):
    u"""所有菜单检查"""
    # screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    screenshot_path = gl.screenshot_path
    pic_path = gl.test_pic_path

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        tools.login(cls.driver)
        cls.menupage = MenuPage(cls.driver)
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

    def test_loan_apply(self):
        """点击申请贷款按钮"""
        casename = sys._getframe().f_code.co_name
        result = "请输入身份证号码"
        try:
            self.menupage.click_loan_apply()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_zhengxinzhuru(self):
        """点击征信准入按钮"""
        casename = sys._getframe().f_code.co_name
        result = "征信银行"
        try:
            self.menupage.click_zhengxinzhunru()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_inside_approve(self):
        """点击内部审批按钮"""
        casename = sys._getframe().f_code.co_name
        result = "审批金额"
        try:
            self.menupage.click_inside_approve()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_interview(self):
        """点击面签提报按钮"""
        casename = sys._getframe().f_code.co_name
        result = "送审银行"
        try:
            self.menupage.click_interview()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_platform_caiwu_approve(self):
        """点击平台财务审核按钮"""
        casename = sys._getframe().f_code.co_name
        result = "客户名称"
        try:
            self.menupage.click_platform_caiwu_approve()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_loan_apply_query(self):
        """点击贷款申请查询按钮"""
        casename = sys._getframe().f_code.co_name
        result = "创建时间"
        try:
            self.menupage.click_loan_apply_query()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_personal_zhengxin_query(self):
        """点击个人征信查询"""
        casename = sys._getframe().f_code.co_name
        result = "创建时间"
        try:
            self.menupage.click_personal_zhengxin_query()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_company_zhengxin_query(self):
        """点击企业征信查询"""
        casename = sys._getframe().f_code.co_name
        result = "营业执照名称"
        try:
            self.menupage.click_company_zhengxin_query()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_release_loan_query(self):
        """点击放款查询"""
        casename = sys._getframe().f_code.co_name
        result = "放款时间"
        try:
            self.menupage.click_release_loan_query()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_five_arive_warning(self):
        """点击5天到期预警"""
        casename = sys._getframe().f_code.co_name
        result = "放款时间"
        try:
            self.menupage.click_five_arive_warning()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_ten_arive_warning(self):
        """点击10天到期预警"""
        casename = sys._getframe().f_code.co_name
        result = "放款时间"
        try:
            self.menupage.click_ten_arive_warning()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_after_loan_check(self):
        """点击贷后定期检查"""
        casename = sys._getframe().f_code.co_name
        result = "回访日期"
        try:
            self.menupage.click_after_loan_check()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_zhengxin_save(self):
        """点击征信归档"""
        casename = sys._getframe().f_code.co_name
        result = "征信银行"
        try:
            self.menupage.click_zhengxin_save()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_after_loan_save(self):
        """点击贷后归档"""
        casename = sys._getframe().f_code.co_name
        result = "归档完成时间"
        try:
            self.menupage.click_after_loan_save()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_repayment_plan(self):
        """点击还款计划"""
        casename = sys._getframe().f_code.co_name
        result = "计划还款日期"
        try:
            self.menupage.click_repayment_plan()
            time.sleep(4)
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_loan_apply_summary(self):
        """点击贷款申请汇总"""
        casename = sys._getframe().f_code.co_name
        result = "省区"
        try:
            self.menupage.click_loan_apply_summary()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_release_loan_summary(self):
        """点击贷款放款汇总"""
        casename = sys._getframe().f_code.co_name
        result = "本月放款笔数"
        try:
            self.menupage.click_release_loan_summary()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_by_time_summary_loan(self):
        """点击按时间区间统计放款量"""
        casename = sys._getframe().f_code.co_name
        result = "按团队统计放款量"
        try:
            self.menupage.click_by_time_summary_loan()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_by_day_summary_loan(self):
        """点击按天统计放款量"""
        casename = sys._getframe().f_code.co_name
        result = "按团队统计放款量"
        try:
            self.menupage.click_by_day_summary_loan()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_release_business_summary_table(self):
        """点击放款业务统计表"""
        casename = sys._getframe().f_code.co_name
        result = "业务按信贷经理统计"
        try:
            self.menupage.click_release_business_summary_table()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_brand_manage(self):
        """点击品牌管理"""
        casename = sys._getframe().f_code.co_name
        result = "品牌名称"
        try:
            self.menupage.click_brand_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_factory_manage(self):
        """点击厂家合作方管理"""
        casename = sys._getframe().f_code.co_name
        result = "合作方名称"
        try:
            self.menupage.click_factory_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_dealer_manage(self):
        """点击经销商合作方管理"""
        casename = sys._getframe().f_code.co_name
        result = "一批商分类"
        try:
            self.menupage.click_dealer_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_channel_manage(self):
        """点击渠道管理"""
        casename = sys._getframe().f_code.co_name
        result = "渠道名称"
        try:
            self.menupage.click_channel_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_play_money_manage(self):
        """点击打款管理"""
        casename = sys._getframe().f_code.co_name
        result = "申请打款"
        try:
            self.menupage.click_play_money_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_back_money_manage(self):
        """点击退款管理"""
        casename = sys._getframe().f_code.co_name
        result = "退款金额（元）:"
        try:
            self.menupage.click_back_money_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_charge_manage(self):
        """点击收费管理"""
        casename = sys._getframe().f_code.co_name
        result = "收费管理列表"
        try:
            self.menupage.click_charge_manage()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_operation_guide(self):
        """点击操作指引"""
        casename = sys._getframe().f_code.co_name
        result = "营销管理"
        try:
            self.menupage.click_operation_guide()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_requirements_apply(self):
        """点击需求申请"""
        casename = sys._getframe().f_code.co_name
        result = "需求类型"
        try:
            self.menupage.click_requirements_apply()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e

    def test_ea_address_book(self):
        """点击EA通讯录"""
        casename = sys._getframe().f_code.co_name
        result = "通讯录"
        try:
            self.menupage.click_ea_address_book()
            assert result in self.driver.page_source
        except Exception as e:
            tools.screenshot(self.driver, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
