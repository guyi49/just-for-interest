# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2022/5/2 下午12:05
# @Function:

'''SQL架构
表：Logs

+-------------+---------+
| Column
Name | Type |
+-------------+---------+
| id | int |
| num | varchar |
+-------------+---------+
id是这个表的主键。
编写一个SQL查询，查找所有至少连续出现三次的数字。

返回的结果表中的数据可以按任意顺序排列。

查询结果格式如下面的例子所示：
示例
1:

输入：
Logs
表：
+----+-----+
| Id | Num |
+----+-----+
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |
| 6 | 2 |
| 7 | 2 |
+----+-----+
输出：
Result
表：
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1 |
+-----------------+
解释：1
是唯一连续出现至少三次的数字。
'''

# 思路
select distinct Num as ConsecutiveNums from
    (select Id, Num, lag(Num,1) Over() as num_1, lag(Num,2) Over() as num_2 from logs) c
where c.Num = c.num_1 and c.num_1 = c.num_2


