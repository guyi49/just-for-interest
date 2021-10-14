# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 9:26
# @Author  : GuYi
# @Function    : 153. 寻找旋转排序数组中的最小值 二分查找
"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素。


[0,1,2,4,5,6,7]
[1,2,4,5,6,7,0]
[2,4,5,6,7,0,1]
[4,5,6,7,0,1,2]
[5,6,7,0,1,2,4]
[6,7,0,1,2,4,5]
[7,0,1,2,4,5,6]
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            # mid = int(right - (right - left)/2)
            mid = (right + left) // 2
            # 如果中间值大于最左值，小于最右值，则最左值是最小值。
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            # 如果中间值大于最左边的值，说明左边有序，往右边找，右边有小值
            # [4,5,6,7,0,1,2]
            # [5,6,7,0,1,2,4]
            elif nums[left] <= nums[mid]:
                left = mid + 1
            # 如果中间值小于最右边的值，说明右边有序，在左边找,左边有小值，也有可能是自己
            # [5,6,7,0,1,2,4]
            # [6, 7, 0, 1, 2, 4, 5]
            # [7, 0, 1, 2, 4, 5, 6]
            else:
                right = mid
        return nums[right]


if __name__ == "__main__":
    list1 = [7,0,1,2,4,5,6]
    list2 = [5,6,7,0,1,2,4]
    list3 = [3,4,5,1,2]
    list4 = [2,1]
    s = Solution
    print(s.findMin(s, list4))