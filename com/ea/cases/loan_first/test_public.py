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
from com.ea.common import inside
from com.ea.common import loan
from com.ea.common import zhengxin
from com.ea.common import put_my_customer_photo
from com.ea.common import pay_money
from com.ea.common import interview
import arrow

logger = tools.create_logger()


class MyTestCase(unittest.TestCase):
    u"""贷款场景用例"""
    logger.info(str(arrow.now()))
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    card_no = None
    fullname = None
    loanno = None
    dakuandanhao = None
    partner_zx_no = ""
    loan_flag = 1
    mode_flag = 1
    marry_flag = 0

    if loan_flag == 1:
        loan_type = "终端贷"
    elif loan_flag == 2:
        loan_type = "流通贷-厂家"
    elif loan_flag == 3:
        loan_type = "流通贷-经销商"
    elif loan_flag == 4:
        loan_type = "流通贷-蔬果"
    elif loan_flag == 5:
        loan_type = "流通贷-烟草"
    elif loan_flag == 6:
        loan_type = "流通贷-商超"
    else:
        loan_type = None

    if mode_flag == 0:
        operate_mode = "共享模式"
    else:
        operate_mode = "自营模式"

    if marry_flag == 1:
        marry_status = "已婚"
    else:
        marry_status = "未婚"

    danbaoren = ""
    bank_name = "浦发广州分行"
    sumofmoney = "150000"
    driver = None
    webdriver = None

    logger.info("场景:" + loan_type + " " + operate_mode + " " + marry_status + " " + bank_name + " " + sumofmoney)
    # print("场景:" + loan_type + " " + operate_mode + " " + marry_status + " " + bank_name + " " + sumofmoney)

    if loan_type == "终端贷" and operate_mode == "共享模式":
        skip_caiwu = 0
    else:
        skip_caiwu = 1

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        cls.webdriver = tools.get_chrome_driver()

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.login_activity)

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
        card_no, fullname, partner_zx_no = loan.loan_zhengxin_apply(self.driver, self.loan_type, self.sumofmoney, self.bank_name, self.operate_mode, self.screenshot_path, self.marry_status, self.danbaoren)
        MyTestCase.card_no, MyTestCase.fullname, MyTestCase.partner_zx_no = card_no, fullname, partner_zx_no
        MyTestCase.loanno = tools.get_loan_no_by_cardno(card_no)

    # @unittest.skip("skip")
    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        # self.card_no = "110100198209269092"
        # pcard_no = "340721197504229264"
        # self.partner_zx_no = tools.get_zx_no_by_cardno(pcard_no)
        zx_no = tools.get_zx_no_by_cardno(self.card_no)
        zhengxin.zhengxin_approve(self.driver, zx_no, self.screenshot_path, partner_zx_no=self.partner_zx_no)

    # @unittest.skip("skip")
    def test_c_put_photo(self):
        u"""上传客户照片"""
        # self.fullname = '谈请'
        put_my_customer_photo.put_my_customer_photo(self.driver, self.fullname, self.screenshot_path)

    # @unittest.skip("skip")
    def test_d_loan_approve(self):
        """审批贷款"""
        # self.loanno = "YN010-BP-1808-00012"

        web_loan.loan_approve(self.webdriver, self.loanno, self.marry_status, self.screenshot_path)

    @unittest.skipUnless(skip_caiwu == 0, "非终端贷共享模式,不执行此用例!")
    def test_e_caiwu_approve(self):
        u"""平台财务审核"""
        from com.ea.common import caiwu_approve
        caiwu_approve.caiwu_approve(self.webdriver, self.loanno, self.screenshot_path)

    def test_e_edit_inside_apply(self):
        u"""编辑内部审批"""
        # self.loanno = "SC010-BP-1808-00003"
        # self.fullname = "张三"
        inside.inside_apply(self.webdriver, self.loanno, self.fullname, self.loan_type, self.marry_status, self.bank_name, self.screenshot_path)

    # @unittest.skip("skip")
    def test_f_inside_approve(self):
        u"""审批内部审批"""
        # self.loanno = 'SC010-BP-1808-00003'
        inside.inside_approve(self.driver, self.loanno, self.screenshot_path)

    # @unittest.skip("skip")
    def test_g_pay_money_apply(self):
        u"""新建打款流程"""
        # self.fullname = "皮剧"
        # self.card_no = "310119197901307537"
        MyTestCase.dakuandanhao = pay_money.pay_money_apply(self.driver, self.fullname, self.card_no, self.screenshot_path)

    # @unittest.skip("skip")
    def test_h_pay_money_approve(self):
        u"""审批打款流程"""
        # self.dakuandanhao = "DK-1808-00057"
        pay_money.pay_money_approve(self.webdriver, self.dakuandanhao, self.screenshot_path)
        # webdriver.quit()

    # @unittest.skip("skip")
    def test_i_interview_apply(self):
        u"""面签提报"""
        # self.loanno = "YN010-BK-1810-00018"
        interview.interview_apply(self.driver, self.loanno, self.screenshot_path)
        # self.driver.quit()

    # @unittest.skip("skip")
    def test_j_interview_approve(self):
        u"""面签审批"""
        # self.fullname = "卜然临"
        # self.loanno = "YN010-BK-1810-00018"
        interview.interview_approve(self.webdriver, self.loanno, self.fullname, self.screenshot_path)


if __name__ == '__main__':
    unittest.main()
