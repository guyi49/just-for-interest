# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 14:29
# @Author  : GuYi
# @Function    :
'''

描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。

提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

4
0 1
0 2
1 2
3 4

27
8 46828
24 47153
3 93735
13 72600
4 44422
8 73704
12 52139
19 47649
21 10445
15 63369
20 48412
17 57017
18 9379
16 51964
19 70049
0 72000
25 38544
18 21967
24 90219
2 17950
3 51355
14 32107
25 81332
23 95607
10 69407
12 53131
19 87351
'''

num = int(input())
table = {}
for i in range(0, num):
    record = input().split(" ")
    key = int(record[0])
    if i >= 1 and key in table:
        origin = table[key]
        table[int(record[0])] = origin + int(record[1])
    else:
        table[int(record[0])] = int(record[1])
key_list = sorted((table.keys()))
for i in list:
    print(i, table[i])
