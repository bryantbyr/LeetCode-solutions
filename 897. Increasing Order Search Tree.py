# 897. Increasing Order Search Tree

from tools import TreeNode, Tree

#Created by bryantbyr on 20181128
#Time:O(N)
#Space:O(N)
#Tree + in-order traversal
class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        isRoot, newRoot, res = True, None, None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if isRoot:
                res = newRoot = root
                isRoot = False
            else:
                root.left = None
                newRoot.right = root
                newRoot = root
            root = root.right
        return res


S = Solution()
T = Tree().creat_tree("5 3 2 1 null null null 4 null null 6 null 8 7 null null 9 null null")
Tree().front_recursion(S.increasingBST(T))
