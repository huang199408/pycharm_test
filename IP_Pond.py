from selenium import webdriver
import time
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import datetime

def Url():
    browser = webdriver.Firefox()  # 启动系统的Firefox浏览器
    browser.get("http://www.xicidaili.com/wt/1")  # 访问该网站
    while 1>=0:
        number = 2
        list = browser.find_elements_by_xpath(".//*[@id='ip_list']/tbody/tr[position()>1]")

        while number <= len(list) + 1:
            Ip_name = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[2]").text
            Port = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[3]").text
            City = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[4]").text
            No_Yes = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[5]").text
            Http_Type = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[6]").text
            Live_time = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[9]").text
            Sudu = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[7]/div").get_attribute('title')
            Link_time = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[8]/div").get_attribute('title')
            Test_time = browser.find_element_by_xpath(".//*[@id='ip_list']/tbody/tr[" + str(number) +"]/td[10]").text
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在时间
            number = number + 1
            # 把结果导入数据库
            config_F = {"host": "localhost", "port": 3306, "user": "root", "passwd": "huangrihua",
                        "db": "test"}
            # 连接数据库
            conn = pymysql.connect(host=config_F["host"], port=config_F["port"], user=config_F["user"],
                                   passwd=config_F["passwd"], db=config_F["db"])


            # 导入数据库的方法，from sqlalchemy import create_engine
            engine = create_engine(
                "mysql+pymysql://" + config_F["user"] + ":" + config_F["passwd"] + "@" + config_F["host"] + ":" +
                str(config_F["port"]) + "/" + config_F["db"] + "?charset=utf8")
            # pandas 的DataFrame方法，选择爬取的定位，导入数据库
            returns_merge = pd.DataFrame()
            returns_merge['Ip_name'] = [Ip_name]
            returns_merge['Port'] = [Port]
            returns_merge['City'] = [City]
            returns_merge['No_Yes'] = [No_Yes]
            returns_merge['Http_Type'] = [Http_Type]
            returns_merge['Live_time'] = [Live_time]
            returns_merge['time'] = [nowTime]
            returns_merge['Sudu'] = [Sudu]
            returns_merge['Link_time'] = [Link_time]
            returns_merge['Test_time'] = [Test_time]

            # print(returns_merge)
            # 执行上面爬取的数据导入数据库 IP_Pond是表名，con=engine是连接数据库语句，if_exists='append'是增量数据
            returns_merge.to_sql("IP_Pond", con=engine, if_exists='append', index=False, index_label=None)
        browser.find_element_by_xpath(".//*[@class='next_page']").click()

Url()