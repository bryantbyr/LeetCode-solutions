#103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#Created by bryantbyr on 20181020
#Time:O(N)
#Space:O(N)
#Tree
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level, direct = [], [root], 'l_r'
        while root and level:
            if direct == 'l_r':
                res.append([node.val for node in level])
                direct = 'r_l'
            else:
                res.append([node.val for node in reversed(level)])
                direct = 'l_r'
            level = [kid for n in level for kid in (n.left,n.right) if kid]
        return res

s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(7)
t.left.left = TreeNode(5)
# t.right.left = TreeNode(6)
t.right.right = TreeNode(8)
print(s.zigzagLevelOrder(t))
