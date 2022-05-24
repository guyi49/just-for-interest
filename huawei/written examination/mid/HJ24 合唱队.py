# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 12:21
# @Author  : GuYi
# @Function    :
# def left_max(l):
#     # 计算每个人左边出现的最多的人数
#     # 186 186 150 200 160 130 197 200
#     dp = [1] * len(l)  # 若左边没有比自己小的数，则为自己本身，所以初始值为1
#     for i in range(len(l)):  # 从左往右遍历
#         for j in range(i):
#             if l[j] < l[i] and dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#         # if l[j]<l[i]:
#         #     dp[i] = max(dp[i],dp[j]+1) 会超时
#     return dp  # 1 1 1 2 2 1 3 4
#     # 从右往左推每个人右边可以站的最多的人数
#     # 3 3 2 3 2 1 1 1
#
#
# while True:
#     try:
#         N = int(input())
#         ss = list(map(int, input().split()))
#         left_s = left_max(ss)
#         right_s = left_max(ss[::-1])[::-1]
#         sum_s = []
#         for i in range(len(left_s)):
#             # left_s[i]+right_s[i]-1表示此人是中间位置的人时，合唱队的人数
#             sum_s.append(left_s[i] + right_s[i] - 1)
#         print(str(N - max(sum_s)))
#     except:
#         break

# 186 186 150 200 160 130 197 200
def _max(queue):
    dp = [1] * len(queue)
    print(dp)
    for i in range(len(queue)):
        for j in range(i):
            # print(i)
            # print(j)
            # print('-'*30)
            if queue[i] > queue[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

while 1:
    try:
        num = int(input())
        height = [int(i) for i in input().split()]
        print(height)
        print(height[::-1])
        if num == len(height):
            left = _max(height)
            print(left)
            right = _max(height[::-1])[::-1]
            # print(_max(height[::-1]))
            print(right)
            max_student = max([left[i] + right[i] - 1 for i in range(len(left))])
            print(num - max_student)
    except:
        break
