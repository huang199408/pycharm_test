from urllib3 import request
import urlopen
doc = request("https://www.baidu.com")
html = doc.read()
print(html)