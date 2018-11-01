#!usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
from com.ea.common import tools
from com.ea.common import web_login
from com.ea.pages.overdue_detail_page import OverdueDetailPage
import time


class MyTestCase(unittest.TestCase):
    def test_overdul_detail(self):
        province = '安徽'
        kaohe_month = '2018-02'
        expect_danhao = 'C380Z0066-BP-1712-00024'
        expect_borrower_name = '刘宏'
        expect_jinbanren = '郭明有'
        expect_fangkuan_jine = '40.0000'
        expect_fangkuan_qixian = '6'
        expect_fangkuan_shijian = '2017-12-29'
        expect_yuqi_shijian = '2018-02-16'
        expect_yuqi_benjin = '0.0000'
        expect_yuqi_lixi = '0.1385'

        webdriver = tools.get_chrome_driver()
        overduedetailpage = OverdueDetailPage(webdriver)
        web_login.login(webdriver)
        url = overduedetailpage.get_url()
        print(url)
        webdriver.get(url)
        overduedetailpage.select_province(province)
        overduedetailpage.input_kaohe_month(kaohe_month)
        overduedetailpage.click_search_button()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
