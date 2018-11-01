#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class LoanCode(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateS')
    loan_date_end_loc = (By.NAME, 'loanDateE')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="贷款单放款台帐报表"]')

    count_loc = (By.CSS_SELECTOR, 'div.searchPage>span')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_count(self):
        tmp = self.find_element(*self.count_loc).text
        return ''.join(list(filter(str.isdigit, tmp.split("|")[1])))


class LiutongdaiPage(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="搜索"]')
    menu_url_loc = (By.XPATH, '//a[text()="流通贷放款台账查询"]')

    loan_count_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_loan_date_start(self, start_date):
        self.input_date_time(self.loan_date_start_loc, start_date)

    def input_loan_date_end(self, end_date):
        self.input_date_time(self.loan_date_end_loc, end_date)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_loan_count(self):
        return self.find_element(*self.loan_count_loc).text
