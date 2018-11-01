#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: loan.py 
@time: 2018/01/03 
"""
from com.ea.common import tools, web_menu, web_login
import time
from com.ea.resource import globalparameter as gl
import sys

logger = tools.create_logger()


def loan_approve(driver, loanno, marry_status, screenshot_path, zx_zongfuzai_yue="0", daikuan_yuqi_cishu="0", danbao_yue="0", xinyongka_yuqi_cishu="0", daikuan_yuqi_24_wai="0", pzx_zongfuzai_yue="0", pdaikuan_yuqi_cishu="0",
                 pdanbao_yue="0",
                 pxinyongka_yuqi_cishu="0", pdaikuan_yuqi_24_wai="0"):
    u"""贷款审批"""
    casename = sys._getframe().f_code.co_name
    number = "0"
    view = "OK"
    process_type = "征信准入"
    except_result = "征信准入完成"
    # self.loanno = "SK0027-BK-1712-00006"
    logger.info("审批贷款开始")
    logger.info("使用的贷款单号是:" + loanno)
    from com.ea.pages.todo_page import TodoPage, ApproveLoanPage
    try:
        current_approver, node_name = tools.get_approver_acount_by_yewuno(loanno, gl.loan_approve)
        if not current_approver:
            raise Exception
        web_login.login(driver, username=current_approver)
        todopage = TodoPage(driver)
        approvepage = ApproveLoanPage(driver)
        # 进入待办查询页面
        web_menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approvepage.scrollto_edit()
        approvepage.click_edit()
        approvepage.input_zx_zfzye(zx_zongfuzai_yue)
        approvepage.input_near_24month_yuqi_cishu(daikuan_yuqi_cishu)
        approvepage.input_near_24month_wai_yuqi_cishu(daikuan_yuqi_24_wai)
        approvepage.input_danbao_yue(danbao_yue)
        approvepage.input_near_24month_xinyongka_yuqi(xinyongka_yuqi_cishu)
        approvepage.input_bank_overdue(number)
        approvepage.input_credit_overdue(number)
        approvepage.input_nobank_overdue(number)
        if marry_status == "已婚":
            approvepage.input_p_zx_zfzye(pzx_zongfuzai_yue)
            approvepage.input_p_near_24month_yuqi_cishu(pdaikuan_yuqi_cishu)
            approvepage.input_p_near_24month_wai_yuqi_cishu(pdaikuan_yuqi_24_wai)
            approvepage.input_p_danbao_yue(pdanbao_yue)
            approvepage.input_p_near_24month_xinyongka_yuqi(pxinyongka_yuqi_cishu)
            approvepage.input_p_bank_overdue(number)
            approvepage.input_p_credit_overdue(number)
            approvepage.input_p_nobank_overdue(number)
        approvepage.scrollto_save_button()
        approvepage.click_save_button()
        time.sleep(2)
        approvepage.scrollto_approve_view()
        approvepage.input_approve_view(view)
        approvepage.click_tongguo()
        approvepage.click_confirm()
        time.sleep(6)
        web_menu.go_to_loan_query(driver)
        approvepage.input_loan_no(loanno)
        approvepage.click_search_button()
        time.sleep(1)
        actual_result = approvepage.get_result(loanno)
        logger.info("预期值:" + except_result + "   实际值:" + actual_result)
        assert actual_result == except_result
        logger.info("审批贷款结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e

# def loan_by_role_approve(driver, loanno, screenshot_path, casename):
#     u"""贷款审批"""
#     number = "0"
#     view = "OK"
#     process_type = "征信准入"
#     except_result = "征信准入完成"
#     # self.loanno = "SK0027-BK-1712-00006"
#     logger.info("审批贷款开始")
#     logger.info("使用的贷款单号是:" + loanno)
#     from com.ea.pages.todo_page import TodoPage, ApproveLoanPage
#     try:
#         approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
#         web_login.login(driver, username=approver_account)
#         todopage = TodoPage(driver)
#         approvepage = ApproveLoanPage(driver)
#         # 进入待办查询页面
#         web_menu.go_to_wait_todo_query(driver)
#         todopage.input_yewuno(loanno)
#         # todopage.click_query_all()
#         todopage.click_search_button()
#         todopage.click_first_row(process_type)
#         approvepage.scrollto_edit()
#         approvepage.click_edit()
#         approvepage.input_bank_overdue(number)
#         approvepage.input_credit_overdue(number)
#         approvepage.input_nobank_overdue(number)
#         approvepage.scrollto_save_button()
#         approvepage.click_save_button()
#         time.sleep(2)
#         approvepage.scrollto_approve_view()
#         approvepage.input_approve_view(view)
#         approvepage.click_tongguo()
#         approvepage.click_confirm()
#         time.sleep(3)
#         menu.go_to_dkcxspg(driver)
#         approvepage.input_loan_no(loanno)
#         approvepage.click_search_button()
#         time.sleep(1)
#         actual_result = approvepage.get_result(loanno)
#         assert actual_result == except_result
#         logger.info("审批贷款结束")
#     except Exception as e:
#         tools.get_screenshot(driver, screenshot_path, casename)
#         raise e
