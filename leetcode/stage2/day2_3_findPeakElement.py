# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 10:10
# @Author  : GuYi
# @Function    : 162. 寻找峰值

"""
峰值元素是指其值严格大于左右相邻值的元素。
给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设nums[-1] = nums[n] = -∞ 。
你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
    或者返回索引 5， 其峰值元素为 6。

    找最值
    罗尔中值定理
    之前一直以为二分查找的前提数组必须是有序的，现在看来，不一定非得有序。
    求极值点 : 导数为0，nums[-1] = nums[n] = -∞ : 1处导数>0、n处导数<0，
    再由导数零点定理知，一定存在一点介于导数>0和<0的点之间，二分法找导数<0或>0的点，并不断缩小区间，最后求得导数=0的点
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            # 若 左值 大于 右值 ，则 左区间 可能存在 峰值
            if nums[mid] > nums[mid + 1]:
                right = mid
            # 若 右值 大于 左值 ，则 右区间 可能存在 峰值
            else:
                left = mid + 1
        return right




if __name__ == "__main__":
    list1 = nums = [1, 2, 3, 1]
    s = Solution
    print(s.findPeakElement(s, list1))
