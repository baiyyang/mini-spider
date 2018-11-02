# mini-spider

### 目录结构
1. mini_spider/: 程序的开发代码。
* config.py: 解析配置文件。
* logger.py: 程序的日志记录文件。
* url_manager.py: 管理url，记录哪些url已经被爬取过。
* html_manager.py: 实现页面的抓取、页面url提取解析、页面保存功能。
* spider_main.py: 程序的入口文件，负责进行各个模块之间的调度。
2. test/: 程序的测试代码。

### mini-spider架构图
![mini-spider]()

上图为mini_spider爬虫的架构图，主要包括五个部分，分别为爬虫调度模块，URL管理模块，网页下载模块，网页解析模块和网页保存木块。
其中爬虫调度模块对应spider_main.py文件，是集成调度各个模块的核心；URL管理模块为url_manager.py文件；
网页下载、网页解析及网页保存对应html_manager.py文件。spider.conf和urls是配置爬虫的相关参数文件。

### 使用方法
进入mini_spider文件夹中，使用命令：
```buildoutcfg
python spider_main.py -c spider.conf
```
爬虫会根据配置文件spide.conf和urls，进行广度优先搜索，抓取特定的网页，同时在控制台中输出无法访问的网页和原因，以及最终程序运行的时间。除此之外，
程序还会在当前文件夹中会生成logs文件夹和对应的输出文件夹，存放爬取过程中的日志，及抓取的网页结果。

### 相关依赖包
* requests>=2.18.4
* chardet>=3.0
* beautifulsoup4>=4.6

可以使用命令，进行部署执行。
```buildoutcfg
python setup.py bdist_egg
python setup.py install
```

fdsafs
12
