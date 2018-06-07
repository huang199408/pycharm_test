
# 导入各种库
from selenium import webdriver
import time
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import datetime

#爬取网页的数据
def data():

    #设定一个无限循环；
    while 1>0:
        # sleep(4)4秒之后再去获取一次数据，因为该网址是3秒更新一次数据

        time.sleep(4)


        # 设定时间
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在时间
        # 设定前天时间是为了删除前天时间之前的数据，避免数据量过大
        befor2day = (datetime.datetime.now() - datetime.timedelta(minutes = 2)).strftime('%Y-%m-%d %H:%M:%S')  # 前天时间

        # 把结果导入数据库
        config_F = {"host": "localhost", "port": 3306, "user": "root", "passwd": "huangrihua",
                    "db": "test"}
        # 连接数据库
        conn = pymysql.connect(host=config_F["host"], port=config_F["port"], user=config_F["user"],
                               passwd=config_F["passwd"], db=config_F["db"])


        #创建游标
        cursor = conn.cursor()
        #删除前天以前的数据
        sql = cursor.execute("delete from gold where time < '%s'"%befor2day)
        cursor.execute('commit')
        print(sql)

# 执行data()函数

data()