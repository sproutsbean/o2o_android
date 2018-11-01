#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class LoanAprroveByAgencies(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="贷款审批经办机构统计"]')

    xinzeng_zhengxin_tibao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    zhengxin_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    neishen_xintijiao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')
    neishen_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')
    yinhang_songshen_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')

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

    def get_xinzeng_zhengxin_tibao(self):
        return self.find_element(*self.xinzeng_zhengxin_tibao_loc).text

    def get_zhengxin_jieshu_xinzeng(self):
        return self.find_element(*self.zhengxin_jieshu_xinzeng_loc).text

    def get_neishen_xintijiao(self):
        return self.find_element(*self.neishen_xintijiao_loc).text

    def get_neishen_jieshu_xinzeng(self):
        return self.find_element(*self.neishen_jieshu_xinzeng_loc).text

    def get_yinhang_songshen_xinzeng(self):
        return self.find_element(*self.yinhang_songshen_xinzeng_loc).text


class LoanAprroveByManager(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="贷款审批贷前信贷经理统计"]')

    xinzeng_zhengxin_tibao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')
    zhengxin_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')
    neishen_xintijiao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')
    neishen_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(9)>div')
    yinhang_songshen_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(10)>div')

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

    def get_xinzeng_zhengxin_tibao(self):
        return self.find_element(*self.xinzeng_zhengxin_tibao_loc).text

    def get_zhengxin_jieshu_xinzeng(self):
        return self.find_element(*self.zhengxin_jieshu_xinzeng_loc).text

    def get_neishen_xintijiao(self):
        return self.find_element(*self.neishen_xintijiao_loc).text

    def get_neishen_jieshu_xinzeng(self):
        return self.find_element(*self.neishen_jieshu_xinzeng_loc).text

    def get_yinhang_songshen_xinzeng(self):
        return self.find_element(*self.yinhang_songshen_xinzeng_loc).text


class LoanAprroveByProvince(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="贷款审批省区统计"]')

    xinzeng_zhengxin_tibao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(3)>div')
    zhengxin_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    neishen_xintijiao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    neishen_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')
    yinhang_songshen_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')

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

    def get_xinzeng_zhengxin_tibao(self):
        return self.find_element(*self.xinzeng_zhengxin_tibao_loc).text

    def get_zhengxin_jieshu_xinzeng(self):
        return self.find_element(*self.zhengxin_jieshu_xinzeng_loc).text

    def get_neishen_xintijiao(self):
        return self.find_element(*self.neishen_xintijiao_loc).text

    def get_neishen_jieshu_xinzeng(self):
        return self.find_element(*self.neishen_jieshu_xinzeng_loc).text

    def get_yinhang_songshen_xinzeng(self):
        return self.find_element(*self.yinhang_songshen_xinzeng_loc).text


class LoanAprroveByBank(BasePage):
    loan_date_start_loc = (By.NAME, 'loanDateStart')
    loan_date_end_loc = (By.NAME, 'loanDateEnd')
    province_loc = (By.NAME, 'province')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="贷款审批银行统计"]')

    xinzeng_zhengxin_tibao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(3)>div')
    zhengxin_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    neishen_xintijiao_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    neishen_jieshu_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')
    yinhang_songshen_xinzeng_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')

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

    def get_xinzeng_zhengxin_tibao(self):
        return self.find_element(*self.xinzeng_zhengxin_tibao_loc).text

    def get_zhengxin_jieshu_xinzeng(self):
        return self.find_element(*self.zhengxin_jieshu_xinzeng_loc).text

    def get_neishen_xintijiao(self):
        return self.find_element(*self.neishen_xintijiao_loc).text

    def get_neishen_jieshu_xinzeng(self):
        return self.find_element(*self.neishen_jieshu_xinzeng_loc).text

    def get_yinhang_songshen_xinzeng(self):
        return self.find_element(*self.yinhang_songshen_xinzeng_loc).text
