# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 15:04
# @Author  : GuYi
# @Function    :    广度优先算法
'''
    1. 什么是广度优先算法？
        是一种盲目搜寻法
        解决最短路径问题的算法被称为广度优先搜索
    2.需要几个步骤
        a. 使用图来建立问题模型。
        b.使用广度优先搜索解决问题。
    3.什么是图？
        图是由顶点的有穷非空集合和顶点之间边的集合组成，通过表示为G(V,E)，其中，G标示一个图，V是图G中顶点的集合，E是图G中边的集合。
    4.图的分类
        a.无边图
        b.有向图
    5. 什么是队列？
        故队列又称为先进先出（FIFO—first in first out）线性表。尾部插入，头部删除。
    例子出于《算法图解》，找到芒果经销商。
'''

from collections import deque


# 芒果经销商
def is_seller(name):
    return name[-1] == 'q'


# 实现图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
print(graph)

# 首先现创建一个队列
search_queue = deque()
# 将邻居入队
search_queue += graph["you"]


# for i in graph["you"]:
#     print(i)
#     search_queue += graph[i]

def your_friend_is_mango_seller(search_queue):
    while search_queue:
        person = search_queue.popleft()
        if is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
    return False


print(your_friend_is_mango_seller(search_queue))
