# -*- codeing = utf-8 -*-
# @Time: 2020/12/26 12:34
# @Author:高灵聪
# @File:05函数的使用.py
# @Software:PyCharm
def henxian():
    print('----------')
henxian()

def duogehenxian():
        henxian()

duogehenxian()

def sum(a,b,c):
    return a+b+c
print(sum(1,2,3))

def avg(a,b,c):
    return sum(a,b,c)/3

print(avg(1,2,3))

def xiantiao(x):
    print('-'*x)

xiantiao(100)





