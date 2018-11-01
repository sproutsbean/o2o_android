#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: web_login.py
@time: 2017/12/06 
"""
from com.ea.pages.web_login_page import LoginPage
from com.ea.resource import globalparameter as gl
import time


def login(driver, username="jun.lu", url=gl.url, title=gl.title):
    loginpage = LoginPage(driver)
    loginpage.open(url, title)
    loginpage.input_username(username)
    loginpage.click_login()
