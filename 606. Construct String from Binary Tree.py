#606. Construct String from Binary Tree
#
#Created by bryantbyr on 20180714
#Space:O(1)
#Time:O(n)
#recursion


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if not right and not left:
            return str(t.val)
        if not right:
            return str(t.val) + "(" + left + ")"
        return str(t.val) + "(" + left + ")" + "(" + right + ")"


s = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.right = TreeNode(4)
print(s.tree2str(t1))
