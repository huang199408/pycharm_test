#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# coding=utf-8
# 做一个银行账号密码判断语句
import time

from pip._vendor.distlib.compat import raw_input

time.sleep(1)
your_user_name = "huangrihua"
your_password = "huangrihua"
shurus = 3
while 3 >= shurus >= 1:
    your_input_name = raw_input("请输入您的账号：")
    your_input_password = raw_input("请输入您的密码：")
    if your_input_name == your_user_name and your_input_password == your_password:
        print("您输入的账号密码正确！")
        break
    elif (your_input_name != your_user_name or your_input_password != your_password) and shurus != 1:
        print("您输入的账号密码不正确,请重新输入")
    time.sleep(1)
    shurus -= 1
    if shurus != 0:
        print ("您还有%d次机会" % shurus)
    else:
        print ("您没有机会了")
