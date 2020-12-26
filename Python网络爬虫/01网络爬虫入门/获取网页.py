# -*- codeing = utf-8 -*-
# @Time: 2020/12/26 20:02
# @Author:高灵聪
# @File:获取网页.py
# @Software:PyCharm
import requests #引入包
import requests #引入包requests

#获取页面

#定义link为目标网页地址
link = "https://blog.csdn.net/weixin_39740419/article/details/110761779"
# 定义请求头的浏览器代理，伪装成浏览器
headers = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;'
                        ' en-US; rv:1.9,1,6) '
                        'Gecko/20091201 Firefos/3.5.6'}
#请求网页
r=requests.get(link,headers= headers)
#r.text是获取的网页内容代码
print(r.text)

#提取需要的数据
