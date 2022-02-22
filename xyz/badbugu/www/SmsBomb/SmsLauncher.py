# -*- coding: utf-8 -*-
# DateTime  : 2022/2/17 10:45
# Author    : Badbugu17
# File      : SmsLauncher.py
# Software  : PyCharm
from xyz.badbugu.www.Platform.ronglian_sms_sdk import SmsSDK

class SmsLauncher:

    accId = 'xxxxx'
    accToken = 'xxxxxx'
    appId = 'xxxxxx'

    def send_message(self):
        sdk = SmsSDK(self.accId, self.accToken, self.appId)
        # tid = '容联云通讯创建的模板'
        tid = 'xxx'
        # mobile = '手机号1,手机号2'
        mobile = 'xxxx'
        # datas = ('变量1', '变量2')
        datas = ('5250', '5分钟')
        # datas = ()
        resp = sdk.sendMessage(tid, mobile, datas)
        print(resp)