# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 下午9:42
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : spider_main.py
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

import os
import argparse
import time
import threading
import datetime
from mini_spider.logger import logger
from mini_spider.config import get_config
from mini_spider.url_manager import UrlManager
from mini_spider.html_manager import HtmlManager

# 配置参数
parser = argparse.ArgumentParser(description="A Simple Spider With Python")
parser.add_argument("-v", "--version", help="view version number", action="store_true")
parser.add_argument("-c", "--config", type=str, help="mini-spider config file")
args = parser.parse_args()
if args.version:
    print("0.1.0")
    sys.exit()
if not args.config:
    print("Please use -c to add a spider.conf")
    sys.exit()


SECTION = "spider"  # 读取配置文件模块
SPLIT = ";"  # 配置文件注释分隔符
lock = threading.Lock()  # 线程的并发锁


def initialization():
    # 读取配置文件路径
    config_path = os.path.join(os.path.curdir, args.config)
    params_dict = get_config(config_path, SECTION, SPLIT)
    # 校验配置文件是否正常读取
    if params_dict is None:
        logger.error("the config file is read failed")
        sys.exit()
    logger.info("reading the config file")
    try:
        url_path = params_dict["url_list_file"]
        output_directory = params_dict["output_directory"]

        # 以当前运行时间为子目录保存文件
        output_directory = os.path.join(output_directory, time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time())))
        html_directory = os.path.join(os.curdir, output_directory)
        if not os.path.exists(html_directory):
            try:
                os.makedirs(html_directory)
            except FileExistsError as error:
                logger.error("happening several threads created directory at the same time. error: {}".format(error))
            except IOError as error:
                logger.error("the dir: {} is not be made. error: {}".format(html_directory, error))

        max_depth = int(params_dict["max_depth"])
        crawl_interval = int(params_dict["crawl_interval"])
        crawl_timeout = int(params_dict["crawl_timeout"])
        target_url_pattern = params_dict["target_url"]
        thread_count = int(params_dict["thread_count"])
        logger.info("the config keys have been read successfully")
    except KeyError as error:
        logger.error("the key {} is not in config file".format(error))
        sys.exit()
    except ValueError as error:
        logger.error(error)
        sys.exit()

    # 读取目标urls
    target_url_list = list()
    try:
        with open(url_path, "r", encoding="utf-8") as fr:
            for line in fr:
                target_url_list.append(line.strip())
        logger.info("the target urls have been read successfully")
    except FileNotFoundError as error:
        logger.error("the urls file isn't be found, error {}".format(error))
        sys.exit()
    except IOError as error:
        logger.error("the urls file read failed, error {}".format(error))
        sys.exit()

    # url管理器
    url_manager_object = UrlManager()
    for target_url in target_url_list:
        url_manager_object.add_new_url(target_url)

    # html 管理器
    html_manager_object = HtmlManager(crawl_timeout, crawl_interval, thread_count,
                                      target_url_pattern, html_directory, url_manager_object, lock)

    return url_manager_object, html_manager_object, max_depth


if __name__ == "__main__":
    url_manager_class, html_manager_class, max_depth_value = initialization()
    # 开始爬取
    start_time = datetime.datetime.now()
    print("mini spider is running....")
    count = 0
    while count <= max_depth_value:
        logger.info("crawl the {} level html pages".format(count))
        # 下载页面
        html_text = html_manager_class.get_html(url_manager_class.url)
        # clean 当前url
        html_manager_class.url_manager_class.url.clear()
        # 获取当前页面下的url，并保存当前页面
        html_manager_class.get_urls(html_text)
        count += 1
    end_time = datetime.datetime.now()
    seconds = (end_time - start_time).seconds
    logger.info("crawl finished, spend total time: {} minutes {} seconds".format((seconds / 60), (seconds % 60)))
    print("crawl finished, spend total time: {} minutes {} seconds".format((seconds / 60), (seconds % 60)))
