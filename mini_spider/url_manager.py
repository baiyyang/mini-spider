# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 下午3:51
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : url_manager.py
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

import hashlib
import re


class UrlManager(object):
    """
    url 调度，管理类
    """
    def __init__(self):
        self.url = list()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        如果该url没有被爬取过，添加到url list中
        :param url: 新的url
        :return:
        """
        # 简单验证url的合法性
        if re.match("^https?:/{2}\w.+$", url):
            md5 = hashlib.md5()
            md5.update(url.encode(encoding="utf-8"))
            if md5.hexdigest() not in self.old_urls:
                self.old_urls.add(md5.hexdigest())
                self.url.append(url)









