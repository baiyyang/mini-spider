# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 8:08 PM
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : test_html_manager.py
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

import unittest
from mini_spider.url_manager import UrlManager
from mini_spider.html_manager import HtmlManager


class TestHtmlManager(unittest.TestCase):
    """
    测试html_manager模块
    """
    def setUp(self):
        url_manager_class = UrlManager()
        html_manager_class = HtmlManager(crawl_timeout=1, crawl_interval=1, thread_count=8,
                                         target_url_pattern=".*", output_directory="./output",
                                         url_manager_class=url_manager_class)
        self.html_manager_class = html_manager_class

    def test_init(self):
        self.assertEqual(self.html_manager_class.crawl_timeout, 1)
        self.assertEqual(self.html_manager_class.crawl_interval, 1)
        self.assertEqual(self.html_manager_class.thread_count, 8)
        self.assertEqual(self.html_manager_class.target_url_pattern, ".*")
        self.assertEqual(self.html_manager_class.output_directory, "./output")

    def test_download_html(self):
        baidu_url = "http://www.baidu.com"
        self.assertIsNotNone(self.html_manager_class.download_html(baidu_url))
        ref_url, html_text = self.html_manager_class.download_html(baidu_url)
        self.assertEqual(ref_url, baidu_url)
        print(html_text)

    def test_get_html_urls(self):
        baidu_url = "http://www.baidu.com"
        ref_url, html_text = self.html_manager_class.download_html(baidu_url)
        self.assertIsNotNone(self.html_manager_class.get_html_urls(ref_url, html_text))
        urls = self.html_manager_class.get_html_urls(ref_url, html_text)
        print(urls)

    def test_get_html(self):
        urls = ["http://www.baidu.com", "http://www.sina.com.cn"]
        refs = self.html_manager_class.get_html(urls)
        self.assertIsNotNone(refs)
        ref_urls = [ref[0] for ref in refs if ref is not None]
        ref_text = [ref[1] for ref in refs if ref is not None]
        self.assertEqual(urls, ref_urls)
        print(ref_text)

    def test_get_urls(self):
        urls = ["http://www.baidu.com", "http://www.sina.com.cn"]
        refs = self.html_manager_class.get_html(urls)
        self.assertIsNotNone(refs)
        new_urls = self.html_manager_class.get_urls(refs)
        print(new_urls)


if __name__ == "__main__":
    unittest.main()


