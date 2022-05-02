# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 8:48
# @Author  : GuYi
# @Function    : 74. 搜索二维矩阵 二分查找

"""
    题目:
    编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
        每行中的整数从左到右按升序排列。
        每行的第一个整数大于前一行的最后一个整数。
        [ 1, 3, 5, 7]
        [10,11,16,20]
        [23,30,34,60]
    输入：matrix = [[1,3,5,7],[1,3,5,7],[23,30,34,60]], target = 3
    输出：true
    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    输出：false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            # 判断目标值在哪一行，然后再用标准二分查找。
            if matrix[i][0] <= target <= matrix[i][-1]:
                left = 0
                right = n - 1
                while left <= right:
                    mid = int(right - (right - left) / 2)
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
        return False


if __name__ == "__main__":
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    s = Solution
    print(s.searchMatrix(s, matrix1, 7))
