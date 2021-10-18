# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 15:09
# @Author  : GuYi
# @Function    : 209. 长度最小的子数组
"""
给定一个含有n个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。

队列

"""
from typing import List
import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum = 0
        min_value = sys.maxsize
        while right < len(nums):
            right_value = nums[right]
            right += 1
            sum += right_value
            while sum >= target:
                # 判断小值
                min_value = min(min_value,right-left)
                left_value = nums[left]
                left += 1
                sum -= left_value
        return 0 if min_value == sys.maxsize else min_value


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,2,4,3]
    target = 7
    print(s.minSubArrayLen(target, nums))