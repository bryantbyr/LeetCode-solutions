#98. Validate Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181020
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = [True]
        self.helper(root, res)
        return res[0]

    def helper(self, root, res):
        if not root:
            return
        self.isGreater(root.right, root.val, res)
        self.isLess(root.left, root.val, res)
        self.helper(root.left, res)
        self.helper(root.right, res)

    def isGreater(self, node, val, res):
        if not node:
            return
        if node.val <= val:
            res[0] = False
        self.isGreater(node.left, val, res)
        self.isGreater(node.right, val, res)

    def isLess(self, node, val, res):
        if not node:
            return
        if node.val >= val:
            res[0] = False
        self.isLess(node.left, val, res)
        self.isLess(node.right, val, res)

#Learn from discuss on 20181020
#Time:O(N)
#Space:O(1)
#Tree + iterative_inorder_traversal
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if (pre and node.val <= pre.val):
                return False
            pre = node
            root = node.right
        return True


s = Solution()
t = TreeNode(1)
t.left = TreeNode(1)
# t.right = TreeNode(7)
# t.right.left = TreeNode(6)
# t.right.right = TreeNode(8)
print(s.isValidBST(t))
