# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 14:16
# @Author  : GuYi
# @Function    :    572. 另一棵树的子树
"""
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。
如果存在，返回 true ；否则，返回 false 。
二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true

输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
一个树是另一个树的子树 则
    要么这两个树相等
    要么这个树是左树的子树
    要么这个树是右树的子树
"""


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# 判断是否为同一棵树
def is_same_tree(root: TreeNode, subRoot: TreeNode) -> bool:
    if root is None and subRoot is None:
        return True
    return root and subRoot and root.val == subRoot.val and is_same_tree(root.left, subRoot.left) \
           and is_same_tree(root.right, subRoot.right)


if __name__ == '__main__':
    s = Solution()
    # left_left = TreeNode(1, None, None)
    # left_right = TreeNode(2, None, None)
    # left = TreeNode(4, left_left, left_right)
    # right = TreeNode(5, None, None)
    # root = TreeNode(3, left, right)
    # print(root.left.val)
    # sub_left = TreeNode(1, None, None)
    # sub_right= TreeNode(2, None, None)
    # sub_root = TreeNode(4,sub_left,sub_right)
    # print(sub_root.left.val)
    root = TreeNode(1, None, None)
    sub_root = TreeNode(0, None, None)
    print(s.isSubtree(root, sub_root))
