#!/usr/bin/python
# -*- coding: utf-8

'''
工具类
Created on 2020-06-24 13:23:26
@author: author
'''

class LibTool():

    # 读取 csv
    def readCSV(self):
        return


    # 读取 csv 指定行
    def readCSVByLine(self):
        return

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