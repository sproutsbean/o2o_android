#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: add_factory_page.py 
@time: 2018/01/19 
"""
from com.ea.common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LoanApplyListPage(BasePage):
    first_row_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout')

    shenheliucheng_loc = (By.XPATH, '//android.widget.TextView[@text="审核流程"]/..')
    daikuan_jiben_ziliao_loc = (By.XPATH, '//android.widget.TextView[@text="贷款基本资料"]/..')
    jiekuanren_jiben_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="借款人基本信息"]/..')
    jiekuanren_peiou_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="借款人配偶基本信息"]/..')
    kehu_zichan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="客户资产信息"]/..')  # add
    # daikuan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="贷款信息"]/..') #neishen
    mendian_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="门店信息"]/..')
    jinji_lianxiren_loc = (By.XPATH, '//android.widget.TextView[@text="紧急联系人"]/..')
    fuqi_fuzhai_qingkuang_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方负债情况"]/..')
    fuqi_fangchan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方房产信息"]/..')
    fuqi_chechan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方车产信息"]/..')
    fuqi_qita_zichan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方其他资产信息"]/..')
    jingying_zhuti_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="经营主体信息"]/..')

    qiye_guanlian_daikuan_jilu_loc = (By.XPATH, '//android.widget.TextView[@text="企业关联贷款记录"]/..')
    jingying_lishi_loc = (By.XPATH, '//android.widget.TextView[@text="经营历史"]/..')
    jinliugeyue_yingyee_qingkuang_loc = (By.XPATH, '//android.widget.TextView[@text="近六个月营业额情况"]/..')
    jingying_zhuangkuang_loc = (By.XPATH, '//android.widget.TextView[@text="经营状况"]/..')
    cangku_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="仓库信息"]/..')
    qudao_shuju_loc = (By.XPATH, '//android.widget.TextView[@text="渠道数据"]/..')
    shangyou_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="上游信息"]/..')
    xiayou_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="下游信息"]/..')
    zhuyao_xiaoshou_chanpin_loc = (By.XPATH, '//android.widget.TextView[@text="主要销售产品"]/..')
    anfang_neirong_loc = (By.XPATH, '//android.widget.TextView[@text="暗访内容"]/..')
    diaocha_jielun_loc = (By.XPATH, '//android.widget.TextView[@text="调查结论"]/..')

    shenpi_baogao_loc = (By.XPATH, '//android.widget.TextView[@text="审批报告"]/..')
    fuqi_zhengxin_fuzhai_qingkuang_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方征信负债情况"]/..')
    jiekuanren_zhengxin_fujian_loc = (By.XPATH, '//android.widget.TextView[@text="借款人征信附件"]/..')
    qiye_zhengxin_baogao_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="企业征信报告信息"]/..')
    qiye_zhengxin_fujian_loc = (By.XPATH, '//android.widget.TextView[@text="企业征信附件"]/..')
    peiou_zhengxin_fujian_loc = (By.XPATH, '//android.widget.TextView[@text="配偶征信附件"]/..')
    buchong_zhengxin_fujian_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="补充征信附件信息"]/..')
    qita_fujian_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="其他附件信息"]/..')
    caiwu_shenhe_sd_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="财务审核SD信息"]/..')
    sd_xitong_jiaoyi_jilu_huizongbiao_loc = (By.XPATH, '//android.widget.TextView[@text="SD系统交易记录汇总表"]/..')
    caiwu_shenhe_jilu_loc = (By.XPATH, '//android.widget.TextView[@text="财务审核记录"]/..')
    shenpi_edu_yu_shoufei_feilv_loc = (By.XPATH, '//android.widget.TextView[@text="审批额度与收费费率"]/..')
    fuqi_daikuan_jilu_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方的贷款记录"]/..')
    daichang_he_yuqi_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="代偿和逾期信息"]/..')
    fuqi_danbao_daikuan_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方担保贷款信息"]/..')
    danbaoren_xiangqing_loc = (By.XPATH, '//android.widget.TextView[@text="担保人详情"]/..')
    baozhengjin_guanlifei_loc = (By.XPATH, '//android.widget.TextView[@text="保证金、管理费和风险补偿金详情"]/..')  # add
    huankuan_jihua_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="还款计划信息"]/..')  # add

    # jiekuanren_qiye_zhengxin_baogao_loc = (By.XPATH, '//android.widget.TextView[@text="借款人企业征信报告"]/..')  # add
    # dianhe_fankui_loc = (By.XPATH, '//android.widget.TextView[@text="电核反馈"]/..')
    # yinhangka_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="银行卡信息"]/..')
    # danbaoren_loc = (By.XPATH, '//android.widget.TextView[@text="担保人"]/..')

    # fuqi_zhengxin_baogao_xinxi_loc = (By.XPATH, '//android.widget.TextView[@text="夫妻双方征信报告信息"]/..')
    def get_first_row_status(self):
        status = self.find_element(*(By.XPATH, '//android.widget.TextView[@text="申请状态"]/following-sibling::android.widget.TextView')).text
        print("第一条记录的状态是:", status)
        return status

    def click_first_row(self):
        print("点击第一条记录")
        self.find_element(*self.first_row_loc).click()

    def click_shenheliucheng(self):
        print("点击审核流程")
        self.find_element(*self.shenheliucheng_loc).click()

    def click_daikuan_jiben_ziliao(self):
        print("点击贷款基本资料")
        self.find_element(*self.daikuan_jiben_ziliao_loc).click()

    def click_jiekuanren_jiben_xinxi(self):
        print("点击借款人基本信息")
        self.find_element(*self.jiekuanren_jiben_xinxi_loc).click()
        marry_status = self.find_element(*(By.XPATH, '//android.widget.TextView[@text="婚姻状况:"]/following-sibling::android.widget.LinearLayout/android.widget.TextView')).text
        print("婚姻状况是:", marry_status)
        return marry_status

    def click_jiekuanren_peiou_xinxi(self):
        print("点击借款人配偶基本信息")
        self.find_element(*self.jiekuanren_peiou_xinxi_loc).click()

    # def click_daikuan_xinxi(self):
    #     self.find_element(*self.daikuan_xinxi_loc).click()

    def click_jinji_lianxiren(self):
        print("点击紧急联系人")
        self.find_element(*self.jinji_lianxiren_loc).click()

    def click_fuqi_fuzhai_qingkuang(self):
        print("点击夫妻双方负债情况")
        self.find_element(*self.fuqi_fuzhai_qingkuang_loc).click()

    def click_fuqi_fangchan_xinxi(self):
        print("点击夫妻双方房产信息")
        self.find_element(*self.fuqi_fangchan_xinxi_loc).click()

    def click_fuqi_chechan_xinxi(self):
        print("点击夫妻双方车产信息")
        self.find_element(*self.fuqi_chechan_xinxi_loc).click()

    def click_fuqi_qita_zichan_xinxi(self):
        print("点击夫妻双方其他资产信息")
        self.find_element(*self.fuqi_qita_zichan_xinxi_loc).click()

    def click_jingying_zhuti_xinxi(self):
        print("点击经营主体信息")
        self.find_element(*self.jingying_zhuti_xinxi_loc).click()

    def click_qiye_guanlian_daikuan_jilu(self):
        print("点击企业关联贷款记录")
        self.find_element(*self.qiye_guanlian_daikuan_jilu_loc).click()

    def click_jingying_lishi(self):
        print("点击经营历史")
        self.find_element(*self.jingying_lishi_loc).click()

    def click_jinliugeyue_yingyee_qingkuang(self):
        print("点击近六个月营业额情况")
        self.find_element(*self.jinliugeyue_yingyee_qingkuang_loc).click()

    def click_jingying_zhuangkuang(self):
        print("点击经营状况")
        self.find_element(*self.jingying_zhuangkuang_loc).click()

    def click_mendian_xinxi(self):
        print("点击门店信息")
        self.find_element(*self.mendian_xinxi_loc).click()

    def click_cangku_xinxi(self):
        print("点击仓库信息")
        self.find_element(*self.cangku_xinxi_loc).click()

    def click_qudao_shuju(self):
        print("点击渠道数据")
        self.find_element(*self.qudao_shuju_loc).click()

    def click_shangyou_xinxi(self):
        print("点击上游信息")
        self.find_element(*self.shangyou_xinxi_loc).click()

    def click_xiayou_xinxi(self):
        print("点击下游信息")
        self.find_element(*self.xiayou_xinxi_loc).click()

    def click_zhuyao_xiaoshou_chanpin(self):
        print("点击主要销售产品")
        self.find_element(*self.zhuyao_xiaoshou_chanpin_loc).click()

    def click_anfang_neirong(self):
        print("点击暗访内容")
        self.find_element(*self.anfang_neirong_loc).click()

    def click_diaocha_jielun(self):
        print("点击调查结论")
        self.find_element(*self.diaocha_jielun_loc).click()

    def click_shenpi_baogao(self):
        print("点击审批报告")
        self.find_element(*self.shenpi_baogao_loc).click()

    def click_fuqi_zhengxin_fuzhai_qingkuang(self):
        print("点击夫妻双方征信负债情况")
        self.find_element(*self.fuqi_zhengxin_fuzhai_qingkuang_loc).click()

    def click_jiekuanren_zhengxin_fujian(self):
        print("点击借款人征信附件")
        self.find_element(*self.jiekuanren_zhengxin_fujian_loc).click()

    # def click_jiekuanren_qiye_zhengxin_baogao(self):
    #     self.find_element(*self.jiekuanren_qiye_zhengxin_baogao_loc).click()

    def click_qiye_zhengxin_baogao_xinxi(self):
        print("点击企业征信报告信息")
        self.find_element(*self.qiye_zhengxin_baogao_xinxi_loc).click()

    def click_qiye_zhengxin_fujian(self):
        print("点击企业征信附件")
        self.find_element(*self.qiye_zhengxin_fujian_loc).click()

    def click_peiou_zhengxin_fujian(self):
        print("点击配偶征信附件")
        self.find_element(*self.peiou_zhengxin_fujian_loc).click()

    def click_buchong_zhengxin_fujian_xinxi(self):
        print("点击补充征信附件信息")
        self.find_element(*self.buchong_zhengxin_fujian_xinxi_loc).click()

    def click_qita_fujian_xinxi(self):
        print("点击其他附件信息")
        self.find_element(*self.qita_fujian_xinxi_loc).click()

    def click_caiwu_shenhe_sd_xinxi(self):
        print("点击财务审核SD信息")
        self.find_element(*self.caiwu_shenhe_sd_xinxi_loc).click()

    def click_sd_xitong_jiaoyi_jilu_huizongbiao(self):
        print("点击SD系统交易记录汇总表")
        self.find_element(*self.sd_xitong_jiaoyi_jilu_huizongbiao_loc).click()

    # def click_yinhangka_xinxi(self):
    #     self.find_element(*self.yinhangka_xinxi_loc).click()

    def click_shenpi_edu_yu_shoufei_feilv(self):
        print("点击审批额度与收费费率")
        self.find_element(*self.shenpi_edu_yu_shoufei_feilv_loc).click()

    # def click_fuqi_zhengxin_baogao_xinxi(self):
    #     self.find_element(*self.fuqi_zhengxin_baogao_xinxi_loc).click()

    def click_fuqi_daikuan_jilu(self):
        print("点击夫妻双方的贷款记录")
        self.find_element(*self.fuqi_daikuan_jilu_loc).click()

    def click_daichang_he_yuqi_xinxi(self):
        print("点击代偿和逾期信息")
        self.find_element(*self.daichang_he_yuqi_xinxi_loc).click()

    def click_fuqi_danbao_daikuan_xinxi(self):
        print("点击夫妻双方担保贷款信息")
        self.find_element(*self.fuqi_danbao_daikuan_xinxi_loc).click()

    def click_danbaoren_xiangqing(self):
        print("点击担保人详情")
        self.find_element(*self.danbaoren_xiangqing_loc).click()

    # def click_danbaoren(self):
    #     self.find_element(*self.danbaoren_loc).click()

    def click_caiwu_shenhe_jilu(self):
        print("点击财务审核记录")
        self.find_element(*self.caiwu_shenhe_jilu_loc).click()

    # def click_dianhe_fankui(self):
    #     self.find_element(*self.dianhe_fankui_loc).click()

    def click_kehu_zichan_xinxi(self):
        print("点击客户资产信息")
        self.find_element(*self.kehu_zichan_xinxi_loc).click()

    def click_baozhengjin_guanlifei(self):
        print("点击保证金管理费")
        self.find_element(*self.baozhengjin_guanlifei_loc).click()

    def click_huankuan_jihua_xinxi(self):
        print("点击还款计划信息")
        self.find_element(*self.huankuan_jihua_xinxi_loc).click()
