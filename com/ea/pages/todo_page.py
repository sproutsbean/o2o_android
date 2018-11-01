#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: todo_page.py 
@time: 2017/12/08 
"""

from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
import time
from selenium.common.exceptions import NoSuchElementException


class TodoPage(BasePage):
    u"""代办查询主页面"""
    yewuNo_loc = (By.CSS_SELECTOR, "input[name='referCode']")
    queryAll_loc = (By.CSS_SELECTOR, "input[name='queryAll']")
    serchButton_loc = (By.CSS_SELECTOR, "input[value='搜索']")

    def is_have_rows(self, types):
        u"""判断待办页面是否有记录"""
        firstrow_loc = (By.XPATH, "//td[contains(text(),'" + types + "')]/preceding-sibling::td[3]/a")
        if len(self.find_elements(*firstrow_loc)) == 0:
            return False
        else:
            return True
        # try:
        #     self.find_element(*firstrow_loc)
        #     return True
        # except NoSuchElementException:
        #     return False

    def click_first_row(self, types):
        u"""点击代办页面类型为types的第一条记录"""
        firstrow_loc = (By.XPATH, "//td[contains(text(),'" + types + "')]/preceding-sibling::td[3]/a")
        self.find_element(*firstrow_loc).click()

    def input_yewuno(self, yewuno):
        u"""输入业务号码"""
        self.send_keys(self.yewuNo_loc, yewuno)

    def click_query_all(self):
        u"""勾选查询所有复选框"""
        if len(self.find_elements(*self.queryAll_loc)):
            self.find_element(*self.queryAll_loc).click()
        else:
            pass

    def click_search_button(self):
        u"""点击查询按钮"""
        self.find_element(*self.serchButton_loc).click()


class ApproveZhengxinPage(BasePage):
    u"""审批征信"""
    pageDown_loc = (By.XPATH, "//th[text()='开始时间']")
    approveView_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    approveButton_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirmButton_loc = (By.XPATH, "//button[text()='确认']")
    upLoadFile_loc = (By.CSS_SELECTOR, "input[name='file']")
    cardate_loc = (By.NAME, "zxDate")
    frame_loc = (By.TAG_NAME, "iframe")
    date_loc = (By.XPATH, "//td[text()='15']")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")

    def get_result(self, zhengxingdanhao):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + zhengxingdanhao + "']/../following-sibling::td[7]")
        return self.find_element(*result_loc).text

    def page_down(self):
        u"""拖动页面"""
        self.script(*self.pageDown_loc)

    def input_approve_view(self, approveview):
        u"""输入审批意见"""
        self.send_keys(self.approveView_loc, approveview)

    def click_approve_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.approveButton_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirmButton_loc).click()
        time.sleep(1)

    def upload_file(self, filepath):
        u"""上传附件"""
        self.find_element(*self.upLoadFile_loc).send_keys(filepath)

    def input_cardno_date(self, date):
        u"""点击证件到期日志"""
        self.input_date_time(self.cardate_loc, date)

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(1)


class ApproveLoanPage(BasePage):
    u"""贷款审批"""
    edit_loc = (By.XPATH, "//a[text()='编辑']")
    zx_zfzye_loc = (By.ID, 'debetTotalBesideHouseCar')
    near_24month_yuqi_cishu_loc = (By.ID, 'twentyFourOverdueCount')
    near_24month_wai_yuqi_cishu_loc = (By.ID, 'outTwentyFourOverdueCount')
    danbao_yue_loc = (By.ID, 'assureBalance')
    near_24month_xinyongka_yuqi_loc = (By.ID, 'twentyFourOverdueCreditCount')
    bank_overdue_loc = (By.NAME, "bankBalanceOverdue")
    credit_overdue_loc = (By.NAME, "creditLimitOverdue")
    nobank_overdue_loc = (By.NAME, "nonbankBalanceOverdue")
    p_zx_zfzye_loc = (By.ID, 'debetTotalBesideHouseCar1')
    p_near_24month_yuqi_cishu_loc = (By.ID, 'twentyFourOverdueCount1')
    p_near_24month_wai_yuqi_cishu_loc = (By.ID, 'outTwentyFourOverdueCount1')
    p_danbao_yue_loc = (By.ID, 'assureBalance1')
    p_near_24month_xinyongka_yuqi_loc = (By.ID, 'twentyFourOverdueCreditCount1')
    p_bank_overdue_loc = (By.NAME, "bankBalanceOverdue1")
    p_credit_overdue_loc = (By.NAME, "creditLimitOverdue1")
    p_nobank_overdue_loc = (By.NAME, "nonbankBalanceOverdue1")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")
    loan_no_loc = (By.ID, "billCode")
    search_button_loc = (By.CSS_SELECTOR, "input[value='搜索']")
    result_loc = ""

    def have_partner(self):
        return self.find_elements(*self.p_zx_zfzye_loc)

    def get_result(self, loanno):
        u"""获取结果状态"""
        self.result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[8]")
        return self.find_element(*self.result_loc).text

    def scrollto_edit(self):
        u"""滚动页面到编辑按钮位置"""
        self.script(*self.edit_loc)
        time.sleep(1)

    def click_edit(self):
        u"""点击编辑按钮"""
        self.find_element(*self.edit_loc).click()

    def input_zx_zfzye(self, number):
        self.send_keys(self.zx_zfzye_loc, number)

    def input_near_24month_yuqi_cishu(self, number):
        self.send_keys(self.near_24month_yuqi_cishu_loc, number)

    def input_near_24month_wai_yuqi_cishu(self, cishu):
        self.send_keys(self.near_24month_wai_yuqi_cishu_loc, cishu)

    def input_danbao_yue(self, number):
        self.send_keys(self.danbao_yue_loc, number)

    def input_near_24month_xinyongka_yuqi(self, number):
        self.send_keys(self.near_24month_xinyongka_yuqi_loc, number)

    def input_bank_overdue(self, number):
        u"""输入银行机构贷款:目前逾期_万元"""
        self.send_keys(self.bank_overdue_loc, number)

    def input_credit_overdue(self, number):
        u"""输入信用卡(贷记卡及准贷记卡):目前逾期_万元"""
        self.send_keys(self.credit_overdue_loc, number)

    def input_nobank_overdue(self, number):
        u"""输入非银行机构贷款:目前逾期_万元"""
        self.send_keys(self.nobank_overdue_loc, number)

    def input_p_zx_zfzye(self, number):
        self.send_keys(self.p_zx_zfzye_loc, number)

    def input_p_near_24month_yuqi_cishu(self, number):
        self.send_keys(self.p_near_24month_yuqi_cishu_loc, number)

    def input_p_near_24month_wai_yuqi_cishu(self, cishu):
        self.send_keys(self.p_near_24month_wai_yuqi_cishu_loc, cishu)

    def input_p_danbao_yue(self, number):
        self.send_keys(self.p_danbao_yue_loc, number)

    def input_p_near_24month_xinyongka_yuqi(self, number):
        self.send_keys(self.p_near_24month_xinyongka_yuqi_loc, number)

    def input_p_bank_overdue(self, number):
        u"""输入银行机构贷款:目前逾期_万元"""
        self.send_keys(self.p_bank_overdue_loc, number)

    def input_p_credit_overdue(self, number):
        u"""输入信用卡(贷记卡及准贷记卡):目前逾期_万元"""
        self.send_keys(self.p_credit_overdue_loc, number)

    def input_p_nobank_overdue(self, number):
        u"""输入非银行机构贷款:目前逾期_万元"""
        self.send_keys(self.p_nobank_overdue_loc, number)

    def scrollto_save_button(self):
        u"""拖动页面到保存按钮位置"""
        self.script(*self.save_button_loc)
        time.sleep(1)

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(1)

    def scrollto_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.script(*self.approve_view_loc)
        time.sleep(1)

    def input_approve_view(self, view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, view)

    def click_tongguo(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()

    def click_confirm(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()
        time.sleep(1)

    def input_loan_no(self, loan_no):
        u"""输入贷款单号"""
        self.send_keys(self.loan_no_loc, loan_no)

    def click_search_button(self):
        u"""点击搜索按钮"""
        self.find_element(*self.search_button_loc).click()


class ApproveCaiwuPage(BasePage):
    u"""财务审批"""
    scroll_loc = (By.ID, "zxRemark")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    confirm_button_loc = (By.XPATH, "//button[text()='确认']")
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    result_loc = ""

    def get_result(self, loanno):
        u"""获取结果状态"""
        self.result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[8]")
        return self.find_element(*self.result_loc).text

    def get_result_by_role(self, loanno):
        u"""获取结果状态"""
        self.result_loc = (By.XPATH, "//td[text()='" + loanno + "']/following-sibling::td[3]")
        return self.find_element(*self.result_loc).text

    def scroll_to_special_condition(self):
        u"""拖动页面到特殊情况说明位置"""
        self.script(*self.scroll_loc)
        time.sleep(1)

    def input_special_condition(self, condition):
        u"""输入特殊情况说明"""
        self.send_keys(self.scroll_loc, condition)

    def click_save_button(self):
        u"""点击特殊情况说明的保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(1)

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_button_loc).click()
        time.sleep(1)

    def input_approve_view(self, view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()


class ApproveInsidePage(BasePage):
    u"""审批内部审批流程"""
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[9]")
        return self.find_element(*result_loc).text

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.script(*self.approve_view_loc)
        time.sleep(1)

    def input_approve_view(self, view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()
        time.sleep(1)


class ApproveCharge(BasePage):
    u"""审批收费流程"""
    payer_loc = (By.NAME, "payName")
    pay_time_loc = (By.ID, "submitDate")
    iframe_loc = (By.TAG_NAME, "iframe")
    datetime_loc = (By.XPATH, "//td[text()='15']")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    put_print_voucher_loc = (By.CSS_SELECTOR, "input[name='file']")
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_button_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_button_loc = (By.XPATH, "//button[text()='确认']")
    daokuan_total_loc = (By.ID, "reDaokuanTotal")
    pay_date_loc = (By.ID, "payDate")
    collect_acount_loc = (By.ID, "skBankAccountBZJ")

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[8]")
        return self.find_element(*result_loc).text

    def scroll_to_payer(self):
        u"""拖动页面到付款人位置"""
        self.script(*self.payer_loc)
        time.sleep(1)

    def input_payer(self, payer):
        u"""输入付款人"""
        self.send_keys(self.payer_loc, payer)

    def input_pay_time(self, date):
        u"""点击付款时间"""
        self.input_date_time(self.pay_time_loc, date)

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(1)

    def input_print_voucher(self, pic_path):
        u"""上传打印凭证"""
        self.find_element(*self.put_print_voucher_loc).send_keys(pic_path)

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.script(*self.approve_view_loc)
        time.sleep(1)

    def input_approve_view(self, view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_button_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_button_loc).click()
        time.sleep(1)

    def scroll_to_daokuan_total(self):
        u"""拖动页面到本次到款合计金额位置"""
        self.script(*self.daokuan_total_loc)
        time.sleep(1)

    def input_daokuan_total(self, daokuan_total):
        u"""输入本次到款合计金额"""
        self.send_keys(self.daokuan_total_loc, daokuan_total)

    def input_pay_date(self, date):
        u"""点击付款日期"""
        self.input_date_time(self.pay_date_loc, date)

    def select_collect_acount(self, acount):
        u"""拖动页面到实际收款账户"""
        self.select_widget(acount, *self.collect_acount_loc)


class ApproveInterview(BasePage):
    u"""面签审批"""
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")
    isPhoneCheck_loc = (By.NAME, "isPhoneCheck")
    phoneCheckMessage_loc = (By.NAME, "phoneCheckMessage")
    phone_save_button_loc = (By.CSS_SELECTOR, "form[action$='save_bankLoanData_phone'] input[value='保存']")
    fujian_save_button_loc = (By.CSS_SELECTOR, "form[action$='save_bankLoanData'] input[value='保存']")
    isFujianOver_loc = (By.NAME, "isCheckMqCl")
    card_daoqi_date_loc = (By.NAME, "paymentTime")
    save_bank_loan_data_loc = (By.CSS_SELECTOR, "input[value='保存银行放款数据']")
    input_file_loc = (By.CSS_SELECTOR, "input[name='file']")
    frame_loc = (By.TAG_NAME, "iframe")
    date_loc = (By.XPATH, "//td[text()='15']")
    koufei_loc = (By.XPATH, "//a[text()='扣费']")

    def click_koufei_button(self):
        u"""点击扣费按钮"""
        self.find_element(*self.koufei_loc).click()
        time.sleep(2)

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[7]")
        return self.find_element(*result_loc).text

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.script(*self.approve_view_loc)
        time.sleep(1)

    def input_approve_view(self, approve_view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, approve_view)

    def click_tongguo(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()

    def click_confirm(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()
        time.sleep(1)

    def scroll_to_is_phone_check(self):
        u"""拖动页面到是否电核位置"""
        self.script(*self.isPhoneCheck_loc)
        time.sleep(1)

    def select_is_phone_check(self, isphonecheck):
        u"""选择是否电核"""
        self.select_widget(isphonecheck, *self.isPhoneCheck_loc)

    def input_phone_check_message(self, phonecheckmessage):
        u"""输入电核意见"""
        self.send_keys(self.phoneCheckMessage_loc, phonecheckmessage)

    def click_phone_save_button(self):
        u"""点击电核意见的保存按钮"""
        self.find_element(*self.phone_save_button_loc).click()
        time.sleep(1)

    def select_is_fujian_over(self, isfujianover):
        u"""选择确认附件是否上传齐全"""
        self.select_widget(isfujianover, *self.isFujianOver_loc)

    def click_fujian_save_button(self):
        u"""点击确认附件是否上传齐全的保存按钮"""
        self.find_element(*self.fujian_save_button_loc).click()
        time.sleep(1)

    def scroll_to_card_date(self):
        u"""拖动页面到实际放款日位置"""
        self.script(*self.card_daoqi_date_loc)
        time.sleep(1)

    def input_card_daoqi_date(self, date):
        u"""点击实际放款日"""
        self.input_date_time(self.card_daoqi_date_loc, date)

    def click_save_bank_loan_data(self):
        u"""点击保存银行放款数据按钮"""
        self.find_element(*self.save_bank_loan_data_loc).click()
        time.sleep(1)

    def input_file(self, file_path):
        u"""导入还款计划"""
        self.find_element(*self.input_file_loc).send_keys(file_path)


class LoanClearApprove(BasePage):
    u"""审批贷款结清流程"""
    clear_date_loc = (By.NAME, "settleDate")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[7]")
        return self.find_element(*result_loc).text

    def scroll_to_clear_date(self):
        u"""拖动页面到结清日期位置"""
        self.script(*self.clear_date_loc)

    def input_clear_date(self, date):
        u"""输入结清日期"""
        self.input_date_time(self.clear_date_loc, date, click=False)

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()

    def input_approve_view(self, approve_view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, approve_view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()


class BrandApprove(BasePage):
    u"""审批贷款结清流程"""
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")

    def get_result(self, brand_no):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//td[text()='" + brand_no + "']/following-sibling::td[4]/div")
        return self.find_element(*result_loc).text

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.scroll_to_element(*self.approve_view_loc)

    def input_approve_view(self, approve_view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, approve_view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()


class FactoryApprove(BasePage):
    u"""审批添加厂家合作方流程"""
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


class DealerApprove(BasePage):
    u"""审批添加厂家合作方流程"""
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")

    def get_result(self, yewu_no):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + yewu_no + "']/../following-sibling::td[8]/div")
        return self.find_element(*result_loc).text

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.scroll_to_element(*self.approve_view_loc)

    def input_approve_view(self, approve_view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, approve_view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()


class PayMoneyApprove(BasePage):
    u"""审批打款流程"""
    collect_date_loc = (By.ID, "collectDate")
    collect_no_loc = (By.NAME, "collectNo")
    shifoudaozhang_loc = (By.NAME, "noYes")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")

    def get_result(self, yewuno):
        u"""获取结果"""
        result_loc = (By.XPATH, "//a[text()='" + yewuno + "']/../following-sibling::td[7]")
        return self.find_element(*result_loc).text

    def input_collect_date(self, collect_date):
        u"""输入到账日期"""
        self.input_date_time(self.collect_date_loc, collect_date)

    def select_collect_no(self):
        u"""选择收款账户"""
        self.select_widget(1, *self.collect_no_loc)

    def select_shifoudaozhang(self, shifoudaozhang="是"):
        u"""选择是否到账"""
        self.select_widget(shifoudaozhang, *self.shifoudaozhang_loc)

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(1)

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.scroll_to_element(*self.approve_view_loc)
        time.sleep(2)

    def input_approve_view(self, approve_view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, approve_view)

    def click_tongguo_button(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_loc).click()
        time.sleep(5)
