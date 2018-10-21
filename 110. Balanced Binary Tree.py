#110. Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181021
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        if root:
            left_height = depth(root.left)
            right_height = depth(root.right)
            return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        return True

#Learn from discuss on 20181021
#Time:O(N)
#Space:O(1)
#Tree + Better Recursion
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self,node):
        if not node:
            return 0
        left = self.dfsHeight(node.left)
        if left==-1:
            return -1
        right = self.dfsHeight(node.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return max(left,right) + 1



s = Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.right = TreeNode(7)
t.right.left = TreeNode(15)
print(s.isBalanced(t))
