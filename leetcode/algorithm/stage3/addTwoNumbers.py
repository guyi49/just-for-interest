# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2022/5/2 下午12:38
# @Function:
'''

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

'''
from typing import Optional


# l1 = [2, 4, 3]


# l1 -> []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 首先考虑空值
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 如何存这个结果 ListNode
        result = ListNode(0)
        p = result

        # 创建一个保存进位的变量
        carry = 0

        while l1 and l2:
            # l1.val = 2 , l2.val =5
            p.next = ListNode((l1.val + l2.val + carry) % 10)

            # // 返回其商的整数部分，舍掉整数
            carry = (l1.val + l2.val + carry) // 10

            # 在ListNode中刷新下一位
            l1 = l1.next
            l2 = l2.next

            # 存储ListNode的变量也要进一位
            p = p.next
        # 接下来考虑l2的位数比l1长的情况
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next
        # 接下来考虑l1的位数比l2长的情况
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next
        if carry == 1:
            p.next = ListNode(1)

        return result.next