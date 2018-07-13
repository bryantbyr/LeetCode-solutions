#653. Two Sum IV - Input is a BST
#
#Learn from discuss on 20180713
#Space:O(n)
#Time:O(n)
#HashSet/DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.findTarget_Helper(root, set(), k)

    def findTarget_Helper(self, node, nodes, k):
        if not node:
            return False
        if k - node.val in nodes:
            return True
        nodes.add(node.val)
        return self.findTarget_Helper(node.left, nodes, k) or self.findTarget_Helper(node.right, nodes, k)


s = Solution()
t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(6)
t1.left.right = TreeNode(4)
t1.left.left = TreeNode(2)
t1.right.right = TreeNode(7)
print(s.findTarget(t1, 28))
