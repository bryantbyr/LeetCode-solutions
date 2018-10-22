#114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181022
#Time:O(N)
#Space:O(N)
#Tree + Recursion
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def pre_order_recursion(root, list):
            if root:
                list.append(root)
                pre_order_recursion(root.left, list)
                pre_order_recursion(root.right, list)

        list = []
        pre_order_recursion(root, list)
        length = len(list)
        for i in range(length):
            if i == length - 1:
                list[i].left, list[i].right = None, None
            else:
                list[i].left, list[i].right = None, list[i + 1]

#Learn from discuss on 20181022
#Time:O(N)
#Space:O(1)
#Tree + Better Recursion
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


s = Solution()
t = TreeNode(5)
t.left = TreeNode(4)
t.right = TreeNode(8)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right.right = TreeNode(4)
t.right.right.right = TreeNode(1)
t.right.right.left = TreeNode(5)
t.right.left = TreeNode(13)
s.flatten(t)
