# 814. Binary Tree Pruning

from tools import TreeNode, Tree

#Created by bryantbyr on 20181119
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root: return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return None if not root.right and not root.left and root.val == 0 else root


S = Solution()
T = Tree().creat_tree("1 1 1 0 null null null 1 null null 0 0 null null 1 null null")
Tree().front_recursion(S.pruneTree(T))
