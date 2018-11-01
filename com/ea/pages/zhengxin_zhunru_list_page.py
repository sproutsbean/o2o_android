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


class ZhengxinZhunruListPage(BasePage):
    first_row_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')

    zhengxin_zhunru_liucheng_loc = (By.XPATH, '//android.widget.TextView[@text="征信准入流程"]/..')
    daikuan_yaosu_loc = (By.XPATH, '//android.widget.TextView[@text="贷款要素"]/..')
    jiekuanren_jiben_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="借款人基本信息"]/..')
    jiekuanren_peiou_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="借款人配偶基本信息"]/..')
    fuqishuangfang_zhengxin_report_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方征信报告信息"]/..')
    jiekuanren_zhengxin_fujian_loc = (By.XPATH, '//android.widget.TextView[@text="借款人征信附件"]/..')
    peiou_zhengxin_fujian_loc = (By.XPATH, '//android.widget.TextView[@text="配偶征信附件"]/..')
    qiye_zhengxin_baogao_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="企业征信报告信息"]/..')
    qiye_zhengxin_fujian_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="企业征信附件信息"]/..')
    buchong_zhengxin_fujian_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="补充征信附件信息"]/..')
    qita_fujian_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="其他附件信息"]/..')

    fuqi_shuangfang_daikuan_jilu_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方的贷款记录"]/..')
    fuqi_shuangfang_daichang_shuju_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方代偿数据"]/..')
    fuqi_shuangfang_yuqi_shuju_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方逾期数据"]/..')
    daichang_yuqi_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="代偿和逾期信息"]/..')
    fuqi_shuangfang_danbao_daikuan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方担保贷款信息"]/..')
    danbaoren_xiangqing_loc = (By.XPATH, '//android.widget.TextView[@text="担保人详情"]/..')

    def click_first_row(self):
        self.find_element(*self.first_row_loc).click()

    def click_zhengxin_zhunru_liucheng(self):
        self.find_element(*self.zhengxin_zhunru_liucheng_loc).click()

    def click_daikuan_yaosu(self):
        self.find_element(*self.daikuan_yaosu_loc).click()

    def click_jiekuanren_jiben_xinxi(self):
        self.find_element(*self.jiekuanren_jiben_xinxi_loc).click()

    def click_jiekuanren_peiou_xinxi(self):
        self.find_element(*self.jiekuanren_peiou_xinxi_loc).click()

    def click_fuqishuangfang_zhengxin_report_xinxi(self):
        self.find_element(*self.fuqishuangfang_zhengxin_report_xinxi_loc).click()

    def click_jiekuanren_zhengxin_fujian(self):
        self.find_element(*self.jiekuanren_zhengxin_fujian_loc).click()

    def click_peiou_zhengxin_fujian(self):
        self.find_element(*self.peiou_zhengxin_fujian_loc).click()

    def click_qiye_zhengxin_baogao_xinxi(self):
        self.find_element(*self.qiye_zhengxin_baogao_xinxi_loc).click()

    def click_qiye_zhengxin_fujian_xinxi(self):
        self.find_element(*self.qiye_zhengxin_fujian_xinxi_loc).click()

    def click_buchong_zhengxin_fujian_xinxi(self):
        self.find_element(*self.buchong_zhengxin_fujian_xinxi_loc).click()

    def click_qita_fujian_xinxi(self):
        self.find_element(*self.qita_fujian_xinxi_loc).click()

    def click_fuqi_shuangfang_daikuan_jilu(self):
        self.find_element(*self.fuqi_shuangfang_daikuan_jilu_loc).click()

    def click_fuqi_shuangfang_daichang_shuju(self):
        self.find_element(*self.fuqi_shuangfang_daichang_shuju_loc).click()

    def click_fuqi_shuangfang_yuqi_shuju(self):
        self.find_element(*self.fuqi_shuangfang_yuqi_shuju_loc).click()

    def click_daichang_yuqi_xinxi(self):
        self.find_element(*self.daichang_yuqi_xinxi_loc).click()

    def click_fuqi_shuangfang_danbao_daikuan_xinxi(self):
        self.find_element(*self.fuqi_shuangfang_danbao_daikuan_xinxi_loc).click()

    def click_danbaoren_xiangqing(self):
        self.find_element(*self.danbaoren_xiangqing_loc).click()
