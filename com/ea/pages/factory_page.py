#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: add_factory_page.py 
@time: 2018/01/19 
"""
from com.ea.common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class FactoryPage(BasePage):
    add_button_loc = (By.XPATH, '//android.widget.TextView[@text="新增"]/..')
    brand_option_loc = (By.XPATH, '//android.widget.TextView[@text="请输入品牌名称"]')
    brand_edit_loc = (By.XPATH, '//android.widget.EditText[@text="请输入品牌名称"]')
    brand_value_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')
    next_button_loc = (By.XPATH, '//android.widget.TextView[@text="下一步"]/..')

    channel_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入渠道名称']")
    channel_shared_loc = (By.XPATH, '//android.widget.TextView[@text="渠道共享:"]/..')
    channel_shared_value_loc = (By.XPATH, '//android.widget.TextView[@text="是"]')
    province_option_loc = (By.XPATH, "//android.widget.TextView[@text='申报省份:']/..")
    province_value_loc = (By.XPATH, "//android.widget.TextView[@text='重庆']/..")

    main_head_loc = (By.XPATH, "//android.widget.EditText[@text='请输入主要负责人']")
    setup_time_loc = (By.XPATH, "//android.widget.EditText[@text='请输入成立时间']")
    setup_time_confirm_loc = (By.XPATH, '//android.widget.TextView[@text="确定"]')
    sale_area_loc = (By.XPATH, "//android.widget.EditText[@text='请输入销售区域']")
    operate_range_loc = (By.XPATH, "//android.widget.EditText[@text='请输入经营范围']")
    phone_loc = (By.XPATH, "//android.widget.EditText[@text='请输入联系电话']")
    jiesuan_fangshi_option_loc = (By.XPATH, "//android.widget.TextView[@text='结算方式']")
    jiesuan_fangshi_select_loc = (By.XPATH, '//android.widget.TextView[@text="结算方式:"]/..')
    jiesuan_fangshi_value_loc = (By.XPATH, '//android.widget.TextView[@text="先款后货"]')
    xiaoshou_jiegou_option_loc = (By.XPATH, '//android.widget.TextView[@text="销售结构"]')
    salesPatternOne_loc = (By.XPATH, "//android.widget.TextView[@text='一级批发商(家):']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    salesPatternTwo_loc = (By.XPATH, "//android.widget.TextView[@text='二级批发商(家):']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    salesPatternTerminal_loc = (By.XPATH, "//android.widget.TextView[@text='销售终端(家):']/following-sibling::android.widget.LinearLayout/android.widget.EditText")
    work_addr_option_loc = (By.XPATH, '//android.widget.TextView[@text="请选择办公地址"]')
    work_addr_info_loc = (By.XPATH, '//android.widget.EditText[@text="请选择区域后输入详细地址"]')
    work_addr_confirm_loc = (By.XPATH, "//android.widget.Button[@text='确定']")

    sales_year_loc = (By.XPATH, "//android.widget.EditText[@text='请输入年销售收入']")
    sales_year_maolilv_loc = (By.XPATH, "//android.widget.EditText[@text='请输入年销售毛利率']")
    loan_object_option_loc = (By.XPATH, "//android.widget.TextView[@text='贷款对象']")
    loan_object_select_loc = (By.XPATH, "//android.widget.TextView[@text='贷款对象:']/..")
    loan_object_value_loc = (By.XPATH, "//android.widget.TextView[@text='一级批发商']")

    buy_back_option_loc = (By.XPATH, '//android.widget.TextView[@text="是否签署回购协议"]')
    buy_back_select_loc = (By.XPATH, '//android.widget.TextView[@text="是否签署回购协议:"]/..')
    buy_back_value_loc = (By.XPATH, '//android.widget.TextView[@text="无"]')

    allow_get_data_option_loc = (By.XPATH, '//android.widget.TextView[@text="该品牌厂家、销售分公司或办事处是否允许怡亚通信贷经理进入其销售管理系统采集相关数据:"]/..')
    allow_get_data_value_loc = (By.XPATH, '//android.widget.TextView[@text="有"]')

    allow_customer_research_loc = (By.XPATH, '//android.widget.TextView[@text="该品牌厂家、销售分公司或办事处是否愿意安排业务经理配合怡亚通信贷经理参与借款客户的调查:"]/..')
    allow_customer_research_value_loc = (By.XPATH, '//android.widget.TextView[@text="有"]')

    zhengshi_jiaoyi_pinzheng_option_loc = (By.XPATH, '//android.widget.TextView[@text="该品牌厂家、销售分公司或办事处可提供给怡亚通证实客户真实交易的凭证"]/..')
    zhengshi_jiaoyi_pinzheng_value_loc = (By.XPATH, '//android.widget.CheckBox[@text="购销合同"]')

    danbao_fangshi_option_loc = (By.XPATH, '//android.widget.TextView[@text="担保方式"]')
    danbao_fangshi_select_loc = (By.XPATH, '//android.widget.TextView[@text="担保方式:"]')
    danbao_fangshi_value_loc = (By.XPATH, '//android.widget.TextView[@text="无"]')
    save_button_loc = (By.XPATH, '//android.widget.TextView[@text="保存"]')

    fujian_info_loc = (By.XPATH, '//android.widget.TextView[@text="附件信息"]')
    hezuofang_shenqing_baogao_loc = (By.XPATH, '//android.widget.TextView[@text="合作方申请报告"]')
    upload_button_loc = (By.XPATH, '//android.widget.TextView[@text="上传"]')
    shangmen_yingxiao_zhaopian_loc = (By.XPATH, '//android.widget.TextView[@text="上门营销照片"]')
    changjia_zhengming_wenjian_loc = (By.XPATH, '//android.widget.TextView[@text="厂家证明文件"]')
    more_buttion_loc = (By.XPATH, '//android.widget.TextView[@text="厂家合作方管理"]/../following-sibling::android.widget.RelativeLayout')
    start_flow_loc = (By.XPATH, '//android.widget.CheckedTextView[@text="发起流程"]')
    start_flow_confirm_loc = (By.XPATH, '//android.widget.TextView[@text="确定"]')

    from_paizhao_loc = (By.XPATH, '//android.widget.TextView[@text="拍照"]')
    kuaimen_loc = (By.XPATH, '//GLButton[@text="快门"]')
    paizhao_confirm_loc = (By.ID, 'com.sec.android.app.camera:id/okay')

    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    def click_brand_option(self):
        self.find_element(*self.brand_option_loc).click()

    def input_brand_edit(self, brand_name):
        self.send_keys(self.brand_edit_loc, brand_name)

    def click_brand_name(self):
        self.find_element(*self.brand_value_loc).click()

    def click_next_button(self):
        self.find_element(*self.next_button_loc).click()

    def input_channel_name(self, channel_name):
        self.send_keys(self.channel_name_loc, channel_name)

    def click_channel_shared_option(self):
        self.find_element(*self.channel_shared_loc).click()

    def click_channel_shared_value(self):
        self.find_element(*self.channel_shared_value_loc).click()

    def click_province_option(self):
        self.find_element(*self.province_option_loc).click()

    def click_province_value(self):
        self.find_element(*self.province_value_loc).click()

    def input_main_head(self, main_head):
        self.send_keys(self.main_head_loc, main_head)

    def click_setup_time_option(self):
        self.find_element(*self.setup_time_loc).click()

    def click_setup_time_confirm(self):
        self.find_element(*self.setup_time_confirm_loc).click()

    def input_sales_area(self, sales_area):
        self.send_keys(self.sale_area_loc, sales_area)

    def input_operate_range(self, operate_range):
        self.send_keys(self.operate_range_loc, operate_range)

    def input_phone(self, phone):
        self.send_keys(self.phone_loc, phone)

    def click_jiesuan_fangshi_option(self):
        self.find_element(*self.jiesuan_fangshi_option_loc).click()

    def click_jiesuan_fangshi_select(self):
        self.find_element(*self.jiesuan_fangshi_select_loc).click()

    def click_jiesuan_fangshi_value(self):
        self.find_element(*self.jiesuan_fangshi_value_loc).click()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()

    def click_xiaoshou_jiegou_option(self):
        self.find_element(*self.xiaoshou_jiegou_option_loc).click()

    def input_salesPatternOne(self, one):
        self.send_keys(self.salesPatternOne_loc, one)

    def input_salesPatternTwo(self, two):
        self.send_keys(self.salesPatternTwo_loc, two)

    def input_salesPatternTerminal(self, terminal):
        self.send_keys(self.salesPatternTerminal_loc, terminal)

    def click_work_addr_option(self):
        self.find_element(*self.work_addr_option_loc).click()

    def input_work_addr_info(self, addr_info):
        self.send_keys(self.work_addr_info_loc, addr_info)

    def click_work_addr_confirm(self):
        self.find_element(*self.work_addr_confirm_loc).click()

    def input_sales_year(self, sales_year):
        self.send_keys(self.sales_year_loc, sales_year)

    def input_year_maolilv(self, sales_year_maolilv):
        self.send_keys(self.sales_year_maolilv_loc, sales_year_maolilv)

    def click_loan_object_option(self):
        self.find_element(*self.loan_object_option_loc).click()

    def click_loan_object_select(self):
        self.find_element(*self.loan_object_select_loc).click()

    def click_loan_object_value(self):
        self.find_element(*self.loan_object_value_loc).click()

    def click_buy_back_option(self):
        self.find_element(*self.buy_back_option_loc).click()

    def click_buy_back_select(self):
        self.find_element(*self.buy_back_select_loc).click()

    def click_buy_back_value(self):
        self.find_element(*self.buy_back_value_loc).click()

    def click_allow_get_data_option(self):
        self.find_element(*self.allow_get_data_option_loc).click()

    def click_allow_get_data_value(self):
        self.find_element(*self.allow_get_data_value_loc).click()

    def click_allow_customer_research_option(self):
        self.find_element(*self.allow_customer_research_loc).click()

    def click_allow_customer_research_value(self):
        self.find_element(*self.allow_customer_research_value_loc).click()

    def click_zhenshi_jiaoyi_pinzheng_option(self):
        self.find_element(*self.zhengshi_jiaoyi_pinzheng_option_loc).click()

    def click_zhenshi_jiaoyi_pinzheng_value(self):
        self.find_element(*self.zhengshi_jiaoyi_pinzheng_value_loc).click()

    def click_danbao_fangshi_option(self):
        self.find_element(*self.danbao_fangshi_option_loc).click()

    def click_danbao_fangshi_select(self):
        self.find_element(*self.danbao_fangshi_select_loc).click()

    def clcik_danbao_fangshi_value(self):
        self.find_element(*self.danbao_fangshi_value_loc).click()

    def click_channel_name(self, channel_name):
        self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + channel_name + '"]')).click()

    def get_yewuno(self, channel_name):
        return self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + channel_name + '"]/../../../..//android.widget.TextView[@text="申报单号:"]/following-sibling::android.widget.TextView')).text

    def click_fujian_info(self):
        self.find_element(*self.fujian_info_loc).click()

    def click_hezuofang_shenqing_baogao(self):
        self.find_element(*self.hezuofang_shenqing_baogao_loc).click()

    def click_upload(self):
        self.find_element(*self.upload_button_loc).click()

    def click_paizhao(self):
        self.find_element(*self.from_paizhao_loc).click()

    def click_kuaimen(self):
        self.find_element(*self.kuaimen_loc).click()

    def click_paizhao_confirm(self):
        self.find_element(*self.paizhao_confirm_loc).click()

    def click_shangmen_yingxiao_zhaopian(self):
        self.find_element(*self.shangmen_yingxiao_zhaopian_loc).click()

    def click_changjia_zhengming_wenjian(self):
        self.find_element(*self.changjia_zhengming_wenjian_loc).click()

    def click_more_button(self):
        self.find_element(*self.more_buttion_loc).click()

    def click_start_flow(self):
        self.find_element(*self.start_flow_loc).click()

    def click_start_flow_confirm(self):
        self.find_element(*self.start_flow_confirm_loc).click()
