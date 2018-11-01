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


class DealerPage(BasePage):
    fenlei_loc = (By.ID, "batchClassification")
    next_button_loc = (By.CSS_SELECTOR, "input[value='下一步']")
    province_loc = (By.ID, "orgProvinceId")
    xiaoshouliantiaojiegou_loc = (By.NAME, "salesChainStructure")
    businessLicenseName_loc = (By.ID, "businessLicenseName")
    businessLicenseNo_loc = (By.ID, "businessLicenseNo")
    corporationName_loc = (By.ID, "corporationName")
    foundingTime_loc = (By.NAME, "foundingTime")
    registeredCapital_loc = (By.ID, "registeredCapital")
    manageProvince_loc = (By.NAME, "manageProvince")
    manageArea_loc = (By.NAME, "manageArea")
    manageDetail_loc = (By.NAME, "manageDetail")
    warehouseArea_loc = (By.ID, "warehouseArea")
    transportVehiclesNum_loc = (By.ID, "transportVehiclesNum")
    brandCooperationTerm_loc = (By.ID, "brandCooperationTerm")
    otherBrandNum_loc = (By.ID, "otherBrandNum")
    brandLicensingDeadline_loc = (By.ID, "brandLicensingDeadline")
    agencyOtherBrand_loc = (By.ID, "agencyOtherBrand")
    downstreamTwoPattern_loc = (By.ID, "downstreamTwoPattern")
    annualSales_loc = (By.ID, "annualSales")
    brandLicensingArea_loc = (By.XPATH, "//label[text()='省级代理']")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保 存']")

    start_flow_loc = (By.XPATH, "//a[starts-with(@href,'/jxsPartner/rest/jxsStartFlow') and text()='发起流程']")
    upload_report_loc = (By.XPATH, "//div[text()='上传合作方申请报告']/following-sibling::div/input")
    upload_marketing_photo_loc = (By.XPATH, "//div[text()='上传上门营销照片']/following-sibling::div/input")
    upload_factory_prove_file_loc = (By.XPATH, "//div[text()='上传厂家证明文件']/following-sibling::div/input")

    def click_add_dealer(self, brand_no):
        u"""点击添加经销商合作方"""
        add_factory_loc = (By.XPATH, "//td[text()='" + brand_no + "']/following-sibling::td[5]/a[text()='添加经销商合作方']")
        self.find_element(*add_factory_loc).click()

    def select_fenlei(self, isloan):
        u"""点击添加经销商合作方"""
        self.select_widget(isloan, *self.fenlei_loc)

    def click_next_button(self):
        u"""点击下一步按钮"""
        self.find_element(*self.next_button_loc).click()

    def select_province(self, province):
        u"""选择申报省份"""
        self.select_widget(province, *self.province_loc)

    def input_xiaoshouliantiaojiegou(self, xiaoshouliantiaojiegou):
        u"""输入销售链条结构"""
        self.send_keys(self.xiaoshouliantiaojiegou_loc, xiaoshouliantiaojiegou)

    def input_businessLicenseName(self, businessLicenseName):
        u"""输入营业执照名称"""
        self.send_keys(self.businessLicenseName_loc, businessLicenseName)

    def input_businessLicenseNo(self, businessLicenseNo):
        u"""输入营业执照号"""
        self.send_keys(self.businessLicenseNo_loc, businessLicenseNo)

    def input_law_name(self, law_name):
        u"""输入法人代表姓名"""
        self.send_keys(self.corporationName_loc, law_name)

    def input_setup_time(self, setup_time):
        u"""输入成立时间"""
        self.input_date_time(self.foundingTime_loc, setup_time)

    def input_registeredCapital(self, registeredCapital):
        u"""输入注册资本"""
        self.send_keys(self.registeredCapital_loc, registeredCapital)

    def select_manage_province(self, manage_province):
        u"""输入经营地址省份"""
        self.select_widget(manage_province, *self.manageProvince_loc)

    def select_manage_area(self, manage_area):
        u"""输入经营地址市"""
        self.select_widget(manage_area, *self.manageArea_loc)

    def input_manage_detail(self, manage_detail):
        u"""输入经营详细地址"""
        self.send_keys(self.manageDetail_loc, manage_detail)

    def input_warehouseArea(self, warehouseArea):
        u"""输入仓库面积"""
        self.send_keys(self.warehouseArea_loc, warehouseArea)

    def input_transportVehiclesNum(self, transportVehiclesNum):
        u"""输入运输车辆数"""
        self.send_keys(self.transportVehiclesNum_loc, transportVehiclesNum)

    def input_brandCooperationTerm(self, brandCooperationTerm):
        u"""输入与品牌合作时长"""
        self.send_keys(self.brandCooperationTerm_loc, brandCooperationTerm)

    def input_otherBrandNum(self, otherBrandNum):
        u"""输入代理其他品牌数"""
        self.send_keys(self.otherBrandNum_loc, otherBrandNum)

    def input_brandLicensingDeadline(self, brandLicensingDeadline):
        u"""输入品牌授权期限"""
        self.send_keys(self.brandLicensingDeadline_loc, brandLicensingDeadline)

    def input_agencyOtherBrand(self, agencyOtherBrand):
        u"""输入代理的其他3大品牌"""
        self.send_keys(self.agencyOtherBrand_loc, agencyOtherBrand)

    def input_downstreamTwoPattern(self, downstreamTwoPattern):
        u"""输入本一批商下游二批商数量"""
        self.send_keys(self.downstreamTwoPattern_loc, downstreamTwoPattern)

    def input_annualSales(self, annualSales):
        u"""输入年销售额"""
        self.send_keys(self.annualSales_loc, annualSales)

    def click_brandLicensingArea(self):
        u"""点击省级代理"""
        self.find_element(*self.brandLicensingArea_loc).click()

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(2)

    def scroll_to_save_button(self):
        u"""拖动页面到保存按钮位置"""
        self.scroll_to_element(*self.save_button_loc)

    def scroll_to_start_flow(self):
        u"""拖动页面到发起流程位置"""
        self.scroll_to_element(*self.start_flow_loc)
        time.sleep(1)

    def click_start_flow(self):
        u"""点击发起流程按钮"""
        self.find_element(*self.start_flow_loc).click()
        time.sleep(2)

    def scroll_to_edit(self, business_license_name):
        u"""拖动页面到编辑位置"""
        edit_loc = (By.XPATH, "//td[text()='" + business_license_name + "']/following-sibling::td[6]/a[text()='编辑']")
        self.scroll_to_element(*edit_loc)
        time.sleep(1)

    def click_edit(self, business_license_name):
        u"""根据渠道名称点击编辑按钮"""
        edit_loc = (By.XPATH, "//td[text()='" + business_license_name + "']/following-sibling::td[6]/a[text()='编辑']")
        self.find_element(*edit_loc).click()
        time.sleep(1)

    def input_upload_report(self, file):
        u"""上传合作方申请报告"""
        self.find_element(*self.upload_report_loc).send_keys(file)
        time.sleep(1)

    def input_upload_marketing_photo(self, file):
        u"""上传合作方申请报告"""
        self.find_element(*self.upload_marketing_photo_loc).send_keys(file)
        time.sleep(1)

    def input_upload_factory_prove_file(self, file):
        u"""上传合作方申请报告"""
        self.find_element(*self.upload_factory_prove_file_loc).send_keys(file)
        time.sleep(1)

    def get_result(self, channel_name):
        u"""获取结果"""
        result_loc = (By.XPATH, "//td[text()='" + channel_name + "']/following-sibling::td[5]/div")
        return self.find_element(*result_loc).text

    def get_yewuno(self, channel_name):
        u"""获取申报单号"""
        yewuno_loc = (By.XPATH, "//td[text()='" + channel_name + "']/preceding-sibling::td[1]/a")
        return self.find_element(*yewuno_loc).text
