#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: interview_page.py 
@time: 2018/03/19 
"""

from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By
from com.ea.resource import globalparameter as gl
import time


class InterviewPage(BasePage):
    menu_loc = (By.XPATH, "//android.widget.TextView[@text='详情']/../following-sibling::android.widget.LinearLayout/android.widget.RelativeLayout[2]")
    edit_interview_info_loc = (By.XPATH, "//android.widget.CheckedTextView[@text='编辑面签资料']")
    xiazai_daishuju_hetong_loc = (By.XPATH, "//android.widget.CheckedTextView[@text='下载带数据合同']")
    next_button_loc = (By.XPATH, "//android.widget.TextView[@text='下一步']")
    bank_info_loc = (By.XPATH, "//android.widget.TextView[@text='银行卡信息']")
    hetongshifouqibei_loc = (By.XPATH, "//android.widget.TextView[@text='借款合同是否齐备:']")
    yes_loc = (By.XPATH, "//android.widget.TextView[@text='是']")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")
    mianqianfujian_loc = (By.XPATH, "//android.widget.TextView[@text='面签附件']")
    upload_loc = (By.XPATH, "//android.widget.TextView[@text='上传']")
    from_local_photos_loc = (By.XPATH, "//android.widget.TextView[@text='从本地相册选择']")
    photo_name_loc = (By.ID, gl.packagename + ":id/iv_select")
    mianqianshenbao_loc = (By.XPATH, "//android.widget.CheckedTextView[@text='面签申报']")
    confirm_text_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")

    bank_name_loc = (By.XPATH, '//android.widget.TextView[@text="开户行全称:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')
    bank_card_no_loc = (By.XPATH, '//android.widget.TextView[@text="银行卡号:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')

    def click_loan_no(self, loan_no):
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + loan_no + "']/preceding-sibling::android.widget.TextView")).click()

    def click_menu(self):
        self.find_element(*self.menu_loc).click()

    def click_edit_interview_info(self):
        self.find_element(*self.edit_interview_info_loc).click()

    def click_xiazai_daishuju_hetong(self):
        self.find_element(*self.xiazai_daishuju_hetong_loc).click()

    def click_next_button(self):
        self.find_element(*self.next_button_loc).click()

    def click_bank_info(self):
        self.find_element(*self.bank_info_loc).click()

    def input_bank_name(self, bankname):
        self.send_keys(self.bank_name_loc, bankname)

    def input_bank_no(self, bank_no):
        self.send_keys(self.bank_card_no_loc, bank_no)

    def select_hetongshifouqibei(self,qibei="是"):
        self.find_element(*self.hetongshifouqibei_loc).click()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if qibei == "是":
            count = 1
        elif qibei == "否":
            count = 0
        for i in range(count):
            self.driver.swipe(x / 2, y * 12 / 15, x / 2, y * 13 / 15, 2000)
        self.click_confirm()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def click_mianqianfujian(self):
        self.find_element(*self.mianqianfujian_loc).click()

    def click_upload(self):
        self.find_element(*self.upload_loc).click()

    def click_from_local_photos(self):
        self.find_element(*self.from_local_photos_loc).click()

    def click_photo_name(self):
        self.find_element(*self.photo_name_loc).click()
        self.click_confirm()

    def click_mianqianshenbao(self):
        self.find_element(*self.mianqianshenbao_loc).click()

    def click_confirm(self):
        self.find_element(*self.confirm_text_loc).click()
