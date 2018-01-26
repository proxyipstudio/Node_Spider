#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#__Author__ = Chronos

from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request
from com.ProsyIP.JsonUtils.JsonReqImpl import JsonCollectionRule

app = Flask(__name__)

'''
测试单元(接口)
Unit test (interface)
'''
@app.route('/Rule/GetRuleReg', methods=['Get'])
def GetRuleReg():
    if(request.json):
        try:
            Jsoncon = JsonCollectionRule(request.json)
            print(Jsoncon.toTuple())
            return make_response(jsonify({'message':'success'}), 200)
        except RuntimeError:
            return make_response(jsonify({'message': 'Json Error'}), 404)
    else:
        return make_response(jsonify({'message':'fail'}), 404)
    pass


'''
不存在的API连接
返回404错误

not exist API
return 404
'''
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message':'error_url'}), 404)

if __name__ == '__main__':
    app.run()
