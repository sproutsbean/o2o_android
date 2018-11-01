#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: pay_money.py 
@time: 2018/01/24 
"""
from com.ea.pages.pay_money_page import PayMoneyPage
from com.ea.common import web_menu, tools, web_login
import time
from com.ea.resource import globalparameter as gl
import sys

logger = tools.create_logger()


def pay_money_apply(driver, full_name, card_no, screenshot_path):
    logger.info("新建打款流程开始")
    casename = sys._getframe().f_code.co_name
    logger.info("使用的姓名是:" + full_name)
    logger.info("使用的身份证号是:" + card_no)
    jine = "50000"
    from com.ea.pages.pay_money_page import PayMoneyPage
    from com.ea.pages.menu_page import MenuPage
    menupage = MenuPage(driver)
    paymoneypage = PayMoneyPage(driver)
    try:
        tools.login(driver)
        menupage.click_play_money_manage()
        paymoneypage.click_shenqingdakuan()
        paymoneypage.input_name(full_name)
        paymoneypage.input_cardno(card_no)
        paymoneypage.click_next_button()
        paymoneypage.input_dakuanjine(jine)
        paymoneypage.select_dakuanshijian()
        paymoneypage.input_shiji_dakuanren(full_name)
        paymoneypage.click_save_button()
        # paymoneypage.click_shaixuan()
        # paymoneypage.input_shaixuan_xingming(full_name)
        # paymoneypage.click_search_button()
        # paymoneypage.click_row_by_name(full_name)
        paymoneypage.click_start_flow()
        paymoneypage.click_confirm_text()
        time.sleep(1)
        paymoneypage.back()
        dakuandanhao = paymoneypage.get_dakuandanhao()
        logger.info("新建打款流程结束")
        logger.info("产生的业务单号是:" + dakuandanhao)
        return dakuandanhao
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def pay_money_approve(driver, yewuno, screenshot_path):
    casename = sys._getframe().f_code.co_name
    process_type = "个人账户打款"
    collect_date = "2018-01-01"
    approve_view = "OK"
    expect_result = "审批完成"
    from com.ea.pages.approve_page import TodoPage, PayMoneyApprove
    logger.info("审批打款流程开始")
    logger.info("使用的单号是:" + yewuno)
    try:
        cureent_approver, node_name = tools.get_approver_acount_by_yewuno(yewuno, gl.pay_approve)
        if not cureent_approver:
            raise Exception
        web_login.login(driver, username=cureent_approver)
        web_menu.go_to_wait_todo_query(driver)
        todopage = TodoPage(driver)
        paymoneyapprovepage = PayMoneyApprove(driver)
        todopage.input_yewuno(yewuno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        time.sleep(2)
        paymoneyapprovepage.scroll_to_approve_view()
        paymoneyapprovepage.input_collect_date(collect_date)
        paymoneyapprovepage.select_collect_no()
        paymoneyapprovepage.input_shiji_shoukuan_jine()
        # paymoneyapprovepage.select_shifoudaozhang()
        paymoneyapprovepage.scroll_to_save_button()
        paymoneyapprovepage.click_save_button()
        paymoneyapprovepage.click_confirm_button()
        paymoneyapprovepage.input_approve_view(approve_view)
        time.sleep(1)
        paymoneyapprovepage.click_tongguo_button()
        time.sleep(1)
        paymoneyapprovepage.click_confirm_button()
        time.sleep(5)
        web_menu.go_to_yiban_query(driver)
        todopage.input_yewuno(yewuno)
        todopage.click_search_button()
        actual_result = paymoneyapprovepage.get_result(yewuno)
        assert actual_result == expect_result
        logger.info("审批打款流程结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e

# def pay_money_approve_by_role(driver, yewuno, screenshot_path, casename):
#     process_type = "个人账户打款"
#     collect_date = "2018-01-01"
#     approve_view = "OK"
#     expect_result = "流程结束"
#     from com.ea.pages.todo_page import TodoPage, PayMoneyApprove
#     from com.ea.common import login
#     logger.info("审批打款流程开始")
#     logger.info("使用的单号是:" + yewuno)
#     try:
#         approver_account = tools.get_approver_acount_by_yewuno(yewuno, process_type)
#         login.login(driver, username=approver_account)
#         menu.go_to_wait_todo_query(driver)
#         todopage = TodoPage(driver)
#         paymoneyapprovepage = PayMoneyApprove(driver)
#         todopage.input_yewuno(yewuno)
#         # todopage.click_query_all()
#         todopage.click_search_button()
#         todopage.click_first_row(process_type)
#         paymoneyapprovepage.scroll_to_approve_view()
#         paymoneyapprovepage.input_collect_date(collect_date)
#         paymoneyapprovepage.select_collect_no()
#         paymoneyapprovepage.click_save_button()
#         paymoneyapprovepage.click_confirm_button()
#         paymoneyapprovepage.input_approve_view(approve_view)
#         paymoneyapprovepage.click_tongguo_button()
#         paymoneyapprovepage.click_confirm_button()
#         menu.go_to_dakuanguanli(driver)
#         actual_result = paymoneyapprovepage.get_result(yewuno)
#         assert actual_result == expect_result
#         logger.info("审批打款流程结束")
#     except Exception as e:
#         tools.get_screenshot(driver, screenshot_path, casename)
#         raise e
