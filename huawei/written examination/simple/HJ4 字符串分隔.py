# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 11:03
# @Author  : GuYi
# @Function    :
'''
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串
1sadwwwwguyyxxxxxxxx
1sadwwwwguyy
'''
str = input()
l = len(str)
# print(l)
times = l // 8
# print(times)
num = l%8
# print(num)
for i in range(0,times+1):
    index = i*8
    tail = i*8+8
    # print(index)
    # print(str[index:tail])
    if i == times and num>0:
        last_tail = (8-num) * '0'
        print(str[index:] + last_tail)
    else:
        print(str[index:tail])









