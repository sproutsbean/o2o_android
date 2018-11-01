#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: inside_page.py 
@time: 2018/03/13 
"""

from com.ea.common.base_page import BasePage
from appium.webdriver.webdriver import By
import time


class InsidePage(BasePage):
    filter_loc = (By.XPATH, "//android.widget.TextView[@text='筛选']")
    loan_no_loc = (By.XPATH, '//android.widget.TextView[@text="贷款单号:"]/following-sibling::android.widget.LinearLayout/android.widget.EditText[@text="请输入"]')
    search_button_loc = (By.XPATH, "//android.widget.Button[@text='搜索']")
    more_button_loc = (By.XPATH, '//android.widget.TextView[@text="详情"]/../following-sibling::android.widget.RelativeLayout')
    start_flow_loc = (By.XPATH, "//android.widget.CheckedTextView[@text='启动流程']")

    def get_status_by_danhao(self, danhao):
        return self.find_element(*(By.XPATH, '//android.widget.TextView[@text="' + danhao + '"]/../../..//android.widget.TextView[@text="单据状态"]/following-sibling::android.widget.TextView')).text

    def click_filter_button(self):
        self.find_element(*self.filter_loc).click()

    def input_loanno(self, loanno):
        self.send_keys(self.loan_no_loc, loanno)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    def click_more_button(self):
        self.find_element(*self.more_button_loc).click()

    def click_start_flow(self):
        self.find_element(*self.start_flow_loc).click()

    # 借款人基本信息
    borrower_info_loc = (By.XPATH, "//android.widget.TextView[@text='借款人基本信息']")
    edit_button_loc = (By.XPATH, "//android.widget.TextView[@text='编辑']")
    organization_loc = (By.XPATH, "//android.widget.TextView[@text='发证机构:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    education_loc = (By.XPATH, "//android.widget.TextView[@text='学历:']")
    marry_status_loc = (By.XPATH, "//android.widget.TextView[@text='婚姻状况:']")
    borrower_name_loc = (By.XPATH, "//android.widget.TextView[@text='借款人姓:']")
    wechat_no_loc = (By.XPATH, "//android.widget.TextView[@text='微信号:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    home_phone_loc = (By.XPATH, "//android.widget.TextView[@text='住宅电话:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    post_code_loc = (By.XPATH, "//android.widget.TextView[@text='单位邮编:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    hukousuozaidi_loc = (By.XPATH, "//android.widget.TextView[@text='借款人户口所在地:']")
    hukousuozaidi_value_loc = (By.XPATH, "//android.widget.TextView[@text='本市内']")
    hujidizhi_loc = (By.XPATH, "//android.widget.TextView[@text='户籍地址:']")
    hujidizhi_info_loc = (By.XPATH, "//android.widget.Button[@text='确定']/../../preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    confirm_button_loc = (By.XPATH, "//android.widget.Button[@text='确定']")
    confirm_text_loc = (By.XPATH, "//android.widget.TextView[@text='确定']")
    live_addr_loc = (By.XPATH, "//android.widget.TextView[@text='居住地址:']")
    live_addr_info_loc = (By.XPATH, "//android.widget.Button[@text='确定']/../../preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    live_years_loc = (By.XPATH, "//android.widget.TextView[@text='居住年限:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    children_info_loc = (By.XPATH, "//android.widget.TextView[@text='子女情况']")
    children_info_edit_loc = (By.XPATH, "//android.widget.EditText[@index='1']")
    save_button_loc = (By.XPATH, "//android.widget.TextView[@text='保存']")
    other_info_loc = (By.XPATH, "//android.widget.TextView[@text='其他信息描述']")
    other_info_edit_loc = (By.XPATH, "//android.widget.EditText[@index='1']")
    # 贷款信息
    daikuanxinxi_loc = (By.XPATH, "//android.widget.TextView[@text='贷款信息']")
    jibenxinxi_loc = (By.XPATH, "//android.widget.TextView[@text='基本信息']")
    daikuanqixian_loc = (By.XPATH, "//android.widget.TextView[@text='贷款期限:']")
    daikuanqixian_value_loc = (By.XPATH, "//android.widget.TextView[@text='6个月']")
    huankuanfangshi_loc = (By.XPATH, "//android.widget.TextView[@text='还款方式:']")
    huankuanfangshi_value_loc = (By.XPATH, "//android.widget.TextView[@text='等额本息']")
    eapifuedu_loc = (By.XPATH, "//android.widget.TextView[@text='EA批复额度:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    daikuanyongtu_loc = (By.XPATH, "//android.widget.TextView[@text='贷款用途:']")
    daikuanyongtu_value_loc = (By.XPATH, "//android.widget.TextView[@text='流动资金']")
    songshenyinhang_loc = (By.XPATH, "//android.widget.TextView[@text='送审银行:']")
    songshenyinhang_value_loc = (By.XPATH, "//android.widget.TextView[@text='江西银行']")
    danbaofangshi_loc = (By.XPATH, "//android.widget.TextView[@text='担保方式:']")
    danbaofangshi_value_loc = (By.XPATH, "//android.widget.TextView[@text='其它方式']")

    # 紧急联系人
    jinjilianxiren_loc = (By.XPATH, "//android.widget.TextView[@text='紧急联系人']")
    add_button_loc = (By.XPATH, "//android.widget.TextView[@text='新增']")
    contacts_name_loc = (By.XPATH, "//android.widget.EditText[@text='请输入姓名']")
    guanxi_loc = (By.XPATH, "//android.widget.TextView[@text='与借款人关系:']")
    guanxi_value_loc = (By.XPATH, "//android.widget.TextView[@text='朋友']")
    contact_phone_loc = (By.XPATH, "//android.widget.EditText[@text='请输入联系电话']")
    contact_addr_loc = (By.XPATH, "//android.widget.EditText[@text='请输入联系地址']")
    # 夫妻双方负债情况
    fuqishuangfangfuzhaiqingkuang_loc = (By.XPATH, "//android.widget.TextView[@text='夫妻双方负债情况']")
    total_zichan_loc = (By.XPATH, "//android.widget.EditText[@text='请输入资产总计']")
    zichanxinximiaoshu_loc = (By.XPATH, "//android.widget.TextView[@text='资产信息描述']")
    zichanxinximiaoshu_value_loc = (By.XPATH, "//android.widget.EditText[@text='请输入资产信息描述']")
    minjianjiedai_loc = (By.XPATH, "//android.widget.EditText[@text='请输入民间借贷']")
    fuzhaixinximiaoshu_loc = (By.XPATH, "//android.widget.TextView[@text='负债信息描述']")
    fuzhaixinximiaoshu_value_loc = (By.XPATH, "//android.widget.EditText[@text='请输入负债信息描述']")
    # 经营主体信息
    jingyingzhuti_info_loc = (By.XPATH, "//android.widget.TextView[@text='经营主体信息']")
    yingyezhizhao_name_loc = (By.XPATH, "//android.widget.TextView[@text='营业执照名称:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    yingyezhizhao_zhucehao_loc = (By.XPATH, "//android.widget.TextView[@text='营业执照注册号:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    zuzhixingshi_loc = (By.XPATH, "//android.widget.TextView[@text='组织形式:']")
    zuzhixingshi_value_loc = (By.XPATH, "//android.widget.TextView[@text='个体工商户']")
    register_time_loc = (By.XPATH, "//android.widget.EditText[@text='请选择注册时间']")
    yingyezhizhao_addr_loc = (By.XPATH, "//android.widget.TextView[@text='营业执照地址:']")
    yingyezhizhao_addr_value_loc = (By.XPATH, "//android.widget.Button[@text='确定']/../../preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    office_addr_loc = (By.XPATH, "//android.widget.TextView[@text='办公地址:']")
    office_addr_value_loc = (By.XPATH, "//android.widget.Button[@text='确定']/../../preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    gudongrenshu_loc = (By.XPATH, "//android.widget.TextView[@text='股东人数（人）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    fuqizhangubili_loc = (By.XPATH, "//android.widget.TextView[@text='借款人夫妻占股比例(%):']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    gongshangyichang_loc = (By.XPATH, "//android.widget.TextView[@text='工商查询是否异常:']")
    gongshangyichang_value_loc = (By.XPATH, "//android.widget.TextView[@text='无']")
    borrower_is_controler_loc = (By.XPATH, "//android.widget.TextView[@text='借款人是否为实际控制人:']")
    borrower_iscontroler_value_loc = (By.XPATH, "//android.widget.TextView[@text='是']")
    controler_name_loc = (By.XPATH, "//android.widget.TextView[@text='实际控制人姓名:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    yingye_mode_loc = (By.XPATH, "//android.widget.TextView[@text='营业模式:']")
    yingye_mode_value_loc = (By.XPATH, "//android.widget.TextView[@text='一级批发']")
    hangye_leibie_loc = (By.XPATH, "//android.widget.TextView[@text='行业类别:']")
    hangye_leibie_value_loc = (By.XPATH, "//android.widget.TextView[@text='其他']")
    jingyingqishi_time_loc = (By.XPATH, "//android.widget.EditText[@text='请选择注册时间']")
    # 经营历史
    jingyinglishi_loc = (By.XPATH, "//android.widget.TextView[@text='经营历史']")
    jingli_loc = (By.XPATH, "//android.widget.EditText[@text='请输入净利（万元）']")
    fuzhaizonge_loc = (By.XPATH, "//android.widget.EditText[@text='请输入负债总额（万元）']")
    nianxiaoshoue_loc = (By.XPATH, "//android.widget.EditText[@text='请输入年销售额（元）']")
    # 近六个月营业额情况
    near_six_month_loc = (By.XPATH, "//android.widget.TextView[@text='近六个月营业额情况']")
    first_month_loc = (By.XPATH, "//android.widget.TextView[@text='第一个月（万元）:']")
    second_month_loc = (By.XPATH, "//android.widget.TextView[@text='第二个月（万元）:']")
    third_month_loc = (By.XPATH, "//android.widget.TextView[@text='第三个月（万元）:']")
    fourth_month_loc = (By.XPATH, "//android.widget.TextView[@text='第四个月（万元）:']")
    fifth_month_loc = (By.XPATH, "//android.widget.TextView[@text='第五个月（万元）:']")
    sixth_month_loc = (By.XPATH, "//android.widget.TextView[@text='第六个月（万元）:']")
    # 经营状况
    jingying_status_loc = (By.XPATH, "//android.widget.TextView[@text='经营状况']")
    yuangong_renshu_loc = (By.XPATH, "//android.widget.TextView[@text='员工人数:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    nianyingyee_yanzhengcailiao_loc = (By.XPATH, "//android.widget.TextView[@text='年营业额的验证资料:']/following-sibling::android.widget.TextView[2]")
    bank_liushui_loc = (By.XPATH, "//android.widget.CheckBox[@index='0']")
    jingying_weijinshixiang_miaoshu_loc = (By.XPATH, "//android.widget.TextView[@text='经营信息未尽事项描述']")
    miaoshu_value_loc = (By.XPATH, "//android.widget.EditText[@index='1']")
    # 门店信息
    mendian_info_loc = (By.XPATH, "//android.widget.TextView[@text='门店信息']")
    chanquanxingzhi_loc = (By.XPATH, "//android.widget.TextView[@text='产权性质:']")
    chanquanxingzhi_value_loc = (By.XPATH, "//android.widget.TextView[@text='自有']")
    mendian_huanjing_miaoshu_loc = (By.XPATH, "//android.widget.TextView[@text='门店经营环境描述']")
    mendian_huanjing_miaoshu_value_loc = (By.XPATH, "//android.widget.EditText[@index='1']")
    mendian_phone_loc = (By.XPATH, "//android.widget.EditText[@text='请输入门店电话']")
    mendian_chengli_date_loc = (By.XPATH, "//android.widget.EditText[@text='请选择门店成立日期']")
    mendian_dizhi_loc = (By.XPATH, "//android.widget.EditText[@text='请输选择门店地址']")
    mendian_xiangxi_dizhi_loc = (By.XPATH, "//android.widget.EditText[@text='请选择区域后输入详细地址']")
    yingye_mianji_loc = (By.XPATH, "//android.widget.EditText[@text='请输入营业面积']")
    nian_zujin_loc = (By.XPATH, "//android.widget.EditText[@text='请输入年租金']")
    zudinghetongqizhiriqi_loc = (By.XPATH, "//android.widget.EditText[@text='请选择租赁合同起止日期']")
    jieshu_shijian_loc = (By.XPATH, "//android.widget.TextView[@text='结束时间']")
    cunhuojiazhiyugu_loc = (By.XPATH, "//android.widget.EditText[@text='请输入存货价值预估']")
    zhuangxiuxinjiuchengdu_loc = (By.XPATH, "//android.widget.TextView[@text='装修新旧程度:']")
    zhuangxiuxinjiuchengdu_value_loc = (By.XPATH, "//android.widget.TextView[@text='很新']")
    huojiashifouzhengqi_loc = (By.XPATH, "//android.widget.TextView[@text='货架是否整齐:']")
    huojiashifouzhengqi_value_loc = (By.XPATH, "//android.widget.TextView[@text='整齐']")
    cunhuoxiaoqimiaoshu_loc = (By.XPATH, "//android.widget.TextView[@text='存货效期描述']")
    cunhuoxiaoqimiaoshu_value_loc = (By.XPATH, "//android.widget.EditText[@index='1']")
    # 渠道数据
    qudao_shuju_loc = (By.XPATH, "//android.widget.TextView[@text='渠道数据']")
    yuqudaoqiyecaigoudechanpin_loc = (By.XPATH, "//android.widget.TextView[@text='与渠道企业采购的产品']")
    qudao_product_name_loc = (By.XPATH, "//android.widget.EditText[@index='1']")
    yuqudaoqiyehezuoqishishijian_loc = (By.XPATH, "//android.widget.EditText[@text='请输入']")
    # 商超渠道数据
    yubaimingdanneishangchaohezuokaishishijian_loc = (By.XPATH, "//android.widget.TextView[@text='与白名单内商超合作开始时间:']/following-sibling::android.widget.LinearLayout")
    # 蔬果渠道数据
    benshichangjingyingkaishishijian_loc = (By.XPATH, "//android.widget.TextView[@text='本市场经营开始时间:']/following-sibling::android.widget.LinearLayout")
    dangkouyouwuchewei_loc = (By.XPATH, "//android.widget.TextView[@text='档口有无车位:']")
    yes_loc = (By.XPATH, "//android.widget.TextView[@text='是']")
    # 主要供货渠道
    zhuyaogonghuoqudao_loc = (By.XPATH, "//android.widget.TextView[@text='主要供货渠道']")
    imgview_loc = (By.XPATH, "//android.widget.LinearLayout[@index='1']/android.widget.ImageView")
    erpishang_loc = (By.XPATH, "//android.widget.TextView[@text='二批商（近六个月销售占比）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    shangchao_loc = (By.XPATH, "//android.widget.TextView[@text='商超（近六个月销售占比）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    zhijielingshou_loc = (By.XPATH, "//android.widget.TextView[@text='直接零售（近六个月销售占比）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    lingshouzhongduan_loc = (By.XPATH, "//android.widget.TextView[@text='零售终端（近六个月销售占比）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    # 上游信息
    shangyou_info_loc = (By.XPATH, "//android.widget.TextView[@text='上游信息']")
    zhongyaogongyingshang_loc = (By.XPATH, "//android.widget.TextView[@text='重要供应商:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    hezuochanpin_loc = (By.XPATH, "//android.widget.TextView[@text='合作产品:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    zhangqi_loc = (By.XPATH, "//android.widget.TextView[@text='账期:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    # 蔬果上游信息
    shifouziyounongchang_loc = (By.XPATH, "//android.widget.TextView[@text='是否有自有农场:']")
    ziyounongchangdizhi_loc = (By.XPATH, "//android.widget.TextView[@text='自有农场地址:']")
    ziyounongchangdizhi_info_loc = (By.XPATH, "//android.widget.Button[@text='确定']/../../preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    shifouxianggudingnonghucaigou_loc = (By.XPATH, "//android.widget.TextView[@text='是否向固定农户采购:']")
    shifouxiangqitagongyingshangcaigou_loc = (By.XPATH, "//android.widget.TextView[@text='是否向其他供菜商采购:']")
    # 十大下游客户近6月供货量
    shidaxiayoukehugonghuoliang_loc = (By.XPATH, "//android.widget.TextView[@text='十大下游客户近6月供货量']")
    kehumingcheng_loc = (By.XPATH, "//android.widget.TextView[@text='客户名称:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    jiesuanzhangqi_loc = (By.XPATH, "//android.widget.TextView[@text='结算账期:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    gonghuoliang_loc = (By.XPATH, "//android.widget.TextView[@text='供货量:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    # 下游信息
    xiayouxinxi_loc = (By.XPATH, "//android.widget.TextView[@text='下游信息']")
    shuguo_erpishang_loc = (By.XPATH, "//android.widget.TextView[@text=' 二批商（近六个月销售量）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    shuguo_shangchao_loc = (By.XPATH, "//android.widget.TextView[@text='商超（近六个月销售量）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    shuguo_lingshouzhongduan_loc = (By.XPATH, "//android.widget.TextView[@text='零售终端（近六个月销售量）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    shuguo_tuangou_loc = (By.XPATH, "//android.widget.TextView[@text='团购（近六个月销售量）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    # 主要销售产品
    zhuyaoxiaoshouchanpin_loc = (By.XPATH, "//android.widget.TextView[@text='主要销售产品']")
    chanpinmingchen_loc = (By.XPATH, "//android.widget.EditText[@text='请输入产品名称']")
    pinpai_loc = (By.XPATH, "//android.widget.EditText[@text='请输入品牌']")
    jinhuojia_loc = (By.XPATH, "//android.widget.EditText[@text='请输入进货价（元）']")
    xinghao_loc = (By.XPATH, "//android.widget.EditText[@text='请输入型号']")
    xiaohuojia_loc = (By.XPATH, "//android.widget.EditText[@text='请输入销货价（元）']")
    shangyuexiaoliang_loc = (By.XPATH, "//android.widget.EditText[@text='请输入上月销量（元）']")
    # 商超主要销售产品
    chanpinpinpai_loc = (By.XPATH, "//android.widget.TextView[@text='产品品牌:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    chanpinleixing_loc = (By.XPATH, "//android.widget.TextView[@text='产品类型:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    dailizizhi_loc = (By.XPATH, "//android.widget.TextView[@text='代理资质:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    hezuoqixian_loc = (By.XPATH, "//android.widget.TextView[@text='合作期限（年）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    nianxiaoshourenwu_loc = (By.XPATH, "//android.widget.TextView[@text='年销售任务（万元）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")

    # 蔬果主要销售产品
    shuguo_chanpinmingchen_loc = (By.XPATH, "//android.widget.TextView[@text='产品名称:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")
    chandi_loc = (By.XPATH, "//android.widget.TextView[@text='产地（仅水果）:']")
    guonei_loc = (By.XPATH, "//android.widget.TextView[@text='国内']")
    shuguo_shangyuexiaoliang_loc = (By.XPATH, "//android.widget.TextView[@text='上月销量（元）:']/preceding-sibling::android.widget.LinearLayout/android.widget.EditText")

    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()

    def click_confirm_text(self):
        self.find_element(*self.confirm_text_loc).click()

    def click_save_button(self):
        self.find_element(*self.save_button_loc).click()
        time.sleep(2)

    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    def click_edit_button(self):
        self.find_element(*self.edit_button_loc).click()

    def click_loan_no(self, loan_no):
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + loan_no + "']/preceding-sibling::android.widget.TextView")).click()

    # 借款人基本信息
    def click_borrower_info(self):
        self.find_element(*self.borrower_info_loc).click()

    def input_organization(self, organization):
        self.send_keys(self.organization_loc, organization)

    def select_education(self, education="本科"):
        self.find_element(*self.education_loc).click()
        self.find_element(*(By.XPATH, "//android.widget.TextView[@text='" + education + "']")).click()

    def scroll_to_marry_status(self):
        self.drag_and_drop(self.marry_status_loc, self.borrower_name_loc)

    def input_wechat_no(self, wechat_no):
        self.send_keys(self.wechat_no_loc, wechat_no)

    def input_home_phone(self, home_phone):
        self.send_keys(self.home_phone_loc, home_phone)

    def input_post_code(self, post_code):
        self.send_keys(self.post_code_loc, post_code)

    def select_home_addr(self):
        self.find_element(*self.hukousuozaidi_loc).click()
        self.find_element(*self.hukousuozaidi_value_loc).click()

    def input_hujidizhi(self, hujidizhi):
        self.find_element(*self.hujidizhi_loc).click()
        self.send_keys(self.hujidizhi_info_loc, hujidizhi)
        self.click_confirm_button()

    def input_juzhudizhi(self, juzhudizhi):
        self.find_element(*self.live_addr_loc).click()
        self.send_keys(self.live_addr_info_loc, juzhudizhi)
        self.click_confirm_button()

    def input_live_years(self, live_years):
        self.send_keys(self.live_years_loc, live_years)

    def input_children_info(self, children_info):
        self.find_element(*self.children_info_loc).click()
        self.send_keys(self.children_info_edit_loc, children_info)
        self.click_save_button()

    def input_other_info(self, other_info):
        self.find_element(*self.other_info_loc).click()
        self.send_keys(self.other_info_edit_loc, other_info)
        self.click_save_button()

    # 贷款信息
    def click_loan_info(self):
        self.find_element(*self.daikuanxinxi_loc).click()

    def click_jibenxinxi(self):
        self.find_element(*self.jibenxinxi_loc).click()

    def select_daikuanqixian(self):
        self.find_element(*self.daikuanqixian_loc).click()
        self.find_element(*self.daikuanqixian_value_loc).click()

    def select_huankuanfangshi(self):
        self.find_element(*self.huankuanfangshi_loc).click()
        self.find_element(*self.huankuanfangshi_value_loc).click()

    def input_ea_pifuedu(self, pifuedu):
        self.send_keys(self.eapifuedu_loc, pifuedu)

    def select_daikuanyongtu(self):
        self.find_element(*self.daikuanyongtu_loc).click()
        self.find_element(*self.daikuanyongtu_value_loc).click()

    def select_songshen_yinhang(self):
        self.find_element(*self.songshenyinhang_loc).click()
        self.find_element(*self.songshenyinhang_value_loc).click()

    def select_danbaofangshi(self):
        self.find_element(*self.danbaofangshi_loc).click()
        self.find_element(*self.danbaofangshi_value_loc).click()

    # 紧急联系人
    def click_jinjilianxiren(self):
        self.find_element(*self.jinjilianxiren_loc).click()

    def input_contact_name(self, name):
        self.send_keys(self.contacts_name_loc, name)

    def select_yujiekuanrenguanxi(self):
        self.find_element(*self.guanxi_loc).click()
        self.find_element(*self.guanxi_value_loc).click()

    def input_contact_phone(self, contact_phone):
        self.send_keys(self.contact_phone_loc, contact_phone)

    def input_contact_addr(self, contact_addr):
        self.send_keys(self.contact_addr_loc, contact_addr)

    # 夫妻双方负债情况
    def click_fuqishuangfangfuzhaiqingkuang(self):
        self.find_element(*self.fuqishuangfangfuzhaiqingkuang_loc).click()

    def input_zichanzongji(self, zichanzongji):
        self.send_keys(self.total_zichan_loc, zichanzongji)

    def input_minjianjiedai(self, minjianjiedai):
        self.send_keys(self.minjianjiedai_loc, minjianjiedai)

    # 经营主体信息
    def click_jingyingzhutixinxi(self):
        self.find_element(*self.jingyingzhuti_info_loc).click()

    def input_zhizhao_name(self, zhizhao_name):
        self.send_keys(self.yingyezhizhao_name_loc, zhizhao_name)

    def input_zhucehao(self, zhucehao):
        self.send_keys(self.yingyezhizhao_zhucehao_loc, zhucehao)

    def select_zuzhixingshi(self):
        self.find_element(*self.zuzhixingshi_loc).click()
        self.find_element(*self.zuzhixingshi_value_loc).click()

    def select_zhuceshijian(self):
        self.find_element(*self.register_time_loc).click()
        self.click_confirm_text()

    def input_yingyezhizhaodizhi(self, yingyezhizhaodizhi):
        self.find_element(*self.yingyezhizhao_addr_loc).click()
        self.send_keys(self.yingyezhizhao_addr_value_loc, yingyezhizhaodizhi)
        self.click_confirm_button()

    def input_office_addr(self, office_addr):
        self.find_element(*self.office_addr_loc).click()
        self.send_keys(self.office_addr_value_loc, office_addr)
        self.click_confirm_button()

    def input_gudongrenshu(self, gudongrenshu):
        self.send_keys(self.gudongrenshu_loc, gudongrenshu)

    def input_fuqizhanbi(self, fuqizhanbi):
        self.send_keys(self.fuqizhangubili_loc, fuqizhanbi)

    def select_gongshangshifouyichang(self):
        self.find_element(*self.gongshangyichang_loc).click()
        self.find_element(*self.gongshangyichang_value_loc).click()

    def select_borrower_is_controler(self):
        self.find_element(*self.borrower_is_controler_loc).click()
        self.find_element(*self.borrower_iscontroler_value_loc).click()

    def input_controler_name(self, controler_name):
        self.send_keys(self.controler_name_loc, controler_name)

    def select_yingye_mode(self):
        self.find_element(*self.yingye_mode_loc).click()
        self.find_element(*self.yingye_mode_value_loc).click()

    def scroll_to_yingye_mode(self):
        self.drag_and_drop(self.yingye_mode_loc, self.borrower_is_controler_loc)

    def select_hangye_leibie(self):
        self.find_element(*self.hangye_leibie_loc).click()
        self.find_element(*self.hangye_leibie_value_loc).click()

    def select_jingyingqishishijian(self):
        self.find_element(*self.jingyingqishi_time_loc).click()
        self.click_confirm_text()

    # 经营历史
    def click_jingyinglishi(self):
        self.find_element(*self.jingyinglishi_loc).click()

    def input_jingli(self, jingli):
        self.send_keys(self.jingli_loc, jingli)

    def input_fuzhaizonge(self, fuzhaizonge):
        self.send_keys(self.fuzhaizonge_loc, fuzhaizonge)

    def input_nianxiaoshoue(self, nianxiaoshoue):
        self.send_keys(self.nianxiaoshoue_loc, nianxiaoshoue)

    # 近六个月营业额情况
    def click_near_six_month(self):
        self.find_element(*self.near_six_month_loc).click()

    def scroll_to_loan_info(self):
        self.drag_and_drop(self.near_six_month_loc, self.borrower_info_loc)

    # 经营状况
    def click_jingyingzhuangkuang(self):
        self.find_element(*self.jingying_status_loc).click()

    def input_yuangongrenshu(self, yuangongrenshu):
        self.send_keys(self.yuangong_renshu_loc, yuangongrenshu)

    def select_nianyingyeeyanzhengziliao(self):
        self.find_element(*self.nianyingyee_yanzhengcailiao_loc).click()
        self.find_element(*self.bank_liushui_loc).click()
        self.click_confirm_text()

    # 门店信息
    def click_mendian_info(self):
        self.find_element(*self.mendian_info_loc).click()

    def select_chanquanxingzhi(self):
        self.find_element(*self.chanquanxingzhi_loc).click()
        self.find_element(*self.chanquanxingzhi_value_loc).click()

    def input_mendianhuanjingmiaoshu(self, mendianhuanjingmiaoshu):
        self.find_element(*self.mendian_huanjing_miaoshu_loc).click()
        self.send_keys(self.mendian_huanjing_miaoshu_value_loc, mendianhuanjingmiaoshu)
        self.click_save_button()

    def input_mendian_phone(self, mendian_phone):
        self.send_keys(self.mendian_phone_loc, mendian_phone)

    def select_mendian_chengliriqi(self):
        self.find_element(*self.mendian_chengli_date_loc).click()
        self.click_confirm_text()

    def input_mendian_addr(self, mendian_addr):
        self.find_element(*self.mendian_dizhi_loc).click()
        self.send_keys(self.mendian_xiangxi_dizhi_loc, mendian_addr)
        self.click_confirm_button()

    def input_yingyemianji(self, yingyemianji):
        self.send_keys(self.yingye_mianji_loc, yingyemianji)

    def input_nianzujin(self, nianzujin):
        self.send_keys(self.nian_zujin_loc, nianzujin)

    def select_zulinhetongqizhiriqi(self):
        self.find_element(*self.zudinghetongqizhiriqi_loc).click()
        self.find_element(*self.jieshu_shijian_loc).click()
        self.click_confirm_text()

    def input_cunhuojiazhiyugu(self, cunhuojiazhiyugu):
        self.send_keys(self.cunhuojiazhiyugu_loc, cunhuojiazhiyugu)

    def select_zhuangxiuxinjiuchengdu(self):
        self.find_element(*self.zhuangxiuxinjiuchengdu_loc).click()
        self.find_element(*self.zhuangxiuxinjiuchengdu_value_loc).click()

    def select_huojiashifouzhengqi(self):
        self.find_element(*self.huojiashifouzhengqi_loc).click()
        self.find_element(*self.huojiashifouzhengqi_value_loc).click()

    def input_cunhuoxiaoqimiaoshu(self, cunhuoxiaoqimiaoshu):
        self.find_element(*self.cunhuoxiaoqimiaoshu_loc).click()
        self.send_keys(self.cunhuoxiaoqimiaoshu_value_loc, cunhuoxiaoqimiaoshu)
        self.click_save_button()

    # 渠道数据
    def click_qudaoshuju(self):
        self.find_element(*self.qudao_shuju_loc).click()

    def input_yuqudaoqiyecaigoudechanpin(self, yuqudaoqiyecaigoudechanpin):
        self.find_element(*self.yuqudaoqiyecaigoudechanpin_loc).click()
        self.send_keys(self.qudao_product_name_loc, yuqudaoqiyecaigoudechanpin)
        self.click_save_button()

    def select_yubaimingdanneishangchaohezuokaishishijian(self):
        self.find_element(*self.yubaimingdanneishangchaohezuokaishishijian_loc).click()
        self.click_confirm_text()

    # 商超渠道数据
    def select_yuqudaoqiyehezuoqishishijian(self):
        self.find_element(*self.yuqudaoqiyehezuoqishishijian_loc).click()
        self.click_confirm_text()

    # 蔬果渠道数据
    def select_shichangjingyingkaishishijian(self):
        self.find_element(*self.benshichangjingyingkaishishijian_loc).click()
        self.click_confirm_text()

    def select_dangkouyouwuchewei(self):
        self.find_element(*self.dangkouyouwuchewei_loc).click()
        self.find_element(*self.yes_loc).click()

    # 主要供货渠道
    def click_zhuyaogonghuoqudao(self):
        self.find_element(*self.zhuyaogonghuoqudao_loc).click()
        self.find_element(*self.imgview_loc).click()

    def input_erpishang(self, erpishang):
        self.send_keys(self.erpishang_loc, erpishang)

    def input_shangchao(self, shangchao):
        self.send_keys(self.shangchao_loc, shangchao)

    def input_zhijielingshou(self, zhijielingshou):
        self.send_keys(self.zhijielingshou_loc, zhijielingshou)

    def input_lingshouzhongduan(self, lingshouzhongduan):
        self.send_keys(self.lingshouzhongduan_loc, lingshouzhongduan)

    # 上游信息
    def click_shangyouxinxi(self):
        self.find_element(*self.shangyou_info_loc).click()

    def input_zhongyaogongyingshang(self, zhongyaogongyingshang):
        self.send_keys(self.zhongyaogongyingshang_loc, zhongyaogongyingshang)

    def input_hezuochanpin(self, hezuochanpin):
        self.send_keys(self.hezuochanpin_loc, hezuochanpin)

    def input_zhangqi(self, zhangqi):
        self.send_keys(self.zhangqi_loc, zhangqi)

    # 蔬果上游信息
    def select_shifouziyounongchang(self):
        self.find_element(*self.shifouziyounongchang_loc).click()
        self.find_element(*self.yes_loc).click()

    def click_imgview(self):
        self.find_element(*self.imgview_loc).click()

    def input_ziyounongchangdizhi(self, ziyounongchangdizhi):
        self.find_element(*self.ziyounongchangdizhi_loc).click()
        self.send_keys(self.ziyounongchangdizhi_info_loc, ziyounongchangdizhi)
        self.click_confirm_button()

    def select_shifouxianggudingnonghucaigou(self):
        self.find_element(*self.shifouxianggudingnonghucaigou_loc).click()
        self.find_element(*self.yes_loc).click()

    def select_shifouxiangqitagongyingshangcaigou(self):
        self.find_element(*self.shifouxiangqitagongyingshangcaigou_loc).click()
        self.find_element(*self.yes_loc).click()

    # 十大下游客户近6月供货量
    def click_shidaxiayoukehugonghuoliang(self):
        self.find_element(*self.shidaxiayoukehugonghuoliang_loc).click()

    def input_kehumingcheng(self, kehumingcheng):
        self.send_keys(self.kehumingcheng_loc, kehumingcheng)

    def input_jiesuanzhangqi(self, jiesuanzhangqi):
        self.send_keys(self.jiesuanzhangqi_loc, jiesuanzhangqi)

    def input_gonghuoliang(self, gonghuoliang):
        self.send_keys(self.gonghuoliang_loc, gonghuoliang)

    # 下游信息
    def click_xiayouxinxi(self):
        self.find_element(*self.xiayouxinxi_loc).click()

    def input_shuguo_erpishang(self, shuguo_erpishang):
        self.send_keys(self.shuguo_erpishang_loc, shuguo_erpishang)

    def input_shuguo_shangchao(self, shuguo_shangchao):
        self.send_keys(self.shuguo_shangchao_loc, shuguo_shangchao)

    def input_shuguo_lingshouzhongduan(self, shuguo_lingshouzhongduan):
        self.send_keys(self.shuguo_lingshouzhongduan_loc, shuguo_lingshouzhongduan)

    def input_shuguo_tuangou(self, shuguo_tuangou):
        self.send_keys(self.shuguo_tuangou_loc, shuguo_tuangou)

    # 主要销售产品
    def click_zhuyaoxiaoshouchanpin(self):
        self.find_element(*self.zhuyaoxiaoshouchanpin_loc).click()

    def input_product_name(self, product_name):
        self.send_keys(self.chanpinmingchen_loc, product_name)

    def input_pinpai(self, pinpai):
        self.send_keys(self.pinpai_loc, pinpai)

    def input_jinhuojia(self, jinhuojia):
        self.send_keys(self.jinhuojia_loc, jinhuojia)

    def input_xinghao(self, xinghao):
        self.send_keys(self.xinghao_loc, xinghao)

    def input_xiaohuojia(self, xiaohuojia):
        self.send_keys(self.xiaohuojia_loc, xiaohuojia)

    def input_shangyuexiaoliang(self, shangyuexiaoliang):
        self.send_keys(self.shangyuexiaoliang_loc, shangyuexiaoliang)

    # 商超主要销售产品
    def input_chanpinpinpai(self, pinpai):
        self.send_keys(self.chanpinpinpai_loc, pinpai)

    def input_chanpinleixing(self, chanpinleixing):
        self.send_keys(self.chanpinleixing_loc, chanpinleixing)

    def input_dailizizhi(self, dailizizhi):
        self.send_keys(self.dailizizhi_loc, dailizizhi)

    def input_hezuoqixian(self, hezuoqixian):
        self.send_keys(self.hezuoqixian_loc, hezuoqixian)

    def input_nianxiaoshourenwu(self, nianxiaoshourenwu):
        self.send_keys(self.nianxiaoshourenwu_loc, nianxiaoshourenwu)

    # 蔬果主要销售产品
    def input_shuguo_chanpinmingchen(self, shuguochanpinming):
        self.send_keys(self.shuguo_chanpinmingchen_loc, shuguochanpinming)

    def select_chandi(self):
        self.find_element(*self.chandi_loc).click()
        self.find_element(*self.guonei_loc).click()

    def input_shuguo_shangyuexiaoliang(self, shuguo_shangyuexiaoliang):
        self.send_keys(self.shuguo_shangyuexiaoliang_loc, shuguo_shangyuexiaoliang)
