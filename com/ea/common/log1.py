#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:user
@file: log.py
@time: 2017/12/05
"""

import logging
from com.ea.resource import globalparameter as gl

'''
配置日志文件，输出INFO级别以上的日志
'''


class log:
    def __init__(self):
        self.logname = "mylog"
        # 之前把下面定义log的一大段代码写在了__init__里面，造成了日志重复输出
        # 此大坑，谨记谨记！！！!
        self.logger = logging.getLogger()
        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(gl.log_path)
        ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter(
            "[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # 添加Handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        self.logger.setLevel(logging.INFO)

    def __getattr__(self, item):
        return getattr(self.logger, item)
