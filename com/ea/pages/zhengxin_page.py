#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: zhengxin_page.py 
@time: 2018/03/05 
"""
from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By
from com.ea.resource import globalparameter as gl


class ZhengxinPage(BasePage):
    apply_button_loc = (By.XPATH, "//android.widget.TextView[@text='申请']")
    cardno_loc = (By.XPATH, "//android.widget.EditText[@text='请输入身份证号码']")
    next_button_loc = (By.XPATH, "//android.widget.TextView[@text='下一步']")
    first_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入借款人姓']")
    second_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入借款人名']")
    first_english_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入客户姓拼音']")
    second_english_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入客户名拼音']")
    card_expire_date_loc = (By.XPATH, "//android.widget.EditText[@text='请选择证件到期日']")
    confirm_button_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    phoneno_loc = (By.XPATH, "//android.widget.EditText[@text='请输入联系电话']")

    customer_type_option_loc = (By.XPATH, "//android.widget.TextView[@text='客户类型:']")
    customer_type_value_loc = (By.XPATH, "//android.widget.TextView[@text='借款人']")
    loan_manager_option_loc = (By.XPATH, "//android.widget.TextView[@text='请输入信贷经理']")
    loan_manager_editview_loc = (By.XPATH, "//android.widget.EditText[@text='请输入信贷经理']")
    loan_manager_name_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    platform_option_loc = (By.XPATH, "//android.widget.TextView[@text='请输入经办平台']")
    platform_editview_loc = (By.XPATH, "//android.widget.EditText[@text='请输入经办平台']")
    platform_name_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    zhengxin_bank_option_loc = (By.XPATH, "//android.widget.TextView[@text='征信银行:']/..")
    zhengxin_bank_name_loc = (By.XPATH, "//android.widget.TextView[@text='征信银行:']/following-sibling::android.widget.LinearLayout/android.widget.TextView")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")
    danhao_option_loc = (By.XPATH, "//android.widget.TextView[@text='单号:']")
    zhengxin_attachment_loc = (By.XPATH, "//android.widget.TextView[@text='征信附件']")
    upload_attachment_button_loc = (By.XPATH, "//android.widget.TextView[@text='上传附件']")
    shenfenzhengfuyinjian_loc = (By.XPATH, "//android.widget.TextView[@text='客户身份证复印件']")
    shouchishouquanshu_loc = (By.XPATH, "//android.widget.TextView[@text='客户手持授权书及身份证照片']")
    zhengxinshouquanshu_loc = (By.XPATH, "//android.widget.TextView[@text='客户征信授权书']")
    disanfangshujuchaxunshouquanshu_loc = (By.XPATH, "//android.widget.TextView[@text='客户第三方数据查询授权书']")
    shouchishenfenzheng_loc = (By.XPATH, "//android.widget.TextView[@text='客户手持身份证及查询授权书']")
    kehuhukouben_loc = (By.XPATH, "//android.widget.TextView[@text='客户户口本复印件']")
    zxbgsysqsm_loc = (By.XPATH, "//android.widget.TextView[@text='征信报告使用授权声明']")
    sxsqyxs_loc = (By.XPATH, "//android.widget.TextView[@text='授信申请意向书']")
    jkryyytmywlfj_loc = (By.XPATH, "//android.widget.TextView[@text='借款人与怡亚通贸易往来附件']")
    from_photo_album_loc = (By.XPATH, "//android.widget.TextView[@text='从本地相册选择']")
    photo_name_loc = (By.ID, gl.packagename + ':id/iv_select')
    back_img_loc = (By.XPATH, "//android.widget.TextView[@text='上传征信附件']/../preceding-sibling::android.widget.RelativeLayout")
    start_flowing_button_loc = (By.XPATH, "//android.widget.TextView[@text='启动流程']")

    filter_button_loc = (By.XPATH, '//android.widget.TextView[@text="筛选"]/..')
    danju_zhuangtai_loc = (By.XPATH, '//android.widget.TextView[@text="单据状态:"]/..')
    search_button_loc = (By.XPATH, '//android.widget.Button[@text="搜索"]')
    first_row_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')
    first_row_no_loc = (By.XPATH, '//android.widget.TextView[@text="单号:"]/following-sibling::android.widget.TextView')
    zhengxin_jiben_ziliao_loc = (By.XPATH, '//android.widget.TextView[@text="征信基本资料"]/..')
    kehu_leixing_loc = (By.XPATH, '//android.widget.TextView[@text="客户类型:"]/following-sibling::android.widget.LinearLayout/android.widget.TextView')
    kehu_leixing_optin_loc = (By.XPATH, '//android.widget.TextView[@text="客户类型:"]/..')

    kehu_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="客户信息"]/..')
    kehu_xingpinyin_value_loc = (By.XPATH, '//android.widget.TextView[@text="客户姓拼音"]/../following-sibling::android.widget.LinearLayout/android.widget.TextView')
    kehu_mingpinyin_value_loc = (By.XPATH, '//android.widget.TextView[@text="客户名拼音"]/../following-sibling::android.widget.LinearLayout/android.widget.TextView')
    phone_value_loc = (By.XPATH, '//android.widget.TextView[@text="联系电话"]/../following-sibling::android.widget.LinearLayout/android.widget.TextView')
    date_value_loc = (By.XPATH, '//android.widget.TextView[@text="证件到期日"]/../following-sibling::android.widget.LinearLayout/android.widget.TextView')
    kehu_xingpinyin_loc = (By.XPATH, '//android.widget.TextView[@text="客户姓拼音:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')
    kehu_mingpinyin_loc = (By.XPATH, '//android.widget.TextView[@text="客户名拼音:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')
    phone_loc = (By.XPATH, '//android.widget.TextView[@text="联系电话:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')
    date_loc = (By.XPATH, '//android.widget.TextView[@text="证件到期日:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText')
    edit_button_loc = (By.XPATH, '//android.widget.TextView[@text="编辑"]/..')

    def click_apply_button(self):
        u"""点击申请按钮"""
        self.find_element(*self.apply_button_loc).click()

    def send_cardno(self, cardno):
        u"""输入身份证号"""
        self.send_keys(self.cardno_loc, cardno)

    def click_next_button(self):
        u"""点击下一步按钮"""
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

    def click_confirm_button(self):
        u"""点击确定按钮"""
        self.find_element(*self.confirm_button_loc).click()

    def send_phoneno(self, phoneno):
        u"""输入手机号"""
        self.send_keys(self.phoneno_loc, phoneno)

    def click_customer_type_option(self):
        u"""点击客户类型选项框"""
        self.find_element(*self.customer_type_option_loc).click()

    def click_customer_type_value(self):
        u"""点击客户类型的值"""
        self.find_element(*self.customer_type_value_loc).click()

    def click_loan_manager_option(self):
        u"""点击信贷经理选项框"""
        self.find_element(*self.loan_manager_option_loc).click()

    def send_loan_manager_editview(self, loan_manager_name):
        u"""输入信贷经理"""
        self.send_keys(self.loan_manager_editview_loc, loan_manager_name)

    def click_loan_manager_name(self):
        u"""点击信贷经理的名字"""
        self.find_element(*self.loan_manager_name_loc).click()

    def click_platform_option(self):
        u"""点击经办平台选项框"""
        self.find_element(*self.platform_option_loc).click()

    def send_platform_editview(self, platform):
        u"""输入经办平台"""
        self.send_keys(self.platform_editview_loc, platform)

    def click_platform_name(self):
        u"""点击经办平台名字"""
        self.find_element(*self.platform_name_loc).click()

    def click_zhengxin_bank_option(self):
        u"""点击征信银行选项框"""
        self.find_element(*self.zhengxin_bank_option_loc).click()

    def click_zhengxin_bank_name(self, bank_name="浦发广州分行"):
        u"""点击征信银行名字"""
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + bank_name + "']")).click()

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()

    def click_danhao_option(self):
        u"""点击单号选项框"""
        self.find_element(*self.danhao_option_loc).click()

    def click_zhengxin_attachment(self):
        u"""点击征信附件选项框"""
        self.find_element(*self.zhengxin_attachment_loc).click()

    def click_upload_attachment_button(self):
        u"""点击上传附件按钮"""
        self.find_element(*self.upload_attachment_button_loc).click()

    def click_from_photo_album(self):
        u"""点击从本地相册"""
        self.find_element(*self.from_photo_album_loc).click()

    def click_photo_name(self):
        u"""点击相片的名字"""
        self.find_element(*self.photo_name_loc).click()

    def click_back_img(self):
        u"""点击左上角返回按钮"""
        self.find_element(*self.back_img_loc).click()

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
        u"""征信报告使用授权声明"""
        self.find_element(*self.zxbgsysqsm_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_sxsqyxs(self):
        u"""授信申请意向书"""
        self.find_element(*self.sxsqyxs_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_jkryyytmywlfj(self):
        u"""借款人与怡亚通贸易往来附件"""
        self.find_element(*self.jkryyytmywlfj_loc).click()
        self.click_from_photo_album()
        self.click_photo_name()
        self.click_confirm_button()

    def click_start_flowing_button(self):
        u"""点击启动按钮"""
        self.find_element(*self.start_flowing_button_loc).click()

    def click_filter_button(self):
        u"""点击筛选按钮"""
        self.find_element(*self.filter_button_loc).click()

    def select_danju_zhuangtai(self, status):
        u"""选择单据状态"""
        self.find_element(*self.danju_zhuangtai_loc).click()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        count = None
        if status == "新建":
            count = 0
        elif status == "审核中":
            count = 1
        elif status == "流程结束":
            count = 2
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def click_search_button(self):
        u"""点击搜索按钮"""
        self.find_element(*self.search_button_loc).click()

    def click_first_row(self):
        u"""点击第一条记录"""
        self.find_element(*self.first_row_loc).click()

    def get_first_row_no(self):
        u"""获取第一条记录的单号"""
        no = self.find_element(*self.first_row_no_loc).text
        return no

    def click_zhengxin_jiben_ziliao(self):
        u"""点击征信基本资料"""
        self.find_element(*self.zhengxin_jiben_ziliao_loc).click()

    def get_kehu_leixing(self):
        u"""获取客户类型"""
        return self.find_element(*self.kehu_leixing_loc).text

    def click_kehu_leixing(self, leixing):
        u"""点击客户类型"""
        self.find_element(*self.kehu_leixing_optin_loc).click()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        count = None
        if leixing == "借款人":
            self.driver.swipe(x / 2, y * 12 / 15, x / 2, y * 13 / 15, 2000)
        elif leixing == "配偶":
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def get_zhengxin_bank_name(self):
        u"""获取征信银行名称"""
        return self.find_element(*self.zhengxin_bank_name_loc).text

    def click_kehu_xinxi(self):
        u"""点击客户信息"""
        self.find_element(*self.kehu_xinxi_loc).click()

    def get_first_english_name(self):
        u"""获取客户姓拼音"""
        return self.find_element(*self.kehu_xingpinyin_value_loc).text

    def get_last_english_name(self):
        u"""获取客户名拼音"""
        return self.find_element(*self.kehu_mingpinyin_value_loc).text

    def get_phone(self):
        u"""获取联系电话"""
        return self.find_element(*self.phone_value_loc).text

    def get_date(self):
        u"""获取证件到期日"""
        return self.find_element(*self.date_value_loc).text

    def click_edit_button(self):
        u"""点击编辑按钮"""
        self.find_element(*self.edit_button_loc).click()

    def input_first_english_name(self, first_english_name):
        u"""输入姓拼音"""
        self.send_keys(self.kehu_xingpinyin_loc, first_english_name)

    def input_last_english_name(self, last_english_name):
        u"""输入名拼音"""
        self.send_keys(self.kehu_mingpinyin_loc, last_english_name)

    def input_phone(self, phone):
        u"""输入联系电话"""
        self.send_keys(self.phone_loc, phone)

    def click_zhengjian_daoqiri(self):
        u"""点击证件到期日"""
        self.find_element(*self.date_loc).click()
