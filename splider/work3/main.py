from scrapy.cmdline import execute
import sys
import os
# 配置路径--当前路径追加到系统路径里
sys.path.append(os.path.dirname(__file__))

execute(["scrapy","crawl","IThome"])