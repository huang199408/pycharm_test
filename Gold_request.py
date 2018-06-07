import requests
import time
import json
from lxml import etree
headers={"User-Agent":"Mac OS X/ Safari: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30"}

html = requests.get("https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0",headers = headers).content.decode("utf-8")
html1 = etree.HTML(html)
print(html.josn)
list = html1.xpath("//*[@id='content']/div/div[1]/div/div[4]/div/a[11]/p/text()")
number = 1
print(list)

