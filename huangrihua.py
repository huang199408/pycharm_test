#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#coding=utf-8
import cookiejar;
import urllib2;

loginUrl = "http://www.qichacha.com/user_login";
cj = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj));
urllib.request.install_opener(opener);
resp = urllib.request.urlopen(loginUrl);
for index, cookie in enumerate(cj):
    print('[', index, ']', cookie);
