#!usr/bin/env python  
# -- coding:utf-8 --
""" 
@author:user 
@file: base_page.py 
@time: 2017/12/05 
"""

from appium.webdriver.webdriver import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from appium.common import exceptions as EC
from com.ea.common import log
import subprocess
import time
import os

'''
project:封装页面公用方法
'''


class BasePage(object):
    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.url = base_url
        # self.title = page_title
        self.mylog = log.log()

    # #   打开页面,并校验链接是否加载正确
    # def _open(self, url, page_title):
    #     try:
    #         self.driver.get(url)
    #         # self.driver.maximize_window()
    #         # 通过断言输入的title是否在当前title中
    #         assert page_title in self.driver.title
    #     except Exception as e:
    #         self.mylog.error(u'未能正确打开页面:' + url)
    #         raise e

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

    # 重写set_value
    def set_value(self, loc, value, clear=False):
        if clear:
            self.find_element(*loc).clear()
        self.driver.set_value(self.find_element(*loc), value)

    # 重写send_keys方法
    def send_keys(self, loc, value, clear=True, click=True):
        try:
            el = self.find_element(*loc)
            if click:
                el.click()
            if clear:
                el.clear()
            el.send_keys(value)
        except AttributeError as e:
            self.mylog.error(u'输入失败,loc=' + str(loc) + u';value=' + value)
            raise e

    # 快速输入法(试验失败)
    def input_keys(self, element, st):
        print('开始执行clear')
        self.find_element(*element).clear()
        print('clear结束')
        print('开始执行click')
        self.find_element(*element).click()
        print('click结束')
        print('开始执行输入')
        subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg %s' % st, shell=True)
        print('输入结束')

    def drag_and_drop(self, origin_el, destination_el):
        self.driver.drag_and_drop(self.find_element(*origin_el), self.find_element(*destination_el))

    # 重写swipe方法
    def swipe(self, direction):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if direction == "up":
            self.driver.swipe(x / 2, y * 2 / 5, x / 2, y / 5, 200)
        elif direction == "down":
            self.driver.swipe(x / 2, y / 5, x / 2, y * 2 / 5, 200)
        elif direction == "right":
            self.driver.swipe(x / 2, y / 2, x, y / 2, 200)
        elif direction == "left":
            self.driver.swipe(x, y / 2, x / 2, y / 2, 200)

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

    def back(self):
        self.driver.back()
