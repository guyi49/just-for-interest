# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/22 8:18 下午
# @Function: 无重复最长字串

'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''

# 从字符串第一个字符串开始遍历

s = "abcabcbbd"
def fun1(s):
    window =[]
    # 设置无重复最长字串为0
    max_len = 0
    # 遍历字符串
    for i in s:
        # 若窗户中从未出现过某字符
        if i not in window:
            # 将字符入窗
            window.append(i)
        # 否则
        else:
            # 若窗户的第一个元素不与该字符相等 -> 侧面说明 该元素在窗口中出现过，
            while window[0] != i:
                # 出第一个元素
                window.pop(0)
            window.append(i)
            window.pop(0)
        # 判断 窗口的大小 是否 大于 无重复最长字串
        if len(window) > max_len:
            # 无重复最长字串 总等于 窗口长度
            max_len = len(window)
    return max_len


print(fun1(s))
#print(fun1("pwwkew"))

