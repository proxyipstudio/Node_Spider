#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#__Author__ = Chronos

import json

'''
json请求类(基类)
实现json请求类的所有基本操作
对于请求实现读取解析的操作，不实现打包封装的操作

this class is jsonRequest(basic class)
implement all the basic function about jsonRequest
implement the function of read and donot implement the function of write and package
'''
class JsonRequest:
    #构造函数，对传入参数进行初始化
    #constructor, initialize the parameter
    def __init__(self, JsonContent):
        self.jsonContent = json.loads(json.dumps(JsonContent)) #json的内容 the content of Json

