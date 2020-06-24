#!/usr/bin/python
# -*- coding: utf-8

'''
http相关工具类
Created on 2020-06-25 01:42:04
@author: author
'''

class LibHttp():

    def __init__(self):
      self.headers = {}

    # 设置 headers 键值
    def setHeader(self, key, value):
        self.headers[key] = value


    # 整体设置 headers
    def setHeaders(self, dict):
        self.headers = dict


    # 获取 headers
    def getHeaders(self):
        return self.headers
