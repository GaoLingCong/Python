# -*- codeing = utf-8 -*-
# @Time: 2020/12/26 11:02
# @Author:高灵聪
# @File:04遍历字典中所有的键.py
# @Software:PyCharm
favorite_languages = {
    'jen':'python',
    'glc':'java',
    'dsd':'c',
    'glw':'c++',
}
for name in favorite_languages.keys():
    print(name.title())#title转为小写
#字典中的嵌套
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
elien_2 = {'color':'red','points':15}
aliens  = [alien_0,alien_1,elien_2]
for alien in  aliens:
    print(aliens)
#字典中存储列表
