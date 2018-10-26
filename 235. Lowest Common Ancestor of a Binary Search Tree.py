#235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181026
#Time：O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        Min, Max = min(p.val, q.val), max(p.val, q.val)
        if root.val >= Min and root.val <= Max:
            return root
        if root.val < Min:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)

#Created by bryantbyr on 20181026
#Time：O(N)
#Space:O(1)
#Tree + Iteration
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        Min, Max = sorted([p.val, q.val])
        while root.val < Min or root.val > Max:
            if root.val < Min:
                root = root.right
            else:
                root =  root.left
        return root

#Learn from discuss on 20181026
#Time：O(N)
#Space:O(1)
#Tree + Iteration (pythonic)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while (root.val - p.val) * (root.val - q.val) > 0:
            root = root.right if root.val < p.val else root.left
            # root = (root.right,root.left)[root.val > p.val]
        return root


s = Solution()
t = TreeNode(6)
t.left = TreeNode(2)
t.right = TreeNode(8)
t.left.left = TreeNode(0)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(3)
t.left.right.right = TreeNode(5)
t.right.right = TreeNode(9)
t.right.left = TreeNode(7)
print(s.lowestCommonAncestor(t, t.left, t.right).val)
