#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: brand_management.py 
@time: 2018/01/17 
"""
from com.ea.common import tools
from com.ea.resource import globalparameter as gl
from com.ea.pages.todo_page import FactoryApprove
from com.ea.pages.menu_page import MenuPage
import time
import os
import sys
import unittest


class MyTestCase(unittest.TestCase):
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    yewu_no = ""

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        cls.menu = MenuPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.login_activity)

    def tearDown(self):
        pass

    # @unittest.skip('skip')
    def test_a_add_factory(self):
        u""" 添加厂家合作方"""
        casename = sys._getframe().f_code.co_name
        driver = self.driver
        expect_result = "审核中"
        from com.ea.pages.factory_page import FactoryPage
        from com.ea.common.cardname import cardname
        brand_name = "可乐"
        channel_name = tools.get_chinese() + "渠道"
        main_head = "张三"
        sales_area = "贵州省"
        operate_range = "全国"
        phone = cardname.createPhone()
        salesPatternOne = 1
        salesPatternTwo = 1
        salesPatternTerminal = 1
        office_road = "无名路"
        sales_year = 300000
        sales_year_maolilv = 400000
        description = "这里是回购协议描述"
        try:
            tools.login(driver)
            self.menu.click_factory_manage()
            factorypage = FactoryPage(driver)
            factorypage.click_add_button()
            factorypage.click_brand_option()
            factorypage.input_brand_edit(brand_name)
            time.sleep(2)
            factorypage.click_brand_name()
            factorypage.click_next_button()

            factorypage.input_channel_name(channel_name)
            factorypage.click_channel_shared_option()
            factorypage.click_channel_shared_value()
            factorypage.click_province_option()
            factorypage.swipe("up")
            factorypage.click_province_value()
            factorypage.input_main_head(main_head)
            factorypage.click_setup_time_option()
            factorypage.click_setup_time_confirm()
            factorypage.input_sales_area(sales_area)
            factorypage.input_operate_range(operate_range)
            factorypage.input_phone(phone)
            factorypage.click_jiesuan_fangshi_option()
            factorypage.click_jiesuan_fangshi_select()
            factorypage.click_jiesuan_fangshi_value()
            factorypage.click_save_button()
            factorypage.swipe("up")
            factorypage.click_xiaoshou_jiegou_option()
            factorypage.input_salesPatternOne(salesPatternOne)
            factorypage.input_salesPatternTwo(salesPatternTwo)
            factorypage.input_salesPatternTerminal(salesPatternTerminal)
            factorypage.click_save_button()
            factorypage.click_work_addr_option()
            factorypage.input_work_addr_info(office_road)
            factorypage.click_work_addr_confirm()
            factorypage.input_sales_year(sales_year)
            factorypage.input_year_maolilv(sales_year_maolilv)
            factorypage.swipe("up")
            factorypage.click_loan_object_option()
            factorypage.click_loan_object_select()
            factorypage.click_loan_object_value()
            factorypage.click_save_button()
            factorypage.click_buy_back_option()
            factorypage.click_buy_back_select()
            factorypage.click_buy_back_value()
            factorypage.click_save_button()
            factorypage.click_allow_get_data_option()
            factorypage.click_allow_get_data_value()
            factorypage.click_allow_customer_research_option()
            factorypage.click_allow_customer_research_value()
            factorypage.click_zhenshi_jiaoyi_pinzheng_option()
            factorypage.click_zhenshi_jiaoyi_pinzheng_value()
            factorypage.click_save_button()
            factorypage.click_danbao_fangshi_option()
            factorypage.click_danbao_fangshi_select()
            factorypage.clcik_danbao_fangshi_value()
            factorypage.click_save_button()
            factorypage.click_save_button()
            MyTestCase.yewu_no = factorypage.get_yewuno(channel_name)
            factorypage.click_channel_name(channel_name)
            print(self.yewu_no)
            factorypage.click_fujian_info()
            factorypage.click_hezuofang_shenqing_baogao()
            factorypage.click_upload()
            factorypage.click_paizhao()
            factorypage.click_kuaimen()
            factorypage.click_paizhao_confirm()
            time.sleep(5)
            driver.back()
            factorypage.click_shangmen_yingxiao_zhaopian()
            factorypage.click_upload()
            factorypage.click_paizhao()
            factorypage.click_kuaimen()
            factorypage.click_paizhao_confirm()
            time.sleep(5)
            driver.back()
            factorypage.click_changjia_zhengming_wenjian()
            factorypage.click_upload()
            factorypage.click_paizhao()
            factorypage.click_kuaimen()
            factorypage.click_paizhao_confirm()
            time.sleep(5)
            driver.back()
            driver.back()
            factorypage.click_more_button()
            factorypage.click_start_flow()
            factorypage.click_start_flow_confirm()

            # time.sleep(2)
            # actual_result = factorypage.get_result(channel_name)
            # self.assertEqual(actual_result, expect_result)
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e

    # @unittest.skip('skip')
    def test_b_factory_approve(self):
        u"""审批添加厂家合作方流程"""
        casename = sys._getframe().f_code.co_name
        driver = self.driver
        yewu_no = self.yewu_no  # = "HZF-01598"
        # yewu_no = 'HZF-02081'
        process_type = "流通贷-合作方审核"
        approve_view = "OK"
        expect_result = "审批完成"
        print("审批添加厂家合作方流程开始")
        from com.ea.pages import approve_page
        pubapprovepage = approve_page.ApprovePubPage(driver)
        try:
            factoryapprovepage = FactoryApprove(driver)
            approver_account = tools.get_approver_acount_by_yewuno(yewu_no, process_type)
            if not approver_account:
                raise Exception
            while approver_account:
                tools.login(driver, username=approver_account)
                self.menu.click_approve_page()
                pubapprovepage.click_todo_first_row(yewu_no)
                pubapprovepage.click_first_row()
                pubapprovepage.click_my_approve()
                factoryapprovepage.input_approve_view(approve_view)
                factoryapprovepage.click_pass_button()
                factoryapprovepage.click_confirm()
                time.sleep(3)
                next_aprover = tools.get_approver_acount_by_yewuno(yewu_no, process_type)
                if not next_aprover:
                    break
                if approver_account != next_aprover:
                    approver_account = next_aprover
                    driver.start_activity(gl.packagename, gl.login_activity)
            factoryapprovepage.click_yiban()
            actual_result = factoryapprovepage.get_result(yewu_no)
            self.assertEqual(actual_result, expect_result)
            print("审批添加厂家合作方流程结束")
        except Exception as e:
            tools.screenshot(driver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()
