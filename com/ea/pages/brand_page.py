#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: brand_page.py 
@time: 2018/01/17 
"""
from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
import time


class BrandPage(BasePage):
    add_brand_loc = (By.XPATH, "//android.widget.TextView[@text='新增']")
    province_menu_loc = (By.XPATH, "//android.widget.TextView[@text='申请省份:']/..")
    province_loc = (By.XPATH, "//android.widget.TextView[@text='广州']/../..")
    brand_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入品牌名称']")
    brand_come_option_loc = (By.XPATH, '//android.widget.TextView[@text="品牌来源"]')
    brand_come_select_loc = (By.XPATH, '//android.widget.TextView[@text="请选择"]')
    brand_come_value_loc = (By.XPATH, "//android.widget.TextView[@text='平台公司']/../..")
    confirm_button_loc = (By.XPATH, '//android.widget.TextView[@text="确定"]')
    brand_zhimingdu_option_loc = (By.XPATH, '//android.widget.TextView[@text="品牌知名度:"]')
    brand_zhimingdu_value_loc = (By.XPATH, "//android.widget.TextView[@text='全国']")
    hangye_option_loc = (By.XPATH, '//android.widget.TextView[@text="所属行业"]')
    hangye_select_loc = (By.XPATH, '//android.widget.TextView[@text="请选择"]')
    hangye_value_loc = (By.XPATH, "//android.widget.TextView[@text='百货']")
    main_product_option_loc = (By.XPATH, "//android.widget.TextView[@text='主要产品']")
    main_product_content_loc = (By.XPATH, '//android.widget.EditText[@text="请输入文本"]')
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']/..")
    more_loc = (By.XPATH, "//android.widget.TextView[@text='品牌管理']/../following-sibling::android.widget.RelativeLayout")
    start_flow_loc = (By.XPATH, '//android.widget.CheckedTextView[@text="发起流程"]')

    def click_more_button(self):
        u"""点击右上角的..."""
        self.find_element(*self.more_loc).click()

    def click_start_flow(self):
        u"""点击发起流程"""
        self.find_element(*self.start_flow_loc).click()
        self.click_confirm()

    def get_result(self, brand_name):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//android.widget.TextView[@text='" + brand_name + "']/../../../..//android.widget.TextView[@text='状态']/following-sibling::android.widget.TextView")
        return self.find_element(*result_loc).text

    def get_brand_no_and_click(self, brand_name):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//android.widget.TextView[@text='" + brand_name + "']/../../../following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='品牌编码:']/following-sibling::android.widget.TextView")
        brand_no = self.find_element(*result_loc).text
        self.find_element(*result_loc).click()
        return brand_no

    def click_add_brand(self):
        u"""点击新增品牌按钮"""
        self.find_element(*self.add_brand_loc).click()

    def select_province(self):
        u"""选择申报省份"""
        self.find_element(*self.province_menu_loc).click()
        self.find_element(*self.province_loc).click()

    def input_brand_name(self, brand_name):
        u"""输入品牌名称"""
        self.send_keys(self.brand_name_loc, brand_name)

    def click_confirm(self):
        u"""点击确定按钮"""
        self.find_element(*self.confirm_button_loc).click()

    def click_brand_come(self):
        u"""点选品牌来源"""
        self.find_element(*self.brand_come_option_loc).click()
        self.find_element(*self.brand_come_select_loc).click()
        self.find_element(*self.brand_come_value_loc).click()
        self.click_confirm()

    def click_brand_zhimingdu(self):
        u"""点选品牌知名度"""
        self.find_element(*self.brand_zhimingdu_option_loc).click()
        self.find_element(*self.brand_zhimingdu_value_loc).click()

    def click_hangye(self):
        u"""点选所属行业"""
        self.find_element(*self.hangye_option_loc).click()
        self.find_element(*self.hangye_select_loc).click()
        self.find_element(*self.hangye_value_loc).click()
        self.click_confirm()

    def input_main_product(self, main_product):
        u"""输入主要产品"""
        self.find_element(*self.main_product_option_loc).click()
        self.send_keys(self.main_product_content_loc, main_product)
        self.click_confirm()

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()

    def click_brand_no(self, brand_no):
        u"""点击品牌编码"""
        brand_no_loc = (By.XPATH, '//android.widget.TextView[@text="' + brand_no + '"]')
        self.find_element(*brand_no_loc).click()


class BrandApprovePage(BasePage):
    approve_view_loc = (By.XPATH, "//android.widget.EditText[@text='请填写审核意见(不超过2000字)']")
    pass_button_loc = (By.XPATH, "//android.widget.TextView[@text='通过']")
    confirm_text_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    yiban_loc = (By.XPATH, '//android.widget.RadioButton[@text="已办"]')

    def input_approve_view(self, approve_view):
        self.send_keys(self.approve_view_loc, approve_view)

    def click_pass_button(self):
        self.find_element(*self.pass_button_loc).click()

    def click_confirm(self):
        self.find_element(*self.confirm_text_loc).click()

    def click_yiban(self):
        self.find_element(*self.yiban_loc).click()

    def get_result(self, brand_no):
        result = self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + brand_no + '"]/../../..//android.widget.TextView[@text="状态:"]/following-sibling::android.widget.TextView')).text
        return result
