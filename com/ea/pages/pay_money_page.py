#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: pay_money_page.py 
@time: 2018/03/16 
"""

from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By


class PayMoneyPage(BasePage):
    shenqingdakuan_loc = (By.XPATH, "//android.widget.TextView[@text='申请打款']")
    name_loc = (By.XPATH, "//android.widget.TextView[@text='姓名:']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    cardno_loc = (By.XPATH, "//android.widget.TextView[@text='证件号码:']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    next_button_loc = (By.XPATH, "//android.widget.TextView[@text='下一步']")
    dakuanjine_loc = (By.XPATH, "//android.widget.TextView[@text='打款金额（元）:']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    dakuanshijian_loc = (By.XPATH, "//android.widget.TextView[@text='打款时间:']/following-sibling::android.widget.LinearLayout")
    shiji_dakuanren_loc = (By.XPATH, '//android.widget.TextView[@text="实际打款人:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')
    confirm_text_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")
    start_flow_loc = (By.XPATH, "//android.widget.TextView[@text='启动流程']")
    shaixuan_loc = (By.XPATH, "//android.widget.TextView[@text='筛选']")
    shaixuan_xingming_loc = (By.XPATH, "//android.widget.TextView[@text='姓名:']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    search_button_loc = (By.XPATH, "//android.widget.Button[@text='搜索']")

    def click_confirm_text(self):
        self.find_element(*self.confirm_text_loc).click()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def click_row_by_name(self, name):
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + name + "']")).click()

    def get_dakuandanhao(self):
        return self.find_element(*(By.XPATH, "//android.widget.TextView[@text='单号:']/following-sibling::android.widget.TextView")).text

    def click_shenqingdakuan(self):
        self.find_element(*self.shenqingdakuan_loc).click()

    def input_name(self, name):
        self.send_keys(self.name_loc, name)

    def input_cardno(self, cardno):
        self.send_keys(self.cardno_loc, cardno)

    def click_next_button(self):
        self.find_element(*self.next_button_loc).click()

    def input_dakuanjine(self, jine):
        self.send_keys(self.dakuanjine_loc, jine)

    def select_dakuanshijian(self):
        self.find_element(*self.dakuanshijian_loc).click()
        self.click_confirm_text()

    def input_shiji_dakuanren(self, dakuanren):
        self.send_keys(self.shiji_dakuanren_loc, dakuanren)

    def click_shaixuan(self):
        self.find_element(*self.shaixuan_loc).click()

    def input_shaixuan_xingming(self, xingming):
        self.send_keys(self.shaixuan_xingming_loc, xingming)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def click_start_flow(self):
        self.find_element(*self.start_flow_loc).click()
