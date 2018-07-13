#226. Invert Binary Tree
#
#Created by bryantbyr on 20180713
#Space:O(1)
#Time:O(n)
#recursion

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def front_recursion(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.val)
        self.front_recursion(root.left)
        self.front_recursion(root.right)


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root


s = Solution()
t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.right = TreeNode(3)
t1.left.left = TreeNode(1)
t1.right.right = TreeNode(9)
t1.right.left = TreeNode(6)
r = s.invertTree(t1)
Tree().front_recursion(r)
