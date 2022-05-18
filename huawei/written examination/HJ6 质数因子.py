# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 12:01
# @Author  : GuYi
# @Function    :

'''
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围： 1 \le n \le 2 \times 10^{9} + 14 \ 1≤n≤2×10 9 +14
输入描述：
输入一个整数
输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
'''

import math


def method1():
    inter = int(input())
    x = 2
    # print(math.sqrt(180))
    res_list = []
    # 循环太多遍了
    while x <= inter:
        while inter % x == 0:
            inter //= x
            res_list.append(x)
        x += 1
    for i in res_list:
        print(i, end=" ")


inter = int(input())
x = 2
for i in range(2, int(math.sqrt(inter)) + 1):
    while inter % i == 0:
        inter = inter // i
        print(i, end=" ")
if inter > 2:
    print(inter)
