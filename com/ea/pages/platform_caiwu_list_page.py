#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: add_factory_page.py 
@time: 2018/01/19 
"""
from com.ea.common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class PlatformCaiwuListPage(BasePage):
    first_row_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')

    shenheliucheng_loc = (By.XPATH, '//android.widget.TextView[@text="审核流程"]/..')
    daikuan_jiben_ziliao_loc = (By.XPATH, '//android.widget.TextView[@text="贷款基本资料"]/..')
    jiekuanren_jiben_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="借款人基本信息"]/..')
    jiekuanren_peiou_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="借款人配偶基本信息"]/..')
    kehu_zichan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="客户资产信息"]/..')
    sd_xitong_jiaoyi_jilu_huizongbiao_loc = (By.XPATH, '//android.widget.TextView[@text="sd系统交易记录汇总表"]/..')
    caiwu_shenhe_sd_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="财务审核SD信息"]/..')
    caiwu_shenhe_jilu_loc = (By.XPATH, '//android.widget.TextView[@text="财务审核记录"]/..')

    def get_first_row_status(self):
        status = self.find_element(*(By.XPATH, '//android.widget.TextView[@text="单据状态"]/following-sibling::android.widget.TextView')).text
        danhao = self.find_element(*(By.XPATH, '//android.widget.TextView[@text="贷款单号:"]/following-sibling::android.widget.TextView')).text
        print("第一条记录的单号是:", danhao, " 状态是:", status)
        return status

    def click_first_row(self):
        print("点击第一条记录")
        self.find_element(*self.first_row_loc).click()

    def click_shenheliucheng(self):
        print("点击审核流程")
        self.find_element(*self.shenheliucheng_loc).click()

    def click_daikuan_jiben_ziliao(self):
        print("点击贷款基本资料")
        self.find_element(*self.daikuan_jiben_ziliao_loc).click()

    def click_jiekuanren_jiben_xinxi(self):
        print("点击借款人基本信息")
        self.find_element(*self.jiekuanren_jiben_xinxi_loc).click()
        marry_status = self.find_element(*(By.XPATH, '//android.widget.TextView[@text="婚姻状况:"]/following-sibling::android.widget.LinearLayout/android.widget.TextView')).text
        print("婚姻状况是:", marry_status)
        return marry_status

    def click_jiekuanren_peiou_xinxi(self):
        print("点击借款人配偶基本信息")
        self.find_element(*self.jiekuanren_peiou_xinxi_loc).click()

    def click_kehu_zichan_xinxi(self):
        print("点击客户资产信息")
        self.find_element(*self.kehu_zichan_xinxi_loc).click()

    def click_sd_xitong_jiaoyi_jilu_huizongbiao(self):
        print("点击SD系统交易记录汇总表")
        self.find_element(*self.sd_xitong_jiaoyi_jilu_huizongbiao_loc).click()

    def click_caiwu_shenhe_sd_xinxi(self):
        print("点击财务审核SD信息")
        self.find_element(*self.caiwu_shenhe_sd_xinxi_loc).click()

    def click_caiwu_shenhe_jilu(self):
        print("点击财务审核记录")
        self.find_element(*self.caiwu_shenhe_jilu_loc).click()
