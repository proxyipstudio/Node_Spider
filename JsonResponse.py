#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#__Author__ = Chronos

import json

'''
Json响应类(基类)
将数据进行封装成json格式进行传输

this class is jsonResponse(Basic class)
make the information into the json package in order to transfer
'''

class JsonResponse:
    # 构造函数，对传入参数进行初始化
    # constructor, initialize the paramete
    def __init__(self, guid, proxycount, vpsip, vpsrectname, proxys):
        self.guid = guid
        self.proxycount = proxycount
        self.vpsip = vpsip
        self.vpsrectname = vpsrectname
        self.proxys = proxys

    #将有效IP信息封装成Json
    #Conversion of valid IP information into the json
    def toJson(self):
        jsonContent = {
            "guid": self.guid,
            "proxycount": self.proxycount,
            "vpsip": self.vpsip,
            "vpsrectname": self.vpsrectname,
            "proxys": self.proxys
        }

        json_str = json.dumps(jsonContent)
        return json_str