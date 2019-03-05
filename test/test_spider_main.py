# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 8:33 PM
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : test_spider_main.py
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
import os
sys.path.append("../")

os.system("python ../mini_spider/spider_main.py")
os.system("python ../mini_spider/spider_main.py -v")
os.system("python ../mini_spider/spider_main.py -c test_spider.conf")



