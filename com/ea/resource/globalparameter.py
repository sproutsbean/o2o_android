#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: globalparameter.py 
@time: 2017/12/05 
"""
import time
import os

'''
配置全局参数
'''
# 项目的绝对路径（因为 windows执行时需要绝对路径才能执行通过）
# project_path = "D:\\for2017\\SPframework-Helen_2.0\\"
# 获取项目路径
# url = "http://service.380demo.eascs.com"
env = "sit"
if env == "sit":
    url = "http://service.o2osit.eascs.com/"
elif env == "psit":
    url = "http://pservice.o2osit.eascs.com"
title = u"380金服平台"
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)[0])))),'.'))
project_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
# 安装包路径
app = project_path + "\\com\\ea\\app\\apl_test_v1.5.1.apk"
# 切换环境时使用
# 包名
if env == "sit":
    packagename = "com.eascs.jfgd.mainprojecttest"
elif env == "psit":
    packagename = "com.eascs.jfgd.mainprojectpre"
mainactivity = "com.eascs.jfgd.mainproject.activity.BootActivity"
homepage_activity = "com.eascs.jfgd.mainproject.activity.MainActivity"
login_activity = 'com.eascs.jfgd.mainproject.activity.LoginActivity'
# 错误图片截图路径
screenshot_path = project_path + "/com/ea/screenshot"
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path + "/com/ea/cases/loan_first"
# excel测试数据文档存放路径
test_data_path = project_path + "/com/ea/resource"
test_data_name = test_data_path + "/hk_plan.xls"
# 证件图片路径
test_pic_path = project_path + "/com/ea/resource/file.jpg"
# 银行还款计划
file_path = project_path + "/com/ea/resource/hk_plan.xls"
# 日志文件存储路径
log_path = project_path + "/com/ea/log/mylog.log"
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "/com/ea/report/"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())  # 测试环境数据库相关信息
# 日志配置文件路径
logger_conf = project_path + "/com/ea/resource/logger.conf"

if env == "sit":
    db_host = "172.29.12.196"
    db_port = 3306
elif env == "psit":
    db_host = "172.29.12.197"
    db_port = 3307
db_workflow_user = "o2oadmin"
db_workflow_passwd = "o2oadmin@we741"
db_workflow_db = "o2oworkflow"
db_service_user = "o2oservice"
db_service_passwd = "o2oservice@we741"
db_service_db = "o2oservice"
db_crm_user = "o2ocrm"
db_crm_passwd = "o2ocrm@we741"
db_crm_db = "o2ocrm"

# 信贷经理账号
xd_manager_account = 'long.mu'
xd_manager_name = '木龙'
# xd_manager_account = 'jingyang.chen'
# xd_manager_name = '陈景洋'

# 审批流程类型
zx_approve = '新征信查询'
loan_approve = '征信准入'
inside_approve = '内部审批'
pay_approve = '个人账户打款'
interview_approve = '面签提报'

brand_approve = '流通贷品牌审核'
