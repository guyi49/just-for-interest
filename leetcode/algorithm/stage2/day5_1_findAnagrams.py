# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 10:47
# @Author  : GuYi
# @Function    : 438. 找到字符串中所有字母异位词 滑动窗口

"""
给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""
from typing import List

def check_inclusion(nums, target_str):
    '''
    :param nums: 字符串
    :param target_str: 目标字符串
    :return:
    '''
    window = []
    left, right = 0
    while right < len(nums):
        window.append(nums[right])
        right += 1
        while is_valid(window):
            window.pop(0)
            left += 1
def is_valid(win,list):
    if len(win)>3:
        list.append()
        return True

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window, need = {}, {}
        for i in p:
            need[i] = need.setdefault(i, 0) + 1
        valid = 0
        left, right = 0, 0
        res = []
        # 右移窗口
        while right < len(s):
            right_value = s[right]
            right += 1
            if right_value in need:
                window[right_value] = window.setdefault(right_value,0)+1
                if window[right_value] == need[right_value]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                left_value = s[left]
                left += 1
                if left_value in need:
                    if window[left_value] == need[left_value]:
                        valid -= 1
                    window[left_value] -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    str1 = "cbaebabacd"
    # str1 = "abab"
    str2 = "abc"
    ss = "baa"
    d = "aa"
    print(s.findAnagrams(ss, d))

