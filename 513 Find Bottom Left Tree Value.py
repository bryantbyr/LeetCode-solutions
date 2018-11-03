#513 Find Bottom Left Tree Value

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Level Traversal
class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level, res = [root], 0
        while level:
            res, level = level[0].val, [kid for node in level for kid in (node.left, node.right) if kid]
        return res

#Learn from discuss on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Smart Level Traversal(pythonic)
class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val


s = Solution()
t = TreeNode(5)
t.left = TreeNode(2)
t.right = TreeNode(-5)
print(s.findBottomLeftValue(t))
