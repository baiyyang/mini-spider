## mini-spider
### 目录结构
1. mini_spider/: 程序的开发代码。
* config.py: 解析配置文件。
* logger.py: 程序的日志记录文件。
* url_manager.py: 管理url，记录哪些url已经被爬取过。
* html_manager.py: 实现页面的抓取、页面url提取解析、页面保存功能。
* spider_main.py: 程序的入口文件，负责进行各个模块之间的调度。
2. test/: 程序的测试代码。
