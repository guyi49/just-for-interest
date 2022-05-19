
# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 15:26
# @Author  : GuYi
# @Function    :
'''
描述
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

输入描述：
输入一行，为一个只包含小写字母的字符串。

输出描述：
输出该字符串反转后的字符串。

'''

str = input()
res_list = []
for i in range(0,len(str)):
    res_list.append(str[i])
# print(res_list)
res_str = ''
for i in range(1,len(res_list)+1):
    res_str = res_str + res_list[-i]
print(res_str)
