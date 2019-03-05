# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 下午2:42
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : logger.py
# @Software: PyCharm
"""
Copyright 2018 Baidu, Inc. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import time
import os
import logging

# 创建logger实例子
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 输出日志格式
formatter = logging.Formatter("%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s")

# 创建handler，写日志文件
logger_dir = os.path.join(os.curdir, "logs")
try:
    if not os.path.exists(logger_dir):
        os.mkdir(logger_dir)
except IOError as error:
    print("can't make log directory, error: {}".format(error))
logger_name = os.path.join(logger_dir, time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time())) + '.log')
file_handler = logging.FileHandler(logger_name, encoding="utf-8")
file_handler.setFormatter(formatter)

# 控制台日志
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.ERROR)

# 添加handler到logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

