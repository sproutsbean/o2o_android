#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class LoanBalanceByAgencies(BasePage):
    search_button_loc = (By.CSS_SELECTOR, 'input[value="搜索"]')
    menu_url_loc = (By.XPATH, '//a[text()="按经办机构统计"]')

    fangkuan_jine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    bank_zhengchang_daikuan_yue_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    bank_yuqi_daikuan_yue_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')
    daichang_daikuan_jine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')
    daichang_daikuan_qianhuan_yue_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_day(self, day):
        self.driver.execute_script("document.getElementById('selectDate').value='" + day + "'")

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_fangkuan_jine(self):
        return self.find_element(*self.fangkuan_jine_loc).text

    def get_bank_zhengchang_daikuan_yue(self):
        return self.find_element(*self.bank_zhengchang_daikuan_yue_loc).text

    def get_bank_yuqi_daikuan_yue(self):
        return self.find_element(*self.bank_yuqi_daikuan_yue_loc).text

    def get_daichang_daikuan_jine(self):
        return self.find_element(*self.daichang_daikuan_jine_loc).text

    def get_daichang_daikuan_qianhuan_yue(self):
        return self.find_element(*self.daichang_daikuan_qianhuan_yue_loc).text
