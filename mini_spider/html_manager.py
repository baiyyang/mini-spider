# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 下午7:47
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : html_manager.py
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
import time
import re
import urllib.parse
import requests
import chardet
from concurrent import futures
from bs4 import BeautifulSoup
from mini_spider.logger import logger


class HtmlManager(object):
    """
    html页面下载，解析，保存管理类
    """
    def __init__(self, crawl_timeout, crawl_interval, thread_count,
                 target_url_pattern, output_directory, url_manager_class, lock):
        """

        :param crawl_timeout: 页面访问最大时间
        :param crawl_interval: 页面下载时间间隔
        :param thread_count: 线程数量
        :param target_url_pattern: 需要存储的目标url
        :param output_directory: 保存路径
        :param url_manager_class: url管理类
        :param lock: 线程并发锁
        :return:
        """
        self.crawl_timeout = crawl_timeout
        self.crawl_interval = crawl_interval
        self.thread_count = thread_count
        self.target_url_pattern = target_url_pattern
        self.output_directory = output_directory
        self.url_manager_class = url_manager_class
        self.lock = lock

    def download_html(self, url):
        """
        下载html
        :param url: 需要下载的url
        :return: 返回text及对应编码
        """
        # 爬虫时间间隔
        time.sleep(self.crawl_interval)

        if url is None:
            logger.warning("the url [{}] is None".format(url))
            return None
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        response = None
        try:
            response = requests.get(url, headers=headers, timeout=self.crawl_timeout)
        except requests.exceptions.HTTPError as error:
            logger.error('Unsuccessfully get [{}], HTTP Error: {}'.format(url, error))
        except requests.exceptions.ConnectionError as error:
            logger.error('Unsuccessfully get [{}], Connecting Error: {}'.format(url, error))
        except requests.exceptions.Timeout as error:
            logger.error('Unsuccessfully get [{}], Timeout Error: {}'.format(url, error))
        except requests.exceptions.TooManyRedirects as error:
            logger.error('Unsuccessfully get [{}], Redirect Error: {}'.format(url, error))
        except requests.exceptions.RequestException as error:
            logger.error('Unsuccessfully get [{}], Else Error: {}'.format(url, error))
        except Exception as error:
            logger.error('Unsuccessfully get [{}], Exception: {}'.format(url, error))

        if response is not None and response.status_code == 200:
            logger.info("the url [{}] has been visited successfully".format(url))
            charset = chardet.detect(response.content)
            response.encoding = charset["encoding"]
            return url, response.text
        else:
            logger.error("the url [{}] has been visited failed".format(url))
            return None

    def get_html_urls(self, cur_url, html_text):
        """
        得到当前html里面所有的url，同时写入当前url页面
        :param cur_url: 当前url
        :param html_text: html.text
        :return: 该页面中所有符合要求的url
        """
        if html_text is None:
            logger.warning("the url [{}] has no content".format(cur_url))
            return None
        # 提取新的url
        soup = BeautifulSoup(html_text, "html.parser")
        urls = set()
        hrefs = soup.find_all("a")
        for href in hrefs:
            if href.has_attr("href"):
                url = href["href"].strip()
                # 相对路径拼接，https前缀也为http，所以这两种情况一起进行判断
                if not url.startswith("http"):
                    url = urllib.parse.urljoin(cur_url, url)
                urls.add(url)
        logger.info("the url [{}] includes [{}] other urls".format(cur_url, len(urls)))

        # 保存当前页面
        if re.search(self.target_url_pattern, cur_url) is not None:
            file_name = re.sub(r"[\/\\\:\*\?\"\<\>\|]", "_", cur_url)
            # self.output_directory 为初始化时已经创建好的目录路径
            file_path = os.path.join(self.output_directory, file_name)
            try:
                with open(file_path, "w", encoding="utf-8") as fw:
                    fw.write(html_text)
                    logger.info("the url [{}] has been saved in path [{}]".format(cur_url, file_path))
            except FileNotFoundError as error:
                logger.error("the file_path {} is not found. error: {}".format(file_path, error))
            except IOError as error:
                logger.error("the file_path {} is be written fail. error: {}".format(file_path, error))

        return urls

    def get_html(self, urls):
        """
        多线程并发下载每个url对应页面
        :param urls: list, 需要下载的url集合
        :return: 每个url对应的html文件信息
        """
        html_texts = list()
        with futures.ThreadPoolExecutor(self.thread_count) as executor:
            to_do = list()
            for url in urls:
                future = executor.submit(self.download_html, url)
                to_do.append(future)
            # 当Future结束，才产生出futures
            done_iter = futures.as_completed(to_do)
            for future in done_iter:
                result = future.result()
                with self.lock:
                    if result is not None:
                        html_texts.append(result)
        return html_texts

    def get_urls(self, url_html_list):
        """
        多线程并发提取每个页面里面的url，并保存当前页面
        :param url_html_list: 为get_html返回的 [url, response.text] 的list
        :return:
        """
        if url_html_list is None:
            return
        new_urls = list()
        with futures.ThreadPoolExecutor(self.thread_count) as executor:
            to_do = list()
            for (cur_url, html_text) in url_html_list:
                if cur_url is not None and html_text is not None:
                    future = executor.submit(self.get_html_urls, cur_url, html_text)
                    to_do.append(future)
                else:
                    logger.error("the current url is None or html_text is None")
            # 当Future结束，才产生出futures
            done_iter = futures.as_completed(to_do)
            for future in done_iter:
                result = future.result()
                with self.lock:
                    if result is not None:
                        new_urls.extend(result)
        # 添加新的url到url_manager中
        for url in new_urls:
            self.url_manager_class.add_new_url(url)



