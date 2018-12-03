# 655. Print Binary Tree

from tools import TreeNode, Tree

#Created by bryantbyr on 20181203
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def get_tree_depth(root):
            if not root:
                return 0
            return max(get_tree_depth(root.left), get_tree_depth(root.right)) + 1

        m = get_tree_depth(root)
        n = pow(2, m) - 1

        res = [[""] * n for i in range(m)]

        def helper(root, x=0, y=n // 2):
            if not root: return
            res[x][y] = str(root.val)
            helper(root.left, x + 1, y - n // pow(2, x + 2) - 1)
            helper(root.right, x + 1, y + n // pow(2, x + 2) + 1)

        helper(root)
        return res


T = Tree().creat_tree("5 3 2 null null 4 null null 6 null 7 null null")
S = Solution()
print(S.printTree(T))
