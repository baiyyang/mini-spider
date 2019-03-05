# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 3:51 PM
# @Author  : baienyang
# @Email   : baienyang@baidu.com
# @File    : setup.py
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

from setuptools import setup
from setuptools import find_packages

setup(
    name="mini_spider",
    version="0.1.0",
    description="A simple mini spider",
    author="baienyang",
    author_email="baienyang@baidu.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests>=2.18.4",
        "chardet>=3.0",
        "beautifulsoup4>=4.6"
    ]
)