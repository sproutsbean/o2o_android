#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: menu_page.py 
@time: 2018/02/27 
"""

from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By
import time


class MenuPage(BasePage):
    home_page_loc = (By.XPATH, "//android.widget.RadioButton[@text='首页']")
    approve_page_loc = (By.XPATH, "//android.widget.RadioButton[@text='审批']")
    me_page_loc = (By.XPATH, "//android.widget.RadioButton[@text='我']")

    loan_apply_loc = (By.XPATH, "//android.widget.TextView[@text='申请贷款']")
    zhengxinzhuru_loc = (By.XPATH, "//android.widget.TextView[@text='征信准入']")
    inside_approve_loc = (By.XPATH, "//android.widget.TextView[@text='内部审批']")
    interview_loc = (By.XPATH, "//android.widget.TextView[@text='面签提报']")
    platform_caiwu_approve_loc = (By.XPATH, "//android.widget.TextView[@text='平台财务审核']")
    loan_apply_query_loc = (By.XPATH, "//android.widget.TextView[@text='贷款申请查询']")
    personal_zhengxin_query_loc = (By.XPATH, "//android.widget.TextView[@text='个人征信查询']")
    company_zhengxin_query_loc = (By.XPATH, "//android.widget.TextView[@text='企业征信查询']")
    release_loan_query_loc = (By.XPATH, "//android.widget.TextView[@text='放款查询']")
    five_arive_warning_loc = (By.XPATH, "//android.widget.TextView[@text='5天到期预警']")
    ten_arive_warning_loc = (By.XPATH, "//android.widget.TextView[@text='10天到期预警']")
    after_loan_check_loc = (By.XPATH, "//android.widget.TextView[@text='贷后定期检查']")
    zhengxin_save_loc = (By.XPATH, "//android.widget.TextView[@text='征信归档']")
    after_loan_save_loc = (By.XPATH, "//android.widget.TextView[@text='贷后归档']")
    repayment_plan_loc = (By.XPATH, "//android.widget.TextView[@text='还款计划']")
    loan_apply_summary_loc = (By.XPATH, "//android.widget.TextView[@text='贷款申请汇总']")
    release_loan_summary_loc = (By.XPATH, "//android.widget.TextView[@text='贷款放款汇总']")
    by_time_summary_loan_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'按时间区间统计')]")
    by_day_summary_loan_loc = (By.XPATH, "//android.widget.TextView[@text='按天统计放款量']")
    release_business_summary_table_loc = (By.XPATH, "//android.widget.TextView[@text='放款业务统计表']")
    brand_manage_loc = (By.XPATH, "//android.widget.TextView[@text='品牌管理']")
    factory_manage_loc = (By.XPATH, "//android.widget.TextView[@text='厂家合作方管理']")
    dealer_manage_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'经销商合作方')]")
    channel_manage_loc = (By.XPATH, "//android.widget.TextView[@text='渠道管理']")
    play_money_manage_loc = (By.XPATH, "//android.widget.TextView[@text='打款管理']/../..")
    back_money_manage_loc = (By.XPATH, "//android.widget.TextView[@text='退款管理']")
    charge_manage_loc = (By.XPATH, "//android.widget.TextView[@text='收费管理']")
    operation_guide_loc = (By.XPATH, "//android.widget.TextView[@text='操作指引']")
    requirements_apply_loc = (By.XPATH, "//android.widget.TextView[@text='需求申请']")
    ea_address_book_loc = (By.XPATH, "//android.widget.TextView[@text='EA通讯录']")

    def click_home_page(self):
        """点击首页按钮"""
        self.find_element(*self.home_page_loc).click()
        time.sleep(2)

    def click_approve_page(self):
        """点击审批按钮"""
        self.find_element(*self.approve_page_loc).click()
        time.sleep(2)

    def click_me_page(self):
        """点击我按钮"""
        self.find_element(*self.me_page_loc).click()
        time.sleep(2)

    def click_loan_apply(self):
        """点击申请贷款按钮"""
        self.find_element(*self.loan_apply_loc).click()
        time.sleep(2)

    def click_zhengxinzhunru(self):
        """点击征信准入按钮"""
        self.find_element(*self.zhengxinzhuru_loc).click()
        time.sleep(2)

    def click_inside_approve(self):
        """点击内部审批按钮"""
        self.find_element(*self.inside_approve_loc).click()
        time.sleep(2)

    def click_interview(self):
        """点击面签提报按钮"""
        self.find_element(*self.interview_loc).click()
        time.sleep(2)

    def click_platform_caiwu_approve(self):
        """点击平台财务审核按钮"""
        self.find_element(*self.platform_caiwu_approve_loc).click()
        time.sleep(2)

    def click_loan_apply_query(self):
        """点击贷款申请查询按钮"""
        self.find_element(*self.loan_apply_query_loc).click()
        time.sleep(2)

    def click_personal_zhengxin_query(self):
        """点击个人征信查询"""
        self.find_element(*self.personal_zhengxin_query_loc).click()
        time.sleep(2)

    def click_company_zhengxin_query(self):
        """点击企业征信查询"""
        self.find_element(*self.company_zhengxin_query_loc).click()
        time.sleep(2)

    def click_release_loan_query(self):
        """点击放款查询"""
        self.find_element(*self.release_loan_query_loc).click()
        time.sleep(2)

    def click_five_arive_warning(self):
        """点击5天到期预警"""
        self.find_element(*self.five_arive_warning_loc).click()
        time.sleep(2)

    def click_ten_arive_warning(self):
        """点击10天到期预警"""
        self.find_element(*self.ten_arive_warning_loc).click()
        time.sleep(2)

    def click_after_loan_check(self):
        """点击贷后定期检查"""
        self.find_element(*self.after_loan_check_loc).click()
        time.sleep(2)

    def click_zhengxin_save(self):
        """点击征信归档"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.zhengxin_save_loc).click()
        time.sleep(2)

    def click_after_loan_save(self):
        """点击贷后归档"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.after_loan_save_loc).click()
        time.sleep(2)

    def click_repayment_plan(self):
        """点击还款计划"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.repayment_plan_loc).click()
        time.sleep(2)

    def click_loan_apply_summary(self):
        """点击贷款申请汇总"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.loan_apply_summary_loc).click()
        time.sleep(2)

    def click_release_loan_summary(self):
        """点击贷款放款汇总"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.release_loan_summary_loc).click()
        time.sleep(2)

    def click_by_time_summary_loan(self):
        """点击按时间区间统计放款量"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.by_time_summary_loan_loc).click()
        time.sleep(2)

    def click_by_day_summary_loan(self):
        """点击按天统计放款量"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.by_day_summary_loan_loc).click()
        time.sleep(2)

    def click_release_business_summary_table(self):
        """点击放款业务统计表"""
        time.sleep(2)
        self.swipe("up")
        self.find_element(*self.release_business_summary_table_loc).click()
        time.sleep(2)

    def click_brand_manage(self):
        """点击品牌管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.brand_manage_loc).click()
        time.sleep(2)

    def click_factory_manage(self):
        """点击厂家合作方管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.factory_manage_loc).click()
        time.sleep(2)

    def click_dealer_manage(self):
        """点击经销商合作方管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.dealer_manage_loc).click()
        time.sleep(2)

    def click_channel_manage(self):
        """点击渠道管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.channel_manage_loc).click()
        time.sleep(2)

    def click_play_money_manage(self):
        """点击打款管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(2)
        self.swipe("up")
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.find_element(*self.play_money_manage_loc).click()
        time.sleep(2)

    def click_back_money_manage(self):
        """点击退款管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.back_money_manage_loc).click()
        time.sleep(2)

    def click_charge_manage(self):
        """点击收费管理"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.charge_manage_loc).click()
        time.sleep(2)

    def click_operation_guide(self):
        """点击操作指引"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.operation_guide_loc).click()
        time.sleep(2)

    def click_requirements_apply(self):
        """点击需求申请"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.requirements_apply_loc).click()
        time.sleep(2)

    def click_ea_address_book(self):
        """点击EA通讯录"""
        time.sleep(2)
        self.swipe("up")
        time.sleep(1)
        self.swipe("up")
        self.find_element(*self.ea_address_book_loc).click()
        time.sleep(2)
