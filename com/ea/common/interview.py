#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: interview.py 
@time: 2018/01/03 
"""

import time
from com.ea.common import web_menu, tools, web_login
from com.ea.resource import globalparameter as gl
import sys

logger = tools.create_logger()


def interview_apply(driver, loan_no, screenshot_path):
    u"""面签提报"""
    casename = sys._getframe().f_code.co_name
    logger.info("面前提报用例开始")
    logger.info("使用的贷款单号是:" + loan_no)
    try:
        tools.login(driver, username=gl.xd_manager_account)
        from com.ea.pages.menu_page import MenuPage
        menupage = MenuPage(driver)
        menupage.click_interview()
        from com.ea.pages.interview_page import InterviewPage
        interviewpage = InterviewPage(driver)
        interviewpage.click_loan_no(loan_no)
        interviewpage.click_menu()
        # interviewpage.click_edit_interview_info()
        interviewpage.click_xiazai_daishuju_hetong()
        # interviewpage.click_bank_info()
        interviewpage.input_bank_name("深圳银行")
        interviewpage.input_bank_no("221982847192")
        interviewpage.click_next_button()
        interviewpage.click_bank_info()
        interviewpage.select_hetongshifouqibei()
        interviewpage.click_save_button()
        interviewpage.click_mianqianfujian()
        interviewpage.click_upload()
        interviewpage.click_from_local_photos()
        interviewpage.click_photo_name()
        time.sleep(5)
        driver.back()
        # time.sleep(1)
        # driver.back()
        interviewpage.click_menu()
        interviewpage.click_mianqianshenbao()
        interviewpage.click_confirm()
        logger.info("面签提报用例结束")
        time.sleep(5)
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def interview_approve(driver, loanno, fullname, screenshot_path):
    u"""面签审批"""
    casename = sys._getframe().f_code.co_name
    expect_result = "审批完成"
    types = "面签提报"
    card_daoqi_date = "2017-10-10"
    approve_view = "OK"
    isphonecheck = "是"
    phonecheckmessage = "OK"
    isfujianover = "是"
    file_path = gl.file_path
    logger.info("面签审批开始")
    logger.info("使用的贷款单号是:" + loanno)
    try:
        from com.ea.pages.approve_page import TodoPage, ApproveInterview
        current_approver, node_name = tools.get_approver_acount_by_yewuno(loanno, gl.interview_approve)
        if not current_approver:
            raise Exception
        web_login.login(driver, username=current_approver)
        todopage = TodoPage(driver)
        approveinterviepage = ApproveInterview(driver)
        web_menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(types)
        time.sleep(2)
        approveinterviepage.scroll_to_approve_view()
        time.sleep(2)
        approveinterviepage.input_approve_view(approve_view)
        time.sleep(2)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        time.sleep(5)
        next_approver, node_name = tools.get_approver_acount_by_yewuno(loanno, gl.interview_approve)
        if next_approver != current_approver:
            current_approver = next_approver
            driver.delete_all_cookies()
            web_login.login(driver, username=current_approver)
            web_menu.go_to_wait_todo_query(driver)
            todopage.input_yewuno(loanno)
            todopage.click_query_all()
            todopage.click_search_button()
        todopage.click_first_row(types)
        time.sleep(2)
        approveinterviepage.scroll_to_is_phone_check()
        approveinterviepage.select_is_phone_check(isphonecheck)
        approveinterviepage.input_phone_check_message(phonecheckmessage)
        approveinterviepage.click_phone_save_button()
        time.sleep(1)
        approveinterviepage.select_is_fujian_over(isfujianover)
        approveinterviepage.click_fujian_save_button()
        time.sleep(1)
        approveinterviepage.scroll_to_approve_view()
        approveinterviepage.click_koufei_button()
        approveinterviepage.input_approve_view(approve_view)
        time.sleep(1)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        time.sleep(5)
        next_approver, node_name = tools.get_approver_acount_by_yewuno(loanno, gl.interview_approve)
        if next_approver != current_approver:
            current_approver = next_approver
            driver.delete_all_cookies()
            web_login.login(driver, username=current_approver)
            web_menu.go_to_wait_todo_query(driver)
            todopage.input_yewuno(loanno)
            todopage.click_query_all()
            todopage.click_search_button()
        todopage.click_first_row(types)
        time.sleep(2)
        approveinterviepage.scroll_to_card_date()
        approveinterviepage.input_card_daoqi_date(card_daoqi_date)
        approveinterviepage.click_save_bank_loan_data()
        approveinterviepage.click_confirm()
        time.sleep(1)
        # tools.create_huankuanjihua(fullname)
        # approveinterviepage.input_file(file_path)
        approveinterviepage.click_zidong_shengcheng_huankuan_jihua()
        time.sleep(3)
        approveinterviepage.scroll_to_is_phone_check()
        approveinterviepage.select_is_phone_check(isphonecheck)
        approveinterviepage.input_phone_check_message(phonecheckmessage)
        approveinterviepage.click_save_button()
        time.sleep(1)
        approveinterviepage.input_approve_view(approve_view)
        time.sleep(1)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        time.sleep(5)
        web_menu.go_to_yiban_query(driver)
        actual_result = approveinterviepage.get_result(loanno)
        assert actual_result == expect_result
        logger.info("审批面签提报结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e

# def interview_approve_by_role(driver, loanno, fullname, screenshot_path, casename):
#     u"""面签审批"""
#     expect_result = "已放款"
#     process_type = "面签提报"
#     card_daoqi_date = "2017-10-10"
#     approve_view = "OK"
#     isphonecheck = "是"
#     phonecheckmessage = "OK"
#     isfujianover = "是"
#     file_path = gl.file_path
#     # self.loanno = "SK0027-BP-1801-00002"
#     # self.fullname = "何器"
#     logger.info("面签审批开始")
#     logger.info("使用的贷款单号是:" + loanno)
#     try:
#         from com.ea.pages.todo_page import TodoPage, ApproveInterview
#         approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
#         login.login(driver, username=approver_account)
#         todopage = TodoPage(driver)
#         approveinterviepage = ApproveInterview(driver)
#         menu.go_to_wait_todo_query(driver)
#         todopage.input_yewuno(loanno)
#         # todopage.click_query_all()
#         todopage.click_search_button()
#         todopage.click_first_row(process_type)
#         approveinterviepage.scroll_to_approve_view()
#         approveinterviepage.input_approve_view(approve_view)
#         approveinterviepage.click_tongguo()
#         approveinterviepage.click_confirm()
#         driver.delete_all_cookies()
#         time.sleep(3)
#         approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
#         login.login(driver, username=approver_account)
#         menu.go_to_wait_todo_query(driver)
#         todopage.input_yewuno(loanno)
#         # todopage.click_query_all()
#         todopage.click_search_button()
#         todopage.click_first_row(process_type)
#         approveinterviepage.scroll_to_is_phone_check()
#         approveinterviepage.select_is_phone_check(isphonecheck)
#         approveinterviepage.input_phone_check_message(phonecheckmessage)
#         approveinterviepage.click_phone_save_button()
#         time.sleep(1)
#         approveinterviepage.select_is_fujian_over(isfujianover)
#         approveinterviepage.click_fujian_save_button()
#         time.sleep(1)
#         approveinterviepage.scroll_to_approve_view()
#         approveinterviepage.click_koufei_button()
#         approveinterviepage.input_approve_view(approve_view)
#         approveinterviepage.click_tongguo()
#         approveinterviepage.click_confirm()
#         driver.delete_all_cookies()
#         time.sleep(3)
#         approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
#         login.login(driver, username=approver_account)
#         menu.go_to_wait_todo_query(driver)
#         todopage.input_yewuno(loanno)
#         # todopage.click_query_all()
#         todopage.click_search_button()
#         todopage.click_first_row(process_type)
#         approveinterviepage.scroll_to_card_date()
#         approveinterviepage.input_card_daoqi_date(card_daoqi_date)
#         approveinterviepage.click_save_bank_loan_data()
#         time.sleep(1)
#         tools.create_huankuanjihua(fullname)
#         approveinterviepage.input_file(file_path)
#         time.sleep(3)
#         approveinterviepage.input_approve_view(approve_view)
#         approveinterviepage.click_tongguo()
#         approveinterviepage.click_confirm()
#         driver.delete_all_cookies()
#         login.login(driver)
#         menu.go_to_loan_query(driver)
#         # time.sleep(5)
#         actual_result = approveinterviepage.get_result(loanno)
#         assert actual_result == expect_result
#         logger.info("审批面签提报结束")
#     except Exception as e:
#         tools.get_screenshot(driver, screenshot_path, casename)
#         raise e
