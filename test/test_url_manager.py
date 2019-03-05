# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 8:28 PM
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : test_url_manager.py
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


class TestUrlManager(unittest.TestCase):
    """
    测试url_manager模块
    """
    def test_add_new_url(self):
        baidu_url = "http://www.baidu.com"
        taobao_url = "http://www.taobao.com"
        sina_url = "http://www.sina.com.cn"
        manager = UrlManager()
        manager.add_new_url(baidu_url)
        self.assertEqual(manager.url, [baidu_url])
        manager.add_new_url(taobao_url)
        self.assertEqual(manager.url, [baidu_url, taobao_url])
        manager.add_new_url(sina_url)
        self.assertEqual(manager.url, [baidu_url, taobao_url, sina_url])
        manager.add_new_url(baidu_url)
        self.assertEqual(manager.url, [baidu_url, taobao_url, sina_url])


if __name__ == "__main__":
    unittest.main()



