#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class AfterLoan(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="业务运营分析（贷后数据）"]')

    apply_amount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(9)>div')
    approve_amount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(10)>div')
    fangkuan_amount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(11)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_apply_amount(self):
        return self.find_element(*self.apply_amount_loc).text

    def get_approve_amount(self):
        return self.find_element(*self.approve_amount_loc).text

    def get_fangkuan_amount(self):
        return self.find_element(*self.fangkuan_amount_loc).text


class BeforeLoan(BasePage):
    loan_date_start_loc = (By.NAME, 'createDateStart')
    loan_date_end_loc = (By.NAME, 'createDateEnd')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="业务运营分析（贷前数据）"]')

    apply_amount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(14)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_apply_amount(self):
        return self.find_element(*self.apply_amount_loc).text
