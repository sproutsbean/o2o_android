#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: brand_management.py 
@time: 2018/01/17 
"""
from com.ea.common import tools
from com.ea.resource import globalparameter as gl
from com.ea.pages.brand_page import BrandPage
from com.ea.pages.add_dealer_page import DealerPage
from com.ea.pages.todo_page import TodoPage, FactoryApprove, DealerApprove
from com.ea.pages.menu_page import MenuPage
import time
import os
import sys
import unittest


class MyTestCase(unittest.TestCase):
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    brand_no = ""
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

    def test_a_add_brand(self):
        u"""新增品牌"""
        casename = sys._getframe().f_code.co_name
        driver = self.driver
        except_result = "审核中"
        brand_name = tools.get_chinese()
        main_product = tools.get_chinese()
        try:
            tools.login(self.driver)
            menupage = MenuPage(self.driver)
            menupage.click_brand_manage()
            brandpage = BrandPage(driver)
            brandpage.click_add_brand()
            brandpage.select_province()
            brandpage.input_brand_name(brand_name)
            brandpage.click_brand_come()
            brandpage.click_brand_zhimingdu()
            brandpage.click_hangye()
            brandpage.swipe("up")
            time.sleep(1)
            brandpage.input_main_product(main_product)
            brandpage.click_save_button()
            brandpage.click_confirm()
            time.sleep(2)
            MyTestCase.brand_no = tools.get_brand_no_by_brandname(brand_name)
            brandpage.click_brand_no(self.brand_no)
            brandpage.click_more_button()
            brandpage.click_start_flow()
            time.sleep(3)
            actual_result = brandpage.get_result(brand_name)
            self.assertEqual(except_result, actual_result)
            print(self.brand_no)
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_b_brand_approve(self):
        u"""审批新增品牌流程"""
        casename = sys._getframe().f_code.co_name
        driver = self.driver
        process_type = "流通贷品牌审核"
        approve_view = "OK"
        except_result = "审批完成"
        try:
            approver_account = tools.get_approver_acount_by_yewuno(self.brand_no, process_type)
            tools.login(driver, username=approver_account)
            from com.ea.pages import brand_page
            from com.ea.pages import approve_page
            pubapprovepage = approve_page.ApprovePubPage(driver)
            brandapprovepage = brand_page.BrandApprovePage(driver)
            self.menu.click_approve_page()
            pubapprovepage.click_todo_first_row(self.brand_no)
            pubapprovepage.click_first_row()
            pubapprovepage.click_my_approve()
            brandapprovepage.input_approve_view(approve_view)
            brandapprovepage.click_pass_button()
            brandapprovepage.click_confirm()
            time.sleep(3)
            brandapprovepage.click_yiban()
            actual_result = brandapprovepage.get_result(self.brand_no)
            self.assertEqual(except_result, actual_result)
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e


    #
    # @unittest.skip('skip')
    # def test_e_add_dealer(self):
    #     u"""添加经销商合作方"""
    #     casename = sys._getframe().f_code.co_name
    #     driver = self.driver
    #     brand_no = self.brand_no = "BRAND-00728"
    #     pic_path = gl.test_pic_path
    #     expect_result = "审核中"
    #     channel_name = chinese.get_chinese() + "渠道"
    #     province = "贵州"
    #     isloan = "无贷款户"
    #     xiaoshouliantiaojiegou = "厂家-厂家自有代理-地区-一批"
    #     business_license_name = "营业执照名称A"
    #     business_license_no = "yyzz0001"
    #     frdb = "张三"
    #     setup_time = "2016-10-10"
    #     register_money = "10"
    #     business_province = "北京"
    #     business_area = "北京市市辖区"
    #     business_road = "无名路"
    #     warehouse_area = "120"
    #     cars_no = "5"
    #     brand_time = "2"
    #     brand_limit_time = "5"
    #     other_brand_no = "3"
    #     other_brand_name = "品牌A,品牌B,品牌C"
    #     downstreamTwoPattern = "3"
    #     year_sales = "50"
    #     try:
    #         # login.login(driver)
    #         menu.go_to_brand_manage(driver)
    #         dealerpage = DealerPage(driver)
    #         handle1 = driver.current_window_handle
    #         dealerpage.click_add_dealer(brand_no)
    #         handles = driver.window_handles
    #         for handle in handles:
    #             if handle != handle1:
    #                 driver.switch_to.window(handle)
    #         dealerpage.select_fenlei(isloan)
    #         dealerpage.click_next_button()
    #         dealerpage.select_province(province)
    #         dealerpage.input_xiaoshouliantiaojiegou(xiaoshouliantiaojiegou)
    #         dealerpage.input_businessLicenseName(business_license_name)
    #         dealerpage.input_businessLicenseNo(business_license_no)
    #         dealerpage.input_law_name(frdb)
    #         dealerpage.input_setup_time(setup_time)
    #         dealerpage.input_registeredCapital(register_money)
    #         dealerpage.select_manage_province(business_province)
    #         dealerpage.select_manage_area(business_area)
    #         dealerpage.input_manage_detail(business_road)
    #         dealerpage.input_warehouseArea(warehouse_area)
    #         dealerpage.input_transportVehiclesNum(cars_no)
    #         dealerpage.input_brandCooperationTerm(brand_time)
    #         dealerpage.input_otherBrandNum(other_brand_no)
    #         dealerpage.input_brandLicensingDeadline(brand_limit_time)
    #         dealerpage.input_agencyOtherBrand(other_brand_name)
    #         dealerpage.input_downstreamTwoPattern(downstreamTwoPattern)
    #         dealerpage.input_annualSales(year_sales)
    #         dealerpage.click_brandLicensingArea()
    #         dealerpage.scroll_to_save_button()
    #         dealerpage.click_save_button()
    #         dealerpage.scroll_to_edit(business_license_name)
    #         dealerpage.click_edit(business_license_name)
    #         dealerpage.scroll_to_start_flow()
    #         dealerpage.input_upload_report(pic_path)
    #         dealerpage.input_upload_factory_prove_file(pic_path)
    #         dealerpage.input_upload_marketing_photo(pic_path)
    #         dealerpage.click_start_flow()
    #         actual_result = dealerpage.get_result(business_license_name)
    #         MyTestCase.yewu_no = dealerpage.get_yewuno(business_license_name)
    #         driver.close()
    #         driver.switch_to.window(handle1)
    #         print(MyTestCase.yewu_no)
    #         self.assertEqual(actual_result, expect_result)
    #     except Exception as e:
    #         tools.get_screenshot(driver, self.screenshot_path, casename)
    #         raise e
    #
    # @unittest.skip('skip')
    # def test_e_dealer_approve(self):
    #     u"""审批添加经销商合作方流程"""
    #     casename = sys._getframe().f_code.co_name
    #     driver = self.driver
    #     yewu_no = self.yewu_no = "JXS_HZF-00304"
    #     process_type = "流通贷-经销商合作方审核"
    #     approve_view = "OK"
    #     expect_result = "审核通过"
    #     try:
    #         todopage = TodoPage(driver)
    #         dealerapprovepage = DealerApprove(driver)
    #         menu.go_to_wait_todo_query(driver)
    #         driver.delete_all_cookies()
    #         for i in range(4):
    #             approver_account = tools.get_approver_acount_by_yewuno(yewu_no, process_type)
    #             login.login(driver, username=approver_account)
    #             menu.go_to_wait_todo_query(driver)
    #             todopage.input_yewuno(yewu_no)
    #             todopage.click_search_button()
    #             todopage.click_first_row(process_type)
    #             dealerapprovepage.scroll_to_approve_view()
    #             dealerapprovepage.input_approve_view(approve_view)
    #             dealerapprovepage.click_tongguo_button()
    #             dealerapprovepage.click_confirm_button()
    #             time.sleep(3)
    #             driver.delete_all_cookies()
    #         login.login(driver)
    #         menu.go_to_jxshzf_manage(driver)
    #         actual_result = dealerapprovepage.get_result(yewu_no)
    #         self.assertEqual(actual_result, expect_result)
    #     except Exception as e:
    #         tools.get_screenshot(driver, self.screenshot_path, casename)
    #         raise e


if __name__ == '__main__':
    unittest.main()
