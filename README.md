## mini-spider
### 目录结构
1. mini_spider/: 程序的开发代码。
* config.py: 解析配置文件。
* logger.py: 程序的日志记录文件。
* url_manager.py: 管理url，记录哪些url已经被爬取过。
* html_manager.py: 实现页面的抓取、页面url提取解析、页面保存功能。
* spider_main.py: 程序的入口文件，负责进行各个模块之间的调度。
2. test/: 程序的测试代码。

### 使用方法
进入mini_spider文件夹中，使用命令：
```buildoutcfg
python spider_main.py -c spider.conf
```

### 相关依赖包
* requests>=2.18.4
* chardet>=3.0
* beautifulsoup4>=4.6

可以使用命令，进行部署执行。
```buildoutcfg
python setup.py bdist_egg
python setup.py install
```
