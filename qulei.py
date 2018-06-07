#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# coding=utf-8
# 设定一个4x4表格，有1-16的数字，一次放在表格里
number = raw_input("请输出一个数字:")
lie = int(number) % 4
hang = int(number) // 4
if lie == 0:
    lie = 4
    hang -= 1
if lie != 0:
    hang += 1
print("该数字应该放在：%d列" % lie)
print("该数字应该放在：%d行" % hang)
