# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/22 10:32 下午
# @Function: 字符串的排列
import collections

str1 = "ab"
str2 = "eidbaooo"
def func(s1,s2):
    s1_list = []


# print(collections.Counter(str1))

def checkInclusion(s1,s2):
    L, R = 0, len(s1)
    son = collections.Counter(s1)
    parents = collections.Counter(s2[0:R])
    while R < len(s2) and son != parents:
        parents[s2[R]] += 1
        parents[s2[L]] -= 1
        if not parents[s2[L]] : del parents[s2[L]]
        L += 1
        R += 1
    return True if son == parents else False


print(checkInclusion(str1, str2))
