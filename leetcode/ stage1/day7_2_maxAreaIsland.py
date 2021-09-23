# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 17:04
# @Author  : GuYi
# @Function    : 695. 岛屿的最大面积

'''
    给你一个大小为 m x n 的二进制矩阵 grid 。
    岛屿是由一些相邻的1(代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设grid 的四个边缘都被 0（代表水）包围着。
    岛屿的面积是岛上值为 1 的单元格的数目。
    计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
'''
import math

grid = [[2, 1, 0], [1, 1, 1], [1, 1, 0]]
print(grid[0][2])


# 求最大岛屿面积
def max_area_of_island(grid):
    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count = dfs(grid, i, j)
                max_count = max(count, max_count)
    return max_count


# 深度优先算法
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) \
            or grid[i][j] == 0:
        return 0
    else:
        grid[i][j] = 0
        count = 1
        count += dfs(grid, i + 1, j)
        count += dfs(grid, i - 1, j)
        count += dfs(grid, i, j + 1)
        count += dfs(grid, i, j - 1)
    return count


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(max_area_of_island(grid))
