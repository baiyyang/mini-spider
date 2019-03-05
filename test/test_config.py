# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 8:26 PM
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : test_config.py
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
from mini_spider.config import get_config


class TestConfig(unittest.TestCase):
    """
    测试config.py，读取配置文件模块
    """
    def test_get_config(self):
        params = get_config("test_spider.conf", "spider", ";")
        self.assertEqual(params["url_list_file"], "./test_urls")
        self.assertEqual(params["output_directory"], "./output")
        self.assertEqual(params["max_depth"], "1")
        self.assertEqual(params["crawl_interval"], "1")
        self.assertEqual(params["crawl_timeout"], "1")
        self.assertEqual(params["target_url"], ".*taobao.*")
        self.assertEqual(params["thread_count"], "8")


if __name__ == "__main__":
    unittest.main()

