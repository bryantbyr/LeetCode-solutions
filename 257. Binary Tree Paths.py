#257. Binary Tree Paths

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181028
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        def helper(root, temp):
            if not root: return None
            if not root.left and not root.right: res.append(temp + str(root.val))
            helper(root.left, temp + (str(root.val) + "->"))
            helper(root.right, temp + (str(root.val) + "->"))

        helper(root, "")
        return res


s = Solution()
t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)
t.left.left = TreeNode(0)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(3)
t.left.right.right = TreeNode(5)
t.right.right = TreeNode(9)
t.right.left = TreeNode(7)
print(s.binaryTreePaths(t))
