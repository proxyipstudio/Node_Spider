#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#__Author__ = Chronos

'''
ThirdPartyIP类
第三方网站获取代理IP

this class is ThirdPartyIP
catch the proxyIP from third party web
'''

class ThirdPartyIP:
    # 构造函数，对传入参数进行初始化
    # constructor, initialize the paramete
    def __init__(self, webRule):
        self.Url = webRule[0]
        self.RegIP = webRule[1]
        self.RegPort = webRule[2]
        self.RegAnonymous = webRule[3]
        self.RegType = webRule[4]
        self.RegCountry = webRule[5]
        self.RegAddress = webRule[6]
    pass