# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 9:45
# @Author  : GuYi
# @Function    : 713. 乘积小于K的子数组  滑动窗口

"""
给定一个正整数数组 nums和整数 k 。
请找出该数组内乘积小于 k 的连续的子数组的个数。

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window = []
        valid = 0
        left, right = 0, 0
        res = []
        # 右移窗口
        while right < len(nums):
            right_value = nums[right]
            right += 1
            product = 1
            left_value = nums[left]
            window.append(left_value)
            for i in window:
                product *= i
            # 判断左侧窗口是否要收缩
            while product < 100:
                res.append(window)
                if product:
                    print("1")



        return len(res)


if __name__ == '__main__':
    s = Solution()
    str1 = "cbaebabacd"
    # str1 = "abab"
    str2 = "abc"
    ss = "baa"
    d = "aa"
    print(s.findAnagrams(ss, d))

