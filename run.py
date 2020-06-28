#!/usr/bin/python
# -*- coding: utf-8

'''
执行测试方法
Created on 2020-06-24 11:41:00
@author: author
'''

from lib import tool
from lib import http


# 可以传参数指定执行哪些测试  case.csv 1 /case.csv 1,3,6
#


if __name__ == '__main__':
    # print(dir(tool.LibTool))
    print(tool.LibTool().getUrl("login"))

    libHttp = http.LibHttp()
    libHttp.setHeaders({"connection": "keep-alive", "content-type": "json"})
    print(libHttp.getHeaders())
    libHttp.setHeader("cookie", "test——cookie")
    print(libHttp.getHeaders())

    # 读取 csv
    print(tool.LibTool().readCSV("./data/case.csv"))
    # 读取 csv 含有指定内容的行
    print(tool.LibTool().readCSVByLine("./data/case.csv", "url", "check"))

    # 