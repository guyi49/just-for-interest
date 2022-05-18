# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 15:56
# @Author  : GuYi
# @Function    :
'''
描述
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。

数据范围：保证在 32 位整型数字范围内
输入描述：
 输入一个整数（int类型）

输出描述：
 这个数转换成2进制后，输出1的个数

输入：
5
输出：
2
256 128 64 32 16 8 4 2 1

'''
num = int(input())
cnt = 0
while num != 0:
    # 取模得1，说明进2，记1
    if num % 2 == 1:
        cnt += 1
    num //= 2
print(cnt)


def sum_method():
    basic_list = []
    for i in range(0, 8):
        basic_list.append(2 ** i)
    print(basic_list)
    num = int(input())
    p = 0
    sum = 0
    res_index = 0
    while p < len(basic_list) and sum < num:
        sum = sum + basic_list[p]
        if sum != num:
            p += 1
            print("index ", p)
            print("sum ", sum)
        if sum == num:
            res_index = p + 1
            break
        res_index = p

    print(res_index)
