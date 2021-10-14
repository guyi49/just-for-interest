# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 13:43
# @Author  : GuYi
# @Function    : 滑动窗口

'''
    概念：
        滑动窗口是双指针算法的一种，利用双指针在数组单一方向滑动，形成一个子区间，对子区间进行剪枝，最终得出满足条件的解。
        【-1 ， 0 ， 3， 5， 9 ，12】
         l
         r
    过程：
        若window中元素未完全包含target时，right向右滑动；
        若window包含target中所有元素，将left向右滑动
'''

def is_valid(win):
    return True

# 滑动窗口模板1
def check_inclusion(nums, target_str):
    '''
    :param nums: 字符串
    :param target_str: 目标字符串
    :return:
    '''
    window = []
    left, right = 0
    while right < len(nums):
        window.append(nums[right])
        right += 1
        while is_valid(window):
            window.pop(0)
            left += 1

def is_window_needs_shrink():
    return True
# 滑动窗口模板2
def sliding_window(s,t):
    # 字典 判断key值是否存在
    window = {}
    left, right = 0
    valid = 0
    while right < len(s):
        # 移入窗口的字符
        c = s[right]
        # window.append(s[right])
        # 右移窗口
        right += 1
        # 窗口数据更新
        # code1

        # 判断左窗口是否要收缩
        while is_window_needs_shrink():
            window.pop(0)
            # 移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1
            # 窗口数据更新
            # code2







