# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 12:12
# @Author  : GuYi
# @Function    :
'''

描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入
一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，
而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

数据范围：字符串长度满足 1≤n≤2500
输入描述：
输入一个字符串（字符串的长度不超过2500）

输出描述：
返回有效密码串的最大长度

ABBA->12ABBA,ABA->ABAKK,123321->51233214

ABBA
4

ABBBA
5

12HHHHA
4

找回文串
'''
# 中心扩散法

password = input()
max_len = 0
for i in range(len(password)):
    low = i - 1
    high = i
    # 偶数
    while low >= 0 and high < len(password) and password[low] == password[high]:
        low -= 1
        high += 1
    max_len = max(max_len, high - low - 1)
    low = i - 1
    high = i + 1
    # 奇数
    while low >= 0 and high < len(password) and password[low] == password[high]:
        low -= 1
        high += 1
    max_len = max(max_len, high - low - 1)
print(max_len)
