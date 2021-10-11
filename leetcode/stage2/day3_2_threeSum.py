# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 13:26
# @Author  : GuYi
# @Function    : 15. 三数之和
"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，
使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
"""
from typing import List


# while cur.next and cur.next.next:
#     if cur.next.val == cur.next.next.next.val:
#         x = cur.next.val
#         while cur.next and cur.next.val == x:
#             cur.next = cur.next.next
#     else:
#         cur = cur.next
# return dummy.next

def threeSum(nums: List[int]) -> List[List[int]]:
    # if len(nums) < 3 or nums is None:
    #     return []
    nums.sort()
    # print(nums)
    sum_list = []
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        # 若当前该元素>0 了，怎么加都是大于0
        if nums[i] > 0:
            break
        # 去重
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 进入循环
        while left < right:
            # 判断当前值是否等于0
            target_sum = nums[i] + nums[left] + nums[right]
            if target_sum == 0:
                # 若等于0，加入list
                sum_list.append([nums[i],nums[left],nums[right]])
                # 判断左指针的下一个位置的值是否相等，若相等则右移
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # 判断右指针的前一个位置的值是否相等，若相等则左移
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                # 同时收缩
                left += 1
                right -= 1
            elif target_sum < 0:
                left += 1
            elif target_sum > 0:
                right -= 1
    return sum_list


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = []
    nums2 = [0, 0, 0]
    nums3 = [0]
    print(threeSum(nums))
    print(threeSum(nums1))
    print(threeSum(nums2))
    print(threeSum(nums3))
