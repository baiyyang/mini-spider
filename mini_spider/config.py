# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午7:56
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : config.py
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

import sys
sys.path.append("../")

import configparser
from mini_spider.logger import logger


def get_config(config_path, section, split=";"):
    """
    读取配置文件中的参数
    :param config_path: 配置文件路径
    :param section: 需要读取的配置文件的section模块
    :param split: 注释行的分隔符
    :return:
    """
    config = configparser.ConfigParser()
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            config.read_file(config_file)
            logger.info("config file has read successfully")
    except FileNotFoundError as error:
        logger.error("config file path: {} is not found. error: {}".format(config_path, error))
        return None
    except IOError as error:
        logger.error("config file read file, error: {}".format(error))
        return None
    except configparser.ParsingError as error:
        logger.error("config file format error {}".format(error))
        return None

    # 配置文件读取
    if section in config.sections():
        params_dict = dict()
        for (key, value) in config.items(section):
            # 过滤掉value后面的注释信息
            params_dict[key] = value.split(split)[0].strip()
        return params_dict
    else:
        logger.error("config file has no [{}] sections".format(section))
        return None

