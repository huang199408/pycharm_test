# coding=utf-8
''' 必须使用自定义函数，完成对程序的模块化
    学生信息必须包括：姓名，年龄，学号，除此之外可以适当添加
    必须完成的功能：添加，删除，修改，查询，退出
    '''


# 定义一个学生管理界面函数
from pip._vendor.distlib.compat import raw_input


def studentsGuanLi():
    print("================学生管理系统==================")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.退出系统")


# 定义一个装学生信息的集合
studentList = []
# while的设置主要是让程序一直执行
while True:
    studentsGuanLi()
    num = int(input("输入您想操作的选项:"))
    if num == 1:
        # 输入需要录入的信息
        name = raw_input("请输入名字：")
        age = raw_input("请输入年龄：")
        xueHao = raw_input("请输入学号：")
        # 定义一个学生信息的集合
        studentInformation = []
        # studentInformation = {'name': name, 'age': age, 'xueHao': xueHao}
        studentInformation.append(name)
        studentInformation.append(age)
        studentInformation.append(xueHao)
        studentList.append(studentInformation)
    if num == 2:
        delNum = input("请输入您要删除学生信息的序号：")
        delNum -= 1
        del studentList[delNum]
        print("序号    学号    年龄    姓名")
        i = 0
        for temp in studentList:
            i += 1
            print ('%s' % i), temp
    # 当用户现在3的时候，请示用户需要修改的序号
    if num == 3:
        repNum = input("请输入您要修改学生信息的序号：")
        repNum -= 1
        name = raw_input("请输入名字：")
        age = raw_input("请输入年龄：")
        xueHao = raw_input("请输入学号：")
        studentList[repNum] = [name, age, xueHao]
    # 当用户选择4的时候，查询现在存在的集合
    if num == 4:
        i = 0
        print("序号    学号    年龄    姓名")
        for temp in studentList:
            i += 1
            print ('%s' % i), temp
    # 当用户选择5的时候，就是退出程序
    if num == 5:
        print("程序已退出，谢谢使用")
        break
