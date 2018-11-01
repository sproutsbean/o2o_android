#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class OverdueDetailPage(BasePage):
    province_loc = (By.ID, 'province')
    kaohe_month_loc = (By.NAME, 'month')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="逾期明细表"]')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def select_province(self, province):
        self.select_widget(province, *self.province_loc)

    def input_kaohe_month(self, kaohe_month):
        self.driver.execute_script("document.getElementById('month').value='" + kaohe_month + "'")
        # self.input_date_time(self.kaohe_month_loc, kaohe_month)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_kaohe_month(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(1)')).text

    def get_province(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(2)')).text

    def get_danhao(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(3)')).text

    def get_borrower_name(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(4)')).text

    def get_jinbanren_name(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(5)')).text

    def get_fangkuan_jine(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(6)>div')).text

    def get_fangkuan_qixian(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(7)>div')).text

    def get_fangkuan_shijian(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(8)')).text

    def get_yuqi_shijian(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(9)')).text

    def get_yuqi_benjin(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(10)>div')).text

    def get_yuqi_lixi(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(11)>div')).text

    def get_yuqi_leixing(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(12)')).text

    def get_yuqi_faxi(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(13)>div')).text

    def get_yuqi_zonge(self):
        return self.find_element(*(By.CSS_SELECTOR, 'div[id="o2o_result"] tbody>tr>td:nth-child(14)>div')).text
