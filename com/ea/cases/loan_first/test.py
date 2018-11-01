#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:user
@file: test_zhongduandai_changjia.py
@time: 2018/03/05
"""
from com.ea.common import tools
from com.ea.common.base_page import BasePage
from selenium.webdriver.common.by import By
from com.ea.common.cardname import cardname
from com.ea.common.cardnumber import IdCardNumber
import unittest
import time
import os
import sys
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_page import MenuPage
from com.ea.pages import approve_page
from com.ea.common import web_login
from com.ea.pages.zhengxin_page import ZhengxinPage
from com.ea.common import web_menu
from com.ea.common import web_loan
from appium import webdriver


class test(BasePage):
    u"""流通贷-厂家-共享"""

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['automationName'] = "uiautomator2"
    desired_caps['deviceName'] = 'Galaxy On5(2016)'
    # 这个是要安装的app的安装包地址，不是必须的，有  # 这个项的话会先通过这个地址安装app，我没有用这个，直接用的Package名和activity名
    # desired_caps['app'] = gl.app
    desired_caps['appPackage'] = "com.zhouyue.Bee"
    desired_caps['appActivity'] = "com.zhouyue.Bee.module.welcome.WelcomeActivity"
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True
    desired_caps['newCommandTimeout'] = 30000
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='小卖部']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//android.view.View[@text='衡中真相揭秘 ¥2.99 ']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//android.view.View[@text='立即购买']").click()

# time.sleep(10)
# driver.start_activity(gl.packagename, gl.homepage_activity)
#
# time.sleep(3)
# tools.login(driver)
#
# driver.quit()
# if not tools.get_approver_acount_by_yewuno('121212', '新征信查询'):
#     print("aaaa")


# import pymysql
#
# sit_host = "172.29.12.196"
# sit_port = 3306
# psit_host = "172.29.12.197"
# psit_port = 3307
# user = "o2oadmin"
# passwd = "o2oadmin@we741"
# db = "o2oworkflow"
# charset = "utf8"
# # 打开数据库连接
# sit_db = pymysql.connect(host=sit_host, port=sit_port, user=user, passwd=passwd, db=db, charset=charset)
# psit_db = pymysql.connect(host=psit_host, port=psit_port, user=user, passwd=passwd, db=db, charset=charset)
#
# # 使用cursor()方法获取操作游标
# sit_cursor = sit_db.cursor()
# psit_cursor = psit_db.cursor()
#
# # SQL 删除语句
# sql = 'delete from o2o_employee where employee_namecn="陈凯"'
# try:
#     # 执行SQL语句
#     sit_cursor.execute(sql)
#     # 提交修改
#     sit_db.commit()
# except:
#     # 发生错误时回滚
#     sit_db.rollback()
# # 关闭连接
# if sit_db:
#     sit_db.close()
#
# try:
#     # 执行SQL语句
#     psit_cursor.execute(sql)
#     # 提交修改
#     psit_db.commit()
# except:
#     # 发生错误时回滚
#     psit_db.rollback()
# # 关闭连接
# if psit_db:
#     psit_db.close()
