#100. Same Tree
#
#Created by bryantbyr on 20180801
#Space:O(1)
#Time:O(N)
#Recursion
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p and not q):
            return True
        if (p and q) and (p.val == q.val):
            return self.isSameTree(p.left,q.left)  and   self.isSameTree(p.right,q.right)
        return False


s = Solution()
t1 = TreeNode(1)
# t1.left = TreeNode(2)
t1.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
# t2.right = TreeNode(3)
print(s.isSameTree(t1,t2))
