'''
步骤：
    1.打开网址
    2.定位到需要的价格的位置
    3.获取数据
    4.创建数据库表
    5.连接数据库
    6.导入数据库
难点：
    1.因为该网址是3秒更新一次数据，所以应该3~4秒去爬取一次数据。
    2.删除数据。因为不删除数据，数据量会过大，数据库没发支撑这么多数据量，所以只保留2天的数据，2天之前的数据就删掉。
    3.如果要在爬取到的数据加0.1，因为爬取的数据都是文本格式，所以要装换数字类型才能进行运算。
    4.实时插入数据库，因为爬完一条数据是要插入数据库才能在前端显示。
'''
# coding=utf-8

# 导入各种库
from selenium import webdriver
import time
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import datetime


# 爬取网页的数据
def data():
    browser = webdriver.Firefox()  # 启动系统的Firefox浏览器
    browser.get("http://www.lfgold.cn/?from=singlemessage&isappinstalled=0")  # 访问该网站

    # 设定一个无限循环；
    while 1 > 0:
        # sleep(4)4秒之后再去获取一次数据，因为该网址是3秒更新一次数据

        time.sleep(4)
        # 爬取的定位方式，用xpath来定位，
        gold_sale = browser.find_element_by_xpath(".//*[@id='HJSP1']").text
        gold_buy = browser.find_element_by_xpath(".//*[@id='HJBP1']").text
        gold_high = browser.find_element_by_xpath(".//*[@id='HJHigh']").text
        gold_low = browser.find_element_by_xpath(".//*[@id='HJLow']").text
        BJ_gold_sale = browser.find_element_by_xpath(".//*[@id='BJSP1']").text
        BJ_gold_buy = browser.find_element_by_xpath(".//*[@id='BJBP1']").text
        BJ_gold_high = browser.find_element_by_xpath(".//*[@id='BJHigh']").text
        BJ_gold_low = browser.find_element_by_xpath(".//*[@id='BJLow']").text
        BY_gold_sale = browser.find_element_by_xpath(".//*[@id='BYSP1']").text
        BY_gold_buy = browser.find_element_by_xpath(".//*[@id='BYBP1']").text
        BY_gold_high = browser.find_element_by_xpath(".//*[@id='BYHigh']").text
        BY_gold_low = browser.find_element_by_xpath(".//*[@id='BYLow']").text
        HK_gold_sale = browser.find_element_by_xpath(".//*[@id='HKgoldSP1']").text
        HK_gold_buy = browser.find_element_by_xpath(".//*[@id='HKgoldBP1']").text
        HK_gold_high = browser.find_element_by_xpath(".//*[@id='HKgoldHigh']").text
        HK_gold_low = browser.find_element_by_xpath(".//*[@id='HKgoldLow']").text
        London_gold_sale = browser.find_element_by_xpath(".//*[@id='LondongoldSP1']").text
        London_gold_buy = browser.find_element_by_xpath(".//*[@id='LondongoldBP1']").text
        London_gold_high = browser.find_element_by_xpath(".//*[@id='LondongoldHigh']").text
        London_gold_low = browser.find_element_by_xpath(".//*[@id='LondongoldLow']").text

        # 设定时间，现在的时间主要是为了到时候在前端直接取最大时间的数据就是我们需要的数据
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在时间
        # 设定前天时间是为了删除前天时间之前的数据，避免数据量过大
        befor2day = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')  # 前天时间

        # 把结果导入数据库
        config_F = {"host": "localhost", "port": 3306, "user": "root", "passwd": "huangrihua",
                    "db": "test"}
        # 连接数据库
        conn = pymysql.connect(host=config_F["host"], port=config_F["port"], user=config_F["user"],
                               passwd=config_F["passwd"], db=config_F["db"])

        # 创建游标
        cursor = conn.cursor()
        # 删除前天以前的数据
        cursor.execute("delete from gold where time < ('%s')" % befor2day)
        cursor.execute('commit')

        # 导入数据库的方法，from sqlalchemy import create_engine
        engine = create_engine(
            "mysql+pymysql://" + config_F["user"] + ":" + config_F["passwd"] + "@" + config_F["host"] + ":" +
            str(config_F["port"]) + "/" + config_F["db"] + "?charset=utf8")
        # pandas 的DataFrame方法，选择爬取的定位，导入数据库
        returns_merge = pd.DataFrame()
        returns_merge['gold_sale'] = [gold_sale]
        returns_merge['gold_buy'] = [gold_buy]
        returns_merge['gold_high'] = [gold_high]
        returns_merge['gold_low'] = [gold_low]
        returns_merge['BJ_gold_sale'] = [BJ_gold_sale]
        returns_merge['BJ_gold_buy'] = [BJ_gold_buy]
        returns_merge['BJ_gold_high'] = [BJ_gold_high]
        returns_merge['BJ_gold_low'] = [BJ_gold_low]
        returns_merge['BY_gold_sale'] = [BY_gold_sale]
        returns_merge['BY_gold_buy'] = [BY_gold_buy]
        returns_merge['BY_gold_high'] = [BY_gold_high]
        returns_merge['BY_gold_low'] = [BY_gold_low]
        returns_merge['HK_gold_sale'] = [HK_gold_sale]
        returns_merge['HK_gold_buy'] = [HK_gold_buy]
        returns_merge['HK_gold_high'] = [HK_gold_high]
        returns_merge['HK_gold_low'] = [HK_gold_low]
        returns_merge['London_gold_sale'] = [London_gold_sale]
        returns_merge['London_gold_buy'] = [London_gold_buy]
        returns_merge['London_gold_high'] = [London_gold_high]
        returns_merge['London_gold_low'] = [London_gold_low]
        returns_merge['time'] = [nowTime]

        # print(returns_merge)
        # 执行上面爬取的数据导入数据库 gold是表名，con=engine是连接数据库语句，if_exists='append'是增量数据
        returns_merge.to_sql("gold", con=engine, if_exists='append', index=False, index_label=None)


# 执行data()函数
if __name__ == '__main__':

    data()
