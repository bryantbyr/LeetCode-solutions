#94.Binary Tree Inorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181019
#Time:O(n)
#Space:O(n)
#Tree + Recursion
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.in_order_recursion(root, list)
        return list

    def in_order_recursion(self, node, list):
        if not node:
            return
        self.in_order_recursion(node.left, list)
        list.append(node.val)
        self.in_order_recursion(node.right, list)


#Learn from Solution on 20181019
#Time:O(n)
#Space:O(n)
#Tree + Stack
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


s = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(6)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right.left = TreeNode(5)
print(s.inorderTraversal(t1))
