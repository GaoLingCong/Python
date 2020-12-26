# -*- codeing = utf-8 -*-
# @Time: 2020/12/26 20:38
# @Author:高灵聪
# @File:存储数据.py
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
soup = BeautifulSoup(r.text,"html.parser")
title = soup.find("h1",class_="post-title").a.text.strip()

print(title)
#打开一个空白的text,然后使用f.write写入刚刚的字符串title
with open('title_text.txt',"a+")as f:
     f.write(title)

