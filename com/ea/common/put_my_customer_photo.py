#!usr/bin/env python
# -- coding:utf-8 --


import time
from com.ea.common import tools
import sys

logger = tools.create_logger()


def put_my_customer_photo(driver, fullname, screenshot_path):
    u"""上传客户照片"""
    casename = sys._getframe().f_code.co_name
    logger.info("上传照片用例开始")
    expect_result = "实地调查照片"
    try:
        from com.ea.pages.my_customer_page import MyCustomerPage
        from com.ea.pages.menu_page import MenuPage
        tools.login(driver)
        menupage = MenuPage(driver)
        mycustomerpage = MyCustomerPage(driver)
        menupage.click_me_page()
        mycustomerpage.click_my_customer()
        time.sleep(3)
        # mycustomerpage.input_search_name(fullname)
        mycustomerpage.click_customer_name(fullname)
        mycustomerpage.click_put_photo()
        mycustomerpage.click_shidi_photo()
        mycustomerpage.click_quanjing()
        # 从本地相册选择
        # mycustomerpage.click_from_local_select()
        # mycustomerpage.click_tupian()
        # mycustomerpage.click_photo_name()
        # 拍照
        mycustomerpage.click_paizhao()
        mycustomerpage.click_kuaimen()
        mycustomerpage.click_confirm()
        time.sleep(7)
        driver.back()
        actual_result = mycustomerpage.get_result()
        assert expect_result == actual_result
        logger.info("上传照片用例结束")
    except Exception as e:
        tools.screenshot(driver, screenshot_path, casename)
        raise e
