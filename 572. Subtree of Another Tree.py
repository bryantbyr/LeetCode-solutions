#572. Subtree of Another Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181105
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def helper(s, t, lable):
            if not s and not t: return True
            if not s or not t: return False
            if s.val == t.val:
                return (helper(s.left, t.left, True) and helper(s.right, t.right, True)) \
                       or helper(s.left, t, False) or helper(s.right, t, False)
            if lable: return False
            return helper(s.left, t, False) or helper(s.right, t, False)

        return helper(s, t, False)


#Learn from discuss on 20181105
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def helper(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return helper(s.left, t.left) and helper(s.right, t.right) if s.val == t.val else False

        if not s: return False
        if helper(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

#Learn from solution on 20181105
#Time:O(N)
#Space:O(1)
#Tree + pre order traversal
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def helper(root):
            if not root:
                return 'null'
            return "#" + str(root.val) + helper(root.left) + helper(root.right)

        s_pre = helper(s)
        t_pre = helper(t)
        return s_pre.index(t_pre) != -1


S = Solution()
t = TreeNode(3)
t.left = TreeNode(4)
t.right = TreeNode(5)
t.left.left = TreeNode(1)
t.left.right = TreeNode(2)
s = TreeNode(4)
s.left = TreeNode(1)
s.right = TreeNode(2)
print(S.isSubtree(t, s))
