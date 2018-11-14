# 124. Binary Tree Maximum Path Sum

from tools import Tree

#Learn from discuss on 20181114
#Time:O(N)
#Space:O(1)
#Tree + Recursion*/DFS*
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ans = float('-inf')

        def helper(node):
            if not node: return 0
            # left, right = helper(node.left), helper(node.right)
            # self.ans = max(self.ans, node.val + left + right, node.val + left, node.val + right, node.val)
            # return max(node.val + left, node.val + right, node.val)

            left, right = max(helper(node.left), 0), max(helper(node.right), 0)
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        helper(root)
        return self.ans


S = Solution()
T = Tree().creat_tree("1 2 null null 3 null null")
print(S.maxPathSum(T))
