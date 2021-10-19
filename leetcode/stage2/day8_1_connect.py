# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 11:01
# @Author  : GuYi
# @Function    : 117. 填充每个节点的下一个右侧节点指针 II
"""
    给定一个二叉树
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有next 指针都被设置为 NULL。
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        # 若左子树不为空且右子树不为空
        if root.left is not None and root.right is not None:
            # 则左子树的next节点则指向右子树
            root.left.next = root.right
        # 若左子树不为空且右子树为空
        if root.left is not None and root.right is None:
            # 左子树的next由根节点的下一节点找到
            root.left.next = get_next(root.next)
        # 若右子树不为空
        if root.right is not None:
            # 右子树的next由根节点的下一节点找到
            root.right.next = get_next(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root



# 找下个节点
def get_next(root:Node):
    if root is None:
        return None
    if root.left is not None:
        return root.left
    if root.right is not None:
        return root.right
    if root.next is not None:
        return get_next(root.next)
    return None

if __name__ == '__main__':
    s = Solution()
    # root = Node(1,Node(2,Node(4,None,None)),Node(5,None,None)),Node(3,None,Node(7,None,None))

    left_left = Node(4, None, None)
    left_right = Node(5, None, None)
    right_right = Node(7,None,None)
    left = Node(2,left_left,left_right)
    right = Node(3, None, right_right)
    parent = Node(1,left,right)
    # print(parent.val)

    # print(parent.val)
    # print(root.val)
    print(s.connect(parent).left.next.val)