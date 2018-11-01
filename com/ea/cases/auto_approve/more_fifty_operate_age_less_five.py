#!usr/bin/env python  
# -*- coding:utf-8 -*-
"""
@author:user 
@file: test_zhongduandai_changjia.py 
@time: 2018/03/05 
"""
from com.ea.common import tools
import unittest
import os
from com.ea.resource import globalparameter as gl
from com.ea.common import web_loan
from com.ea.common import loan
from com.ea.common import inside

"""持续经营年限小于5年"""


class MyTestCase(unittest.TestCase):
    u"""申请金额60万,营业起始时间为:2017-01-01"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    driver = None
    webdriver = None
    card_no = None
    fullname = None
    loanno = None
    dakuandanhao = None
    partner_zx_no = ""
    loan_type = "流通贷-厂家"
    operate_mode = "共享模式"
    marry_status = "已婚"
    bank_name = "浦发广州分行"
    sumofmoney = "600000"

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        cls.webdriver = tools.get_chrome_driver()

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.login_activity)
        # pass

    def tearDown(self):
        self.webdriver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
        if cls.webdriver:
            cls.webdriver.quit()

    # @unittest.skip("skip")
    def test_a_loan_apply(self):
        """申请贷款"""
        card_no, fullname, partner_zx_no = loan.loan_zhengxin_apply(self.driver, self.loan_type, self.sumofmoney, self.bank_name, self.operate_mode, self.screenshot_path, marry_status=self.marry_status)
        MyTestCase.card_no, MyTestCase.fullname, MyTestCase.partner_zx_no = card_no, fullname, partner_zx_no
        MyTestCase.loanno = tools.get_loan_no_by_cardno(card_no)

    # @unittest.skip("skip")
    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        zx_no = tools.get_zx_no_by_cardno(self.card_no)
        # zx_no = "O2OZX-1804-00967"
        from com.ea.common import zhengxin
        zhengxin.zhengxin_approve(self.driver, zx_no, self.screenshot_path, partner_zx_no=self.partner_zx_no)

    # @unittest.skip("skip")
    def test_c_put_photo(self):
        u"""上传客户照片"""
        from com.ea.common import put_my_customer_photo
        # self.fullname = '郝斯将'
        put_my_customer_photo.put_my_customer_photo(self.driver, self.fullname, self.screenshot_path)

    # @unittest.skip("skip")
    def test_d_loan_approve(self):
        """审批贷款"""
        zx_zongfuzai_yue = "0"
        daikuan_yuqi_cishu = "0"
        danbao_yue = "0"
        xinyongka_yuqi_cishu = "0"
        # self.loan_no = "CMY000001-BK-1803-00012"
        web_loan.loan_approve(self.webdriver, self.loanno, self.marry_status, self.screenshot_path)

    # @unittest.skip('skip')
    def test_e_edit_inside_apply(self):
        u"""编辑内部审批"""
        start_time = "2018-01-01"
        eamount = "600000"
        year_sales = "700"
        lianbao_daikuan_yue = "0"
        jiufen = "否"
        inside.inside_apply(self.webdriver, self.loanno, self.fullname, self.loan_type, self.marry_status, self.bank_name, self.screenshot_path, start_time=start_time, eamount=eamount, year_sales=year_sales,
                            lianbao_daikuan_yue=lianbao_daikuan_yue, jiufen=jiufen)

    # @unittest.skip("skip")
    def test_f_inside_approve(self):
        u"""审批内部审批"""
        inside.inside_auto_approve(self.driver, self.loanno, self.screenshot_path)


if __name__ == '__main__':
    unittest.main()
