# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 17:23
# @Author  : GuYi
# @Function    :
nums1= [1,2]
nums = [1,2,3,4,5,6,7]
def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # l = len(nums)
    # nums[:] = nums[l-k:] + nums[:l-k]
    # return  nums


print(rotate(nums1, 2))

def test(nums,k):
    nums[:] = nums[k % len(nums):] + nums[: k % len(nums)]
    return nums

print(test(nums1, 5))

print(-3%2)