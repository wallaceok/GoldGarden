#!/usr/bin/python3
# coding：utf-8
import requests
import json


class WechatSender(object):

    def __init__(self):
        self.corp_id = 'wwc970d773f2883409'
        self.secret = 'nkiM5L0pP438RDjO-oiX-MMzzWg2gaQI96t9NxtTQNs'

    def get_token(self):
        """
        获取access_token
        ----------------------------------------------------------------
        请求方式：GET（HTTPS）
        请求URL：https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRECT
        ----------------------------------------------------------------
        参数说明：
        参数	       必须	  说明
        corpid	   是	  企业ID
        corpsecret 是	  应用的凭证密钥
        :return:  access_token	获取到的凭证,最长为512字节
        """
        token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.corp_id, self.secret)
        response = requests.get(token_url, verify=False).text
        response_dict = json.loads(response)
        token = response_dict['access_token']
        return token

    def send_message(self, message):
        """
        发送消息
        ----------------------------------------------------------------
        请求方式：POST（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN
        ----------------------------------------------------------------
        参数	     是否必须	说明
        touser	 否	        成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为@all，则向该企业应用的全部成员发送
        toparty  否         部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        totag	 否	        标签ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        msgtype	 是      	消息类型，此时固定为：text
        agentid	 是	        企业应用的id，整型。可在应用的设置页面查看
        content	 是	        消息内容，最长不超过2048个字节
        safe	 否	        表示是否是保密消息，0表示否，1表示是，默认0
        :param message:    发送的消息 string类型
        :return:           无返回值
        """
        send_url = ' https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (self.get_token())
        post_data = {
            "touser": "@all",
            "msgtype": "text",
            "agentid": 1000002,
            "text": {
                "content": message
            },
            "safe": 0
        }
        response = requests.post(send_url, data=json.dumps(post_data), verify=False)
        result = json.loads(response.text)['errmsg']
        if result == 'ok':
            print('消息发送成功')
        else:
            print('消息未能发送成功过')


if __name__ == '__main__':
    send = WechatSender()
    send.send_message('帅气')



