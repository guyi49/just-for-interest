# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/20 3:34 下午
# @Function:
'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
'''

chars= "Let's take LeetCode contest"
def reverse_words(s):
    split_list = s.split(" ")
    str =""
    for sp in split_list:
        # 反转字符串
        new = sp[::-1]
        str += new + " "
    print(str)
    str = str[:-1]
    print(str)

reverse_words(chars)