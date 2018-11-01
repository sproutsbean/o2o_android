#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: zhengxin.py 
@time: 2018/03/20 
"""
import time
from com.ea.common import tools
from com.ea.pages.menu_page import MenuPage
from com.ea.pages.my_customer_page import MyCustomerPage
from com.ea.resource import globalparameter as gl
from com.ea.pages.zhengxin_page import ZhengxinPage
import sys

logger = tools.create_logger()


def zhengxin_apply(driver, card_no, first_name, second_name, first_english_name, last_english_name, phone_no, screenshot_path, casename):
    logger.info("申请征信用例开始")
    logger.info("使用的身份证号是:", card_no)
    try:
        tools.login(driver)
        menupage = MenuPage(driver)
        zhengxinpage = ZhengxinPage(driver)
        menupage.click_personal_zhengxin_query()
        zhengxinpage.click_apply_button()
        logger.info(card_no)
        zhengxinpage.send_cardno(card_no)
        zhengxinpage.click_next_button()
        zhengxinpage.send_first_name(first_name)
        zhengxinpage.send_second_name(second_name)
        zhengxinpage.send_first_english_name(first_english_name)
        zhengxinpage.send_second_english_name(last_english_name)
        zhengxinpage.click_card_expire_date()
        zhengxinpage.click_confirm_button()
        zhengxinpage.send_phoneno(phone_no)
        zhengxinpage.click_loan_manager_option()
        zhengxinpage.send_loan_manager_editview(gl.xd_manager_name)
        time.sleep(1)
        zhengxinpage.click_loan_manager_name()
        zhengxinpage.click_next_button()
        time.sleep(2)
        zhengxinpage.click_customer_type_option()
        zhengxinpage.click_customer_type_value()
        zhengxinpage.click_zhengxin_bank_option()
        zhengxinpage.click_zhengxin_bank_name()
        time.sleep(1)
        zhengxinpage.click_save_button()
        # zhengxinpage.click_platform_option()
        # zhengxinpage.send_platform_editview("深圳")
        # time.sleep(2)
        # zhengxinpage.click_platform_name()
        zhengxinpage.click_danhao_option()
        zhengxinpage.click_zhengxin_attachment()
        zhengxinpage.click_upload_attachment_button()
        zhengxinpage.click_shenfenzhengfuyinjian()
        time.sleep(4)
        zhengxinpage.click_shouchishouquanshu()
        time.sleep(4)
        zhengxinpage.click_zhengxinshouquanshu()
        time.sleep(4)
        zhengxinpage.click_disanfangshujuchaxunshouquanshu()
        time.sleep(4)
        zhengxinpage.click_shouchishenfenzheng()
        time.sleep(4)
        zhengxinpage.click_kehuhukouben()
        time.sleep(4)
        zhengxinpage.click_zxbgsysqsm()
        time.sleep(4)
        zhengxinpage.click_sxsqyxs()
        time.sleep(4)
        zhengxinpage.click_jkryyytmywlfj()
        time.sleep(4)
        zhengxinpage.click_back_img()
        time.sleep(1)
        driver.back()
        zhengxinpage.click_start_flowing_button()
        zhengxinpage.click_confirm_button()
        logger.info("申请征信用例结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def zhengxin_approve(driver, zx_no, screenshot_path, partner_zx_no=""):
    casename = sys._getframe().f_code.co_name
    logger.info("审批征信用例开始")
    logger.info("使用的征信单号是:" + zx_no)
    approve_view = "OK"
    try:
        turns = 1
        if partner_zx_no:
            turns = 2
        from com.ea.pages import approve_page
        menupage = MenuPage(driver)
        pubapprovepage = approve_page.ApprovePubPage(driver)
        zhengxinapprovepage = approve_page.ZhengxinApprovePage(driver)
        for i in range(turns):
            current_approver = None
            if i == 0:
                current_approver, node_name = tools.get_approver_acount_by_yewuno(zx_no, gl.zx_approve)
                if not current_approver:
                    logger.info("借款人征信没有走到审批环节来!")
                    raise Exception
                driver.start_activity(gl.packagename, gl.login_activity)
                tools.login(driver, username=current_approver)
                menupage.click_approve_page()
            if i == 1:
                zx_no = partner_zx_no
                current_approver, node_name = tools.get_approver_acount_by_yewuno(zx_no, gl.zx_approve)
                if not current_approver:
                    logger.info("配偶征信没有走到审批环节来!")
                    raise Exception
            pubapprovepage.click_todo_first_row(zx_no)
            pubapprovepage.click_first_row()
            pubapprovepage.click_my_approve()
            zhengxinapprovepage.input_approve_view(approve_view)
            zhengxinapprovepage.click_pass_button()
            zhengxinapprovepage.click_confirm()
            time.sleep(10)
            next_approver, node_name = tools.get_approver_acount_by_yewuno(zx_no, gl.zx_approve)
            if not next_approver:
                continue
            if next_approver != current_approver:
                current_approver = next_approver
                driver.start_activity(gl.packagename, gl.login_activity)
                tools.login(driver, username=current_approver)
                menupage.click_approve_page()
                pubapprovepage.click_todo_first_row(zx_no)
            pubapprovepage.click_first_row()
            pubapprovepage.click_my_approve()
            zhengxinapprovepage.click_upload_zhengxin_report()
            time.sleep(5)
            zhengxinapprovepage.click_back_img()
            zhengxinapprovepage.click_customer_zhengxin_report_date()
            time.sleep(1)
            zhengxinapprovepage.click_back_img()
            zhengxinapprovepage.input_approve_view(approve_view)
            zhengxinapprovepage.click_pass_button()
            zhengxinapprovepage.click_confirm()
            time.sleep(10)
        logger.info("审批征信用例结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def zhengxin_apply_from_mycustomer(driver, card_no, first_name, second_name, first_english_name, last_english_name, phone_no, bank_name, screenshot_path, casename):
    logger.info("申请征信用例开始")
    logger.info("使用的身份证号是:", card_no)
    try:
        tools.login(driver)
        # menupage = MenuPage(driver)
        mycustomerpage = MyCustomerPage(driver)
        from com.ea.common import add_customer
        add_customer.add_customer(driver, first_name, second_name, first_english_name, last_english_name, card_no, phone_no)
        mycustomerpage.click_customer_name(first_name + second_name)
        mycustomerpage.click_archives()
        mycustomerpage.click_apply_personal_zhengxin()
        mycustomerpage.click_next_button()
        mycustomerpage.click_next_button()
        mycustomerpage.select_customer_type()
        mycustomerpage.select_bank(bank_name)
        mycustomerpage.click_save_button()
        time.sleep(3)
        zx_no = tools.get_zx_no_by_cardno(card_no)
        logger.info(zx_no)
        mycustomerpage.click_zx_no(zx_no)
        mycustomerpage.click_zhengxin_attachment()
        mycustomerpage.click_upload_attachment_button()
        mycustomerpage.click_shenfenzhengfuyinjian()
        time.sleep(4)
        mycustomerpage.click_shouchishouquanshu()
        time.sleep(4)
        mycustomerpage.click_zhengxinshouquanshu()
        time.sleep(4)
        mycustomerpage.click_disanfangshujuchaxunshouquanshu()
        time.sleep(4)
        mycustomerpage.click_shouchishenfenzheng()
        time.sleep(4)
        mycustomerpage.click_kehuhukouben()
        time.sleep(4)
        mycustomerpage.click_zxbgsysqsm()
        time.sleep(4)
        mycustomerpage.click_sxsqyxs()
        time.sleep(4)
        mycustomerpage.click_jkryyytmywlfj()
        time.sleep(4)
        mycustomerpage.click_back_img()
        time.sleep(1)
        driver.back()
        mycustomerpage.click_start_flowing_button()
        mycustomerpage.click_confirm_button()
        # menupage.click_home_page()
        # menupage.click_personal_zhengxin_query()
        assert "审核中" == mycustomerpage.get_zx_status(zx_no)
        logger.info("申请征信用例结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e
