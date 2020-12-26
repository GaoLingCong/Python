# -*- codeing = utf-8 -*-
# @Time: 2020/12/26 21:01
# @Author:高灵聪
# @File:获取响应内容.py
# @Software:PyCharm
import  requests
r = requests.get('http://www.santostang.com/')

#r.status_code用于检测响应的状态码，如果返回200，就表示请求成功了；
# 如果返回的是4xx，就表示客户端错误；返回5xx则表示服务器错误响应。
# 我们可以用r.status_code来检测请求是否正确响应。
# r.json()是Requests中内置的JSON解码器。
# r.content是字节方式的响应体，会自动解码gzip和deflate编码的响应数据。
print("文本编码",r.encoding)
#r.encoding是服务器内容使用的文本编码。
print("响应状态码：",r.status_code)
#r.text是服务器响应的内容，会自动根据响应头部的字符编码进行解码。
print("字符串方式的响应体：",r.text)
