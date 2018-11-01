#!usr/bin/env python  
# -- coding:utf-8 --
""" 
@author:user 
@file: base_page.py 
@time: 2017/12/05 
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.ea.common import log
from selenium.webdriver.support.select import Select

'''
project:封装页面公用方法
'''


class SeleniumBasePage(object):
    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        # self.url = base_url
        # self.title = page_title
        self.mylog = log.log()

    #   打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            # self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert page_title in self.driver.title
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + url)
            raise e

    # 重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            self.mylog.error(u'找不到元素:' + str(loc))
            raise e

    # 重写find_elements方法，增加定位元素的健壮性
    def find_elements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            self.mylog.error(u'找不到元素:' + str(loc))

    # 重写send_keys方法
    def send_keys(self, loc, value, clear=True, click=True):
        try:
            if click:
                self.find_element(*loc).click()
            if clear:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            self.mylog.error(u'输入失败,loc=' + str(loc) + u';value=' + value)
            raise e

    # 重写switch_frame方法
    def switch_frame(self, *loc):
        return self.driver.switch_to.frame(self.find_element(*loc))

    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, *loc):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*loc))
        except Exception as e:
            raise e

    def scroll_to_element(self, *loc):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*loc))
        except Exception as e:
            raise e

    def page_down(self):
        # 拉动滚动条到最后
        try:
            js = "var q=document.documentElement.scrollTop=1000000"
            self.driver.execute_script(js)
        except Exception as e:
            raise e

    # 重写select方法
    def select_widget(self, els, *loc):
        try:
            select = Select(self.find_element(*loc))
            if isinstance(els, str):
                select.select_by_visible_text(els)
            else:
                select.select_by_index(els)
        except Exception as e:
            raise e

    def click_date_time(self, loc, iframe, datetime):
        try:
            self.find_element(*loc).click()
            self.switch_frame(*iframe)
            self.find_element(*datetime).click()
            self.switch_to_default()
        except Exception as e:
            raise e

    def input_date_time(self, el_name, date, click=False, clear=True):
        js = "$('input[name=" + el_name[1] + "]').removeAttr('readonly')"
        self.driver.execute_script(js)
        # self.find_element(*el_name).send_keys(date)
        self.send_keys(el_name, date, click=click, clear=clear)
