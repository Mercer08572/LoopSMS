# -*- coding: utf-8 -*-
# DateTime  : 2022/2/17 11:13
# Author    : Badbugu17
# File      : Main.py
# Software  : PyCharm
from xyz.badbugu.www.SmsBomb.SmsLauncher import SmsLauncher

if __name__ == '__main__':
    sb = SmsLauncher()
    sb.send_message()
    print('完成')