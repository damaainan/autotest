#!/usr/bin/python
# -*- coding: utf-8

'''
工具类
Created on 2020-06-24 13:23:26
@author: author
'''

import csv

class LibTool():

    # 读取 csv
    def readCSV(self, filename):
        f = csv.reader(open(filename,'r'))
        # 拼装 list dict [{"id":1,"method":"GET"}, {"id":2,"method":"POST"}]
        ret = []
        name = []
        for i in f:
            # 判断是否含有表头字段
            if "method" in i:
                name = i
            else:
                res = {}
                for j, val in enumerate(i):
                    res[name[j]] = val
                ret.append(res)
        return ret


    # 读取 csv 指定行
    # 返回 key 关键字列，值为 value 的行所在的数据
    def readCSVByLine(self, filename, key, value):
        ret = self.readCSV(filename)
        for i in ret:
            for k, v in i.items():
                if(key == k and value == v):
                    return i
        return {}

    # 写入文件
    def writeFile(self, filename, content):
        return



    # 存储 token
    # 获取 token
    # 存储 cookie
    # 获取 cookie
    # base64 转码
    # json 转 dict
    # json 转 list
    # 获取对应的 url
    def getUrl(self, key):
        # 实际 urls 配置可以写在配置文件或者其他文件中
        urls = {
            "login": "login_url",
            "check": "check_url",
        }
        return urls[key]