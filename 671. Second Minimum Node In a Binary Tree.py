# 671. Second Minimum Node In a Binary Tree

from tools import TreeNode
import math

#Created by bryantbyr on 20181112
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root.left: return float('inf')
            if root.left.val < root.right.val:
                return min(helper(root.left), root.right.val)
            elif root.left.val > root.right.val:
                return min(root.left.val, helper(root.right))
            return min(helper(root.left), helper(root.right))

        res = helper(root)
        return -1 if math.isinf(res) else res


#Learn from discuss on 20181112
#Time:O(N)
#Space:O(1)
#Tree + Traversal
class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = [float('inf')]

        def helper(node):
            if not node: return
            if root.val < node.val < res[0]:
                res[0] = node.val
            helper(node.right)
            helper(node.left)

        helper(root)
        return -1 if math.isinf(res[0]) else res[0]


s = Solution()
t = TreeNode(5)
t.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right = TreeNode(9)
print(s.findSecondMinimumValue(t))
