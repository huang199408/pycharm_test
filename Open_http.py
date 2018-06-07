# coding = utf-8
import redis
import requests
import random
import time

r = redis.Redis('localhost', 6379, password='huangrihua')
user_agent_list = [
    "Linux / Firefox 54: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mac OS X/ Safari: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30",
    "Windows / IE 11: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Windows / Edge: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
    "Windows / Chrome: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    "Android / Chrome 40: Mozilla/5.0 (Linux; Android 5.1.1; Nexus 4 Build/LMY48T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.89 Mobile Safari/537.36",
    "iOS / Safari 10: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Google Bot: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "PS4: Mozilla/5.0 (PlayStation 4 3.15) AppleWebKit/537.73 (KHTML, like Gecko)"
    "Curl: curl/7.51.0"
    ]
ip = ["http://171.37.178.86:9797",
      "http://27.37.47.176:9797"]
ip1 = random.choice(ip)
proxies = {"http":ip1}
head1 = random.choice(user_agent_list)
headers={"User-Agent":head1}
html = requests.get('http://www.baidu.com',headers = headers,proxies = proxies)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(html.status_code)
print(proxies)
print(headers)