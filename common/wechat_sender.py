#!/usr/bin/python3
# coding：utf-8
from __future__ import print_function
import urllib.request
import json
'''
Created on 2017-10-18
@author: luting
Project:基础类WechatSender，发送至企业微信错误的日志信息
'''


class WechatSender(object):

    def __init__(self):
        self.grop_id = 'wwc970d773f2883409'
        self.secret = 'nkiM5L0pP438RDjO-oiX-MMzzWg2gaQI96t9NxtTQNs'

    def get_access_token(self):
        """
        得到token值
        :return:   返回token string类型
        """
        token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.grop_id, self.secret)
        result = urllib.request.urlopen(token_url).read().decode()
        result_json = json.loads(result)
        print(result_json)
        access_token = result_json['access_token']
        return access_token

    @staticmethod
    def message(message):
        """
        发送至企业微信的信息
        :param message:    信息
        :return:           生成企业微信api要传送的json值
        """
        values = {
            "touser": '@all',
            "msgtype": 'text',
            "agentid": 1000002,
            "text": {'content': message},
            "safe": 0
        }
        print(message)
        data = (bytes(json.dumps(values), 'utf-8'))
        return data

    def send_message(self, mes_data):
        """
        发送信息
        :param mes_data:    企业微信api要传送的json值
        :return:
        """
        send_message_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % self.get_access_token()
        respone = urllib.request.urlopen(urllib.request.Request(url=send_message_url, data=mes_data)).read()
        print(json.loads(respone.decode()))
        if json.loads(respone.decode())['errmsg'] == 'ok':
            print('消息发送成功')
        else:
            print('消息未能发送成功过')

if __name__ == '__main__':
    send = WechatSender()
    print(send.get_access_token())
    # data = (send.message('宇宙无敌测试仔'))
    # send.send_message(data)



