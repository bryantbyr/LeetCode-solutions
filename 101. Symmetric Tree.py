#101. Symmetric Tree

import operator

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181017
#Time:O(N)
#Space:O(N)
#Tree + Recursion
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre_order_list = []
        post_order_list = []
        self.pre_order_recursion(root, pre_order_list)
        self.post_order_recursion(root, post_order_list)
        print(pre_order_list)
        print(post_order_list)
        return operator.eq(pre_order_list, post_order_list)

    def pre_order_recursion(self, root, list):
        if root is None:
            list.append('null')
            return
        else:
            list.append(root.val)
        if root.left is None and root.right is None:
            return
        self.pre_order_recursion(root.left, list)
        self.pre_order_recursion(root.right, list)

    def post_order_recursion(self, root, list):
        if root is None:
            list.append('null')
            return
        else:
            list.append(root.val)
        if root.left is None and root.right is None:
            return
        self.post_order_recursion(root.right, list)
        self.post_order_recursion(root.left, list)

#Learn from discussion on 20181017
#Time:O(N)
#Space:O(N)
#Tree +  Better Recursion
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


s = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(2)
# t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right.left = TreeNode(5)
# t1.right.right = TreeNode(3)
print(s.isSymmetric(t1))
