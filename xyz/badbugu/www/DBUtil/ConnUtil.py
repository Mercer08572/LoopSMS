# -*- coding: utf-8 -*-
# DateTime  : 2022/1/30 19:50
# Author    : Badbugu17
# File      : ConnUtil.py
# Software  : PyCharm

import pymysql

# 进行数据库连接
# getConnect() 获取cursor，建立数据库连接。
# closeConnetc(cursor)，关闭数据库连接。

class ConnUtil:

    # 获取数据库信息，创建连接并返回dbconn，目前是直接获取的样式，之后会改成从配置文件中获取
    def getConnector(self):

        try:
            dbconn = pymysql.connect(
                host='xxxxxxxx',
                # port=3306,
                user='xxxxxxxx',
                password='xxxxxxx',
                db='xxxxxx',
                charset='utf8mb4'
            )
        except Exception as e:
            print(e)
            raise e
        else:
            return dbconn

    # 获取指针
    def getCursor(self, dbconn: pymysql.connect):
        return dbconn.cursor()

    # 关闭数据库连接，在进行数据库操作之后，必须关闭数据库连接
    def closeConnector(self, dbconn: pymysql.connect):
        dbconn.close()