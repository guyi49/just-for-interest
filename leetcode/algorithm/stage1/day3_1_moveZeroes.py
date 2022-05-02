# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/20 9:43 上午
# @Function:

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,12,0,3,1]
输出: [1,3,12,0,0]
'''

def fun2(nums):
    count = 0
    # 从后往前遍历
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 0:
            if i == len(nums)-1:
                continue
            else:
                nums.remove(nums[i])
                count +=1
    for i in range(0,count):
        nums.append(0)
    print(nums)
fun2([0,1,0,3,12])


def fun3(nums):
    length = len(nums)
    k = 0
    for i in range(0,length):
        if nums[i] != 0:
            nums[i-k] = nums[i]
        else:
            k +=1
    for i in range(length-k,length):
        nums[i]=0
    print(nums)
fun3([0,1,0,3,12,0])