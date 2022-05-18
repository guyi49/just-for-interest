# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 10:44
# @Author  : GuYi
# @Function    :
'''

写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

数据范围： 1 \le n \le 1000 \ 1≤n≤1000
输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）
ABCabc
'''

import sys


str = input()
n = len(str)
target = input()
cnt = 0
for i in range(0,n):
    if target.upper() == str[i] or target.lower() == str[i]:
        cnt += 1
print(cnt)
