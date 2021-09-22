# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/21 9:22 上午
# @Function: 删除链表的倒数第 N 个结点

'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def func(head:ListNode,n:int):
    return head.next if removeNode(head,n) == n else head

def removeNode(node:ListNode,n:int):
    if node.next == None:
        return 1
    m = removeNode(node.next,n)
    if m == n:
        if m == 1:
            node.next = None
        else:
            node.next = node.next.next
    return m + 1

func()

def fun2(head,n):
    a = head
    b = head
    for i in range(n):
        if a.next:
            a = a.next
        else:
            return head.next
    while a.next:
        a = a.next
        b = b.next
    b.next = b.next.next
    return head