# 865. Smallest Subtree with all the Deepest Nodes

from tools import *

#Learn from discuss on 20181126
#Time:O(N)
#Space:O(N)
#Tree + Recursion/DFS
class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def helper(root):
            if not root:
                return 0, None
            left, right = helper(root.left), helper(root.right)
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return helper(root)[1]


S = Solution()
T = Tree().creat_tree("3 5 6 null null 2 7 null null 4 null null 1 0 null null 8 null null")
print(S.subtreeWithAllDeepest(T).val)
