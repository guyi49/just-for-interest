# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 16:10
# @Author  : GuYi
# @Function    : 547. 省份数量

"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 algorithm 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 algorithm 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
即 求无向图中的连通域的个数
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 数组标记位置
        visited = [False for i in range(len(isConnected))]
        # 省份变量
        province = 0
        # 遍历
        for i in range(len(isConnected)):
            if visited[i] == False:
                province += 1
                dfs(isConnected, visited, i)
        return province


# 深度优先算法
def dfs(grid, visited, i):
    visited[i] = True
    for j in range(len(grid)):
        if grid[i][j] == 1 and visited[j] == False :
            dfs(grid, visited, j)


if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,0],[1,1,0],[0,0,1]]
    print(s.findCircleNum(grid))
