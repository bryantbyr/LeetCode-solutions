#144. Binary Tree Preorder Traversal


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#Created by bryantbyr on 20181025
#Time:O(N)
#Space:O(N)
#Tree + Iteration
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop().right
        return res


s = Solution()
t = TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)
# t.right.right = TreeNode(4)
# t.right.right.right = TreeNode(1)
# t.right.left = TreeNode(13)
print(s.preorderTraversal(t))
