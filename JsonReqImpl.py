#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#__Author__ = Chronos

from com.ProsyIP.JsonUtils.JsonRequest import JsonRequest

'''
jsonCollectionRule类
该类继承JsonRequest类
获取需要采集规则json包中的所有信息

this class is jsonCollection
this class inherit from jsonRequest
catch the information from the rule-json package
'''
class JsonCollectionRule(JsonRequest):

    # 获取一条采集地址及其所需要的规则
    # 将json解析的数据存入tuple中
    # catch one the url and the rule of matching
    # package the json information into the Tuple
    def catchOneContent(self, index):
        try:
            Url = self.jsonContent[index]["Url"]  # 网站网址 webUrl
            RegIP = self.jsonContent[index]["RegIp"]  # IP匹配规则 the matching rule of IP
            RegPort = self.jsonContent[index]["RegPort"]  # 端口号匹配规则 the matching rule of Port
            RegAnonymous = self.jsonContent[index]["RegAnonymous"]  # 匿名匹配规则 the matching rule of Anonymous
            RegType = self.jsonContent[index]["RegType"]  # 类型(http/https)匹配规则 the matching rule of Type(http/https)
            RegCountry = self.jsonContent[index]["RegCountry"]  # 国家匹配规则 the matching rule of country
            RegAddress = self.jsonContent[index]["RegAddress"]  # 城市匹配规则 the matching rule of city
            return (Url, RegIP, RegPort, RegAnonymous, RegType, RegCountry, RegAddress)
        except TypeError:
            print("Json Error")


    # 获取所有采集地址及其所需要的规则
    # 将得到的每一条规则，存入到的List中
    # catch one the url and the rule of matching
    # insert the One rule into the List
    def catchAllContent(self):
        self.RuleList = []
        for index in range(len(self.jsonContent)):
            if(self.catchOneContent(index) != None):
                self.RuleList.append(self.catchOneContent(index))

    # 将json内容存储在Tuple中，并返回
    # return content of json via Tuple
    def toTuple(self):
        self.catchAllContent()
        jsonTuple = tuple(self.RuleList)
        return jsonTuple


'''
JsonCheckRule类
该类继承JsonRequest类
获取需要校验IP的网络规则

this class is jsonCollection
this class inherit from jsonRequest
catch the information about checking IP
'''
class JsonCheckRule(JsonRequest):

    # 获取一条采集地址及其所需要的规则
    # 将json解析的数据存入tuple中
    # catch one the url and the rule of matching
    # package the json information into the Tuple
    def catchOneContent(self, index):
        try:
            Url = self.jsonContent[index]["Url"]  # 网站网址 webUrl
            RegIP = self.jsonContent[index]["RegIp"]  # IP匹配规则 the matching rule of IP
            RegPort = self.jsonContent[index]["RegPort"]  # 端口号匹配规则 the matching rule of Port
            RegAnonymous = self.jsonContent[index]["RegAnonymous"]  # 匿名匹配规则 the matching rule of Anonymous
            RegType = self.jsonContent[index]["RegType"]  # 类型(http/https)匹配规则 the matching rule of Type(http/https)
            RegCountry = self.jsonContent[index]["RegCountry"]  # 国家匹配规则 the matching rule of country
            RegAddress = self.jsonContent[index]["RegAddress"]  # 城市匹配规则 the matching rule of city
            return (Url, RegIP, RegPort, RegAnonymous, RegType, RegCountry, RegAddress)
        except TypeError:
            print("Json Error")


    # 获取所有采集地址及其所需要的规则
    # 将得到的每一条规则，存入到的List中
    # catch one the url and the rule of matching
    # insert the One rule into the List
    def catchAllContent(self):
        self.RuleList = []
        for index in range(len(self.jsonContent)):
            if(self.catchOneContent(index) != None):
                self.RuleList.append(self.catchOneContent(index))

    # 将json内容存储在Tuple中，并返回
    # return content of json via Tuple
    def toTuple(self):
        self.catchAllContent()
        jsonTuple = tuple(self.RuleList)
        return jsonTuple

'''
jsonCollectionIP类
该类继承JsonRequest类
获取需要检验IP-json包中的所有信息

this class is jsonCollection
this class inherit from jsonRequest
catch the checkIP from the IP-json package
'''
class JsonCollectionIP(JsonRequest):

    #获取所有的失效IP信息并存入到List中
    def catchInvalidIP(self):
        self.IPList = []
        for index in range(len(self.jsonContent)): #获取一个json包的json数据条数 catch the number of json in one json-package
            for invalidIP in self.jsonContent[index]: #获取一条json数据的信息 catch the information of a json
                self.IPList.append(self.jsonContent[index][invalidIP])

    # 将json内容存储在Tuple中，并返回
    # return content of json via Tuple
    def toTuple(self):
        self.catchInvalidIP()
        jsonTuple = tuple(self.IPList)
        return jsonTuple