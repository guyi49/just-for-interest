# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:02
# @Author  : GuYi
# @Function    : 986. 区间列表的交集

"""
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ,
其中 firstList[i] = [starti, endi] 而secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
返回这 两个区间列表的交集 。
形式上，闭区间[a, b]（其中a <= b）表示实数x的集合，而a <= x <= b 。
两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

输入：firstList = [[0,2],[5,10],[13,23],[24,25]],
    secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

"""
from typing import List


#         # 无非只有两个数字，找到大小关系即可;
#         # 0 -> left ; 1 -> right
#         # 找到交集的情况
#         if firstList[i][0] <= secondList[i][0] < firstList[i][1]:
#             if secondList[i][1] <= firstList[i][1]:
#                 intersection_list.append([[secondList[i][0],secondList[i][1]]])
#             else:
#                 intersection_list.append([[secondList[i][0], firstList[i][1]]])
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 这是一个列表，遍历列表中的元素，是一个区间列表
        p = 0
        q = 0
        first_len = len(firstList)
        second_len = len(secondList)
        intersection_list = []
        while p < first_len and q < second_len:
            left = max(firstList[p][0],secondList[q][0])
            right = min(firstList[p][1], secondList[q][1])
            # 说明有交集
            if left <= right:
                intersection_list.append([left,right])
            # 找到被比较元素的小右区间，则该列表指针右移动
            if firstList[p][1] < secondList[q][1]:
                p += 1
            else:
                q += 1
        return intersection_list


if __name__ == '__main__':
    s = Solution()
    # firstList = [[0, 2], [5, 10]]
    # secondList = [[1, 5], [8, 12]]
    # firstList = [[1,7]]
    # secondList = [[3,10]]
    firstList = []
    secondList = [[1,3],[5,9]]
    print(s.intervalIntersection(firstList,secondList))
