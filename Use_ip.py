'''
介绍：爬取的IP不一定都是可以用的，因此要测试IP的可用性
        1.连接超时的不要
        2.连接不上的不要
        3.访问网址返回的不是200的不要
        4.其他异常的不要
'''
import requests
import pymysql

# 设置数据库参数

config_F = {"host": "localhost", "port": 3306, "user": "root", "passwd": "huangrihua",
                        "db": "test"}

# 连接数据库
conn = pymysql.connect(host=config_F["host"], port=config_F["port"], user=config_F["user"],
                       passwd=config_F["passwd"], db=config_F["db"])

# 创建游标
# 为了可以单独执行SQL语句
cursor = conn.cursor()
# 设置执行SQL
cursor.execute("select * from IP_Pond ORDER BY TIME DESC ")
# 设置访问游标中的语句，cursor.fetchall()是全访问游标中的数据
use_ip = cursor.fetchall()
# 遍历游标中的数据
for row in use_ip:
    ip = row[0]
    port = row[1]
    test_ip = "http://" + ip + ":" + port
    proxies = {"http": test_ip}   # 设置代理IP的


    # 设置异常处理
    try:
        # 使用代理IP访问网址
        html = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        while html.status_code != 200:
            cursor.execute("delete from IP_Pond WHERE Ip_name = ('%s')" % ip)
            cursor.execute("commit")
    except :
        cursor.execute("delete from IP_Pond WHERE Ip_name = ('%s')"%ip)
        cursor.execute("commit")
