# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/20 3:19 下午
# @Function:

'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。


输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

输入：["h","a","h"]
输出：["h","a","h"]
'''

def reserve_string(s):
    low = 0
    high = len(s)-1
    mid = int(high - (high - low)/2)
    while low < mid:
        temp = s[low]
        s[low] = s[high]
        s[high] = temp
        low += 1
        high -= 1
    print(s)

reserve_string(["h","e","l","l","o"])
reserve_string(["h","a","h"])
