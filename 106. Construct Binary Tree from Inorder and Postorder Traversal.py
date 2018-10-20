#106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def front_recursion(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.val)
        self.front_recursion(root.left)
        self.front_recursion(root.right)

#Created by bryantbyr on 20181020
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index + 1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root


s = Solution()
t = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
Tree().front_recursion(t)
