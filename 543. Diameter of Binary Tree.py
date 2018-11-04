#543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181104
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        def helper(root):
            if not root: return 0
            return max(1 + helper(root.left), 1 + helper(root.right))

        return max(helper(root.left) + helper(root.right),
                   max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))

#Learn from discuss on 20181104
#Time:O(N)
#Space:O(1)
#Tree + Recursion*
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def helper(root):
            if not root: return 0
            left, right = helper(root.left), helper(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        helper(root)
        return self.ans


s = Solution()
t = TreeNode(3)
t.left = TreeNode(1)
t.left.right = TreeNode(2)
print(s.diameterOfBinaryTree(t))
