# 701. Insert into a Binary Search Tree

from tools import Tree, TreeNode

#Created by bryantbyr on 20181118
#Time:O(N)
#Space:O(1)
#Tree + Iteration
class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp = root
        while temp:
            if temp.val > val:
                if not temp.left:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root

#Learn from discuss on 20181118
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


S = Solution()
T = Tree().creat_tree("4 2 1 null null 3 null null 7 null null")
Tree().front_recursion(S.insertIntoBST(T, 5))
