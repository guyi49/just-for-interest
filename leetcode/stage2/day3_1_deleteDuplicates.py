# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 9:49
# @Author  : GuYi
# @Function    :    82. 删除排序链表中的重复元素 II
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。
返回同样按升序排列的结果链表。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         p: ListNode = ListNode(0)
#         p.next = head
#         head = p
#         # low: ListNode = ListNode(None)
#         # fast: ListNode = ListNode(None)
#         while p.next is not None:
#             low = p.next
#             fast = low
#             # 判断快慢指针所指向的值是否相等，若快指针下一个位置还有元素并且 快慢指针指向的值相等
#             while fast.next is not None and fast.next.val == low.val:
#                 # 快指针后移
#                 fast = fast.next
#                 # 若快慢指针当前位置不相等
#                 if low != fast:
#                     # 则说明有重复的元素，将p的下一个节点为快指针指向的下一个节点
#                     p.next = fast.next
#                 # 若快慢指针位置相同，说明没有重复元素
#                 else:
#                     # p节点的指针后移
#                     p = p.next
#         return head.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 声明，笨指针和尾指针
        dummy = tail = ListNode(-1)
        while head is not None:
            # 确保head不会与上一个节点相同
            if head.next is None or head.val != head.next.val:
                tail.next = head
                tail = head
            # 若head与下一个节点相同，跳过相同节点
            while head.next is not None and head.val == head.next.val:
                head = head.next
            head = head.next
        tail.next = None
        return dummy.next

class Solution:
    """
        1.重复的元素在链表中的位置是连续的
        2.使用一个笨节点dummy指向链表的头节点
        3.指针cur指向dummy节点，进行遍历
            3.1 若 cur.next 与 cur.next.next的元素相同，
                则 cur.next及后面的相同元素值的链表节点全部删除,且记下这个元素值 x。
            3.2 若cur.next 与 cur.next.next的元素不相同，
                则 cur 指向 cur.next
        4. 遍历完整个链表后，返回 dummy.next 即可。


    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5))))))))
    s = Solution
    print(s.deleteDuplicates(s, head))
