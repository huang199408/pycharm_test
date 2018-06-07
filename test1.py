# coding=utf-8
# 有三个办公室，还有8个老师等待随机分配

import random

# 先创建3个办公室
offices = [[], [], []]
# 假设8个老师是ABCDEFGH
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

b = 0
while b < len(teachers):
    a = random.randint(0, 2)
    if len(offices[a]) < 3:
        offices[a].append(teachers[b])
        b += 1
for temp in offices:
    print (temp)
