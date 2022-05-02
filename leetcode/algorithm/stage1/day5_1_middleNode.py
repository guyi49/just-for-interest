# -*- coding: utf-8 -*-
# @Author  : GuYi
# @Time    : 2021/9/21 9:01 上午
# @Function:


'''
给定一个头结点为 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

'''
class ListNode(object):
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

'''
    快慢指针
    定义一个慢指针，走一步
    定义一个快指针，走两步
    只要快指针和快指针的下一个还有值说明还没有遍历完，当遍历完时，慢指针就是为中间节点。
    1  ， 2 ， 3，  4，  5，  6
    s1   s1   s2   s3
    f1        f2       f2   f3
'''
def fun(head:ListNode):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


print(fun([1, 2, 3, 4, 5]))

