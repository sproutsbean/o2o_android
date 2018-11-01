#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: menu.py 
@time: 2017/11/15 
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# --------------客户管理主菜单------------------------------------------

def go_to_customer_manage(driver):
    u"""进入客户主菜单"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='客户管理']")))
        el = driver.find_element_by_xpath("//a[text()='客户管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_brand_manage(driver):
    u"""进入客户管理下的品牌管理页面"""
    actions = ActionChains(driver)
    go_to_customer_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='品牌管理']")
    actions.move_to_element(el).click().perform()


def go_to_channel_manage(driver):
    u"""进入客户管理下的渠道管理页面"""
    actions = ActionChains(driver)
    go_to_customer_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='渠道管理']")
    actions.move_to_element(el).click().perform()


def go_to_factor_manage(driver):
    u"""进入客户管理下的厂家合作方管理页面"""
    actions = ActionChains(driver)
    go_to_customer_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='厂家合作方管理']")
    actions.move_to_element(el).click().perform()


def go_to_brand_store_query(driver):
    u"""进入客户管理下的品牌贷门店查询页面"""
    actions = ActionChains(driver)
    go_to_customer_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='品牌贷门店查询']")
    actions.move_to_element(el).click().perform()


def go_to_jxshzf_manage(driver):
    u"""进入客户管理下的经销商合作方管理页面"""
    actions = ActionChains(driver)
    go_to_customer_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='经销商合作方管理']")
    actions.move_to_element(el).click().perform()


# --------------客户管理主菜单------------------------------------------

# ----------------------征信管理主菜单 ----------------------------------
def go_to_zhengxin_manage(driver):
    u"""进入征信管理主菜单"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='征信管理']")))
        el = driver.find_element_by_xpath("//a[text()='征信管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_personnel_zhengxin_query(driver):
    u"""进入征信查询页面"""
    actions = ActionChains(driver)
    go_to_zhengxin_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='征信查询']")
    actions.move_to_element(el).click().perform()


def go_to_company_zhengxin_query(driver):
    u"""进入企业征信查询页面"""
    actions = ActionChains(driver)
    go_to_zhengxin_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='企业征信查询']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------征信管理主菜单------------------------------------------

# ------------------------------------------贷款管理主菜单-----------------------------------------

def go_to_loan_manage(driver):
    u"""贷款管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷款管理']")))
        el = driver.find_element_by_xpath("//a[text()='贷款管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_loan_apply(driver):
    u"""申请贷款"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    time.sleep(1)
    el = driver.find_element_by_xpath("//a[text()='申请贷款']")
    actions.move_to_element(el).click().perform()


def go_to_loan_query(driver):
    u"""贷款查询"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[contains(text(),'贷款查询')]")
    actions.move_to_element(el).click().perform()


def go_to_allow_zhengxin(driver):
    u"""征信准入"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='征信准入']")
    actions.move_to_element(el).click().perform()


def go_to_inside_approve(driver):
    u"""进入贷款管理下的内部审批页面"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='内部审批']")
    actions.move_to_element(el).click().perform()


def go_to_charge_query(driver):
    u"""收费查询"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='收费查询']")
    actions.move_to_element(el).click().perform()


def go_to_interview_report(driver):
    u"""面签提报"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='面签提报']")
    actions.move_to_element(el).click().perform()


def go_to_platform_caiwu_approve(driver):
    u"""平台财务审核"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='平台财务审核']")
    actions.move_to_element(el).click().perform()


def go_to_customer_apply_loan_query(driver):
    u"""用户申请贷款查询"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='用户申请贷款查询']")
    actions.move_to_element(el).click().perform()


def go_to_loaned_info_confirm(driver):
    u"""放款信息确认"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='放款信息确认']")
    actions.move_to_element(el).click().perform()


def go_to_apply_loan_again(driver):
    u"""申请续贷"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='申请续贷']")
    actions.move_to_element(el).click().perform()


def go_to_old_platform_data_query(driver):
    u"""旧系统数据查询"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='旧系统数据查询']")
    actions.move_to_element(el).click().perform()


def go_to_notification(driver):
    u"""通知函"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='通知函']")
    actions.move_to_element(el).click().perform()


def go_to_cancel(driver):
    u"""作废"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='作废']")
    actions.move_to_element(el).click().perform()


def go_to_cancel_loan_query(driver):
    u"""作废贷款查询"""
    actions = ActionChains(driver)
    go_to_loan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='作废贷款查询']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------贷款管理主菜单 ------------------------------------------

# ------------------------------------------ 贷后管理主菜单 ------------------------------------------
def go_to_afterloan_manage(driver):
    u"""进入贷后管理主菜单"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el = driver.find_element_by_xpath("//a[text()='贷后管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_afterloan_query(driver):
    u"""贷后查询"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷后查询']")
    actions.move_to_element(el).click().perform()


def go_to_daihoudingqijiancha_query(driver):
    u"""贷后定期检查查询"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷后定期检查查询']")
    actions.move_to_element(el).click().perform()


def go_to_huankuanguanli(driver):
    u"""还款管理"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='还款管理']")
    actions.move_to_element(el).click().perform()


def go_to_yinhangfangkuanshuju(driver):
    u"""银行放款数据"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='还款管理']")
        el3 = driver.find_element_by_xpath("//a[text()='银行放款数据']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_huankuanjihuashuju(driver):
    u"""还款计划数据"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='还款管理']")
        el3 = driver.find_element_by_xpath("//a[text()='还款计划数据']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_fangkuanshujuqueren(driver):
    u"""放款数据确认"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='还款管理']")
        el3 = driver.find_element_by_xpath("//a[text()='放款数据确认']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_tiqianhuankuanchaxun(driver):
    u"""提前还款查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='还款管理']")
        el3 = driver.find_element_by_xpath("//a[text()='提前还款查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daihouyujing(driver):
    u"""贷后预警"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷后预警']")
    actions.move_to_element(el).click().perform()


def go_to_daoqiyujingshirinei(driver):
    u"""到期预警(10日内)"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='贷后预警']")
        el3 = driver.find_element_by_xpath("//a[text()='到期预警(10日内)']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daoqiyujingwurinei(driver):
    u"""到期预警(5日内)"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='贷后预警']")
        el3 = driver.find_element_by_xpath("//a[text()='到期预警(5日内)']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_buliangguanli(driver):
    u"""不良管理"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='不良管理']")
    actions.move_to_element(el).click().perform()


def go_to_daichangshuju(driver):
    u"""代偿数据"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿数据']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yuqiliebiao(driver):
    u"""逾期列表"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='逾期列表']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_jielifenqishuju(driver):
    u"""接力分期数据"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='接力分期数据']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daichangfukuanchaxun(driver):
    u"""代偿付款查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿付款查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daichanghuikuanjilu(driver):
    u"""代偿回款记录"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿回款记录']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daichangfankuichaxun(driver):
    u"""代偿反馈查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿反馈查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yuqixinxiweihu(driver):
    u"""逾期信息维护"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='逾期信息维护']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yuqihuikuanjilu(driver):
    u"""逾期回款记录"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='逾期回款记录']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daichangjieqing(driver):
    u"""代偿结清"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿结清']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daichangfenqijihuachaxun(driver):
    u"""代偿分期计划查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='不良管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿分期计划查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_guidangguanli(driver):
    u"""归档管理"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='归档管理']")
    actions.move_to_element(el).click().perform()


def go_to_zhengxinguidang(driver):
    u"""征信归档"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='归档管理']")
        el3 = driver.find_element_by_xpath("//a[text()='征信归档']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daihouguidang(driver):
    u"""贷后归档"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='归档管理']")
        el3 = driver.find_element_by_xpath("//a[text()='贷后归档']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daichangziliaoluru(driver):
    u"""代偿资料录入"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='归档管理']")
        el3 = driver.find_element_by_xpath("//a[text()='代偿资料录入']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_guidangchaxun(driver):
    u"""归档查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='归档管理']")
        el3 = driver.find_element_by_xpath("//a[text()='归档查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_zhengxinjiluchaxun(driver):
    u"""征信记录查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='归档管理']")
        el3 = driver.find_element_by_xpath("//a[text()='征信记录查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daikuanfenlei(driver):
    u"""贷款分类"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷款分类']")
    actions.move_to_element(el).click().perform()


def go_to_daikuanfenleichaxun(driver):
    u"""贷款分类查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='贷款分类']")
        el3 = driver.find_element_by_xpath("//a[text()='贷款分类查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daikuanrengongfenlei(driver):
    u"""贷款人工分类"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='贷后管理']")))
        el1 = driver.find_element_by_xpath("//a[text()='贷后管理']")
        el2 = driver.find_element_by_xpath("//a[text()='贷款分类']")
        el3 = driver.find_element_by_xpath("//a[text()='贷款人工分类']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_jiangxiyinhangkaweihu(driver):
    u"""江西银行银行卡维护"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='江西银行银行卡维护']")
    actions.move_to_element(el).click().perform()


def go_to_buchongguidang(driver):
    u"""补充归档"""
    actions = ActionChains(driver)
    go_to_afterloan_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='补充归档']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------   贷后管理主菜单 ------------------------------------------


# ------------------------------------------ 审批管理主菜单  ------------------------------------------
def go_to_approve_manage(driver):
    u"""审批管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='审批管理']")))
        el = driver.find_element_by_xpath("//a[text()='审批管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_wait_todo_query(driver):
    u"""待办查询"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='待办查询']")
    actions.move_to_element(el).click().perform()


def go_to_yiban_query(driver):
    u"""已办查询"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='已办查询']")
    actions.move_to_element(el).click().perform()


def go_to_yifaqi_query(driver):
    u"""已发起查询"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='已发起查询']")
    actions.move_to_element(el).click().perform()


def go_to_shixiao_query(driver):
    u"""时效查询"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='时效查询']")
    actions.move_to_element(el).click().perform()


def go_to_chaxunjiekuanren(driver):
    u"""查询借款人"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='查询借款人']")
    actions.move_to_element(el).click().perform()


def go_to_liuchengshixiaoweijieshu(driver):
    u"""流程时效未结束"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='流程时效未结束']")
    actions.move_to_element(el).click().perform()


def go_to_liuchengshixiaoyijieshu(driver):
    u"""流程时效已结束"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='流程时效已结束']")
    actions.move_to_element(el).click().perform()


def go_to_jiedianshixiaoweichuli(driver):
    u"""节点时效未处理"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='节点时效未处理']")
    actions.move_to_element(el).click().perform()


def go_to_jiedianshixiaoyichuli(driver):
    u"""节点时效已处理"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='节点时效已处理']")
    actions.move_to_element(el).click().perform()


def go_to_daikuanshenqingshixiaochaxun(driver):
    u"""贷款申请时效查询"""
    actions = ActionChains(driver)
    go_to_approve_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷款申请时效查询']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------ 审批管理主菜单 ------------------------------------------

# ------------------------------------------ 财务管理主菜单 ------------------------------------------
def go_to_caiwu_manage(driver):
    u"""财务管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='财务管理']")))
        el = driver.find_element_by_xpath("//a[text()='财务管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_dakuanguanli(driver):
    u"""打款管理"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='打款管理']")
    actions.move_to_element(el).click().perform()


def go_to_tuikuanguanli(driver):
    u"""退款管理"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='退款管理']")
    actions.move_to_element(el).click().perform()


def go_to_kehuzhanghuyueechaxun(driver):
    u"""客户账户余额查询"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='客户账户余额查询']")
    actions.move_to_element(el).click().perform()


def go_to_dkdzhyecx(driver):
    u"""贷款单账户余额查询"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷款单账户余额查询']")
    actions.move_to_element(el).click().perform()


def go_to_baozhengjinyuguanlifei(driver):
    u"""保证金与管理费"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='保证金与管理费']")
    actions.move_to_element(el).click().perform()


def go_to_tuifeichaxun(driver):
    u"""退费查询"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='退费查询']")
    actions.move_to_element(el).click().perform()


def go_to_shouzhimingxi(driver):
    u"""收支明细"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='收支明细']")
    actions.move_to_element(el).click().perform()


def go_to_fukuanzhuanzhang(driver):
    u"""付款转账"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='付款转账']")
    actions.move_to_element(el).click().perform()


def go_to_jieqingqueren(driver):
    u"""结清确认"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='结清确认']")
    actions.move_to_element(el).click().perform()


def go_to_daihuankuangongneng(driver):
    u"""代还款功能"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='代还款功能']")
    actions.move_to_element(el).click().perform()


def go_to_yinhangzhanghuguanli(driver):
    u"""银行账户管理"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='银行账户管理']")
    actions.move_to_element(el).click().perform()


def go_to_daikuandantuijiantongji(driver):
    u"""贷款单推荐统计"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='贷款单推荐统计']")
    actions.move_to_element(el).click().perform()


def go_to_caiwuchaxun(driver):
    u"""财务查询"""
    actions = ActionChains(driver)
    go_to_caiwu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='财务查询']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------ 财务管理主菜单 ------------------------------------------


# ------------------------------------------ 法务管理主菜单 ------------------------------------------
def go_to_fawu_manage(driver):
    u"""法务管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='法务管理']")))
        el = driver.find_element_by_xpath("//a[text()='法务管理']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_anjianbaosong(driver):
    u"""案件报送"""
    actions = ActionChains(driver)
    go_to_fawu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='案件报送']")
    actions.move_to_element(el).click().perform()


def go_to_anjianguanli(driver):
    u"""案件管理"""
    actions = ActionChains(driver)
    go_to_fawu_manage(driver)
    el = driver.find_element_by_xpath("//a[text()='案件管理']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------ 法务管理主菜单 ------------------------------------------

# ------------------------------------------ 报表查询主菜单 ------------------------------------------
def go_to_baobiaochaxun(driver):
    u"""报表查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el = driver.find_element_by_xpath("//a[text()='报表查询']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_fangkuanyewubaobiao(driver):
    u"""放款业务报表"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='放款业务报表']")
    actions.move_to_element(el).click().perform()


def go_to_yewuanpingtaitongji(driver):
    u"""业务按平台统计"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='放款业务报表']")
        el3 = driver.find_element_by_xpath("//a[text()='业务按平台统计']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yewuanxindaijinglitongji(driver):
    u"""业务按信贷经理统计"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='放款业务报表']")
        el3 = driver.find_element_by_xpath("//a[text()='业务按信贷经理统计']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yewuanshengqutongji(driver):
    u"""业务按省区统计"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='放款业务报表']")
        el3 = driver.find_element_by_xpath("//a[text()='业务按省区统计']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yewuanfangkuanyinhangtongji(driver):
    u"""业务按放款银行统计"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='放款业务报表']")
        el3 = driver.find_element_by_xpath("//a[text()='业务按放款银行统计']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_anshijianqujiantongjifangkuanliang(driver):
    u"""按时间区间统计放款量"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='按时间区间统计放款量']")
    actions.move_to_element(el).click().perform()


def go_to_anxindaijinglitongjifangkuanliang(driver):
    u"""按信贷经理统计放款量"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='按时间区间统计放款量']")
        el3 = driver.find_element_by_xpath("//a[text()='按信贷经理统计放款量']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_antuanduitongjifangkuanliang(driver):
    u"""按团队统计放款量"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='按时间区间统计放款量']")
        el3 = driver.find_element_by_xpath("//a[text()='按团队统计放款量']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_anshengqutongjifangkuanliang(driver):
    u"""按省区统计放款量"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='按时间区间统计放款量']")
        el3 = driver.find_element_by_xpath("//a[text()='按省区统计放款量']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_antiantongjifangkuanliang(driver):
    u"""按天统计放款量"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='按天统计放款量']")
    actions.move_to_element(el).click().perform()


def go_to_antian_anxindaijinglitongjifangkuanliang(driver):
    u"""按信贷经理统计放款量"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='按天统计放款量']")
        el3 = driver.find_element_by_xpath("//a[text()='按信贷经理统计放款量']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_antian_antuanduitongjifangkuanliang(driver):
    u"""按团队统计放款量"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='按天统计放款量']")
        el3 = driver.find_element_by_xpath("//a[text()='按团队统计放款量']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_antian_anshengqutongjifangkuanliang(driver):
    u"""按省区统计放款量"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='按天统计放款量']")
        el3 = driver.find_element_by_xpath("//a[text()='按省区统计放款量']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_daikuanyuetongji(driver):
    u"""贷款余额统计"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='贷款余额统计']")
    actions.move_to_element(el).click().perform()


def go_to_anpingtaitongjidaikuanyue(driver):
    u"""按平台统计贷款余额"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='贷款余额统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按平台统计贷款余额']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_andijishitongjidaikuanyue(driver):
    u"""按地级市统计贷款余额"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='贷款余额统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按地级市统计贷款余额']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_anshengqutongjidaikuanyue(driver):
    u"""按省区统计贷款余额"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='贷款余额统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按省区统计贷款余额']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yinhangshenbaoshenchafangkuanjine(driver):
    u"""银行申报审查放款金额"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='银行申报审查放款金额']")
    actions.move_to_element(el).click().perform()


def go_to_yuqianpingtaibaobiaotongji(driver):
    u"""逾期按平台报表统计"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='逾期按平台报表统计']")
    actions.move_to_element(el).click().perform()


def go_to_yuqianshengqubaobiaotongji(driver):
    u"""逾期按省区报表统计"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='逾期按省区报表统计']")
    actions.move_to_element(el).click().perform()


def go_to_qudaoyewutongji(driver):
    u"""渠道业务统计"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='渠道业务统计']")
    actions.move_to_element(el).click().perform()


def go_to_anqudaojingbanrentongji(driver):
    u"""按渠道经办人统计"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='渠道业务统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按渠道经办人统计']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_andaikuandantongjizb(driver):
    u"""按渠道经办人统计(总部)"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='渠道业务统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按渠道经办人统计(总部)']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_anqudaotongjiguanliceng(driver):
    u"""按渠道统计（管理层）"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='渠道业务统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按渠道统计（管理层）']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_anqudaotongjijingbanren(driver):
    u"""按渠道统计（经办人）"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='报表查询']")))
        el1 = driver.find_element_by_xpath("//a[text()='报表查询']")
        el2 = driver.find_element_by_xpath("//a[text()='渠道业务统计']")
        el3 = driver.find_element_by_xpath("//a[text()='按渠道统计（经办人）']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yinhangeduweihu(driver):
    u"""银行额度维护"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='银行额度维护']")
    actions.move_to_element(el).click().perform()


def go_to_pinpaidaifangkuantaizhangchaxun(driver):
    u"""流通贷放款台账查询"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='流通贷放款台账查询']")
    actions.move_to_element(el).click().perform()


def go_to_ribaochaxun(driver):
    u"""日报查询"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='日报查询']")
    actions.move_to_element(el).click().perform()


def go_to_jianglibaobiao(driver):
    u"""奖励报表"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='奖励报表']")
    actions.move_to_element(el).click().perform()


def go_to_yuebaochaxun(driver):
    u"""月报查询"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='月报查询']")
    actions.move_to_element(el).click().perform()


def go_to_yewuhuizongtongji(driver):
    u"""业务汇总统计"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='业务汇总统计']")
    actions.move_to_element(el).click().perform()


def go_to_daichanghuikuanbaobiao(driver):
    u"""代偿回款报表"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='代偿回款报表']")
    actions.move_to_element(el).click().perform()


def go_to_yinhangshenbaojinduchaxun(driver):
    u"""银行申报进度查询"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='银行申报进度查询']")
    actions.move_to_element(el).click().perform()


def go_to_jiaqianyijiandaochu(driver):
    u"""加签意见导出"""
    actions = ActionChains(driver)
    go_to_baobiaochaxun(driver)
    el = driver.find_element_by_xpath("//a[text()='加签意见导出']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------ 报表查询主菜单 ------------------------------------------
# ------------------------------------------ 系统设置主菜单 ------------------------------------------
def go_to_xitongshezhi(driver):
    u"""系统设置"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el = driver.find_element_by_xpath("//a[text()='系统设置']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_jichushezhi(driver):
    u"""基础设置"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='基础设置']")
    actions.move_to_element(el).click().perform()


def go_to_jigouguanli(driver):
    u"""机构管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='基础设置']")
        el3 = driver.find_element_by_xpath("//a[text()='机构管理']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_caidanguanli(driver):
    u"""菜单管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='基础设置']")
        el3 = driver.find_element_by_xpath("//a[text()='菜单管理']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_ziliaoleixingguanli(driver):
    u"""资料类型管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='基础设置']")
        el3 = driver.find_element_by_xpath("//a[text()='资料类型管理']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_caozuozhiyinguanli(driver):
    u"""操作指引管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='基础设置']")
        el3 = driver.find_element_by_xpath("//a[text()='操作指引管理']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_guidangziliaopeizhi(driver):
    u"""归档资料配置"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='基础设置']")
        el3 = driver.find_element_by_xpath("//a[text()='归档资料配置']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_gangweiweihu(driver):
    u"""岗位维护"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='基础设置']")
        el3 = driver.find_element_by_xpath("//a[text()='岗位维护']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_liuchengguanli(driver):
    u"""流程管理"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='流程管理']")
    actions.move_to_element(el).click().perform()


def go_to_liuchengmobanguanli(driver):
    u"""流程模板管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='流程管理']")
        el3 = driver.find_element_by_xpath("//a[text()='流程模板管理']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_liuchengshenherenchakan(driver):
    u"""流程审核人查看"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='流程管理']")
        el3 = driver.find_element_by_xpath("//a[text()='流程审核人查看']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_liuchengshenherentihuan(driver):
    u"""流程审核人替换"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='流程管理']")
        el3 = driver.find_element_by_xpath("//a[text()='流程审核人替换']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_liuchengshouquan(driver):
    u"""流程授权"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='流程管理']")
        el3 = driver.find_element_by_xpath("//a[text()='流程授权']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_renyuanguanli(driver):
    u"""人员管理"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='人员管理']")
    actions.move_to_element(el).click().perform()


def go_to_renyuanguanxiweihu(driver):
    u"""人员关系维护"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='人员管理']")
        el3 = driver.find_element_by_xpath("//a[text()='人员关系维护']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_juesequanxian(driver):
    u"""角色权限"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='人员管理']")
        el3 = driver.find_element_by_xpath("//a[text()='角色权限']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_renyuanchaxun(driver):
    u"""人员查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='人员管理']")
        el3 = driver.find_element_by_xpath("//a[text()='人员查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_renyuanmingdanweihu(driver):
    u"""人员名单维护"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='人员管理']")
        el3 = driver.find_element_by_xpath("//a[text()='人员名单维护']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_renyuanquanxianchakan(driver):
    u"""人员权限查看"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='人员管理']")
        el3 = driver.find_element_by_xpath("//a[text()='人员权限查看']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_caozuojiluchaxun(driver):
    u"""操作记录查询"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='操作记录查询']")
    actions.move_to_element(el).click().perform()


def go_to_jieqingcaozuojiluchaxun(driver):
    u"""结清操作记录查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='操作记录查询']")
        el3 = driver.find_element_by_xpath("//a[text()='结清操作记录查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_zuofeicaozuojiluchaxun(driver):
    u"""作废操作记录查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='操作记录查询']")
        el3 = driver.find_element_by_xpath("//a[text()='作废操作记录查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_youjianguanli(driver):
    u"""邮件管理"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='操作记录查询']")
        el3 = driver.find_element_by_xpath("//a[text()='邮件管理']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_duanxinchaxun(driver):
    u"""短信查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='操作记录查询']")
        el3 = driver.find_element_by_xpath("//a[text()='短信查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_zhxtjyjlcx(driver):
    u"""账户系统交易记录查询"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='系统设置']")))
        el1 = driver.find_element_by_xpath("//a[text()='系统设置']")
        el2 = driver.find_element_by_xpath("//a[text()='操作记录查询']")
        el3 = driver.find_element_by_xpath("//a[text()='账户系统交易记录查询']")
        actions.move_to_element(el1).move_to_element(el2).move_to_element(el3).click().perform()
    except Exception as e:
        print(e)


def go_to_yinhangjiekoujiaohuxinxi(driver):
    u"""银行接口交互信息"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='银行接口交互信息']")
    actions.move_to_element(el).click().perform()


def go_to_MQyichangchaxun(driver):
    u"""MQ异常查询"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='MQ异常查询']")
    actions.move_to_element(el).click().perform()


def go_to_qunfaduanxin(driver):
    u"""群发短信"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='群发短信']")
    actions.move_to_element(el).click().perform()


def go_to_xuqiushenqing(driver):
    u"""需求申请"""
    actions = ActionChains(driver)
    go_to_xitongshezhi(driver)
    el = driver.find_element_by_xpath("//a[text()='需求申请']")
    actions.move_to_element(el).click().perform()


# ------------------------------------------ 系统设置主菜单 ------------------------------------------
# ------------------------------------------ 操作指引主菜单 ------------------------------------------
def go_to_caozuozhiyin(driver):
    u"""操作指引"""
    actions = ActionChains(driver)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='操作指引']")))
        el = driver.find_element_by_xpath("//a[text()='操作指引']")
        actions.move_to_element(el).perform()
    except Exception as e:
        print(e)


def go_to_yewuzhiyin(driver):
    u"""业务指引"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_xpath("//a[text()='业务指引']")
    actions.move_to_element(el).click().perform()


def go_to_yingxiaoguanli(driver):
    u"""营销管理"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_xpath("//a[text()='营销管理']")
    actions.move_to_element(el).click().perform()


def go_to_peixunguanli(driver):
    u"""培训管理"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_xpath("//a[text()='培训管理']")
    actions.move_to_element(el).click().perform()


def go_to_fengxianguanli(driver):
    u"""风险管理"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_xpath("//a[text()='风险管理']")
    actions.move_to_element(el).click().perform()


def go_to_renliguanli(driver):
    u"""人力管理"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_xpath("//a[text()='人力管理']")
    actions.move_to_element(el).click().perform()


def go_to_caiwuguanli(driver):
    u"""财务管理"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_css_selector("a[href$='financialManagement']")
    actions.move_to_element(el).click().perform()


def go_to_ITguanli(driver):
    u"""IT管理"""
    actions = ActionChains(driver)
    go_to_caozuozhiyin(driver)
    el = driver.find_element_by_xpath("//a[text()='IT管理']")
    actions.move_to_element(el).click().perform()

# ------------------------------------------ 操作指引主菜单 ------------------------------------------
