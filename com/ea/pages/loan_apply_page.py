#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: loan_apply_page.py 
@time: 2018/03/12 
"""
from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By
import time
from com.ea.resource import globalparameter as gl


class LoanApplyPage(BasePage):
    loan_type_loc = (By.XPATH, "//android.widget.TextView[@text='贷款类型:']")
    cardno_loc = (By.XPATH, "//android.widget.EditText[@text='请输入身份证号码']")
    next_button_loc = (By.XPATH, "//android.widget.TextView[@text='下一步']")
    first_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入借款人姓']")
    second_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入借款人名']")
    first_english_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入借款人姓拼音']")
    second_english_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入借款人名拼音']")
    card_expire_date_loc = (By.XPATH, "//android.widget.EditText[@text='请选择证件到期日']")
    phoneno_loc = (By.XPATH, "//android.widget.EditText[@text='请输入联系电话']")
    marry_status_option_loc = (By.XPATH, "//android.widget.TextView[@text='婚姻状况:']")

    apply_sum_of_money_loc = (By.XPATH, "//android.widget.EditText[@text='请输入申请金额']")
    loan_manager_option_loc = (By.XPATH, "//android.widget.TextView[@text='请输入信贷经理']")
    loan_manager_editview_loc = (By.XPATH, "//android.widget.EditText[@text='请输入信贷经理']")
    loan_manager_name_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    operate_mode_option_loc = (By.XPATH, "//android.widget.TextView[@text='经营模式:']")
    platform_option_loc = (By.XPATH, "//android.widget.TextView[@text='经营平台:']/following-sibling::android.widget.LinearLayout/android.widget.TextView")
    platform_editview_loc = (By.XPATH, "//android.widget.EditText[@text='请输入经办平台']")
    platform_name_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    sd_customer_name_option_loc = (By.XPATH, "//android.widget.TextView[@text='请输入SD客户名称,至少输入4个字才能搜索']")
    sd_customer_name_editview_loc = (By.XPATH, "//android.widget.EditText[@text='请输入SD客户名称,至少输入4个字才能搜索']")
    sd_customer_name_value_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    channel_name_option_loc = (By.XPATH, "//android.widget.TextView[@text='渠道名称:']//following-sibling::android.widget.LinearLayout/android.widget.TextView")
    channel_name_edit_loc = (By.XPATH, "//android.widget.EditText[@text='请输入渠道名称']")
    channel_name_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")
    guanlian_loc = (By.XPATH, '//android.widget.TextView[@text="关联"]')
    loan_no_loc = (By.XPATH, "//android.widget.TextView[@text='CMY000001-BK-1803-00003']")
    zhengxin_report_option_loc = (By.XPATH, "//android.widget.TextView[@text='夫妻双方征信报告信息']")
    name_loc = (By.XPATH, "//android.widget.TextView[@text='姓名']")
    radio_button_loc = (By.XPATH, "//android.widget.RadioButton[@index='0']")
    confirm_button_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    start_flow_loc = (By.XPATH, "//android.widget.TextView[@text='启动流程']")

    zhengxin_apply_loc = (By.XPATH, '//android.widget.TextView[@text="申请征信"]')
    zhengxin_bank_option_loc = (By.XPATH, "//android.widget.TextView[@text='征信银行:']")
    zhengxin_bank_name_loc = (By.XPATH, "//android.widget.TextView[@text='江西银行']")
    shenfenzhengfuyinjian_loc = (By.XPATH, "//android.widget.TextView[@text='客户身份证复印件']")
    shouchishouquanshu_loc = (By.XPATH, "//android.widget.TextView[@text='客户手持授权书及身份证照片']")
    zhengxinshouquanshu_loc = (By.XPATH, "//android.widget.TextView[@text='客户征信授权书']")
    disanfangshujuchaxunshouquanshu_loc = (By.XPATH, "//android.widget.TextView[@text='客户第三方数据查询授权书']")
    shouchishenfenzheng_loc = (By.XPATH, "//android.widget.TextView[@text='客户手持身份证及查询授权书']")
    kehuhukouben_loc = (By.XPATH, "//android.widget.TextView[@text='客户户口本复印件']")
    zxbgsysqsm_loc = (By.XPATH, "//android.widget.TextView[@text='征信报告使用授权声明']")
    sxsqysx_loc = (By.XPATH, '//android.widget.TextView[@text="授信申请意向书"]')
    jkryyytmywlfj_loc = (By.XPATH, '//android.widget.TextView[@text="借款人与怡亚通贸易往来附件"]')
    from_photo_album_loc = (By.XPATH, "//android.widget.TextView[@text='从本地相册选择']")
    photo_name_loc = (By.ID, gl.packagename + ':id/iv_select')

    partner_first_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶姓"]')
    partner_last_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶名"]')
    partner_first_english_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶姓拼音"]')
    partner_last_english_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶名拼音"]')
    partner_card_no_loc = (By.XPATH, '//android.widget.EditText[@text="请输入证件号码"]')
    partner_card_exprit_date_loc = (By.XPATH, '//android.widget.EditText[@text="请选择证件到期日"]')
    partner_phone_no_loc = (By.XPATH, '//android.widget.EditText[@text="请输入联系电话"]')

    danbaoren_xiangqing_loc = (By.XPATH, '//android.widget.TextView[@text="担保人详情"]/..')
    add_button_loc = (By.XPATH, '//android.widget.TextView[@text="新增"]/..')
    danbaoren_name_option_loc = (By.XPATH, '//android.widget.TextView[@text="担保人姓名:"]/..')
    danbaoren_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入"]')
    first_danbaoren_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')
    yujiekuanren_guanxi_loc = (By.XPATH, '//android.widget.TextView[@text="与借款人关系:"]/..')

    def select_loan_type(self, loan_type):
        self.find_element(*self.loan_type_loc).click()
        time.sleep(1)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if loan_type == "终端贷":
            count = 0
        elif loan_type == "流通贷-厂家":
            count = 1
        elif loan_type == "流通贷-经销商":
            count = 2
        elif loan_type == "流通贷-蔬果":
            count = 3
        elif loan_type == "流通贷-烟草":
            count = 4
        elif loan_type == "流通贷-商超":
            count = 5
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def select_operate_mode(self, operate_mode):
        self.find_element(*self.operate_mode_option_loc).click()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        time.sleep(1)
        if operate_mode == "自营模式":
            count = 0
        elif operate_mode == "共享模式":
            count = 1
        elif operate_mode == "推荐模式":
            count = 2
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def input_cardno(self, cardno):
        self.send_keys(self.cardno_loc, cardno)

    def click_next_button(self):
        self.find_element(*self.next_button_loc).click()

    def send_first_name(self, first_name):
        u"""输入姓"""
        self.send_keys(self.first_name_loc, first_name)

    def send_second_name(self, second_name):
        u"""输入名"""
        self.send_keys(self.second_name_loc, second_name)

    def send_first_english_name(self, first_english_name):
        u"""输入姓拼音"""
        self.send_keys(self.first_english_name_loc, first_english_name)

    def send_second_english_name(self, second_english_name):
        u"""输入名拼音"""
        self.send_keys(self.second_english_name_loc, second_english_name)

    def click_card_expire_date(self):
        u"""点选证件到期日期"""
        self.find_element(*self.card_expire_date_loc).click()
        self.click_confirm_button()

    def send_phoneno(self, phoneno):
        u"""输入手机号"""
        self.send_keys(self.phoneno_loc, phoneno)

    def select_marry_status(self, status='未婚'):
        self.find_element(*self.marry_status_option_loc).click()
        time.sleep(1)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if status == "未婚":
            count = 0
        elif status == "已婚":
            count = 1
        elif status == "离异":
            count = 2
        elif status == "丧偶":
            count = 3
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def input_partner_first_name(self, first_name):
        u"""输入配偶姓"""
        self.send_keys(self.partner_first_name_loc, first_name)

    def input_partner_last_name(self, second_name):
        u"""输入配偶名"""
        self.send_keys(self.partner_last_name_loc, second_name)

    def input_partner_first_english_name(self, first_english_name):
        u"""输入配偶姓拼音"""
        self.send_keys(self.partner_first_english_name_loc, first_english_name)

    def input_partner_last_english_name(self, second_english_name):
        u"""输入配偶名拼音"""
        self.send_keys(self.partner_last_english_name_loc, second_english_name)

    def input_partner_card_no(self, cardno):
        u"""输入配偶身份证号码"""
        self.send_keys(self.partner_card_no_loc, cardno)

    def input_loan_sumofmoney(self, sumofmoney):
        self.send_keys(self.apply_sum_of_money_loc, sumofmoney)

    def select_loan_manager(self, loan_manager):
        self.find_element(*self.loan_manager_option_loc).click()
        self.send_keys(self.loan_manager_editview_loc, loan_manager)
        self.find_element(*self.loan_manager_name_loc).click()

    def input_platform(self, platform):
        self.find_element(*self.platform_option_loc).click()
        self.send_keys(self.platform_editview_loc, platform)
        self.find_element(*self.platform_name_loc).click()

    def input_sd_customer_name(self, sd_customer_name="1111"):
        self.find_element(*self.sd_customer_name_option_loc).click()
        self.send_keys(self.sd_customer_name_editview_loc, sd_customer_name)
        self.find_element(*self.sd_customer_name_value_loc).click()

    def input_channel_name(self, channel_name="1"):
        self.find_element(*self.channel_name_option_loc).click()
        self.send_keys(self.channel_name_edit_loc, channel_name)
        self.find_element(*self.channel_name_loc).click()

    def click_guanlian_button(self):
        self.find_element(*self.guanlian_loc).click()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def click_loan_no(self, loan_no):
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + loan_no + "']/preceding-sibling::android.widget.TextView")).click()

    def click_radio_button(self):
        self.find_element(*self.radio_button_loc).click()

    def select_zhengxin_report(self):
        self.find_element(*self.zhengxin_report_option_loc).click()
        self.find_element(*self.name_loc).click()
        self.click_radio_button()
        self.click_save_button()
        self.click_confirm_button()
        time.sleep(1)
        self.driver.back()

    def select_fuqizhengxin_report(self):
        self.find_element(*self.zhengxin_report_option_loc).click()

    def click_name(self, borrower_name):
        self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + borrower_name + '"]/../preceding-sibling::android.widget.TextView[@text="姓名"]')).click()

    def click_zhengxin_apply(self):
        self.find_element(*self.zhengxin_apply_loc).click()

    def click_zhengxin_bank_option(self):
        u"""点击征信银行选项框"""
        self.find_element(*self.zhengxin_bank_option_loc).click()

    def click_zhengxin_bank_name(self, bank_name="江西银行"):
        u"""点击征信银行名字"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if bank_name == "中国银行":
            count = 0
        elif bank_name == "中国建设银行-深圳":
            count = 1
        elif bank_name == "中国建设银行-湖南":
            count = 2
        elif bank_name == "中信银行":
            count = 3
        elif bank_name == "华夏银行":
            count = 4
        elif bank_name == "上海银行":
            count = 5
        elif bank_name == "国安村镇银行":
            count = 6
        elif bank_name == "齐鲁银行":
            count = 7
        elif bank_name == "兴业银行-济南":
            count = 8
        elif bank_name == "江西银行":
            count = 9
        elif bank_name == "郑州银行":
            count = 10
        elif bank_name == "浦发广州分行":
            count = 11
        elif bank_name == "三湘银行":
            count = 12
        elif bank_name == "中旅银行":
            count = 13
        elif bank_name == "浦发济南分行":
            count = 14
        elif bank_name == "微众银行":
            count = 15
        elif bank_name == "怡亚通":
            count = 16
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def click_from_photo_album(self):
        u"""点击从本地相册"""
        self.find_element(*self.from_photo_album_loc).click()

    def click_photo_name(self):
        u"""点击相片的名字"""
        self.find_element(*self.photo_name_loc).click()

    def click_shenfenzhengfuyinjian(self):
        u"""点击身份证复印件"""
        self.find_element(*self.shenfenzhengfuyinjian_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_shouchishouquanshu(self):
        u"""点击手持授权书"""
        self.find_element(*self.shouchishouquanshu_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_zhengxinshouquanshu(self):
        u"""点击征信授权书"""
        self.find_element(*self.zhengxinshouquanshu_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_disanfangshujuchaxunshouquanshu(self):
        u"""点击第三方数据查询授权书"""
        self.find_element(*self.disanfangshujuchaxunshouquanshu_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_shouchishenfenzheng(self):
        u"""点击手持身份证"""
        self.find_element(*self.shouchishenfenzheng_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_kehuhukouben(self):
        u"""点击客户户口本复印件"""
        self.find_element(*self.kehuhukouben_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_zxbgsysqsm(self):
        u"""点击征信报告使用授权声明"""
        self.find_element(*self.zxbgsysqsm_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_sxsqyxs(self):
        u"""点击授信申请意向书"""
        self.find_element(*self.sxsqysx_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_jkryyytmywlfj(self):
        u"""点击借款人与怡亚通贸易往来附件"""
        self.find_element(*self.jkryyytmywlfj_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()

    def click_start_flow(self):
        self.find_element(*self.start_flow_loc).click()
        self.click_confirm_button()

    def get_zx_status_by_name(self, name):
        return self.find_element(*(By.XPATH,
                                   '//android.widget.TextView[@text="' + name + '"]/../../../following-sibling::android.widget.LinearLayout[6]//android.widget.TextView[@text="征信状态"]/following-sibling::android.widget.LinearLayout/android.widget.TextView')).text

    def click_danbaoren_xiangqing(self):
        self.find_element(*self.danbaoren_xiangqing_loc).click()

    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    def click_danbaoren_name_option(self):
        self.find_element(*self.danbaoren_name_option_loc).click()

    def input_danbaoren_name(self, danbaoren_name="张担保"):
        self.send_keys(self.danbaoren_name_loc, danbaoren_name)

    def click_first_danbaoren(self):
        self.find_element(*self.first_danbaoren_loc).click()

    def click_yujiekuanren_guanxi(self):
        self.find_element(*self.yujiekuanren_guanxi_loc).click()

    def click_guanxi(self, guanxi="朋友"):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if guanxi == "朋友":
            count = 0
        elif guanxi == "亲戚":
            count = 1
        elif guanxi == "直系亲戚":
            count = 2
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()
