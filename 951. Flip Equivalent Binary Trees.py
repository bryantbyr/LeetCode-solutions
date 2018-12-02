# 951. Flip Equivalent Binary Trees

from tools import TreeNode, Tree

#Created by bryantbyr on 20181202
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False

        return (self.flipEquiv(root1.left,root2.left) and  self.flipEquiv(root1.right,root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


S = Solution()
T1 = Tree().creat_tree("1 2 4 null null 5 7 null null 8 null null 3 6 null null null")
T2 = Tree().creat_tree("1 3 null 6 null null 2 4 null null 5 8 null null 7 null null")
print(S.flipEquiv(T1, T2))
