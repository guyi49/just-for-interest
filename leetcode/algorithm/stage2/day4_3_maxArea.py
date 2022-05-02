# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 11:43
# @Author  : GuYi
# @Function    : 11. 盛最多水的容器    双指针
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。
在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        l, r = 0, length - 1
        res = 0
        while l < r:
            # 存水的高度取决于两边较短的那个内壁的高度
            min_height = min(height[l], height[r])
            # 容积 = 左右边界的长度 * 最短高度
            res = max(res, min_height * (r - l))
            # 若左边界与最小高度相等，则左指针右移动
            if height[l] == min_height:
                l += 1
            # 否则右指针左移
            else:
                r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    list1 = [1, 6, 5, 6]
    print(s.maxArea(list1))
