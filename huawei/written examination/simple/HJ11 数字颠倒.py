# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 15:17
# @Author  : GuYi
# @Function    :
'''
描述
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001


数据范围： 0 \le n \le 2^{30}-1 \ 0≤n≤2 30−1
输入描述：
输入一个int整数

输出描述：
将这个整数以字符串的形式逆序输出
输入：
1516000
复制
输出：
0006151

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


