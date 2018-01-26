#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#__Author__ = Chronos

'''
测试单元(逻辑)
Unit test(logic)
'''
from com.ProsyIP.JsonUtils.JsonResponse import JsonResponse

IPList = [{"ip":1,"name":"dgw1"}, {"ip":2,"name":"dgw2"}, {"ip":3,"name":"dgw3"}]
a = JsonResponse("123", 123, "127.0.0.1", "host", IPList)
jsona = a.toJson()
print(jsona)