# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 11:28
# @Author  : GuYi
# @Function    :
'''
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 1 \le n \le 2^{31}-1 \ 1≤n≤2
31
 −1
输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
123456789 ABCDEF
123456789
0xAA 2
10 * 161 + 10* 160
0xAAA
'''


def str_transfer(str):
    if str == 'A':
        return 10
    if str == 'B':
        return 11
    if str == 'C':
        return 12
    if str == 'D':
        return 13
    if str == 'E':
        return 14
    if str == 'F':
        return 15
    else:
        return int(str)
str = input()
# print(str)
len = len(str)
cnt = len - 2
cal = 0
for i in range(3, len + 1):
    power = len - i
    left = 16 ** power
    # print(left)
    # print(i-1)
    right = str_transfer(str[i - 1])
    # print(right)
    res = left * right
    # print(res)
    cal = cal + res
print(cal)
