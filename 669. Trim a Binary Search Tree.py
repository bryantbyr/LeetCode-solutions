#669. Trim a Binary Search Tree

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
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        if root.val < L or root.val > R:
            root = root.left if root.left is not None else root.right
        return root


s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(0)
t1.right = TreeNode(4)
t1.left.right = TreeNode(2)
t1.left.right.left = TreeNode(1)

r = s.trimBST(t1, 1, 3)
Tree().front_recursion(r)
