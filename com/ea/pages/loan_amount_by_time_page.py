#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class LoanAmountByManager(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按信贷经理统计放款量"]')

    fangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')
    fangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(9)>div')
    xinkehufangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(10)>div')
    xinkehufangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(11)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def select_province(self, province):
        self.select_widget(province, *self.province_loc)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_fangkuanzongbishu(self):
        return self.find_element(*self.fangkuanzongbishu_loc).text

    def get_fangkuanzongjine(self):
        return self.find_element(*self.fangkuanzongjine_loc).text

    def get_xinkehufangkuanzongbishu(self):
        return self.find_element(*self.xinkehufangkuanzongbishu_loc).text

    def get_xinkehufangkuanzongjine(self):
        return self.find_element(*self.xinkehufangkuanzongjine_loc).text


class LoanAmountByTeam(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按团队统计放款量"]')

    tuanduifangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')
    tuanduifangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')
    xinkehufangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(9)>div')
    xinkehufangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(10)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def select_province(self, province):
        self.select_widget(province, *self.province_loc)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_tuanduifangkuanzongbishu(self):
        return self.find_element(*self.tuanduifangkuanzongbishu_loc).text

    def get_tuanduifangkuanzongjine(self):
        return self.find_element(*self.tuanduifangkuanzongjine_loc).text

    def get_xinkehufangkuanzongbishu(self):
        return self.find_element(*self.xinkehufangkuanzongbishu_loc).text

    def get_xinkehufangkuanzongjine(self):
        return self.find_element(*self.xinkehufangkuanzongjine_loc).text


class LoanAmountByProvince(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按省区统计放款量"]')

    fangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(3)>div')
    fangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    xinkehufangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    xinkehufangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def select_province(self, province):
        self.select_widget(province, *self.province_loc)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_fangkuanzongbishu(self):
        return self.find_element(*self.fangkuanzongbishu_loc).text

    def get_fangkuanzongjine(self):
        return self.find_element(*self.fangkuanzongjine_loc).text

    def get_xinkehufangkuanzongbishu(self):
        return self.find_element(*self.xinkehufangkuanzongbishu_loc).text

    def get_xinkehufangkuanzongjine(self):
        return self.find_element(*self.xinkehufangkuanzongjine_loc).text


class LoanAmountByBank(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按放款银行统计放款量"]')

    fangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(3)>div')
    fangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    xinkehufangkuanzongbishu_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    xinkehufangkuanzongjine_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def select_province(self, province):
        self.select_widget(province, *self.province_loc)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_fangkuanzongbishu(self):
        return self.find_element(*self.fangkuanzongbishu_loc).text

    def get_fangkuanzongjine(self):
        return self.find_element(*self.fangkuanzongjine_loc).text

    def get_xinkehufangkuanzongbishu(self):
        return self.find_element(*self.xinkehufangkuanzongbishu_loc).text

    def get_xinkehufangkuanzongjine(self):
        return self.find_element(*self.xinkehufangkuanzongjine_loc).text
