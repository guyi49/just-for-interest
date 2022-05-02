# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 14:49
# @Author  : GuYi
# @Function    :    1091. 二进制矩阵中的最短路径
"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

"""
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 非法情况
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        # 起点非0即阻塞
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        # 定义八个方向
        dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 1], [1, -1], [1, 0]]
        search_queue = deque()
        # 起点加入队列
        search_queue.append([0, 0])
        # 标记起点
        grid[0][0] = 1
        cnt = 1
        while search_queue:
            size = len(search_queue)
            while size > 0:
                size -= 1
                cur = search_queue.pop()
                x = cur[0]
                y = cur[1]
                # 如果走到终点，返回路径
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return cnt
                # 开始八个方向的判断
                for i in dir:
                    x1 = x + i[0]
                    y1 = y + i[1]
                    if x1 < 0 or x1 >= len(grid) or y1 < 0 or y1 >= len(grid) or grid[x1][y1] == 1:
                        continue
                    # 做标记
                    grid[x1][y1] = 1
                    # 不阻塞的加入队列
                    search_queue.append([x1, y1])
            cnt += 1
        return -1


class Solution2:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 非法情况
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        # 起点非0即阻塞
        if grid[0][0] != 0:
            return -1
        # 定义八个方向
        dir = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
        search_queue = deque()
        # 起点加入队列
        search_queue.append([0, 0])
        # 标记起点
        grid[0][0] = 1
        cnt = 1
        while search_queue:
            for i in range(len(search_queue)):
                cur = search_queue.pop()
                # 如果走到终点，返回路径
                if cur[0] == len(grid) - 1 and cur[1] == len(grid[0]) - 1:
                    return cnt
                # 开始八个方向的判断
                for d in dir:
                    x1 = cur[0] + d[0]
                    y1 = cur[1] + d[1]
                    if x1 < 0 or x1 >= len(grid) or y1 < 0 or y1 >= len(grid) or grid[x1][y1] == 1:
                        continue
                    # 做标记
                    grid[x1][y1] = 1
                    # 不阻塞的加入队列
                    search_queue.append([x1, y1])
            cnt += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    # grid = [[0, 1], [1, 0]]
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(s.shortestPathBinaryMatrix(grid))
