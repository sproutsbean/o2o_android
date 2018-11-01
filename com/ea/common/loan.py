#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: loan.py 
@time: 2018/03/20 
"""
import time
from com.ea.common import tools
from com.ea.common.cardnumber import IdCardNumber
from com.ea.common.cardname import cardname
from com.ea.pages import approve_page, menu_page
from com.ea.pages.menu_page import MenuPage
from com.ea.resource import globalparameter as gl
import sys

logger = tools.create_logger()


def loan_zhengxin_apply(driver, loan_type, sumofmoney, bank_name, operate_mode, screenshot_path, marry_status, danbaoren=None, start_date=None, end_date=None):
    casename = sys._getframe().f_code.co_name
    logger.info("申请贷款用例开始")
    try:
        if start_date and end_date:
            card_no = IdCardNumber.getRandomIdNumber(1, start=start_date, end=end_date)[0]
        else:
            card_no = IdCardNumber.getRandomIdNumber(1)[0]
        fullname, first_name, second_name, full_english_name, first_english_name, last_english_name = cardname.get_names()
        phone_no = cardname.createPhone()
        logger.info("姓名:" + fullname)
        logger.info("身份证:" + card_no)
        logger.info("电话:" + phone_no)
        partner_zx_no = ""
        tools.login(driver)
        menupage = MenuPage(driver)
        menupage.click_loan_apply()
        from com.ea.pages.loan_apply_page import LoanApplyPage
        loanapplypage = LoanApplyPage(driver)
        loanapplypage.select_loan_type(loan_type)
        loanapplypage.input_cardno(card_no)
        loanapplypage.click_next_button()
        time.sleep(2)
        loanapplypage.send_first_name(first_name)
        loanapplypage.send_second_name(second_name)
        loanapplypage.send_first_english_name(first_english_name)
        loanapplypage.send_second_english_name(last_english_name)
        loanapplypage.select_marry_status(marry_status)
        loanapplypage.click_card_expire_date()
        loanapplypage.send_phoneno(phone_no)
        time.sleep(2)
        loanapplypage.select_loan_manager(gl.xd_manager_name)
        loanapplypage.click_next_button()
        pcard_no = None
        pfullname = None
        if marry_status == "已婚":
            pcard_no = IdCardNumber.getRandomIdNumber(0)[0]
            pfullname, pfirst_name, psecond_name, pfull_english_name, pfirst_english_name, plast_english_name = cardname.get_names()
            pphone_no = cardname.createPhone()
            logger.info("配偶姓名:" + pfullname)
            logger.info("配偶身份证:" + pcard_no)
            logger.info("配偶电话:" + pphone_no)
            loanapplypage.input_partner_first_name(pfirst_name)
            loanapplypage.input_partner_last_name(psecond_name)
            loanapplypage.input_partner_first_english_name(pfirst_english_name)
            loanapplypage.input_partner_last_english_name(plast_english_name)
            loanapplypage.input_partner_card_no(pcard_no)
            loanapplypage.click_card_expire_date()
            loanapplypage.send_phoneno(pphone_no)
            loanapplypage.click_next_button()
        loanapplypage.input_loan_sumofmoney(sumofmoney)
        loanapplypage.select_operate_mode(operate_mode)
        # loanapplypage.input_platform(platform)
        loanapplypage.input_channel_name()
        if loan_type == "终端贷":
            loanapplypage.input_sd_customer_name()
        loanapplypage.click_save_button()
        time.sleep(3)
        # loanno = tools.get_loan_no_by_cardno(card_no)
        # loanapplypage.click_loan_no(loanno)
        loanapplypage.select_fuqizhengxin_report()

        loanapplypage.click_name(first_name + second_name)
        loanapplypage.click_zhengxin_apply()
        loanapplypage.click_zhengxin_bank_option()
        loanapplypage.click_zhengxin_bank_name(bank_name)
        loanapplypage.click_save_button()
        loanapplypage.click_shenfenzhengfuyinjian()
        time.sleep(4)
        loanapplypage.click_shouchishouquanshu()
        time.sleep(4)
        loanapplypage.click_zhengxinshouquanshu()
        time.sleep(4)
        loanapplypage.click_disanfangshujuchaxunshouquanshu()
        time.sleep(4)
        loanapplypage.click_shouchishenfenzheng()
        time.sleep(4)
        loanapplypage.click_kehuhukouben()
        time.sleep(4)
        loanapplypage.click_zxbgsysqsm()
        time.sleep(4)
        loanapplypage.click_sxsqyxs()
        time.sleep(4)
        loanapplypage.click_jkryyytmywlfj()
        time.sleep(4)
        loanapplypage.click_save_button()
        loanapplypage.click_radio_button()
        loanapplypage.click_guanlian_button()
        loanapplypage.click_confirm_button()
        time.sleep(3)
        assert "审核中" == loanapplypage.get_zx_status_by_name(fullname)
        if marry_status == "已婚":
            loanapplypage.click_name(pfullname)
            loanapplypage.click_zhengxin_apply()
            loanapplypage.click_zhengxin_bank_option()
            loanapplypage.click_zhengxin_bank_name(bank_name)
            loanapplypage.click_save_button()
            loanapplypage.click_shenfenzhengfuyinjian()
            time.sleep(4)
            loanapplypage.click_shouchishouquanshu()
            time.sleep(4)
            loanapplypage.click_zhengxinshouquanshu()
            time.sleep(4)
            loanapplypage.click_disanfangshujuchaxunshouquanshu()
            time.sleep(4)
            loanapplypage.click_shouchishenfenzheng()
            time.sleep(4)
            loanapplypage.click_kehuhukouben()
            time.sleep(4)
            loanapplypage.click_zxbgsysqsm()
            time.sleep(4)
            loanapplypage.click_sxsqyxs()
            time.sleep(4)
            loanapplypage.click_jkryyytmywlfj()
            time.sleep(4)
            loanapplypage.click_save_button()
            loanapplypage.click_radio_button()
            loanapplypage.click_guanlian_button()
            loanapplypage.click_confirm_button()
            assert "审核中" == loanapplypage.get_zx_status_by_name(pfullname)
            partner_zx_no = tools.get_zx_no_by_cardno(pcard_no)
        if danbaoren:
            driver.back()
            time.sleep(1)
            loanapplypage.swipe("up")
            loanapplypage.click_danbaoren_xiangqing()
            loanapplypage.click_add_button()
            loanapplypage.click_danbaoren_name_option()
            loanapplypage.input_danbaoren_name(danbaoren)
            loanapplypage.click_first_danbaoren()
            loanapplypage.click_yujiekuanren_guanxi()
            loanapplypage.click_guanxi()
            loanapplypage.click_save_button()
            logger.info("申请贷款用例结束")
        return card_no, fullname, partner_zx_no
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def loan_approve(driver, loan_no, screenshot_path, casename):
    logger.info("审批贷款用例开始")
    logger.info("使用的贷款单号是:", loan_no)
    total_fuzhai = "0"
    bank_overdue = "0"
    approve_view = "OK"
    loanapprovepage = approve_page.LoanApprovePage(driver)
    menupage = menu_page.MenuPage(driver)
    pubapprovepage = approve_page.ApprovePubPage(driver)
    try:
        menupage.click_approve_page()
        pubapprovepage.click_todo_first_row(loan_no)
        pubapprovepage.click_first_row()
        pubapprovepage.click_my_approve()
        loanapprovepage.click_fuzhaiqingkuang()
        loanapprovepage.input_total_fuzhai(total_fuzhai)
        loanapprovepage.input_bank_overdue(bank_overdue)
        loanapprovepage.click_save_button()
        time.sleep(1)
        loanapprovepage.input_approve_view(approve_view)
        loanapprovepage.click_pass_button()
        loanapprovepage.click_confirm_button()
        logger.info("审批贷款用例结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e
