# -*- codeing = utf-8 -*-
# @Time: 2020/12/22 20:57
# @Author:高灵聪
# @File:03循环语句.py
# @Software:PyCharm


#for
#0开始 01234
for i in range(5):
    print(i)
#从0开始到11结束步进值为3 每次+3
for i in  range(0,11,3):
    print(i)
for i in  range(-10,-100,-30):
    print(i)

name = "chengdu"
for x in name:
    print(x)

a = ["aa","bb","cc"]
for i in range(len(a)):
    print(i,a[i])


#while

i = 0
while i <5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i+=1

print("***********")
n=100
sum=0
count = 1
while count<=n:
    sum = sum+count
    count+=1
    print("1到%d的和：%d"%(n,sum))

count=0
while count<5:
    print(count,"小于5")
    count +=1
else:
    print(count,"大于等于5")

j=0
while j<10:
    j+j+1
    print("-"*30)
    if j == 5:
       break
    print(j)

j=0
while j<10:
    j+j+1
    print("-"*30)
    if j == 5:
       continue
    print(j)
