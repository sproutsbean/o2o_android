#!usr/bin/env python
# -*- coding:utf-8 -*-

from com.ea.common.web_base_page import BasePage
from selenium.webdriver.common.by import By


class LoanAmountByDayByManager(BasePage):
    day_loc = (By.NAME, 'statisticDate')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按天统计放款量"]/following-sibling::ul//a[text()="按信贷经理统计放款量"]')

    yesterday_newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')
    yesterday_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(9)>div')
    newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(10)>div')
    loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(11)>div')
    pre_month_newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(12)>div')
    pre_month_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(13)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_day(self, day):
        self.input_date_time(self.day_loc, day)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_yesterday_newcustomer_loanamount(self):
        return self.find_element(*self.yesterday_newcustomer_loanamount_loc).text

    def get_yesterday_loanamount(self):
        return self.find_element(*self.yesterday_loanamount_loc).text

    def get_newcustomer_loanamount(self):
        return self.find_element(*self.newcustomer_loanamount_loc).text

    def get_loanamount(self):
        return self.find_element(*self.loanamount_loc).text

    def get_pre_month_newcustomer_loanamount(self):
        return self.find_element(*self.pre_month_newcustomer_loanamount_loc).text

    def get_pre_month_loanamount(self):
        return self.find_element(*self.pre_month_loanamount_loc).text


class LoanAmountByDayByTeam(BasePage):
    day_loc = (By.NAME, 'statisticDate')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按天统计放款量"]/following-sibling::ul//a[text()="按团队统计放款量"]')

    yesterday_team_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')
    team_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(9)>div')
    team_newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(10)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_day(self, day):
        self.input_date_time(self.day_loc, day)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_yesterday_team_loanamount(self):
        return self.find_element(*self.yesterday_team_loanamount_loc).text

    def get_team_loanamount(self):
        return self.find_element(*self.team_loanamount_loc).text

    def get_team_newcustomer_loanamount(self):
        return self.find_element(*self.team_newcustomer_loanamount_loc).text


class LoanAmountByDayByProvince(BasePage):
    day_loc = (By.NAME, 'statisticDate')
    search_button_loc = (By.CSS_SELECTOR, 'input[value="查询"]')
    menu_url_loc = (By.XPATH, '//a[text()="按天统计放款量"]/following-sibling::ul//a[text()="按省区统计放款量"]')

    yesterday_newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(3)>div')
    yesterday_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(4)>div')
    newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(5)>div')
    loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(6)>div')
    pre_month_newcustomer_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(7)>div')
    pre_month_loanamount_loc = (By.CSS_SELECTOR, 'thead+tbody tr:last-of-type td:nth-child(8)>div')

    def get_url(self):
        return self.find_elements(*self.menu_url_loc)[0].get_attribute('href')

    def input_day(self, day):
        self.input_date_time(self.day_loc, day)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def get_yesterday_newcustomer_loanamount(self):
        return self.find_element(*self.yesterday_newcustomer_loanamount_loc).text

    def get_yesterday_loanamount(self):
        return self.find_element(*self.yesterday_loanamount_loc).text

    def get_newcustomer_loanamount(self):
        return self.find_element(*self.newcustomer_loanamount_loc).text

    def get_loanamount(self):
        return self.find_element(*self.loanamount_loc).text

    def get_pre_month_newcustomer_loanamount(self):
        return self.find_element(*self.pre_month_newcustomer_loanamount_loc).text

    def get_pre_month_loanamount(self):
        return self.find_element(*self.pre_month_loanamount_loc).text
