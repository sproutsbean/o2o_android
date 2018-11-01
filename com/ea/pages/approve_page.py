#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: approve_page.py 
@time: 2018/03/08 
"""

from com.ea.common.base_page import BasePage
from com.ea.common.selenium_base_page import SeleniumBasePage
from appium.webdriver.webdriver import By
import time
from com.ea.resource import globalparameter as gl


class ApprovePubPage(BasePage):
    filter_loc = (By.XPATH, "//android.widget.TextView[@text='筛选']")
    yewu_no_loc = (By.XPATH, "//android.widget.TextView[@text='业务单号:']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    search_all_loc = (By.XPATH, "//android.widget.TextView[@text='查看全部:']")
    yes_loc = (By.XPATH, "//android.widget.TextView[@text='是']")
    search_button_loc = (By.XPATH, "//android.widget.Button[@text='搜索']")
    danhao_loc = (By.XPATH, "//android.widget.TextView[@text='单号:']")
    my_approve_loc = (By.XPATH, "//android.widget.TextView[@text='我的审核']")
    no_data_loc = (By.XPATH, '//android.widget.TextView[@text="未查到相应信息"]')

    def click_filter_button(self):
        self.find_element(*self.filter_loc).click()

    def send_yewu_no(self, yewu_no):
        self.send_keys(self.yewu_no_loc, yewu_no)

    def click_search_all(self):
        self.find_element(*self.search_all_loc).click()

    def click_yes(self):
        self.find_element(*self.yes_loc).click()

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def click_first_row(self):
        self.find_element(*self.danhao_loc).click()

    def have_danhao(self):
        if not self.find_elements(*self.no_data_loc):
            return True
        else:
            return False

    def click_my_approve(self):
        self.find_element(*self.my_approve_loc).click()

    def click_todo_first_row(self, yewu_no):
        self.click_filter_button()
        self.send_yewu_no(yewu_no)
        # self.click_search_all()
        # self.click_yes()
        self.click_search_button()


class ZhengxinApprovePage(BasePage):
    approve_view_loc = (By.XPATH, "//android.widget.EditText[@text='请填写审核意见(不超过2000字)']")
    pass_button_loc = (By.XPATH, "//android.widget.TextView[@text='通过']")
    confirm_text_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    upload_zhengxin_report_loc = (By.XPATH, "//android.widget.TextView[@text='上传征信报告']")
    customer_zhengxin_report_loc = (By.XPATH, "//android.widget.TextView[@text='客户征信报告']")
    customer_zhengxin_report_img_loc = (By.XPATH, "//android.widget.TextView[@text='客户征信报告']")
    from_local_photos_loc = (By.XPATH, "//android.widget.TextView[@text='从本地相册选择']")
    photo_name_loc = (By.ID, gl.packagename + ":id/iv_select")
    back_img_loc = (By.XPATH, "//android.widget.TextView[@text='上传征信报告']/../preceding-sibling::android.widget.RelativeLayout")
    customer_zhengxin_report_date_loc = (By.XPATH, "//android.widget.TextView[@text='客户征信报告日期']")
    customer_zhengxin_report_date_select_loc = (By.XPATH, "//android.widget.TextView[@text='客户征信报告日期:']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")

    def input_approve_view(self, approve_view):
        self.send_keys(self.approve_view_loc, approve_view)

    def click_pass_button(self):
        self.find_element(*self.pass_button_loc).click()

    def click_confirm(self):
        self.find_element(*self.confirm_text_loc).click()

    def click_upload_zhengxin_report(self):
        self.find_element(*self.upload_zhengxin_report_loc).click()
        self.click_customer_zhengxin_report()
        self.click_customer_zhengxin_report_img()
        self.click_from_local_photos()
        self.click_photo_name()
        self.click_confirm()

    def click_customer_zhengxin_report(self):
        self.find_element(*self.customer_zhengxin_report_loc).click()

    def click_customer_zhengxin_report_img(self):
        self.find_element(*self.customer_zhengxin_report_img_loc).click()

    def click_from_local_photos(self):
        self.find_element(*self.from_local_photos_loc).click()

    def click_photo_name(self):
        self.find_element(*self.photo_name_loc).click()

    def click_back_img(self):
        self.find_element(*self.back_img_loc).click()

    def click_customer_zhengxin_report_date(self):
        self.find_element(*self.customer_zhengxin_report_date_loc).click()
        self.click_customer_zhengxin_report_date_select()
        self.click_confirm()
        time.sleep(1)
        self.click_save_button()

    def click_customer_zhengxin_report_date_select(self):
        self.find_element(*self.customer_zhengxin_report_date_select_loc).click()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()


class LoanApprovePage(BasePage):
    fuzhaiqingkuang_loc = (By.XPATH, "//android.widget.TextView[@text='夫妻双方征信负债情况']")
    total_fuzhai_loc = (By.XPATH, "//android.widget.TextView[@text='征信总负债(总额)(万元):']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    bank_overdue_loc = (By.XPATH, "//android.widget.TextView[@text='银行机构贷款目前逾期(万元):']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")
    approve_view_loc = (By.XPATH, "//android.widget.EditText[@text='请填写审核意见(不超过2000字)']")
    pass_button_loc = (By.XPATH, "//android.widget.TextView[@text='通过']")
    confirm_button_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")

    def click_fuzhaiqingkuang(self):
        self.find_element(*self.fuzhaiqingkuang_loc).click()

    def input_total_fuzhai(self, total_fuzhai):
        self.send_keys(self.total_fuzhai_loc, total_fuzhai)

    def input_bank_overdue(self, bank_overdue):
        self.send_keys(self.bank_overdue_loc, bank_overdue)

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def input_approve_view(self, approve_view):
        self.send_keys(self.approve_view_loc, approve_view)

    def click_pass_button(self):
        self.find_element(*self.pass_button_loc).click()

    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()


class InsideApprovePage(BasePage):
    approve_view_loc = (By.XPATH, "//android.widget.EditText[@text='请填写审核意见(不超过2000字)']")
    pass_button_loc = (By.XPATH, "//android.widget.TextView[@text='通过']")
    confirm_button_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    my_approve_view_loc = (By.XPATH, '//android.widget.TextView[@text="我的审核意见"]/..')
    save_button_loc = (By.XPATH, '//android.widget.TextView[@text="保存"]/..')
    approve_report_loc = (By.XPATH, '//android.widget.TextView[@text="审批报告"]/..')

    def click_my_approve_view(self):
        self.find_element(*self.my_approve_view_loc).click()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def click_approve_report(self):
        self.find_element(*self.approve_report_loc).click()

    def input_approve_view(self, approve_view):
        self.send_keys(self.approve_view_loc, approve_view)

    def click_pass_button(self):
        self.find_element(*self.pass_button_loc).click()

    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()


class TodoPage(SeleniumBasePage):
    u"""代办查询主页面"""
    yewuNo_loc = (By.CSS_SELECTOR, "input[name='referCode']")
    queryAll_loc = (By.CSS_SELECTOR, "input[name='queryAll']")
    serchButton_loc = (By.CSS_SELECTOR, "input[value='搜索']")

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


class PayMoneyApprove(SeleniumBasePage):
    u"""审批打款流程"""
    collect_date_loc = (By.ID, "collectDate")
    collect_no_loc = (By.NAME, "collectNo")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    approve_view_loc = (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")
    tongguo_loc = (By.CSS_SELECTOR, "input[value='通 过']")
    confirm_loc = (By.XPATH, "//button[text()='确认']")
    shifoudaozhang_loc = (By.ID, "noYes")
    shiji_shoukuan_jine_loc = (By.ID, 'realDkMoney')

    def get_result(self, yewuno):
        u"""获取结果"""
        result_loc = (By.XPATH, "//td[text()='" + yewuno + "']/following-sibling::td[3]")
        return self.find_element(*result_loc).text

    def input_collect_date(self, collect_date):
        u"""输入到账日期"""
        self.input_date_time(self.collect_date_loc, collect_date)

    def select_collect_no(self):
        u"""选择收款账户"""
        self.select_widget(1, *self.collect_no_loc)

    def input_shiji_shoukuan_jine(self, jine="50000"):
        u"""实际收款金额"""
        self.send_keys(self.shiji_shoukuan_jine_loc, jine)

    def select_shifoudaozhang(self):
        u"""选择是否已到账"""
        self.select_widget("是", *self.shifoudaozhang_loc)

    def scroll_to_save_button(self):
        u"""滚动到保存按钮位置"""
        self.scroll_to_element(*self.save_button_loc)
        time.sleep(2)

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
        # time.sleep(5)


class ApproveInterview(SeleniumBasePage):
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
    zidong_shengcheng_huankuan_jihua_loc = (By.XPATH, '//a[text()="自动生成还款计划"]')
    save_button_loc = (By.CSS_SELECTOR, 'input[value="保存"]')

    def click_koufei_button(self):
        u"""点击扣费按钮"""
        self.find_element(*self.koufei_loc).click()
        time.sleep(2)

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//td[text()='" + loanno + "']/following-sibling::td[3]")
        return self.find_element(*result_loc).text

    def scroll_to_approve_view(self):
        u"""拖动页面到审批意见位置"""
        self.script(*self.approve_view_loc)
        time.sleep(1)

    def click_zidong_shengcheng_huankuan_jihua(self):
        u"""点自动生成还款计划"""
        self.find_element(*self.zidong_shengcheng_huankuan_jihua_loc).click()

    def input_approve_view(self, approve_view):
        u"""输入审批意见"""
        self.send_keys(self.approve_view_loc, approve_view)

    def click_tongguo(self):
        u"""点击通过按钮"""
        self.find_element(*self.tongguo_loc).click()
        time.sleep(2)

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

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

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


class ApproveCaiwuPage(SeleniumBasePage):
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
