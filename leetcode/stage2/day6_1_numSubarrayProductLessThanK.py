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

       将数组元素一个个放进容器内
            遍历到当前元素时，与容器内的元素进行乘积
            如果大于k，从容器中去除头部元素，一直到小于k为止
        将当前元素加入容器

"""
from typing import List
"""
我们使用一重循环枚举 right
同时设置 left 的初始值为 0。在循环的每一步中，表示 right 向右移动了一位，
将乘积乘以 nums[right]。此时我们需要向右移动 left，直到满足乘积小于 kk 的条件。
在每次移动时，需要将乘积除以 nums[left]。当 left 移动完成后，
对于当前的 right，就包含了 right−left+1 个乘积小于 kk 的连续子数组。

"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product = 1
        ans = left = 0
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [10,5]
    key = 100
    print(s.numSubarrayProductLessThanK(nums, key))

