#538. Convert BST to Greater Tree
#
#Learn from the solution on 20180714
#Space:O(1)
#Time:O(n)
#recursion*

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
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


s = Solution()
t1 = TreeNode(2)
t1.left = TreeNode(0)
t1.left.left = TreeNode(-4)
t1.left.right = TreeNode(1)
t1.right = TreeNode(3)
r = s.convertBST(t1)
Tree().front_recursion(r)
