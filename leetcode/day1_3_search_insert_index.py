# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 14:03
# @Author  : GuYi
# @Function    :
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

输入: nums = [1], target = 0
输出: 0

输入: nums = [1,3,5,6], target = 7
输出: 4
'''

test_nums = [1,5]
tar = 2
def search_insert( nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = int(end - (end-start)/2)
        # print(mid)
        if target == nums[mid]:
            return mid
        # 若目标小于中间值，则应放在左区间
        if target < nums[mid]:
            end = mid -1
        else:
            start = mid + 1
    return start

print(search_insert(test_nums, 2))
test_nums = [1,3,5,6]
print(search_insert(test_nums, 5))
test_nums = [1,3,5,6]
print(search_insert(test_nums, 0))