# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 11:09
# @Author  : GuYi
# @Function    : 二分查找
import random

'''

    1. 前提是有序的数组
'''
'''
    什么是二分查找:
    1. 前提是有序的数组
    
    题目：
    给定一个n个元素有序的（升序）整型数组 nums 和一个目标值target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    
    # 输入参数
nums = [1,2,3,4,5,6,7,8]
target 

# 返回值
if exists return index
    else
        return -1
'''

def my_binary_search(search_list, item):
    print(item)
    start = 0
    end = len(search_list)-1
    while start <= end:
        mid = int((start + end) / 2)
        if item == search_list[mid]:
            return mid
        if item < search_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

nums = [1, 2, 3, 4, 5]
target = random.randint(0, 10)

# my_binary_search(nums,target)
print(my_binary_search(nums,target))
