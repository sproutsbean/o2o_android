#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: tools.py 
@time: 2018/02/01 
"""
import time
import datetime
from appium import webdriver
from selenium import webdriver as wd
import os
from com.ea.resource import globalparameter as gl
import random
import string
import pymysql
import platform
from com.ea.common.log import log
import xlrd
from xlutils.copy import copy
import logging


def getAppiumDriver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['automationName'] = "uiautomator2"
    desired_caps['deviceName'] = 'Galaxy On5(2016)'
    # 这个是要安装的app的安装包地址，不是必须的，有  # 这个项的话会先通过这个地址安装app，我没有用这个，直接用的Package名和activity名
    # desired_caps['app'] = gl.app
    desired_caps['appPackage'] = gl.packagename
    desired_caps['appActivity'] = gl.mainactivity
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True
    desired_caps['newCommandTimeout'] = 30000
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver


def get_chrome_driver():
    try:
        platatt = platform.system()
        if platatt == 'Darwin':
            # chromeoptions = webdriver.ChromeOptions()
            # chromeoptions.add_argument("--kiosk")
            # 实例化一个Chrome浏览器
            driver = wd.Chrome()
            driver.set_window_size(1500, 2000)
        elif platatt == "Windows":
            chromeoptions = wd.ChromeOptions()
            chromeoptions.add_argument("--start-maximized")
            # 实例化一个Chrome浏览器
            driver = wd.Chrome(chrome_options=chromeoptions)
        else:
            log.info("This platform is not Mac and Windows!! Please check!!")
            raise Exception
        # 隐式设置等待时间为3秒
        driver.implicitly_wait(10)
        # 显示设置等待时间为20秒，每0.5秒循环一次
        return driver
    except Exception as e:
        raise e


def login(driver, username=gl.xd_manager_account, passwd="1"):
    from com.ea.pages.login_page import LoginPage
    loginpage = LoginPage(driver)
    if username != loginpage.get_username():
        loginpage.input_username(username)
        loginpage.input_passwd(passwd)
    loginpage.click_login_button()
    # time.sleep(7)
    assert have_element(driver, "首页", 10) == True
    # assert "首页" in driver.page_source


def have_element(driver, key_word, timeout):
    start_time = time.time()
    end_time = time.time()
    while end_time - start_time < timeout:
        if key_word in driver.page_source:
            return True
        time.sleep(2)
        end_time = time.time()
    return False


def get_chinese():
    strs = ""
    for i in range(random.randint(2, 10)):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        strs = strs + bytes.fromhex(val).decode('gb2312')
    return strs


def del_pics(screenshot_path):
    u"""删除用例的截图目录下所有的截图文件"""
    # files = os.listdir(screenshot_path)
    # print(files)
    # for file in files:
    #     os.remove(screenshot_path + "\\" + file)
    import glob
    ext = os.path.join(screenshot_path, "*.png")
    files = glob.glob(ext)
    for file in files:
        os.remove(file)


def screenshot(driver, screenshot_path, casename):
    # casename = "test_screenshot"
    # screenshot_path = gl.screenshot_path
    shottime = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S'))
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    picname = screenshot_path + "/" + shottime + casename + ".png"
    driver.get_screenshot_as_file(picname)
    print("运行失败,请查看图片:" + picname)


def get_web_screenshot(driver, screenshot_path, casename):
    shottime = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S'))
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    picname = screenshot_path + "/" + shottime + casename + ".png"
    driver.get_screenshot_as_file(picname)
    print("运行失败,请查看图片:" + picname)


def create_huankuanjihua(fullname):
    u"""修改还款计划表中的名字"""
    filename = gl.file_path
    rb = xlrd.open_workbook(filename)
    w = copy(rb)
    w.get_sheet(0).write(1, 3, fullname)
    w.save(filename)


def get_random_string(number=9):
    salt = 'AUTO' + ''.join(random.sample(string.ascii_letters + string.digits, number))
    return salt


def get_zx_no():
    zx_no = 'O2OZX-' + str(random.randint(0, 9999)).zfill(1) + '-' + str(random.randint(0, 99999)).zfill(1)
    return zx_no


def get_zx_no_by_cardno(cardno):
    service_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_service_user, passwd=gl.db_service_passwd, db=gl.db_service_db, charset='utf8')
    sql = "select oz.bill_code from o2o_loan_user_zx olz,o2o_zx oz where olz.zx_no = oz.id and olz.document_no = '" + cardno + "';"
    print(sql)
    service_cursor = service_db.cursor()
    try:
        service_cursor.execute(sql)
        result = service_cursor.fetchone()
        print("征信单号:", result[0])
        return result[0]
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        service_db.close()


def get_loan_no_by_cardno(cardno):
    service_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_service_user, passwd=gl.db_service_passwd, db=gl.db_service_db, charset='utf8')
    sql = "select ol.bill_code from o2o_loanapply ol, o2o_loan_user olu where ol.loan_id = olu.loan_id and olu.document_no = '" + cardno + "';"
    service_cursor = service_db.cursor()
    try:
        service_cursor.execute(sql)
        result = service_cursor.fetchone()
        print("贷款单号:", result[0])
        return result[0]
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        service_db.close()


def get_zx_status_by_zx_no(zx_no):
    service_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_service_user, passwd=gl.db_service_passwd, db=gl.db_service_db, charset='utf8')
    sql = 'select zx_status from o2o_zx where bill_code = "' + zx_no + '"'
    service_cursor = service_db.cursor()
    try:
        service_cursor.execute(sql)
        result = service_cursor.fetchone()
        return result[0]
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        service_db.close()


def get_undo_count_by_name(name):
    try:
        workflow_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_workflow_user, passwd=gl.db_workflow_passwd, db=gl.db_workflow_db, charset='utf8')
        sql = "select count(*) from wf_process_task_main m,wf_task_node_auditors a where m.cur_node_id = a.task_node_id and a.auditor_name = '" + name + "' and a.auditor_status=0 and m.process_status=2"
        wf_cursor = workflow_db.cursor()
        wf_cursor.execute(sql)
        result = wf_cursor.fetchone()
        return result[0]
    except Exception as e:
        raise e
    finally:
        workflow_db.close()


def get_brand_no_by_brandname(brandname):
    u"""根据品牌名称获取品牌编码"""
    service_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_service_user, passwd=gl.db_service_passwd, db=gl.db_service_db, charset='utf8')
    sql = "select brand_code from o2o_brand_info where brand_name = '" + brandname + "';"
    service_cursor = service_db.cursor()
    try:
        service_cursor.execute(sql)
        result = service_cursor.fetchone()
        return result[0]
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        service_db.close()


def create_zhengxin_data(first_name, second_name, fullname, full_english_name, cardno, phoneno, first_english_name, second_english_name, bill_code, account_id):
    service_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_service_user, passwd=gl.db_service_passwd, db=gl.db_service_db, charset='utf8')
    crm_db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_crm_user, passwd=gl.db_crm_passwd, db=gl.db_crm_db, charset='utf8')
    # 使用cursor()方法获取操作游标
    service_cursor = service_db.cursor()
    crm_cursor = crm_db.cursor()
    loanid = get_random_string()
    zx_no = get_random_string()
    sql_user_zx = "INSERT  INTO  o2o_loan_user_zx(id,loan_id,user_surname,user_name,user_full_name,user_name_pinyin,sex,document_type,document_no,user_phone,zx_no,zx_date,license_expiration_date,surname_pinyin,name_pinyin)  VALUES('" + get_random_string() + "','" + loanid + "','" + first_name + "', '" + second_name + "', '" + fullname + "', '" + full_english_name + "', 'M', 'IDC', '" + cardno + "', '" + phoneno + "', '" + zx_no + "', CURDATE(), CURDATE(),'" + first_english_name + "','" + second_english_name + "');"
    sql_o2o_zx = "INSERT   INTO   o2o_zx(id,bill_code,zx_status,zx_type,is_del,zx_bank,create_id,create_name,create_date,submit_id,submit_name,submit_date,operator_id,operator_name,ltd,ltd_code,ltd_name,end_date,data_source,bc_isagree)  VALUES('" + zx_no + "','" + bill_code + "', 'CLO', 'ZX_JKR', 'N', 'JCB', '154983', '鲁俊', NOW(), '154983', '鲁俊', NOW(), '218464', '李三川', '19580', 'D900', '深圳安新源', NOW(), '3', 'Y')"
    sql_customer = "INSERT  INTO  customer_basic_info(customer_id,customer_family_name,customer_family_name_py,customer_given_name,customer_given_name_py,customer_name,customer_name_pinyin,age,sex,id_type,id_number,license_expiration_date,mobile_number,marital_status,customer_source,creator,modifier,create_date,modify_date,create_id,modify_id,account_id)  VALUES('" + loanid + "','" + first_name + "','" + first_english_name + "','" + second_name + "','" + second_english_name + "','" + fullname + "','" + full_english_name + "', '30', 'M', 'IDC', '" + cardno + "', CURDATE()  ,'" + phoneno + "', '0', '1', '鲁俊', '鲁俊',NOW() ,NOW() , '154983', '154983','" + account_id + "')"
    # print(sql_user_zx)
    try:
        # 执行sql
        service_cursor.execute(sql_user_zx)
        service_cursor.execute(sql_o2o_zx)
        service_db.commit()
    except Exception as e:
        # 发生异常
        service_db.rollback()
        raise e
    try:
        # 执行sql
        crm_cursor.execute(sql_customer)
        crm_db.commit()
    except Exception as e:
        # 发生异常
        crm_db.rollback()
        raise e
    finally:
        # 关闭数据库连接
        service_db.close()
        crm_db.close()


def insert_o2o_zx(bill_code, ):
    db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_service_user, passwd=gl.db_service_passwd, db=gl.db_service_db, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "INSERT   INTO   o2o_zx(id,bill_code,zx_status,zx_type,is_del,zx_bank,create_id,create_name,create_date,submit_id,submit_name,submit_date,operator_id,operator_name,ltd,ltd_code,ltd_name,end_date,data_source,bc_isagree)  VALUES('" + get_random_string() + "','" + bill_code + "', 'CLO', 'ZX_JKR', 'N', 'JCB', '154983', '鲁俊', NOW(), '154983', '鲁俊', NOW(), '218464', '李三川', '19580', 'D900', '深圳安新源', NOW(), '3', 'Y')"
    print(sql)
    try:
        # 执行sql
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        # 发生异常
        db.rollback()
        raise e
    finally:
        # 关闭数据库连接
        db.close()


def insert_customer_basic_info(customer_id, first_name, first_english_name, second_name, second_english_name, fullname, full_english_name, cardno, phoneno, account_id):
    db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_crm_user, passwd=gl.db_crm_passwd, db=gl.db_crm_db, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "INSERT  INTO  customer_basic_info(customer_id,customer_family_name,customer_family_name_py,customer_given_name,customer_given_name_py,customer_name,customer_name_pinyin,age,sex,id_type,id_number,license_expiration_date,mobile_number,marital_status,customer_source,creator,modifier,create_date,modify_date,create_id,modify_id,account_id)  VALUES('" + customer_id + "','" + first_name + "','" + first_english_name + "','" + second_name + "','" + second_english_name + "','" + fullname + "','" + full_english_name + "', '30', 'M', 'IDC', '" + cardno + "', CURDATE()  ,'" + phoneno + "', '0', '1', '鲁俊', '鲁俊',NOW() ,NOW() , '154983', '154983','" + account_id + "')"
    print(sql)
    try:
        # 执行sql
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        # 发生异常
        db.rollback()
        raise e
    finally:
        # 关闭数据库连接
        db.close()


def get_approver_acount_by_yewuno(yewuno, process_type):
    try:
        # # 打开数据库连接
        db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_workflow_user, passwd=gl.db_workflow_passwd, db=gl.db_workflow_db, charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # -- 根据业务ID查询当前节点审批人 - - a.process_status = 2 为处理中(过滤掉其他已经结束的流程), -- b.node_status = 1 为审核中(过滤掉其他审核通过或者待审核的节点)

        acount_sql = "select em.employee_account,bb.node_name from o2o_employee em,(select  c.auditor_name,b.node_name   from wf_process_task_main a, wf_process_task_node   b, wf_task_node_auditors  c  where  a.task_id = b.task_id and b.task_node_id = c.task_node_id  and b.node_status = 1 and a.process_status = 2 and a.process_name like '%" + process_type + "%' and a.refer_code = '" + yewuno + "') bb where em.employee_namecn=bb.auditor_name"
        print(acount_sql)
        cursor.execute(acount_sql)
        result = cursor.fetchone()
        print(cursor.rowcount)
        # employee_account = None
        if cursor.rowcount:
            employee_name = result[0]
            employee_account = employee_name.split(" ", 1)[0].split("-")[-1]
            print("当前审批人账号是: " + str(employee_account) + "   节点名称:" + result[1])
            return employee_account, result[1]
        return None, None
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        db.close()


ch = logging.StreamHandler()
fh = logging.FileHandler(gl.log_path)


def create_logger(level=logging.DEBUG, record_format=None):
    """Create a logger according to the given settings"""
    if record_format is None:
        record_format = "[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s"

    logger = logging.getLogger("mylogger")
    logger.setLevel(level)
    # 修改
    fh.setLevel(level)
    ch.setLevel(level)
    formatter = logging.Formatter(record_format)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def create_random_english():
    s = string.ascii_lowercase
    return random.choice(s)
