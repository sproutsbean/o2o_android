#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:user
@file: brand_page.py
@time: 2018/01/17
"""
from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
from com.ea.resource import globalparameter as gl
import time


class MyCustomerPage(BasePage):
    my_customer_loc = (By.XPATH, '//android.widget.TextView[@text="我的客户"]/..')
    search_name_loc = (By.XPATH, '//android.widget.EditText[@text="搜索"]')
    put_photo_loc = (By.XPATH, '//android.widget.TextView[@text="拍照上传"]/..')
    shidi_photo_loc = (By.XPATH, '//android.widget.TextView[@text="实地调查照片"]/..')
    quanjing_loc = (By.XPATH, '//android.widget.TextView[@text="全景（0）"]/../..')
    from_local_select_loc = (By.XPATH, '//android.widget.Button[@text="从相册选择"]')
    from_paizhao_loc = (By.XPATH, '//android.widget.Button[@text="拍照"]')
    kuaimen_loc = (By.XPATH, '//GLButton[@text="快门"]')
    confirm_loc = (By.ID, 'com.sec.android.app.camera:id/okay')
    tupian_loc = (By.XPATH, '//android.widget.TextView[@text="图片"]/..')
    photo_name_loc = (By.XPATH, '//com.sec.samsung.gallery.glview.composeView.PositionControllerBase$ThumbObject')
    result_loc = (By.XPATH, '//android.widget.TextView[@text="实地调查照片"]')

    add_loc = (By.XPATH, '//android.widget.TextView[@text="新增"]/..')
    next_button_loc = (By.XPATH, '//android.widget.TextView[@text="下一步"]/..')
    first_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入姓"]')
    second_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入名"]')
    first_english_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入客户姓拼音"]')
    second_english_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入客户名拼音"]')
    cardno_loc = (By.XPATH, '//android.widget.EditText[@text="请输入证件号码"]')
    card_expire_date_loc = (By.XPATH, "//android.widget.EditText[@text='请选择证件到期日']")
    card_organization_loc = (By.XPATH, '//android.widget.EditText[@text="请输入发证机关"]')
    phoneno_loc = (By.XPATH, '//android.widget.EditText[@text="请输入手机号码"]')
    confirm_button_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    save_button_loc = (By.XPATH, '//android.widget.TextView[@text="保存"]/..')

    archives_loc = (By.XPATH, '//android.widget.RadioButton[@text="档案"]')
    apply_personal_zhengxin_loc = (By.XPATH, '//android.widget.TextView[@text="申请个人征信"]/../..')
    customer_type_loc = (By.XPATH, '//android.widget.TextView[@text="客户类型:"]/..')
    customer_type_value_loc = (By.XPATH, '//android.widget.TextView[@text="借款人"]/../..')
    bank_loc = (By.XPATH, '//android.widget.TextView[@text="征信银行:"]/..')
    zhengxin_attachment_loc = (By.XPATH, '//android.widget.TextView[@text="征信附件"]/..')
    upload_attachment_button_loc = (By.XPATH, '//android.widget.TextView[@text="上传附件"]/..')
    shenfenzhengfuyinjian_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'身份证复印件')]")
    shouchishouquanshu_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'手持授权书及身份证照片')]")
    zhengxinshouquanshu_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'征信授权书')]")
    disanfangshujuchaxunshouquanshu_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'第三方数据查询授权书')]")
    shouchishenfenzheng_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'手持身份证及查询授权书')]")
    kehuhukouben_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'客户户口本复印件')]")
    zxbgsysqsm_loc = (By.XPATH, "//android.widget.TextView[contains(@text,'征信报告使用授权声明')]")
    sxsqysx_loc = (By.XPATH, '//android.widget.TextView[contains(@text,"授信申请意向书")]')
    jkryyytmywlfj_loc = (By.XPATH, '//android.widget.TextView[contains(@text,"借款人与怡亚通贸易往来附件")]')
    from_photo_album_loc = (By.XPATH, "//android.widget.TextView[@text='从本地相册选择']")
    local_photo_name_loc = (By.ID, gl.packagename + ':id/iv_select')
    back_img_loc = (By.XPATH, '//android.widget.TextView[@text="上传征信附件"]/../preceding-sibling::android.widget.RelativeLayout')
    start_flowing_button_loc = (By.XPATH, '//android.widget.TextView[@text="启动流程"]/..')
    first_row_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')
    follow_up_record_loc = (By.XPATH, '//android.widget.RadioButton[@text="跟进记录"]')
    add_record_loc = (By.XPATH, '//android.widget.TextView[@text="跟进记录"]/..')
    follow_up_type_loc = (By.XPATH, '//android.widget.TextView[@text="请选择"]/../../..')
    follow_up_type_value_loc = (By.XPATH, '//android.widget.TextView[@text="微信拜访"]/../..')
    record_loc = (By.XPATH, '//android.widget.EditText[@text="请输入跟进记录"]')

    loan_apply_loc = (By.XPATH, '//android.widget.TextView[@text="申请贷款"]/../..')
    loan_type_loc = (By.XPATH, '//android.widget.TextView[@text="贷款类型:"]/..')
    marry_status_loc = (By.XPATH, '//android.widget.TextView[@text="婚姻状况:"]/..')
    pfirst_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶姓"]')
    psecond_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶名"]')
    pfirst_english_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶姓拼音"]')
    plast_english_name_loc = (By.XPATH, '//android.widget.EditText[@text="请输入借款人配偶名拼音"]')
    pcard_no_loc = (By.XPATH, '//android.widget.EditText[@text="请输入证件号码"]')
    pphone_no_loc = (By.XPATH, '//android.widget.EditText[@text="请输入联系电话"]')
    loan_amount_loc = (By.XPATH, '//android.widget.EditText[@text="请输入申请金额"]')
    operate_mode_loc = (By.XPATH, '//android.widget.TextView[@text="经营模式:"]/..')
    channel_name_option_loc = (By.XPATH, '//android.widget.TextView[@text="请输入渠道名称"]')
    channel_name_edit_loc = (By.XPATH, '//android.widget.EditText[@text="请输入渠道名称"]')
    channel_name_value_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')
    sd_customer_name_option_loc = (By.XPATH, "//android.widget.TextView[@text='请输入SD客户名称,至少输入4个字才能搜索']")
    sd_customer_name_editview_loc = (By.XPATH, "//android.widget.EditText[@text='请输入SD客户名称,至少输入4个字才能搜索']")
    sd_customer_name_value_loc = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
    zhengxin_report_option_loc = (By.XPATH, "//android.widget.TextView[@text='夫妻双方征信报告信息']")
    zhengxin_apply_loc = (By.XPATH, '//android.widget.TextView[@text="申请征信"]')
    zhengxin_bank_option_loc = (By.XPATH, "//android.widget.TextView[@text='征信银行:']")
    radio_button_loc = (By.XPATH, "//android.widget.RadioButton[@index='0']")
    guanlian_loc = (By.XPATH, '//android.widget.TextView[@text="关联"]')

    def click_loan_apply(self):
        self.find_element(*self.loan_apply_loc).click()

    def select_marry_status(self, status="未婚"):
        self.find_element(*self.marry_status_loc).click()
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

    def select_loan_type(self, loan_type):
        self.find_element(*self.loan_type_loc).click()
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

    def input_pfirst_name(self, pfirst_name):
        self.send_keys(self.pfirst_name_loc, pfirst_name)

    def input_psecond_name(self, psecond_name):
        self.send_keys(self.psecond_name_loc, psecond_name)

    def input_pfirst_english_name(self, pfirst_english_name):
        self.send_keys(self.pfirst_english_name_loc, pfirst_english_name)

    def input_plast_english_name(self, plast_english_name):
        self.send_keys(self.plast_english_name_loc, plast_english_name)

    def input_pcard_no(self, pcard_no):
        self.send_keys(self.pcard_no_loc, pcard_no)

    def input_pphone_no(self, pphone_no):
        self.send_keys(self.pphone_no_loc, pphone_no)

    def input_loan_amount(self, loan_amount):
        self.send_keys(self.loan_amount_loc, loan_amount)

    def select_operate_mode(self, operate_mode):
        self.find_element(*self.operate_mode_loc).click()
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

    def input_channel_name(self, channel_name):
        self.find_element(*self.channel_name_option_loc).click()
        self.send_keys(self.channel_name_edit_loc, channel_name)
        self.find_element(*self.channel_name_value_loc).click()

    def input_sd_customer_name(self, sd_customer_name):
        self.find_element(*self.sd_customer_name_option_loc).click()
        self.send_keys(self.sd_customer_name_editview_loc, sd_customer_name)
        self.find_element(*self.sd_customer_name_value_loc).click()

    def click_loan_no(self, loan_no):
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + loan_no + "']/preceding-sibling::android.widget.TextView")).click()

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

    def click_radio_button(self):
        self.find_element(*self.radio_button_loc).click()

    def get_zx_status(self, zx_no):
        return self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + zx_no + '"]/../../following-sibling::android.widget.LinearLayout[5]//android.widget.TextView[@text="单据状态"]/following-sibling::android.widget.TextView')).text

    def get_follow_up_record_result(self, record):
        return self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + record + '"]')).text

    def click_zx_no(self, zx_no):
        self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + zx_no + '"]/../../../../..')).click()

    def click_customer_name(self, customer_name):
        self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + customer_name + '"]')).click()

    def get_result(self):
        return self.find_element(*self.result_loc).text

    def click_my_customer(self):
        self.find_element(*self.my_customer_loc).click()

    def input_search_name(self, search_name):
        self.send_keys(self.search_name_loc, search_name, clear=False, click=False)

    def click_put_photo(self):
        self.find_element(*self.put_photo_loc).click()

    def click_shidi_photo(self):
        self.find_element(*self.shidi_photo_loc).click()

    def click_quanjing(self):
        self.find_element(*self.quanjing_loc).click()

    def click_from_local_select(self):
        self.find_element(*self.from_local_select_loc).click()

    def click_tupian(self):
        self.find_element(*self.tupian_loc).click()

    def click_photo_name(self):
        self.find_element(*self.photo_name_loc).click()

    def click_paizhao(self):
        self.find_element(*self.from_paizhao_loc).click()

    def click_kuaimen(self):
        self.find_element(*self.kuaimen_loc).click()

    def click_confirm(self):
        self.find_element(*self.confirm_loc).click()

    def click_add_button(self):
        self.find_element(*self.add_loc).click()

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

    def input_cardno(self, cardno):
        u"""输入证件号码"""
        self.send_keys(self.cardno_loc, cardno)

    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()

    def click_card_expire_date(self):
        u"""点选证件到期日期"""
        self.find_element(*self.card_expire_date_loc).click()
        self.click_confirm_button()

    def input_card_organization(self, organization="公安局"):
        u"""输入发证机构"""
        self.send_keys(self.card_organization_loc, organization)

    def send_phoneno(self, phoneno):
        u"""输入手机号"""
        self.send_keys(self.phoneno_loc, phoneno)

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def click_archives(self):
        self.find_element(*self.archives_loc).click()

    def click_apply_personal_zhengxin(self):
        self.find_element(*self.apply_personal_zhengxin_loc).click()

    def select_customer_type(self, type_value="借款人"):
        self.find_element(*self.customer_type_loc).click()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if type_value == "借款人":
            count = 0
        elif type_value == "配偶":
            count = 1
        elif type_value == "担保人":
            count = 2
        for i in range(count):
            self.driver.swipe(x / 2, y * 13 / 15, x / 2, y * 12 / 15, 2000)
        self.click_confirm_button()

    def select_bank(self, bank_name):
        self.find_element(*self.bank_loc).click()
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

    def click_zhengxin_attachment(self):
        self.find_element(*self.zhengxin_attachment_loc).click()

    def click_upload_attachment_button(self):
        self.find_element(*self.upload_attachment_button_loc).click()

    def click_from_photo_album(self):
        u"""点击从本地相册"""
        self.find_element(*self.from_photo_album_loc).click()

    def click_local_photo_name(self):
        self.find_element(*self.local_photo_name_loc).click()

    def click_shenfenzhengfuyinjian(self):
        u"""点击身份证复印件"""
        self.find_element(*self.shenfenzhengfuyinjian_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_shouchishouquanshu(self):
        u"""点击手持授权书"""
        self.find_element(*self.shouchishouquanshu_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_zhengxinshouquanshu(self):
        u"""点击征信授权书"""
        self.find_element(*self.zhengxinshouquanshu_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_disanfangshujuchaxunshouquanshu(self):
        u"""点击第三方数据查询授权书"""
        self.find_element(*self.disanfangshujuchaxunshouquanshu_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_shouchishenfenzheng(self):
        u"""点击手持身份证"""
        self.find_element(*self.shouchishenfenzheng_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_kehuhukouben(self):
        u"""点击客户户口本复印件"""
        self.find_element(*self.kehuhukouben_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_zxbgsysqsm(self):
        u"""点击征信报告使用授权声明"""
        self.find_element(*self.zxbgsysqsm_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_sxsqyxs(self):
        u"""点击授信申请意向书"""
        self.find_element(*self.sxsqysx_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_jkryyytmywlfj(self):
        u"""点击借款人与怡亚通贸易往来附件"""
        self.find_element(*self.jkryyytmywlfj_loc).click()
        self.click_from_photo_album()
        self.click_local_photo_name()
        self.click_confirm_button()

    def click_back_img(self):
        self.find_element(*self.back_img_loc).click()

    def click_start_flowing_button(self):
        self.find_element(*self.start_flowing_button_loc).click()

    def click_first_customer(self):
        self.find_element(*self.first_row_loc).click()

    def click_follow_up_record(self):
        self.find_element(*self.follow_up_record_loc).click()

    def click_add_record(self):
        self.find_element(*self.add_record_loc).click()

    def select_follow_up_type(self):
        self.find_element(*self.follow_up_type_loc).click()
        self.find_element(*self.follow_up_type_value_loc).click()

    def input_record(self, record):
        self.send_keys(self.record_loc, record)

    def click_guanlian_button(self):
        self.find_element(*self.guanlian_loc).click()

    def get_zx_status_by_name(self, name):
        return self.find_element(*(By.XPATH,
                                   '//android.widget.TextView[@text="' + name + '"]/../../../following-sibling::android.widget.LinearLayout[6]//android.widget.TextView[@text="征信状态"]/following-sibling::android.widget.LinearLayout/android.widget.TextView')).text
