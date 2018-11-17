# 700. Search in a Binary Search Tree.py

from tools import Tree, TreeNode

#Created by bryantbyr on 20181117
#Time:O(N)
#Space:O(1)
#Tree + Binary Search
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        return None


S = Solution()
T = Tree().creat_tree("4 2 1 null null 3 null null 7 null null")
Tree().front_recursion(S.searchBST(T, 3))
