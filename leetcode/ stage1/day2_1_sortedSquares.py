# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 16:00
# @Author  : GuYi
# @Function    : 有序组的平方

'''
    给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

    输入：nums = [-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    解释：平方后，数组变为 [16,1,0,9,100]
    排序后，数组变为 [0,1,9,16,100]
    nums = [-7,-3,2,3,11]
'''


# [49, 9, 4, 9, 121]
# [-9 -7,2,4,8]
nums = [-9 -7,2,4,8]
# new_nums = []
# for i in nums:
#     new_nums.append(i * i)
# print(new_nums)
# print(sorted(new_nums))
def fun(nums):
    new_nums = []
    for i in nums:
        new_nums.append(i * i)
    return sorted(new_nums)


print(fun(nums))
def sortedSquares(nums):
    low, high, length = 0,len(nums)-1,len(nums)-1
    new_list = []
    while low <= high:
        if nums[low] * nums[low] <= nums[high] * nums[high]:
            new_list.append(nums[high] * nums[high])
            high -= 1
            continue
        # new_list[length] = nums[low] * nums[low]
        new_list.append(nums[low] * nums[low])
        # length -=1
        low+=1
    return new_list


# print(sortedSquares([-7, -3, 2, 3, 11]))


def sortedSquares(nums):
    n = len(nums)
    low, high, length = 0,n-1,n-1
    new_list = [0] * n
    while low <= high:
        if nums[low] * nums[low] <= nums[high] * nums[high]:
            new_list[length]=(nums[high] * nums[high])
            high -= 1
        else:
        # new_list[length] = nums[low] * nums[low]
            new_list[length]=(nums[low] * nums[low])
            low +=1
        length -= 1
    return new_list


print(sortedSquares([-7, -3, 2, 3, 11]))

def func3(nums):
    n = len(nums)
    low, high, k = 0, n - 1, n - 1
    new_list = [-1] * n
    while low <= high:
        lm = nums[low] ** 2
        hm = nums[high] ** 2
        if lm > hm:
            new_list[k] = lm
            low += 1
        else:
            new_list[k] = hm
            high -= 1
        k -= 1
    return new_list

# 44ms
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        low, high, length = 0,n-1,n-1
        new_list = [0] * n
        while low <= high:
            if nums[low] * nums[low] <= nums[high] * nums[high]:
                new_list[length]=(nums[high] * nums[high])
                length -=1
                high -= 1
                continue
            # new_list[length] = nums[low] * nums[low]
            new_list[length]=(nums[low] * nums[low])
            length -=1
            low +=1
        return new_list