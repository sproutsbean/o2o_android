#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: login_page.py 
@time: 2018/02/26 
"""

from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By
from com.ea.common import tools
import os
from com.ea.resource import globalparameter as gl


class LoginPage(BasePage):
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    username_loc = (By.XPATH, "//android.widget.LinearLayout/android.widget.EditText")
    passwd_loc = (By.XPATH, "//android.widget.RelativeLayout/android.widget.EditText")
    login_button_loc = (By.XPATH, "//android.widget.Button[@text='登录']")
    permission_loc = (By.ID, "com.android.packageinstaller:id/permission_allow_button")

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, username, clear=True)
        # self.set_value(self.username_loc, username)

    def input_passwd(self, passwd):
        """输入密码"""
        self.send_keys(self.passwd_loc, passwd, clear=True)
        # self.set_value(self.passwd_loc, passwd)

    def click_login_button(self):
        """点击登录按钮"""
        self.find_element(*self.login_button_loc).click()

    def click_allow_button(self):
        """点击允许按钮"""
        self.find_element(*self.permission_loc).click()

    def username_have_value(self):
        u"""判断用户名是否有值"""
        try:
            text = self.find_element(*self.username_loc).text
            if text == '用户名':
                return False
            return True
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, "login")
            raise e

    def get_username(self):
        u"""获取用户名"""
        return self.find_element(*self.username_loc).text
