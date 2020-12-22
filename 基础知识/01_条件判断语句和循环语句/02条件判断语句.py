# -*- codeing = utf-8 -*-
# @Time: 2020/12/22 20:38
# @Author:高灵聪
# @File:02条件判断语句.py
# @Software:PyCharm
#冒号不能丢 要缩进Tap 控制范围大小


print("dasdas")
a=1
a="dasdas"


if True:
    print("true")
 # print("sadas") 错判断范围不匹配  缩进方式表示范围 冒号判断语句
else:
    print("false")

score = 77
if score>=90 and score<=100:
    print("A")
else:
    if score>=80and score<90:
        print("c")
if score<60:
    print("B ")

xingbie = 1  #1代表男生 0代表女生
danshen = 1  #1单身 0有
if xingbie == 1:
    print("男生")
    if danshen == 1:
        print("找一个")
    else:
        print("个我个")
else:
    print("女生")
#前面勿加空格
import  random #引入随即库

x = random.randint(0,2)#0 1 2
print(x)
