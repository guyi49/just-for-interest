# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/20 2:17 下午
# @Function:
'''

给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''
nums = [2,7,11,15]
def two_sum(nums,tar):
    low = 0
    high = len(nums)
    mid = int(high - (high-low)/2)
    while high>=2:
        while nums[mid]<=tar:
            for i in range(0,mid):
                left = nums[i]
                right = nums[i+1]
                if left + right == tar:
                    print([left+1,right+1])
                else:
                    right -= 1



def two_sum1(numbers, target):
    left = 0
    right = len(numbers) - 1
    while right > left:
        # 判断头尾两个值相加是否等于目标值
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        # 若头尾两值相加 小于目标值 ，说明头值小了，右移
        elif numbers[left] + numbers[right] < target:
            left += 1
        # 若头尾两值相加 大于目标值 ，说明尾值大了，左移
        elif numbers[left] + numbers[right] > target:
            right -= 1


print(two_sum1(nums, 9))
