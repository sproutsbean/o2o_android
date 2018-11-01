#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: inside.py 
@time: 2018/03/20 
"""
from com.ea.common import tools
import time
from com.ea.resource import globalparameter as gl
from com.ea.common import web_login
from com.ea.common import web_menu
from com.ea.pages import menu_page
import sys

logger = tools.create_logger()


def inside_apply(webdriver, loanno, fullname, loan_type, marry_status, bank_name, screenshot_path, start_time="2017-10-10", eamount="100000", year_sales="200", lianbao_daikuan_yue="0", jiufen="无"):
    u"""编辑内部审批"""
    casename = sys._getframe().f_code.co_name
    expect_result = "审核中"
    organization = "公安局"
    home_phone = "075528560115"
    wechat = "123564456"
    postcode = "518001"
    province = "北京"
    city = "东城区"
    road = "无名路"
    live_years = "5"
    children_description = "这里是子女情况描述"
    contact_names = ["张三", "李四"]
    contact_phones = ["13625648852", "13525648853"]
    relationship = "朋友"
    total_price = "20"
    mj_price = "1"
    zhizhao_name = "YYZZ0001"
    register_no = "1025110001"
    organization_type = "个体工商户"
    register_time = "2012-10-10"
    shareholder_number = "1"
    share_proportion = "100"
    business_isnormal = "无"
    borrower_iscontroler = "是"
    controler_name = fullname
    yingye_mode = "便利店"
    vocation_type = "百货"

    jinglirun = "20"
    fuzhaizonge = "10"
    nianxiaoshoue = "50"
    six_month_sales = "3"
    personnel_number = "5"
    month_pay = "20000"
    water_pay = "1000"
    other_pay = "500"
    transport_pay = "1500"
    capital = "100"
    nianjinglirun = "20"
    should_pay = "50"
    collect = "60"
    liabilities = "10"
    invest = "10"
    property_type = "租赁"
    env_description = "这里是门店经营环境描述"
    store_phone = "57629280"
    store_date = "2016-10-10"
    area = "20"
    shoprent_year = "20000"
    shoprent_starttime = "2017-01-01"
    shoprent_endtime = "2017-05-05"
    store_value = "500000"
    new_old = "很新"
    zhengqi = "整齐"
    store_description = "这里是存货效期描述"
    channel_product = "酒水"
    month_hezuojine = "50000"
    yuqudaoqiyehezuoqishishijian = "2018-04-03"
    supplier = "贵州茅台"
    hezuo_product = "飞天茅台"
    caigouzhanbi = "50"
    zhangqi = "30"
    main_product = "飞天茅台"
    brand = "茅台"
    buyin_price = "1000"
    model = "飞天茅台"
    selling_price = "1500"
    lastmonth_sales = "20000"
    loan_time = "6个月"
    huankuan_type = "等额本息"
    loan_yongtu = "流动资金"

    danbao_type = "其它方式"
    # 商超特有数据
    whitelisttime = "2017-05-05"
    direct_retail = "1"
    custom_name = "客户一"
    jiesuanzhangqi = "30"
    gonghuoliang = "3000"
    product_brand = "耐克"
    product_type = "鞋子"
    dailizizhi = "良好"
    hezuoqixian = "10"
    y_sales_task = "100"
    # 蔬果特有数据
    startoperatetime = "2017-01-01"
    isparking = "否"
    isownfarm = "否"
    isfarmer = "是"
    isotherpurchase = "是"
    twobatch = "1"
    supermarket = "1"
    grouppurch = "1"
    retail = "1"
    fruits_product_name = "荔枝"
    last_six_month_sales = "50000"
    othermode = "这里是其他方式说明"

    # yuqi_cishu = "0"
    zonghe_feilv = "15.00%"

    # self.loanno = "YN010-BP-1808-00012"
    logger.info("开始编辑内部审批")
    logger.info("使用的贷款单号是:" + loanno)
    try:
        web_login.login(webdriver)
        from com.ea.pages.web_inside_page import WebInsidePage
        webinsidepage = WebInsidePage(webdriver)
        web_menu.go_to_inside_approve(webdriver)
        handle1 = webdriver.current_window_handle
        webinsidepage.input_loanno(loanno)
        webinsidepage.click_search_button()
        webinsidepage.click_first_row(loanno)
        handles = webdriver.window_handles
        handle2 = ""
        for handle in handles:
            if handle != handle1:
                webdriver.switch_to.window(handle)
                handle2 = webdriver.current_window_handle
        time.sleep(2)
        webinsidepage.click_editinside_button()
        handles = webdriver.window_handles
        for handle in handles:
            if handle != handle1 and handle != handle2:
                webdriver.switch_to.window(handle)
        # 借款人基本信息
        webinsidepage.click_editborrower_button()
        webinsidepage.input_card_organization(organization)
        webinsidepage.input_home_phone(home_phone)
        webinsidepage.input_wechat(wechat)
        webinsidepage.input_postcode(postcode)
        webinsidepage.select_register_addr_province(province)
        time.sleep(1)
        webinsidepage.select_register_addr_city(city)
        webinsidepage.input_register_addr_road(road)
        webinsidepage.select_sleep_addr_province(province)
        time.sleep(1)
        webinsidepage.select_sleep_addr_city(city)
        webinsidepage.input_sleep_addr_road(road)
        webinsidepage.input_live_years(live_years)
        if marry_status == "已婚":
            webinsidepage.select_marry_date()
        webinsidepage.input_children(children_description)
        webinsidepage.click_borrower_save()
        webinsidepage.click_borrower_confirm()
        time.sleep(3)
        # 配偶基本信息
        if marry_status == "已婚":
            webinsidepage.scroll_to_partner_edit()
            webinsidepage.click_partner_edit()
            webinsidepage.input_card_organization(organization)
            webinsidepage.input_wechat(wechat)
            webinsidepage.select_register_addr_province(province)
            time.sleep(1)
            webinsidepage.select_register_addr_city(city)
            webinsidepage.input_register_addr_road(road)
            webinsidepage.input_work_unit(organization)
            webinsidepage.click_partner_save()
            webinsidepage.click_partner_confirm()
            time.sleep(2)
        # 添加紧急联系人
        webinsidepage.scroll_to_contact()
        time.sleep(1)
        for i in range(2):
            webinsidepage.click_contact_add()
            webinsidepage.input_contact_name(contact_names[i])
            webinsidepage.input_contact_phone(contact_phones[i])
            webinsidepage.select_contacts_relationship(relationship)
            webinsidepage.click_contact_save()
            time.sleep(2)
        time.sleep(2)
        # 夫妻双方负债情况
        webinsidepage.scroll_to_fuqishuangfangfuzhaiqingkuang()
        webinsidepage.click_edit_fuzhai()
        webinsidepage.input_total_price(total_price)
        webinsidepage.input_mj_price(mj_price)
        webinsidepage.click_fuzhai_save()
        time.sleep(1)
        # 经营主体信息
        webinsidepage.scroll_to_jingyingzhuti_edit_button()
        time.sleep(1)
        webinsidepage.click_jingyingzhuti_edit()
        webinsidepage.input_yingyezhizhao_name(zhizhao_name)
        webinsidepage.input_zhucehao(register_no)
        webinsidepage.select_organization_type(organization_type)
        webinsidepage.input_register_time(register_time)
        webinsidepage.select_zhizhao_addr_province(province)
        time.sleep(1)
        webinsidepage.select_zhizhao_addr_city(city)
        webinsidepage.input_zhizhao_addr_road(road)
        webinsidepage.select_office_addr_province(province)
        time.sleep(1)
        webinsidepage.select_office_addr_city(city)
        webinsidepage.input_office_addr_road(road)
        webinsidepage.input_shareholder_number(shareholder_number)
        webinsidepage.input_share_proportion(share_proportion)
        webinsidepage.select_business_isnormal(business_isnormal)
        webinsidepage.select_borrower_iscontroler(borrower_iscontroler)
        webinsidepage.input_controler_name(controler_name)
        webinsidepage.select_yingye_mode(yingye_mode)
        webinsidepage.select_vocation_type(vocation_type)
        webinsidepage.input_start_time(start_time)
        webinsidepage.click_zhuti_submit_button()
        time.sleep(3)
        # 经营历史
        webinsidepage.scroll_to_jingyinglishi()
        webinsidepage.click_history_add()
        webinsidepage.click_years()
        webinsidepage.input_jingli(jinglirun)
        webinsidepage.input_fuzhaizonge(fuzhaizonge)
        webinsidepage.input_nianxiaoshoue(nianxiaoshoue)
        webinsidepage.click_history_save_button()
        time.sleep(2)
        # 近6个月营业额情况
        webinsidepage.scroll_to_jinliugeyueyingyee()
        webinsidepage.click_six_month_edit()
        webinsidepage.input_january(six_month_sales)
        webinsidepage.input_february(six_month_sales)
        webinsidepage.input_march(six_month_sales)
        webinsidepage.input_april(six_month_sales)
        webinsidepage.input_may(six_month_sales)
        webinsidepage.input_june(six_month_sales)
        webinsidepage.click_six_month_submit()
        time.sleep(2)
        # 编辑经营状况
        webinsidepage.scroll_to_jingyingzhuangkuang()
        webinsidepage.click_edit_status()
        webinsidepage.input_personnel_number(personnel_number)
        webinsidepage.input_month_pay(month_pay)
        webinsidepage.input_water_pay(water_pay)
        webinsidepage.input_other_pay(other_pay)
        webinsidepage.input_transport_pay(transport_pay)
        webinsidepage.input_capital(capital)
        webinsidepage.input_nianjinglirun(nianjinglirun)
        webinsidepage.click_bank_water()
        webinsidepage.input_should_pay(should_pay)
        webinsidepage.input_collect(collect)
        webinsidepage.input_liabilities(liabilities)
        webinsidepage.input_invest(invest)
        webinsidepage.click_status_save_button()
        time.sleep(2)
        # 新增门店信息
        webinsidepage.scroll_to_store()
        time.sleep(1)
        webinsidepage.click_store_add_button()
        webinsidepage.select_property_type(property_type)
        webinsidepage.input_env_description(env_description)
        webinsidepage.input_store_phone(store_phone)
        webinsidepage.input_store_date(store_date)
        webinsidepage.select_store_addr_province(province)
        time.sleep(1)
        webinsidepage.select_store_addr_city(city)
        webinsidepage.input_store_addr_road(road)
        webinsidepage.input_business_area(area)
        webinsidepage.input_shoprent_year(shoprent_year)
        webinsidepage.input_shoprent_starttime(shoprent_starttime)
        webinsidepage.input_shoprent_endtime(shoprent_endtime)
        webinsidepage.input_store_value(store_value)
        webinsidepage.select_new_old(new_old)
        webinsidepage.select_zhengqi(zhengqi)
        webinsidepage.input_store_description(store_description)
        webinsidepage.click_store_submit()
        time.sleep(2)
        if loan_type == "流通贷-厂家" or loan_type == "流通贷-经销商" or loan_type == "终端贷":
            # 编辑渠道数据
            webinsidepage.scroll_to_channel()
            webinsidepage.click_channel_edit_button()
            webinsidepage.input_channel_product(channel_product)
            webinsidepage.input_month_hezuojine(month_hezuojine)
            webinsidepage.input_yuqudaoqiyehezuoqishishijian(yuqudaoqiyehezuoqishishijian)
            webinsidepage.click_channel_save_button()
            time.sleep(2)
            # 增加上游信息
            webinsidepage.scroll_to_shangyouxinxi()
            webinsidepage.click_shangyou_add_button()
            webinsidepage.input_supplier(supplier)
            webinsidepage.input_hezuo_product(hezuo_product)
            webinsidepage.input_caigouzhanbi(caigouzhanbi)
            webinsidepage.input_zhangqi(zhangqi)
            webinsidepage.click_shangyou_save_button()
            webinsidepage.click_ok_button()
            time.sleep(2)
            # 增加主要销售产品
            webinsidepage.scroll_to_main_product()
            time.sleep(1)
            webinsidepage.click_main_product_add()
            webinsidepage.input_main_product_name(main_product)
            webinsidepage.input_brand(brand)
            webinsidepage.input_buyin_price(buyin_price)
            webinsidepage.input_model(model)
            webinsidepage.input_selling_price(selling_price)
            webinsidepage.input_lastmonth_sales(lastmonth_sales)
            webinsidepage.click_main_product_save_button()
            webinsidepage.click_ok_button()
            time.sleep(1)
        if loan_type == "流通贷-商超":
            # 编辑渠道数据
            webinsidepage.scroll_to_shangchao_channel()
            webinsidepage.input_whitelisttime(whitelisttime)
            webinsidepage.input_twobatch(twobatch)
            webinsidepage.input_supermarket(supermarket)
            webinsidepage.input_directRetail(direct_retail)
            webinsidepage.input_retail(retail)
            webinsidepage.click_fruits_save_button()
            time.sleep(2)
            # 编辑下游信息
            webinsidepage.scroll_to_shidaxiayoukehujinliuyuegonghuoliang()
            webinsidepage.click_xiayou_add()
            webinsidepage.input_custom_name(custom_name)
            webinsidepage.input_jiesuanzhangqi(jiesuanzhangqi)
            webinsidepage.input_gonghuoliang(gonghuoliang)
            webinsidepage.click_xiayou_save_button()
            webinsidepage.click_ok_button()
            time.sleep(2)
            # 增加主要产品销售情况
            webinsidepage.scroll_to_zhuyaoxiaoshouchanpin()
            webinsidepage.click_shangchao_product_add()
            webinsidepage.input_productBrand(product_brand)
            webinsidepage.input_productType(product_type)
            webinsidepage.input_dailizizhi(dailizizhi)
            webinsidepage.input_hezuoqixian(hezuoqixian)
            webinsidepage.input_y_saleTask(y_sales_task)
            webinsidepage.click_sale_product_save()
            webinsidepage.click_ok_button()
            time.sleep(2)
        if loan_type == "流通贷-蔬果":
            # 编辑渠道数据
            webinsidepage.scroll_to_fruits_channel()
            webinsidepage.input_startoperatetime(startoperatetime)
            webinsidepage.select_isParking(isparking)
            # 编辑上游信息
            webinsidepage.scroll_to_fruits_shangyouxinxi()
            webinsidepage.select_isOwnFarm(isownfarm)
            webinsidepage.select_isFarmer(isfarmer)
            webinsidepage.select_isOtherPurchase(isotherpurchase)
            webinsidepage.select_farme_address_province(province)
            time.sleep(1)
            webinsidepage.select_farme_address_city(city)
            webinsidepage.input_farme_address_road(road)
            webinsidepage.input_othermode(othermode)
            # 编辑下游信息
            webinsidepage.scroll_to_fruits_xiayouxinxi()
            webinsidepage.input_twobatch(twobatch)
            webinsidepage.input_supermarket(supermarket)
            webinsidepage.input_groupPurch(grouppurch)
            webinsidepage.input_retail(retail)
            webinsidepage.click_fruits_save_button()
            time.sleep(1)
            # 增加主要产品销售情况
            webinsidepage.scroll_to_fruits_zhuyaoxiaoshouchanpin()
            webinsidepage.click_fruits_main_product_add()
            webinsidepage.input_fruits_product_name(fruits_product_name)
            webinsidepage.click_fruits_chandi()
            webinsidepage.input_last_six_month_sales(last_six_month_sales)
            webinsidepage.click_fruits_main_product_save()
            time.sleep(1)
        # 编辑调查结论
        webinsidepage.scroll_to_diaochajielun()
        webinsidepage.click_diaochajielun_edit()
        webinsidepage.input_diaochajielun()
        webinsidepage.click_diaochajielun_commit_button()
        # 编辑贷款信息
        webinsidepage.scroll_to_loan_info()
        time.sleep(1)
        webinsidepage.input_year_sales(year_sales)
        webinsidepage.input_lianbao_daikuan_yue(lianbao_daikuan_yue)
        webinsidepage.select_shifou_xindai_jiufen(jiufen)
        # webinsidepage.input_near_24month_yuqi_cishu(yuqi_cishu)
        webinsidepage.select_loan_time(loan_time)
        webinsidepage.select_huankuan_type(huankuan_type)
        webinsidepage.input_eamount(eamount)
        webinsidepage.select_loan_yongtu(loan_yongtu)
        webinsidepage.select_loan_bankname(bank_name)
        webinsidepage.select_zonghe_feilv(zonghe_feilv)
        # insidepage.select_tuijian_type(tuijian_type)
        # insidepage.input_tuijian_name(tuijian_name)
        webinsidepage.select_danbao_type(danbao_type)
        webinsidepage.click_loan_info_save()
        webinsidepage.click_loan_info_confirm()
        webinsidepage.scroll_to_put_photo()
        webinsidepage.click_put_photo()
        webinsidepage.click_photo()
        webinsidepage.click_put_photo_save_button()
        time.sleep(2)
        webdriver.close()
        # 切换到内审详情页面
        webdriver.switch_to.window(handle2)
        webinsidepage.click_submit_inside_approve()
        time.sleep(1)
        # 关闭内审详情页面
        webdriver.close()
        # 切换到内部审批页面
        webdriver.switch_to.window(handle1)
        # 刷新页面
        webdriver.refresh()
        actual_result = webinsidepage.get_result(loanno)
        assert actual_result == expect_result
        logger.info("编辑内部审批结束")
    except Exception as e:
        tools.screenshot(webdriver, screenshot_path, casename)
        raise e


def inside_approve(driver, loan_no, screenshot_path):
    u"""审批内部审批"""
    casename = sys._getframe().f_code.co_name
    logger.info("审批内部审批用例开始")
    logger.info("使用的贷款单号是:" + loan_no)
    # y = None
    approve_view = "OK"
    from com.ea.pages import approve_page
    insideapprovepage = approve_page.InsideApprovePage(driver)
    pubapprovepage = approve_page.ApprovePubPage(driver)
    from com.ea.pages.menu_page import MenuPage
    menupage = MenuPage(driver)
    try:
        current_approver, node_name = tools.get_approver_acount_by_yewuno(loan_no, gl.inside_approve)
        if not current_approver:
            raise Exception
        tools.login(driver, username=current_approver)
        menupage.click_approve_page()
        pubapprovepage.click_todo_first_row(loan_no)
        while current_approver:
            pubapprovepage.click_first_row()
            pubapprovepage.click_my_approve()
            if node_name == "省区终审":
                insideapprovepage.click_my_approve_view()
                insideapprovepage.click_save_button()
                insideapprovepage.click_approve_report()
                insideapprovepage.click_save_button()
                insideapprovepage.click_confirm_button()
            insideapprovepage.input_approve_view(approve_view)
            insideapprovepage.click_pass_button()
            insideapprovepage.click_confirm_button()
            time.sleep(10)
            next_approver, node_name = tools.get_approver_acount_by_yewuno(loan_no, gl.inside_approve)
            if not next_approver:
                break
            if current_approver != next_approver:
                current_approver = next_approver
                driver.start_activity(gl.packagename, gl.login_activity)
                tools.login(driver, username=current_approver)
                menupage.click_approve_page()
                pubapprovepage.click_todo_first_row(loan_no)
        logger.info("审批内部审批用例结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def inside_auto_approve(driver, loanno, screenshot_path):
    u"""审批内部审批"""
    casename = sys._getframe().f_code.co_name
    # self.loanno = 'CQ010-BP-1808-00061'
    try:
        inside_approve(driver, loanno, screenshot_path)
        menupage = menu_page.MenuPage(driver)
        menupage.click_home_page()
        menupage.click_inside_approve()
        from com.ea.pages import inside_page
        insidepage = inside_page.InsidePage(driver)
        actual_result = insidepage.get_status_by_danhao(loanno)
        assert actual_result == "驳回"
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e


def start_inside_apply(driver, loanno, screenshot_path, casename):
    try:
        from com.ea.pages import inside_page
        from com.ea.pages.menu_page import MenuPage
        tools.login(driver, username=gl.xd_manager_account)
        menupage = MenuPage(driver)
        menupage.click_inside_approve()
        insidepage = inside_page.InsidePage(driver)
        insidepage.click_filter_button()
        time.sleep(1)
        insidepage.swipe('up')
        insidepage.input_loanno(loanno)
        insidepage.click_search_button()
        insidepage.click_loan_no(loanno)
        insidepage.click_more_button()
        insidepage.click_start_flow()
        insidepage.click_confirm_text()
        time.sleep(10)
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e
