# -*- codeing = utf-8 -*-
# @Time: 2020/12/26 20:27
# @Author:高灵聪
# @File:提取需要的数据.py
# @Software:PyCharm
import requests
#从bs4这个库中导入Beautifulsoup
from bs4 import BeautifulSoup
link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;'
                        ' en-US; rv:1.9,1,6) '
                        'Gecko/20091201 Firefos/3.5.6'}
r=requests.get(link,headers=headers)
#使用BeautifulSou解析
#找到第一篇文章标题，定位到class是“post-title”的h1元素，提取a里面的字符串 strip（）去除左右空格
soup = BeautifulSoup(r.text,"html.parser")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)