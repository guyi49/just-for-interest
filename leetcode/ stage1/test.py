# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/20 10:11 上午
# @Function:

s = "lets"

low = 0
high = len(s)-1
print(low)
print(high)
mid = int(high - (high - low) / 2)
print(s[low:low+1])
print(s[high - 1:high])
while low < mid:
    s= list(s)
    temp = s[low]
    s[low] = s[high]
    s[high] = temp
    low += 1
    high -= 1
