# 563. Binary Tree Tilt

from tools import TreeNode


#Created by bryantbyr on 20181123
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.res = 0

        def helper(root):
            if not root: return 0
            left,right = helper(root.left), helper(root.right)
            self.res += abs(left - right)
            return root.val + left + right

        helper(root)
        return self.res

#Learn from discuss on 20181123
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root: return (0, 0)
            left, right = helper(root.left), helper(root.right)
            return (root.val + left[0] + right[0], abs(left[0] - right[0]) + left[1] + right[1])

        return helper(root)[1]
