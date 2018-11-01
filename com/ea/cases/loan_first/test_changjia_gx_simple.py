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
import os
import sys
from com.ea.resource import globalparameter as gl
from com.ea.common import web_login
from com.ea.common import web_menu
from com.ea.common import web_loan


class MyTestCase(unittest.TestCase):
    u"""流通贷-厂家-共享"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    pic_path = gl.test_pic_path
    cardNo = IdCardNumber.getRandomIdNumber(1)[0]
    fullname, first_name, second_name, full_english_name, first_english_name, last_english_name = cardname.get_names()
    phoneNo = cardname.createPhone()
    loanno = None
    dakuandanhao = None
    partner_zx_no = ""
    loan_type = "流通贷-厂家"
    operate_mode = "共享模式"
    marry_status = "已婚"
    bank_name = "浦发广州分行"
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
        if cls.driver:
            cls.driver.quit()
        if cls.webdriver:
            cls.webdriver.quit()

    # @unittest.skip("skip")
    def test_a_loan_apply(self):
        """申请贷款"""
        casename = sys._getframe().f_code.co_name
        print("申请贷款用例开始")
        print("使用的身份证号是:", self.cardNo)
        sumofmoney = "150000"
        channel_name = "深圳"
        from com.ea.common import loan
        MyTestCase.loanno, MyTestCase.partner_zx_no = loan.loan_zhengxin_apply(self.driver, self.loan_type, self.cardNo, self.first_name, self.second_name, self.first_english_name, self.last_english_name, self.phoneNo, gl.xd_manager_name,
                                                                               sumofmoney, self.bank_name, self.operate_mode, channel_name, self.screenshot_path, casename, marry_status=self.marry_status)

    # @unittest.skip("skip")
    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        zx_no = tools.get_zx_no_by_cardno(self.cardNo)
        # zx_no = "O2OZX-1804-00967"
        casename = sys._getframe().f_code.co_name
        from com.ea.common import zhengxin
        zhengxin.zhengxin_approve(self.driver, zx_no, self.screenshot_path, casename, partner_zx_no=self.partner_zx_no)

    # @unittest.skip("skip")
    def test_c_put_photo(self):
        u"""上传客户照片"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import put_my_customer_photo
        # self.fullname = '谈请'
        put_my_customer_photo.put_my_customer_photo(self.driver, self.fullname, self.screenshot_path, casename)

    # @unittest.skip("skip")
    def test_d_loan_approve(self):
        """审批贷款"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "YN010-BP-1808-00012"
        web_loan.loan_approve(self.webdriver, self.loanno, self.screenshot_path, casename)

    def test_e_edit_inside_apply(self):
        u"""编辑内部审批"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import inside
        inside.inside_apply(self.webdriver, self.loanno, self.fullname, self.loan_type, self.marry_status, self.bank_name, self.screenshot_path, casename)

    @unittest.skip('skip')
    def test_e_edit_inside_applys(self):
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
        register_time = "2012-10-10"
        shareholder_number = "1"
        share_proportion = "100"
        business_isnormal = "无"
        borrower_iscontroler = "是"
        controler_name = self.fullname
        yingye_mode = "便利店"
        vocation_type = "百货"
        start_time = "2017-10-10"
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
        store_date = "2016-10-10"
        area = "20"
        shoprent_year = "20000"
        shoprent_starttime = "2017-01-01"
        shoprent_endtime = "2017-05-05"
        store_value = "500000"
        new_old = "很新"
        zhengqi = "整齐"
        store_description = "这里是存货效期描述"
        channel_product = "酒水"
        month_hezuojine = "50000"
        yuqudaoqiyehezuoqishishijian = "2018-04-03"
        supplier = "贵州茅台"
        hezuo_product = "飞天茅台"
        caigouzhanbi = "50"
        zhangqi = "30"
        main_product = "飞天茅台"
        brand = "茅台"
        buyin_price = "1000"
        model = "飞天茅台"
        selling_price = "1500"
        lastmonth_sales = "20000"
        loan_time = "6个月"
        huankuan_type = "等额本息"
        loan_yongtu = "流动资金"
        eamount = "100000"
        # tuijian_type = "合作方推荐"
        # tuijian_name = "李超"
        danbao_type = "其它方式"
        year_sales = "200"
        lianbao_daikuan_yue = "0"
        jiufen = "否"
        yuqi_cishu = "0"
        zonghe_feilv = "15.00%"

        # self.loanno = "YN010-BP-1808-00012"
        print("开始编辑内部审批")
        print("使用的贷款单号是:" + self.loanno)
        try:
            web_login.login(self.webdriver)
            from com.ea.pages.web_inside_page import WebInsidePage
            webinsidepage = WebInsidePage(self.webdriver)
            web_menu.go_to_inside_approve(self.webdriver)
            handle1 = self.webdriver.current_window_handle
            webinsidepage.click_first_row(self.loanno)
            handles = self.webdriver.window_handles
            handle2 = ""
            for handle in handles:
                if handle != handle1:
                    self.webdriver.switch_to.window(handle)
                    handle2 = self.webdriver.current_window_handle
            time.sleep(2)
            webinsidepage.click_editinside_button()
            handles = self.webdriver.window_handles
            for handle in handles:
                if handle != handle1 and handle != handle2:
                    self.webdriver.switch_to.window(handle)
            # 借款人基本信息
            webinsidepage.click_editborrower_button()
            webinsidepage.input_card_organization(organization)
            webinsidepage.input_home_phone(home_phone)
            webinsidepage.input_wechat(wechat)
            webinsidepage.input_postcode(postcode)
            webinsidepage.select_register_addr_province(province)
            time.sleep(1)
            webinsidepage.select_register_addr_city(city)
            webinsidepage.input_register_addr_road(road)
            webinsidepage.select_sleep_addr_province(province)
            time.sleep(1)
            webinsidepage.select_sleep_addr_city(city)
            webinsidepage.input_sleep_addr_road(road)
            webinsidepage.input_live_years(live_years)
            if self.marry_status == "已婚":
                webinsidepage.select_marry_date()
            webinsidepage.input_children(children_description)
            webinsidepage.click_borrower_save()
            webinsidepage.click_borrower_confirm()
            time.sleep(3)
            # 配偶基本信息
            if self.marry_status == "已婚":
                webinsidepage.scroll_to_partner_edit()
                webinsidepage.click_partner_edit()
                webinsidepage.input_card_organization(organization)
                webinsidepage.input_wechat(wechat)
                webinsidepage.select_register_addr_province(province)
                time.sleep(1)
                webinsidepage.select_register_addr_city(city)
                webinsidepage.input_register_addr_road(road)
                webinsidepage.input_work_unit(organization)
                webinsidepage.click_partner_save()
                webinsidepage.click_partner_confirm()
                time.sleep(2)
            # 添加紧急联系人
            webinsidepage.scroll_to_contact()
            time.sleep(1)
            for i in range(2):
                webinsidepage.click_contact_add()
                webinsidepage.input_contact_name(contact_names[i])
                webinsidepage.input_contact_phone(contact_phones[i])
                webinsidepage.select_contacts_relationship(relationship)
                webinsidepage.click_contact_save()
                time.sleep(2)
            time.sleep(2)
            # 夫妻双方负债情况
            webinsidepage.scroll_to_fuqishuangfangfuzhaiqingkuang()
            webinsidepage.click_edit_fuzhai()
            webinsidepage.input_total_price(total_price)
            webinsidepage.input_mj_price(mj_price)
            webinsidepage.click_fuzhai_save()
            time.sleep(1)
            # 经营主体信息
            webinsidepage.scroll_to_jingyingzhuti_edit_button()
            time.sleep(1)
            webinsidepage.click_jingyingzhuti_edit()
            webinsidepage.input_yingyezhizhao_name(zhizhao_name)
            webinsidepage.input_zhucehao(register_no)
            webinsidepage.select_organization_type(organization_type)
            webinsidepage.input_register_time(register_time)
            webinsidepage.select_zhizhao_addr_province(province)
            time.sleep(1)
            webinsidepage.select_zhizhao_addr_city(city)
            webinsidepage.input_zhizhao_addr_road(road)
            webinsidepage.select_office_addr_province(province)
            time.sleep(1)
            webinsidepage.select_office_addr_city(city)
            webinsidepage.input_office_addr_road(road)
            webinsidepage.input_shareholder_number(shareholder_number)
            webinsidepage.input_share_proportion(share_proportion)
            webinsidepage.select_business_isnormal(business_isnormal)
            webinsidepage.select_borrower_iscontroler(borrower_iscontroler)
            webinsidepage.input_controler_name(controler_name)
            webinsidepage.select_yingye_mode(yingye_mode)
            webinsidepage.select_vocation_type(vocation_type)
            webinsidepage.input_start_time(start_time)
            webinsidepage.click_zhuti_submit_button()
            time.sleep(3)
            # 经营历史
            webinsidepage.scroll_to_jingyinglishi()
            webinsidepage.click_history_add()
            webinsidepage.click_years()
            webinsidepage.input_jingli(jinglirun)
            webinsidepage.input_fuzhaizonge(fuzhaizonge)
            webinsidepage.input_nianxiaoshoue(nianxiaoshoue)
            webinsidepage.click_history_save_button()
            time.sleep(2)
            # 近6个月营业额情况
            webinsidepage.scroll_to_jinliugeyueyingyee()
            webinsidepage.click_six_month_edit()
            webinsidepage.input_january(six_month_sales)
            webinsidepage.input_february(six_month_sales)
            webinsidepage.input_march(six_month_sales)
            webinsidepage.input_april(six_month_sales)
            webinsidepage.input_may(six_month_sales)
            webinsidepage.input_june(six_month_sales)
            webinsidepage.click_six_month_submit()
            time.sleep(2)
            # 编辑经营状况
            webinsidepage.scroll_to_jingyingzhuangkuang()
            webinsidepage.click_edit_status()
            webinsidepage.input_personnel_number(personnel_number)
            webinsidepage.input_month_pay(month_pay)
            webinsidepage.input_water_pay(water_pay)
            webinsidepage.input_other_pay(other_pay)
            webinsidepage.input_transport_pay(transport_pay)
            webinsidepage.input_capital(capital)
            webinsidepage.input_nianjinglirun(nianjinglirun)
            webinsidepage.click_bank_water()
            webinsidepage.input_should_pay(should_pay)
            webinsidepage.input_collect(collect)
            webinsidepage.input_liabilities(liabilities)
            webinsidepage.input_invest(invest)
            webinsidepage.click_status_save_button()
            time.sleep(2)
            # 新增门店信息
            webinsidepage.scroll_to_store()
            time.sleep(1)
            webinsidepage.click_store_add_button()
            webinsidepage.select_property_type(property_type)
            webinsidepage.input_env_description(env_description)
            webinsidepage.input_store_phone(store_phone)
            webinsidepage.input_store_date(store_date)
            webinsidepage.select_store_addr_province(province)
            time.sleep(1)
            webinsidepage.select_store_addr_city(city)
            webinsidepage.input_store_addr_road(road)
            webinsidepage.input_business_area(area)
            webinsidepage.input_shoprent_year(shoprent_year)
            webinsidepage.input_shoprent_starttime(shoprent_starttime)
            webinsidepage.input_shoprent_endtime(shoprent_endtime)
            webinsidepage.input_store_value(store_value)
            webinsidepage.select_new_old(new_old)
            webinsidepage.select_zhengqi(zhengqi)
            webinsidepage.input_store_description(store_description)
            webinsidepage.click_store_submit()
            time.sleep(2)
            # 编辑渠道数据
            webinsidepage.scroll_to_channel()
            webinsidepage.click_channel_edit_button()
            webinsidepage.input_channel_product(channel_product)
            webinsidepage.input_month_hezuojine(month_hezuojine)
            webinsidepage.input_yuqudaoqiyehezuoqishishijian(yuqudaoqiyehezuoqishishijian)
            webinsidepage.click_channel_save_button()
            time.sleep(2)
            # 增加上游信息
            webinsidepage.scroll_to_shangyouxinxi()
            webinsidepage.click_shangyou_add_button()
            webinsidepage.input_supplier(supplier)
            webinsidepage.input_hezuo_product(hezuo_product)
            webinsidepage.input_caigouzhanbi(caigouzhanbi)
            webinsidepage.input_zhangqi(zhangqi)
            webinsidepage.click_shangyou_save_button()
            webinsidepage.click_ok_button()
            time.sleep(2)
            # 增加主要销售产品
            webinsidepage.scroll_to_main_product()
            time.sleep(1)
            webinsidepage.click_main_product_add()
            webinsidepage.input_main_product_name(main_product)
            webinsidepage.input_brand(brand)
            webinsidepage.input_buyin_price(buyin_price)
            webinsidepage.input_model(model)
            webinsidepage.input_selling_price(selling_price)
            webinsidepage.input_lastmonth_sales(lastmonth_sales)
            webinsidepage.click_main_product_save_button()
            webinsidepage.click_ok_button()
            time.sleep(1)
            # 编辑调查结论
            webinsidepage.scroll_to_diaochajielun()
            webinsidepage.click_diaochajielun_edit()
            webinsidepage.input_diaochajielun()
            webinsidepage.click_diaochajielun_commit_button()
            # 编辑贷款信息
            webinsidepage.scroll_to_loan_info()
            time.sleep(1)
            webinsidepage.input_year_sales(year_sales)
            webinsidepage.input_lianbao_daikuan_yue(lianbao_daikuan_yue)
            webinsidepage.select_shifou_xindai_jiufen(jiufen)
            # webinsidepage.input_near_24month_yuqi_cishu(yuqi_cishu)
            webinsidepage.select_loan_time(loan_time)
            webinsidepage.select_huankuan_type(huankuan_type)
            webinsidepage.input_eamount(eamount)
            webinsidepage.select_loan_yongtu(loan_yongtu)
            webinsidepage.select_loan_bankname(self.bank_name)
            webinsidepage.select_zonghe_feilv(zonghe_feilv)
            # insidepage.select_tuijian_type(tuijian_type)
            # insidepage.input_tuijian_name(tuijian_name)
            webinsidepage.select_danbao_type(danbao_type)
            webinsidepage.click_loan_info_save()
            webinsidepage.click_loan_info_confirm()
            webinsidepage.scroll_to_put_photo()
            webinsidepage.click_put_photo()
            webinsidepage.click_photo()
            webinsidepage.click_put_photo_save_button()
            time.sleep(2)
            self.webdriver.close()
            # 切换到内审详情页面
            self.webdriver.switch_to.window(handle2)
            webinsidepage.click_submit_inside_approve()
            time.sleep(1)
            # 关闭内审详情页面
            self.webdriver.close()
            # 切换到内部审批页面
            self.webdriver.switch_to.window(handle1)
            # 刷新页面
            self.webdriver.refresh()
            actual_result = webinsidepage.get_result(self.loanno)
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

    # @unittest.skip("skip")
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
    #     channel_product = "酒水"
    #     zhongyaogongyingshang = "茅台"
    #     hezuo_product = "飞天茅台"
    #     zhangqi = "30"
    #     main_product = "飞天茅台"
    #     brand = "茅台"
    #     buyin_price = "1000"
    #     model = "飞天茅台"
    #     selling_price = "1500"
    #     lastmonth_sales = "20000"
    #     eamount = "50000"
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
    #         insidepage.input_yuqudaoqiyecaigoudechanpin(channel_product)
    #         insidepage.select_yuqudaoqiyehezuoqishishijian()
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 上游信息
    #         insidepage.click_shangyouxinxi()
    #         insidepage.click_add_button()
    #         insidepage.input_zhongyaogongyingshang(zhongyaogongyingshang)
    #         insidepage.input_hezuochanpin(hezuo_product)
    #         insidepage.input_zhangqi(zhangqi)
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         # 主要销售产品
    #         insidepage.click_zhuyaoxiaoshouchanpin()
    #         insidepage.click_add_button()
    #         insidepage.input_product_name(main_product)
    #         insidepage.input_pinpai(brand)
    #         insidepage.input_jinhuojia(buyin_price)
    #         insidepage.input_xinghao(model)
    #         insidepage.input_xiaohuojia(selling_price)
    #         insidepage.input_shangyuexiaoliang(lastmonth_sales)
    #         insidepage.click_save_button()
    #         time.sleep(2)
    #         self.driver.back()
    #         time.sleep(1)
    #         insidepage.click_start_flow()
    #         insidepage.click_confirm_text()
    #     except Exception as e:
    #         tools.screenshot(self.driver, self.screenshot_path, casename)
    #         raise e

    # @unittest.skip("skip")
    def test_f_inside_approve(self):
        u"""审批内部审批"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import inside
        # self.loanno = 'HEN070-BP-1806-00012'
        inside.inside_approve(self.driver, self.loanno, self.screenshot_path, casename)

    # @unittest.skip("skip")
    def test_g_pay_money_apply(self):
        u"""新建打款流程"""
        casename = sys._getframe().f_code.co_name
        # self.fullname = "康高"
        # self.cardNo = "330600197701294592"
        from com.ea.common import pay_money
        MyTestCase.dakuandanhao = pay_money.pay_money_apply(self.driver, self.fullname, self.cardNo, self.screenshot_path, casename)

    # @unittest.skip("skip")
    def test_h_pay_money_approve(self):
        u"""审批打款流程"""
        casename = sys._getframe().f_code.co_name
        # self.dakuandanhao = "DK-1808-00057"
        from com.ea.common import pay_money
        pay_money.pay_money_approve(self.webdriver, self.dakuandanhao, self.screenshot_path, casename)
        # webdriver.quit()

    # @unittest.skip("skip")
    def test_i_interview_apply(self):
        u"""面签提报"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "YN010-BP-1808-00013"
        from com.ea.common import interview
        interview.interview_apply(self.driver, self.loanno, self.screenshot_path, casename)
        # self.driver.quit()

    # @unittest.skip("skip")
    def test_j_interview_approve(self):
        u"""面签审批"""
        from com.ea.common import interview
        casename = sys._getframe().f_code.co_name
        # self.fullname = "康高"
        # self.loanno = "YN010-BP-1808-00013"
        interview.interview_approve(self.webdriver, self.loanno, self.fullname, self.screenshot_path, casename)


if __name__ == '__main__':
    unittest.main()
