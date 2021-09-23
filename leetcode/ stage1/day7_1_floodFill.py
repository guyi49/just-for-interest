# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 14:46
# @Author  : GuYi
# @Function    :图像渲染

'''
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
给你一个坐标(sr, sc)表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
最后返回经过上色渲染后的图像。

输入:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
'''

'''
二维正数组里的每个整数代表的是颜色，而不是像素大小
图像中 所有颜色相同且上下左右相邻的像素点可以看作一个区域，将初始点所在区域内的所有像素点的颜色值换成新的颜色
-----
1 1 1
1 1 0       以中心 1 为起点 找到其邻居（邻居的邻居也要找） 与其颜色相同的所有元素，换成新的颜色
1 0 1 
-------
2 2 2 
2 2 0
2 0 1
'''


def floodFill(image, sr, sc, newColor):
    '''
    :param image: List[List[int]]
    :param sr:  int
    :param sc:  int
    :param newColor: int
    :return:  List[List[int]]
    '''
    return dfs(image, sr, sc, newColor, image[sr][sc])


# 深度优先算法，使用递归
def dfs(image, i, j, newColor, oldColor):
    # p
    if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) \
            or image[i][j] == newColor or image[i][j] != oldColor:
        pass
    else:
        temp = image[i][j]
        image[i][j] = newColor
        dfs(image, i + 1, j, newColor, temp)
        dfs(image, i - 1, j, newColor, temp)
        dfs(image, i, j + 1, newColor, temp)
        dfs(image, i, j - 1, newColor, temp)
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
print(floodFill(image, sr, sc, newColor))
image2 = [[0, 0, 0], [0, 1, 0]]
print(floodFill(image2, sr, sc, 1))
