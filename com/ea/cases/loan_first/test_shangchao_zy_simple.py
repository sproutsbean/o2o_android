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
from com.ea.common import web_login, web_menu
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
    loanno = None
    dakuandanhao = None
    partner_zx_no = ""
    loan_type = "流通贷-商超"
    operate_mode = "自营模式"
    marry_status = "已婚"
    print("姓名:" + fullname)
    print("身份证:" + cardNo + "\n")

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
        if cls.webdriver:
            cls.webdriver.quit()
        if cls.driver:
            cls.driver.quit()

    def test_a_loan_apply(self):
        """申请贷款"""
        casename = sys._getframe().f_code.co_name
        print("申请贷款用例开始")
        print("使用的身份证号是:", self.cardNo)
        sumofmoney = "500000"
        loan_manager = "李"
        platform = "深圳"
        channel_name = "北京"
        from com.ea.common import loan
        MyTestCase.loanno, MyTestCase.partner_zx_no = loan.loan_zhengxin_apply(self.driver, self.loan_type, self.cardNo, self.first_name, self.second_name, self.first_english_name, self.last_english_name, self.phoneNo, gl.xd_manager_name,
                                                                               sumofmoney, self.operate_mode, channel_name, self.screenshot_path, casename, marry_status=self.marry_status)

    # @unittest.skip("skip")
    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        zx_no = tools.get_zx_no_by_cardno(self.cardNo)
        casename = sys._getframe().f_code.co_name
        from com.ea.common import zhengxin
        zhengxin.zhengxin_approve(self.driver, zx_no, self.screenshot_path, casename, partner_zx_no=self.partner_zx_no)

    def test_c_loan_approve(self):
        """审批贷款"""
        casename = sys._getframe().f_code.co_name
        # self.loan_no = "CMY000001-BK-1803-00012"
        from com.ea.common import web_loan
        web_loan.loan_approve(self.webdriver, self.loanno, self.screenshot_path, casename)

    def test_d_put_photo(self):
        u"""上传客户照片"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import put_my_customer_photo
        # self.fullname = '郝斯将'
        put_my_customer_photo.put_my_customer_photo(self.driver, self.fullname, self.screenshot_path, casename)

    def test_e_edit_inside_apply(self):
        u"""编辑内部审批"""
        casename = sys._getframe().f_code.co_name
        expect_result = "审核中"
        organization = "公安局"
        home_phone = "075528560115"
        wechat = "123564456"
        postcode = "518001"
        province = "北京"
        city = "东城区"
        road = "无名路"
        live_years = "5"
        children_description = "这里是子女情况描述"
        contact_names = ["张三", "李四"]
        contact_phones = ["13625648852", "13525648853"]
        relationship = "朋友"
        total_price = "20"
        mj_price = "1"
        zhizhao_name = "YYZZ0001"
        register_no = "1025110001"
        organization_type = "个体工商户"
        register_time = "2017-01-01"
        shareholder_number = "1"
        share_proportion = "100"
        business_isnormal = "无"
        borrower_iscontroler = "是"
        controler_name = self.fullname
        yingye_mode = "便利店"
        vocation_type = "百货"
        start_time = "2017-01-01"
        jinglirun = "20"
        fuzhaizonge = "10"
        nianxiaoshoue = "50"
        six_month_sales = "3"
        personnel_number = "5"
        month_pay = "20000"
        water_pay = "1000"
        other_pay = "500"
        transport_pay = "1500"
        capital = "100"
        nianjinglirun = "20"
        should_pay = "50"
        collect = "60"
        liabilities = "10"
        invest = "10"
        property_type = "租赁"
        env_description = "这里是门店经营环境描述"
        store_phone = "57629280"
        store_date = "2017-01-01"
        area = "20"
        shoprent_year = "20000"
        shoprent_starttime = "2017-01-01"
        shoprent_endtime = "2017-05-05"
        store_value = "500000"
        new_old = "很新"
        zhengqi = "整齐"
        store_description = "这里是存货效期描述"
        loan_time = "6个月"
        huankuan_type = "等额本息"
        loan_yongtu = "流动资金"
        eamount = "50000"
        bankname = "江西银行"
        tuijian_type = "合作方推荐"
        tuijian_name = "李超"
        danbao_type = "其它方式"
        whitelisttime = "2017-05-05"
        twobatch = "1"
        supermarket = "1"
        directRetail = "1"
        retail = "1"
        custom_name = "客户一"
        jiesuanzhangqi = "30"
        gonghuoliang = "3000"
        productBrand = "耐克"
        productType = "鞋子"
        dailizizhi = "良好"
        hezuoqixian = "10"
        y_saleTask = "100"
        # self.loanno = "SK0027-SC-1712-00004"
        print("开始编辑内部审批")
        print("使用的贷款单号是:" + self.loanno)
        try:
            web_login.login(self.webdriver, username=gl.xd_manager_account)
            from com.ea.pages.web_inside_page import WebInsidePage
            insidepage = WebInsidePage(self.webdriver)
            web_menu.go_to_inside_approve(self.webdriver)
            handle1 = self.webdriver.current_window_handle
            insidepage.click_first_row(self.loanno)
            handles = self.webdriver.window_handles
            handle2 = ""
            for handle in handles:
                if handle != handle1:
                    self.webdriver.switch_to.window(handle)
                    handle2 = self.webdriver.current_window_handle
            time.sleep(2)
            insidepage.click_editinside_button()
            handles = self.webdriver.window_handles
            for handle in handles:
                if handle != handle1 and handle != handle2:
                    self.webdriver.switch_to.window(handle)
            # 借款人基本信息
            insidepage.click_editborrower_button()
            insidepage.input_card_organization(organization)
            insidepage.input_home_phone(home_phone)
            insidepage.input_wechat(wechat)
            insidepage.input_postcode(postcode)
            insidepage.select_register_addr_province(province)
            time.sleep(1)
            insidepage.select_register_addr_city(city)
            insidepage.input_register_addr_road(road)
            insidepage.select_sleep_addr_province(province)
            time.sleep(1)
            insidepage.select_sleep_addr_city(city)
            insidepage.input_sleep_addr_road(road)
            insidepage.input_live_years(live_years)
            if self.marry_status == "已婚":
                insidepage.select_marry_date()
            insidepage.input_children(children_description)
            insidepage.click_borrower_save()
            insidepage.click_borrower_confirm()
            time.sleep(1)
            # 配偶基本信息
            if self.marry_status == "已婚":
                insidepage.scroll_to_partner_edit()
                insidepage.click_partner_edit()
                insidepage.input_card_organization(organization)
                insidepage.input_wechat(wechat)
                insidepage.select_register_addr_province(province)
                time.sleep(1)
                insidepage.select_register_addr_city(city)
                insidepage.input_register_addr_road(road)
                insidepage.input_work_unit(organization)
                insidepage.click_partner_save()
                insidepage.click_partner_confirm()
                time.sleep(2)
            # 添加紧急联系人
            insidepage.scroll_to_contact()
            for i in range(2):
                insidepage.click_contact_add()
                insidepage.input_contact_name(contact_names[i])
                insidepage.input_contact_phone(contact_phones[i])
                insidepage.select_contacts_relationship(relationship)
                insidepage.click_contact_save()
                time.sleep(2)
            # 夫妻双方负债情况
            insidepage.scroll_to_fuqishuangfangfuzhaiqingkuang()
            insidepage.click_edit_fuzhai()
            insidepage.input_total_price(total_price)
            insidepage.input_mj_price(mj_price)
            insidepage.click_fuzhai_save()
            # 经营主体信息
            insidepage.scroll_to_jingyingzhuti_edit_button()
            insidepage.click_jingyingzhuti_edit()
            insidepage.input_yingyezhizhao_name(zhizhao_name)
            insidepage.input_zhucehao(register_no)
            insidepage.select_organization_type(organization_type)
            insidepage.input_register_time(register_time)
            insidepage.select_zhizhao_addr_province(province)
            time.sleep(1)
            insidepage.select_zhizhao_addr_city(city)
            insidepage.input_zhizhao_addr_road(road)
            insidepage.select_office_addr_province(province)
            time.sleep(1)
            insidepage.select_office_addr_city(city)
            insidepage.input_office_addr_road(road)
            insidepage.input_shareholder_number(shareholder_number)
            insidepage.input_share_proportion(share_proportion)
            insidepage.select_business_isnormal(business_isnormal)
            insidepage.select_borrower_iscontroler(borrower_iscontroler)
            insidepage.input_controler_name(controler_name)
            insidepage.select_yingye_mode(yingye_mode)
            insidepage.select_vocation_type(vocation_type)
            insidepage.input_start_time(start_time)
            insidepage.click_zhuti_submit_button()
            time.sleep(3)
            # 经营历史
            insidepage.scroll_to_jingyinglishi()
            insidepage.click_history_add()
            insidepage.click_years()
            insidepage.input_jingli(jinglirun)
            insidepage.input_fuzhaizonge(fuzhaizonge)
            insidepage.input_nianxiaoshoue(nianxiaoshoue)
            insidepage.click_history_save_button()
            time.sleep(2)
            # 近6个月营业额情况
            insidepage.scroll_to_jinliugeyueyingyee()
            insidepage.click_six_month_edit()
            insidepage.input_january(six_month_sales)
            insidepage.input_february(six_month_sales)
            insidepage.input_march(six_month_sales)
            insidepage.input_april(six_month_sales)
            insidepage.input_may(six_month_sales)
            insidepage.input_june(six_month_sales)
            insidepage.click_six_month_submit()
            time.sleep(2)
            # 编辑经营状况
            insidepage.scroll_to_jingyingzhuangkuang()
            insidepage.click_edit_status()
            insidepage.input_personnel_number(personnel_number)
            insidepage.input_month_pay(month_pay)
            insidepage.input_water_pay(water_pay)
            insidepage.input_other_pay(other_pay)
            insidepage.input_transport_pay(transport_pay)
            insidepage.input_capital(capital)
            insidepage.input_nianjinglirun(nianjinglirun)
            insidepage.click_bank_water()
            insidepage.input_should_pay(should_pay)
            insidepage.input_collect(collect)
            insidepage.input_liabilities(liabilities)
            insidepage.input_invest(invest)
            insidepage.click_status_save_button()
            time.sleep(2)
            # 新增门店信息
            insidepage.scroll_to_store()
            insidepage.click_store_add_button()
            insidepage.select_property_type(property_type)
            insidepage.input_env_description(env_description)
            insidepage.input_store_phone(store_phone)
            insidepage.input_store_date(store_date)
            insidepage.select_store_addr_province(province)
            time.sleep(1)
            insidepage.select_store_addr_city(city)
            insidepage.input_store_addr_road(road)
            insidepage.input_business_area(area)
            insidepage.input_shoprent_year(shoprent_year)
            insidepage.input_shoprent_starttime(shoprent_starttime)
            insidepage.input_shoprent_endtime(shoprent_endtime)
            insidepage.input_store_value(store_value)
            insidepage.select_new_old(new_old)
            insidepage.select_zhengqi(zhengqi)
            insidepage.input_store_description(store_description)
            insidepage.click_store_submit()
            time.sleep(2)
            # 编辑渠道数据
            insidepage.scroll_to_shangchao_channel()
            time.sleep(1)
            insidepage.input_whitelisttime(whitelisttime)
            insidepage.input_twobatch(twobatch)
            insidepage.input_supermarket(supermarket)
            insidepage.input_directRetail(directRetail)
            insidepage.input_retail(retail)
            insidepage.click_fruits_save_button()
            time.sleep(2)
            # 编辑下游信息
            insidepage.scroll_to_shidaxiayoukehujinliuyuegonghuoliang()
            insidepage.click_xiayou_add()
            insidepage.input_custom_name(custom_name)
            insidepage.input_jiesuanzhangqi(jiesuanzhangqi)
            insidepage.input_gonghuoliang(gonghuoliang)
            insidepage.click_xiayou_save_button()
            insidepage.click_ok_button()
            time.sleep(2)
            # 增加主要产品销售情况
            insidepage.scroll_to_zhuyaoxiaoshouchanpin()
            insidepage.click_shangchao_product_add()
            insidepage.input_productBrand(productBrand)
            insidepage.input_productType(productType)
            insidepage.input_dailizizhi(dailizizhi)
            insidepage.input_hezuoqixian(hezuoqixian)
            insidepage.input_y_saleTask(y_saleTask)
            insidepage.click_sale_product_save()
            insidepage.click_ok_button()
            time.sleep(2)
            # 编辑调查结论
            insidepage.scroll_to_diaochajielun()
            insidepage.click_diaochajielun_edit()
            insidepage.input_diaochajielun()
            insidepage.click_diaochajielun_commit_button()
            # 编辑贷款信息
            insidepage.scroll_to_loan_info()
            insidepage.select_loan_time(loan_time)
            insidepage.select_huankuan_type(huankuan_type)
            insidepage.input_eamount(eamount)
            insidepage.select_loan_yongtu(loan_yongtu)
            insidepage.select_loan_bankname(bankname)
            # insidepage.select_tuijian_type(tuijian_type)
            # insidepage.input_tuijian_name(tuijian_name)
            insidepage.select_danbao_type(danbao_type)
            insidepage.click_loan_info_save()
            # time.sleep(1)
            insidepage.click_loan_info_confirm()
            insidepage.scroll_to_put_photo()
            insidepage.click_put_photo()
            insidepage.click_photo()
            insidepage.click_put_photo_save_button()
            time.sleep(2)
            self.webdriver.close()
            # 切换到内审详情页面
            self.webdriver.switch_to.window(handle2)
            insidepage.click_submit_inside_approve()
            time.sleep(1)
            # 关闭内审详情页面
            self.webdriver.close()
            # 切换到内部审批页面
            self.webdriver.switch_to.window(handle1)
            # 刷新页面
            self.webdriver.refresh()
            actual_result = insidepage.get_result(self.loanno)
            self.assertEqual(actual_result, expect_result)
            print("编辑内部审批结束")
        except Exception as e:
            tools.screenshot(self.webdriver, self.screenshot_path, casename)
            raise e

    # def test_e_start_inside_apply(self):
    #     u"""启动内审流程"""
    #     print("启动内部审批用例开始")
    #     print("使用的贷款单号是:", self.loanno)
    #     casename = sys._getframe().f_code.co_name
    #     from com.ea.common import inside
    #     inside.start_inside_apply(self.driver, self.loanno, self.screenshot_path, casename)
    #     print("启动内部审批用例结束")

    # @unittest.skip("tiaoguo")
    # def test_e_inside_apply(self):
    #     u"""编辑内部审批"""
    #     print("编辑内部审批用例开始")
    #     print("使用的贷款单号是:", self.loan_no)
    #     casename = sys._getframe().f_code.co_name
    #     organization = "公安局"
    #     home_phone = "075528560115"
    #     wechat = "123564456"
    #     postcode = "518001"
    #     road = "无名路"
    #     live_years = "5"
    #     children_description = "这里是子女情况描述"
    #     other_info = "这里是其他信息描述"
    #     contact_names = ["张三", "李四"]
    #     contact_phones = ["13625648852", "13525648853"]
    #     total_price = "20"
    #     mj_price = "1"
    #     zhizhao_name = "YYZZ0001"
    #     register_no = "1025110001"
    #     gudongrenshu = "1"
    #     fuqizhanbi = "100"
    #     controler_name = self.fullname
    #     jinglirun = "20"
    #     fuzhaizonge = "10"
    #     nianxiaoshoue = "50"
    #     yuangongrenshu = "5"
    #     mendianhuanjingmiaoshu = "这里是门店经营环境描述"
    #     store_phone = "57629280"
    #     area = "20"
    #     nianzujin = "20000"
    #     cunhuojiazhiyugu = "500000"
    #     cunhuoxiaoqimiaoshu = "这里是存货效期描述"
    #     eamount = "50000"
    #     kehumingcheng = "客户1"
    #     jiesuanzhangqi = "30"
    #     gonghuoliang = "30000"
    #     pinpai = "耐克"
    #     chanpinleixing = "百货"
    #     dailizizhi = "优秀"
    #     hezuoqixian = "10"
    #     nianxiaoshourenwu = "100"
    #     erpishang = "10"
    #     shangchao = "20"
    #     zhijielingshou = "30"
    #     lingshouzhongduan = "40"
    #     # self.loan_no = "CMY000001-BK-1803-00038"
    #     from com.ea.pages.inside_page import InsidePage
    #     try:
    #         insidepage = InsidePage(self.driver)
    #         self.menupage.click_inside_approve()
    #         time.sleep(5)
    #         insidepage.click_loan_no(self.loan_no)
    #         # 借款人基本信息
    #         insidepage.click_borrower_info()
    #         insidepage.click_edit_button()
    #         insidepage.input_organization(organization)
    #         insidepage.select_education()
    #         insidepage.scroll_to_marry_status()
    #         insidepage.input_wechat_no(wechat)
    #         insidepage.input_home_phone(home_phone)
    #         insidepage.input_post_code(postcode)
    #         insidepage.select_home_addr()
    #         insidepage.input_hujidizhi(road)
    #         insidepage.input_juzhudizhi(road)
    #         insidepage.input_live_years(live_years)
    #         insidepage.input_children_info(children_description)
    #         insidepage.input_other_info(other_info)
    #         insidepage.click_save_button()
    #         time.sleep(1)
    #         self.driver.back()
    #         time.sleep(1)
    #         # 贷款信息
    #         insidepage.click_loan_info()
    #         insidepage.click_jibenxinxi()
    #         insidepage.click_edit_button()
    #         insidepage.select_daikuanqixian()
    #         insidepage.select_huankuanfangshi()
    #         insidepage.input_ea_pifuedu(eamount)
    #         insidepage.select_daikuanyongtu()
    #         insidepage.select_songshen_yinhang()
    #         insidepage.select_danbaofangshi()
    #         insidepage.click_save_button()
    #         self.driver.back()
    #         self.driver.back()
    #         # 紧急联系人
    #         insidepage.click_jinjilianxiren()
    #         for i in range(2):
    #             insidepage.click_add_button()
    #             insidepage.input_contact_name(contact_names[i])
    #             insidepage.select_yujiekuanrenguanxi()
    #             insidepage.input_contact_phone(contact_phones[i])
    #             insidepage.input_contact_addr(road)
    #             insidepage.click_save_button()
    #         self.driver.back()
    #         # 夫妻双方负债情况
    #         insidepage.click_fuqishuangfangfuzhaiqingkuang()
    #         insidepage.click_add_button()
    #         insidepage.input_zichanzongji(total_price)
    #         insidepage.input_minjianjiedai(mj_price)
    #         insidepage.click_save_button()
    #         self.driver.back()
    #         # 经营主体信息
    #         insidepage.click_jingyingzhutixinxi()
    #         insidepage.click_edit_button()
    #         insidepage.input_zhizhao_name(zhizhao_name)
    #         insidepage.input_zhucehao(register_no)
    #         insidepage.select_zuzhixingshi()
    #         insidepage.select_zhuceshijian()
    #         insidepage.input_yingyezhizhaodizhi(road)
    #         insidepage.input_office_addr(road)
    #         insidepage.input_gudongrenshu(gudongrenshu)
    #         insidepage.input_fuqizhanbi(fuqizhanbi)
    #         insidepage.select_gongshangshifouyichang()
    #         insidepage.select_borrower_is_controler()
    #         insidepage.input_controler_name(controler_name)
    #         insidepage.select_yingye_mode()
    #         insidepage.scroll_to_yingye_mode()
    #         insidepage.select_hangye_leibie()
    #         insidepage.select_jingyingqishishijian()
    #         insidepage.click_save_button()
    #         self.driver.back()
    #         # 经营历史
    #         insidepage.click_jingyinglishi()
    #         insidepage.click_add_button()
    #         insidepage.input_jingli(jinglirun)
    #         insidepage.input_fuzhaizonge(fuzhaizonge)
    #         insidepage.input_nianxiaoshoue(nianxiaoshoue)
    #         insidepage.click_save_button()
    #         self.driver.back()
    #         # 近六个月营业额情况
    #         insidepage.click_near_six_month()
    #         insidepage.click_edit_button()
    #         insidepage.click_save_button()
    #         self.driver.back()
    #         insidepage.scroll_to_loan_info()
    #         # 经营状况
    #         insidepage.click_jingyingzhuangkuang()
    #         insidepage.click_add_button()
    #         insidepage.input_yuangongrenshu(yuangongrenshu)
    #         insidepage.select_nianyingyeeyanzhengziliao()
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 门店信息
    #         insidepage.click_mendian_info()
    #         insidepage.click_add_button()
    #         insidepage.select_chanquanxingzhi()
    #         insidepage.input_mendianhuanjingmiaoshu(mendianhuanjingmiaoshu)
    #         insidepage.input_mendian_phone(store_phone)
    #         insidepage.select_mendian_chengliriqi()
    #         insidepage.input_mendian_addr(road)
    #         insidepage.input_yingyemianji(area)
    #         insidepage.input_nianzujin(nianzujin)
    #         insidepage.select_zulinhetongqizhiriqi()
    #         insidepage.input_cunhuojiazhiyugu(cunhuojiazhiyugu)
    #         insidepage.select_zhuangxiuxinjiuchengdu()
    #         insidepage.select_huojiashifouzhengqi()
    #         insidepage.input_cunhuoxiaoqimiaoshu(cunhuoxiaoqimiaoshu)
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 渠道数据
    #         insidepage.click_qudaoshuju()
    #         insidepage.click_add_button()
    #         insidepage.select_yubaimingdanneishangchaohezuokaishishijian()
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 主要供货渠道
    #         insidepage.click_zhuyaogonghuoqudao()
    #         insidepage.input_erpishang(erpishang)
    #         insidepage.input_shangchao(shangchao)
    #         insidepage.input_zhijielingshou(zhijielingshou)
    #         insidepage.input_lingshouzhongduan(lingshouzhongduan)
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 十大下游客户近6月供货量
    #         insidepage.click_shidaxiayoukehugonghuoliang()
    #         insidepage.click_add_button()
    #         insidepage.input_kehumingcheng(kehumingcheng)
    #         insidepage.input_jiesuanzhangqi(jiesuanzhangqi)
    #         insidepage.input_gonghuoliang(gonghuoliang)
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 主要销售产品
    #         insidepage.click_zhuyaoxiaoshouchanpin()
    #         insidepage.click_add_button()
    #         insidepage.input_chanpinpinpai(pinpai)
    #         insidepage.input_chanpinleixing(chanpinleixing)
    #         insidepage.input_dailizizhi(dailizizhi)
    #         insidepage.input_hezuoqixian(hezuoqixian)
    #         insidepage.input_nianxiaoshourenwu(nianxiaoshourenwu)
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         time.sleep(1)
    #         insidepage.click_start_flow()
    #         insidepage.click_confirm_text()
    #     except Exception as e:
    #         tools.screenshot(self.driver, self.screenshot_path, casename)
    #         raise e

    def test_f_inside_approve(self):
        u"""审批内部审批"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import inside
        inside.inside_approve(self.driver, self.loanno, self.screenshot_path, casename)

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
        interview.interview_apply(self.driver, self.loanno, self.screenshot_path, casename)

    def test_j_interview_approve(self):
        u"""面签审批"""
        from com.ea.common import interview
        casename = sys._getframe().f_code.co_name
        # self.fullname = "伏兴桌"
        # self.loan_no = "CMY000001-BK-1803-00038"
        interview.interview_approve(self.webdriver, self.loanno, self.fullname, self.screenshot_path, casename)


if __name__ == '__main__':
    unittest.main()
