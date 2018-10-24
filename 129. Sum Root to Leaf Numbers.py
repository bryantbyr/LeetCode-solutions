#129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from discuss on 20181024
#Time:O(N)
#Space:O(1)
#Tree + Recursion*
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sum(root, s):
            if not root:
                return 0
            if not root.right and not root.left:
                return root.val + s * 10
            return sum(root.left, s * 10 + root.val) + sum(root.right, s * 10 + root.val)

        return sum(root, 0)


s = Solution()
t = TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)
# t.right.right = TreeNode(4)
# t.right.right.right = TreeNode(1)
# t.right.left = TreeNode(13)
print(s.sumNumbers(t))
