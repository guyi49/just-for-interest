# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 9:58
# @Author  : GuYi
# @Function    : 34. 在排序数组中查找元素的第一个和最后一个位置
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。
进阶：
你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
'''

'''
    思路：
        1.根据二分查找，得知第一次出现的位置，但是不知道左边界和又边界的位置。
            1.1 左右滑动指针，找到区间。
        2.如果二分查找失败，返回-1，表明nums中没有目标值。返回[-1,-1]
    
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = binary_search(nums,target)
        if index == -1:
            return [-1,-1]
        left = index
        right = index
        # 左边界
        while left - 1 >= 0 and nums[left - 1] == nums[index]:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == nums[index]:
            right += 1
        return [left,right]

# 二分查找
def binary_search(nums, target):
    right = len(nums) - 1
    left = 0

    while left <= right:
        mid = int(right - (right - left) / 2)
        # 若中间值相等
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    list1 = [1,3,4,4,4]
    s = Solution
    print(s.searchRange(s, list1, 4))