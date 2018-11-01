#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: test_zhongduandai_changjia.py 
@time: 2018/03/05 
"""
from com.ea.common import tools
from com.ea.common.cardname import cardname
from com.ea.common.cardnumber import IdCardNumber
import unittest
import time
import sys
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_page import MenuPage
from com.ea.pages import approve_page
from com.ea.common import web_login
from com.ea.pages.zhengxin_page import ZhengxinPage
import os


class MyTestCase(unittest.TestCase):
    u"""流通贷-商超-自营"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    cardNo = IdCardNumber.getRandomIdNumber(1)[0]
    fullname, first_name, second_name, full_english_name, first_english_name, last_english_name = cardname.get_names()
    phoneNo = cardname.createPhone()
    accountid = tools.get_random_string()
    zx_no = tools.get_zx_no()
    loan_no = None
    dakuandanhao = None
    loan_type = "流通贷-商超"
    operate_mode = "自营模式"
    print("姓名:" + fullname)
    print("身份证:" + cardNo + "\n")

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.getAppiumDriver()
        cls.webdriver = tools.get_chrome_driver()
        web_login.login(cls.webdriver)
        tools.login(cls.driver)
        cls.menupage = MenuPage(cls.driver)
        cls.zhengxinpage = ZhengxinPage(cls.driver)
        # tools.create_zhengxin_data(cls.first_name, cls.second_name, cls.fullname, cls.full_english_name, cls.cardNo, cls.phoneNo, cls.first_english_name, cls.last_english_name, cls.zx_no, cls.accountid)
        cls.pubapprovepage = approve_page.ApprovePubPage(cls.driver)
        # applyer_acount = tools.get_zhuanyuan_acount()
        # 粤东(xianhui.ling),粤西(feng.yun),山东(wenhui.zhang),重庆(ling.cheng)

    def setUp(self):
        self.driver.start_activity(gl.packagename, gl.homepage_activity)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.webdriver.quit()
        cls.driver.quit()
        # pass

    # @unittest.skip("skip")
    def test_a_zhengxin_apply(self):
        """申请征信"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import zhengxin
        zhengxin.zhengxin_apply(self.driver, self.cardNo, self.first_name, self.second_name, self.first_english_name, self.last_english_name, self.phoneNo, self.screenshot_path, casename)

    # @unittest.skip("skip")
    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        zx_no = tools.get_zx_no_by_cardno(self.cardNo)
        casename = sys._getframe().f_code.co_name
        from com.ea.common import zhengxin
        zhengxin.zhengxin_approve(self.driver, zx_no, self.screenshot_path, casename)

    def test_c_loan_apply(self):
        """申请贷款"""
        casename = sys._getframe().f_code.co_name
        print("申请贷款用例开始")
        print("使用的身份证号是:", self.cardNo)
        sumofmoney = "500000"
        loan_manager = "李"
        platform = "深圳"
        channel_name = "北京"
        self.menupage.click_loan_apply()
        from com.ea.pages.loan_apply_page import LoanApplyPage
        loanapplypage = LoanApplyPage(self.driver)
        try:
            loanapplypage.select_loan_type(self.loan_type)
            loanapplypage.input_cardno(self.cardNo)
            loanapplypage.click_next_button()
            time.sleep(2)
            loanapplypage.select_marry_status()
            loanapplypage.click_next_button()
            loanapplypage.input_loan_sumofmoney(sumofmoney)
            loanapplypage.select_loan_manager(loan_manager)
            loanapplypage.select_operate_mode(self.operate_mode)
            loanapplypage.input_platform(platform)
            loanapplypage.input_channel_name(channel_name)
            loanapplypage.click_save_button()
            time.sleep(3)
            MyTestCase.loan_no = tools.get_loan_no_by_cardno(self.cardNo)
            loanapplypage.click_loan_no(self.loan_no)
            loanapplypage.select_zhengxin_report()
            loanapplypage.click_start_flow()
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_d_loan_approve(self):
        """审批贷款"""
        casename = sys._getframe().f_code.co_name
        # self.loan_no = "CMY000001-BK-1803-00012"
        from com.ea.common import loan
        loan.loan_approve(self.driver, self.loan_no, self.screenshot_path, casename)

    # @unittest.skip("tiaoguo")
    def test_e_inside_apply(self):
        u"""编辑内部审批"""
        print("编辑内部审批用例开始")
        print("使用的贷款单号是:", self.loan_no)
        casename = sys._getframe().f_code.co_name
        organization = "公安局"
        home_phone = "075528560115"
        wechat = "123564456"
        postcode = "518001"
        road = "无名路"
        live_years = "5"
        children_description = "这里是子女情况描述"
        other_info = "这里是其他信息描述"
        contact_names = ["张三", "李四"]
        contact_phones = ["13625648852", "13525648853"]
        total_price = "20"
        mj_price = "1"
        zhizhao_name = "YYZZ0001"
        register_no = "1025110001"
        gudongrenshu = "1"
        fuqizhanbi = "100"
        controler_name = self.fullname
        jinglirun = "20"
        fuzhaizonge = "10"
        nianxiaoshoue = "50"
        yuangongrenshu = "5"
        mendianhuanjingmiaoshu = "这里是门店经营环境描述"
        store_phone = "57629280"
        area = "20"
        nianzujin = "20000"
        cunhuojiazhiyugu = "500000"
        cunhuoxiaoqimiaoshu = "这里是存货效期描述"
        eamount = "50000"
        kehumingcheng = "客户1"
        jiesuanzhangqi = "30"
        gonghuoliang = "30000"
        pinpai = "耐克"
        chanpinleixing = "百货"
        dailizizhi = "优秀"
        hezuoqixian = "10"
        nianxiaoshourenwu = "100"
        erpishang = "10"
        shangchao = "20"
        zhijielingshou = "30"
        lingshouzhongduan = "40"
        # self.loan_no = "CMY000001-BK-1803-00038"
        from com.ea.pages.inside_page import InsidePage
        try:
            insidepage = InsidePage(self.driver)
            self.menupage.click_inside_approve()
            time.sleep(5)
            insidepage.click_loan_no(self.loan_no)
            # 借款人基本信息
            insidepage.click_borrower_info()
            insidepage.click_edit_button()
            insidepage.input_organization(organization)
            insidepage.select_education()
            insidepage.scroll_to_marry_status()
            insidepage.input_wechat_no(wechat)
            insidepage.input_home_phone(home_phone)
            insidepage.input_post_code(postcode)
            insidepage.select_home_addr()
            insidepage.input_hujidizhi(road)
            insidepage.input_juzhudizhi(road)
            insidepage.input_live_years(live_years)
            insidepage.input_children_info(children_description)
            insidepage.input_other_info(other_info)
            insidepage.click_save_button()
            time.sleep(1)
            self.driver.back()
            time.sleep(1)
            # 贷款信息
            insidepage.click_loan_info()
            insidepage.click_jibenxinxi()
            insidepage.click_edit_button()
            insidepage.select_daikuanqixian()
            insidepage.select_huankuanfangshi()
            insidepage.input_ea_pifuedu(eamount)
            insidepage.select_daikuanyongtu()
            insidepage.select_songshen_yinhang()
            insidepage.select_danbaofangshi()
            insidepage.click_save_button()
            self.driver.back()
            self.driver.back()
            # 紧急联系人
            insidepage.click_jinjilianxiren()
            for i in range(2):
                insidepage.click_add_button()
                insidepage.input_contact_name(contact_names[i])
                insidepage.select_yujiekuanrenguanxi()
                insidepage.input_contact_phone(contact_phones[i])
                insidepage.input_contact_addr(road)
                insidepage.click_save_button()
            self.driver.back()
            # 夫妻双方负债情况
            insidepage.click_fuqishuangfangfuzhaiqingkuang()
            insidepage.click_add_button()
            insidepage.input_zichanzongji(total_price)
            insidepage.input_minjianjiedai(mj_price)
            insidepage.click_save_button()
            self.driver.back()
            # 经营主体信息
            insidepage.click_jingyingzhutixinxi()
            insidepage.click_edit_button()
            insidepage.input_zhizhao_name(zhizhao_name)
            insidepage.input_zhucehao(register_no)
            insidepage.select_zuzhixingshi()
            insidepage.select_zhuceshijian()
            insidepage.input_yingyezhizhaodizhi(road)
            insidepage.input_office_addr(road)
            insidepage.input_gudongrenshu(gudongrenshu)
            insidepage.input_fuqizhanbi(fuqizhanbi)
            insidepage.select_gongshangshifouyichang()
            insidepage.select_borrower_is_controler()
            insidepage.input_controler_name(controler_name)
            insidepage.select_yingye_mode()
            insidepage.scroll_to_yingye_mode()
            insidepage.select_hangye_leibie()
            insidepage.select_jingyingqishishijian()
            insidepage.click_save_button()
            self.driver.back()
            # 经营历史
            insidepage.click_jingyinglishi()
            insidepage.click_add_button()
            insidepage.input_jingli(jinglirun)
            insidepage.input_fuzhaizonge(fuzhaizonge)
            insidepage.input_nianxiaoshoue(nianxiaoshoue)
            insidepage.click_save_button()
            self.driver.back()
            # 近六个月营业额情况
            insidepage.click_near_six_month()
            insidepage.click_edit_button()
            insidepage.click_save_button()
            self.driver.back()
            insidepage.scroll_to_loan_info()
            # 经营状况
            insidepage.click_jingyingzhuangkuang()
            insidepage.click_add_button()
            insidepage.input_yuangongrenshu(yuangongrenshu)
            insidepage.select_nianyingyeeyanzhengziliao()
            insidepage.click_save_button()
            time.sleep(2)
            self.driver.back()
            # 门店信息
            insidepage.click_mendian_info()
            insidepage.click_add_button()
            insidepage.select_chanquanxingzhi()
            insidepage.input_mendianhuanjingmiaoshu(mendianhuanjingmiaoshu)
            insidepage.input_mendian_phone(store_phone)
            insidepage.select_mendian_chengliriqi()
            insidepage.input_mendian_addr(road)
            insidepage.input_yingyemianji(area)
            insidepage.input_nianzujin(nianzujin)
            insidepage.select_zulinhetongqizhiriqi()
            insidepage.input_cunhuojiazhiyugu(cunhuojiazhiyugu)
            insidepage.select_zhuangxiuxinjiuchengdu()
            insidepage.select_huojiashifouzhengqi()
            insidepage.input_cunhuoxiaoqimiaoshu(cunhuoxiaoqimiaoshu)
            insidepage.click_save_button()
            time.sleep(2)
            self.driver.back()
            # 渠道数据
            insidepage.click_qudaoshuju()
            insidepage.click_add_button()
            insidepage.select_yubaimingdanneishangchaohezuokaishishijian()
            insidepage.click_save_button()
            time.sleep(2)
            self.driver.back()
            # 主要供货渠道
            insidepage.click_zhuyaogonghuoqudao()
            insidepage.input_erpishang(erpishang)
            insidepage.input_shangchao(shangchao)
            insidepage.input_zhijielingshou(zhijielingshou)
            insidepage.input_lingshouzhongduan(lingshouzhongduan)
            insidepage.click_save_button()
            time.sleep(2)
            self.driver.back()
            # 十大下游客户近6月供货量
            insidepage.click_shidaxiayoukehugonghuoliang()
            insidepage.click_add_button()
            insidepage.input_kehumingcheng(kehumingcheng)
            insidepage.input_jiesuanzhangqi(jiesuanzhangqi)
            insidepage.input_gonghuoliang(gonghuoliang)
            insidepage.click_save_button()
            time.sleep(2)
            self.driver.back()
            # 主要销售产品
            insidepage.click_zhuyaoxiaoshouchanpin()
            insidepage.click_add_button()
            insidepage.input_chanpinpinpai(pinpai)
            insidepage.input_chanpinleixing(chanpinleixing)
            insidepage.input_dailizizhi(dailizizhi)
            insidepage.input_hezuoqixian(hezuoqixian)
            insidepage.input_nianxiaoshourenwu(nianxiaoshourenwu)
            insidepage.click_save_button()
            time.sleep(2)
            self.driver.back()
            time.sleep(1)
            insidepage.click_start_flow()
            insidepage.click_confirm_text()
        except Exception as e:
            tools.screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_f_inside_approve(self):
        u"""审批内部审批"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import inside
        inside.inside_approve(self.driver, self.loan_no, self.screenshot_path, casename, self.operate_mode)

    def test_g_pay_money_apply(self):
        u"""新建打款流程"""
        casename = sys._getframe().f_code.co_name
        # self.fullname = "伏兴桌"
        # self.cardNo = "141129198110114778"
        from com.ea.common import pay_money
        MyTestCase.dakuandanhao = pay_money.pay_money_apply(self.driver, self.fullname, self.cardNo, self.screenshot_path, casename)

    def test_h_pay_money_approve(self):
        u"""审批打款流程"""
        casename = sys._getframe().f_code.co_name
        # self.dakuandanhao = "DK-1803-00024"
        from com.ea.common import pay_money
        pay_money.pay_money_approve(self.webdriver, self.dakuandanhao, self.screenshot_path, casename)

    def test_i_interview_apply(self):
        u"""面签提报"""
        casename = sys._getframe().f_code.co_name
        # self.loan_no = "CMY000001-BK-1803-00038"
        from com.ea.common import interview
        interview.interview_apply(self.driver, self.loan_no, self.screenshot_path, casename)

    def test_j_interview_approve(self):
        u"""面签审批"""
        from com.ea.common import interview
        casename = sys._getframe().f_code.co_name
        # self.fullname = "伏兴桌"
        # self.loan_no = "CMY000001-BK-1803-00038"
        interview.interview_approve(self.webdriver, self.loan_no, self.fullname, self.screenshot_path, casename)


if __name__ == '__main__':
    unittest.main()
