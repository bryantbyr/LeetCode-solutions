#105. Construct Binary Tree from Preorder and Inorder Traversal

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        left_inorder, right_inorder = [], []
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                left_inorder, right_inorder = inorder[:i], inorder[i + 1:]
                break
        left_preorder, right_preorder = preorder[1:len(left_inorder) + 1], preorder[len(left_inorder) + 1:]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

#Learn from discuss on 20181020
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:root_index + 1], inorder[0:root_index])
            root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
            return root

#Learn from discuss on 20181020
#Time:O(N^2)
#Space:O(1)
#Tree + Better Recursion
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root

#Memory Limit Exceeded
# class Solution:
#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         index_map = {}
#         # for i in range(len(inorder)):
#         #     index_map[inorder[i]] = i
#         for i, num in enumerate(inorder):
#             index_map[num] = i
#
#         def helper(preorder, inorder):
#             if not preorder or not inorder:
#                 return None
#             # root = TreeNode(preorder[0])
#             # left_inorder, right_inorder = inorder[:index_map[root.val]], inorder[index_map[root.val]+1:]
#             # left_preorder, right_preorder = preorder[1:len(left_inorder) + 1], preorder[len(left_inorder) + 1:]
#             # root.left = self.buildTree(left_preorder, left_inorder)
#             # root.right = self.buildTree(right_preorder, right_inorder)
#
#             root = TreeNode(preorder.pop(0))
#             root.left = self.buildTree(preorder, inorder[:index_map[root.val]])
#             root.right = self.buildTree(preorder, inorder[index_map[root.val] + 1:])
#
#             return root
#
#         return helper(preorder,inorder)

#Learn from discuss on 20181020
#Time:O(N)
#Space:O(N)
#Tree + Map + Better Recursion (pythonic)
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inor_dict = {}
        for i, num in enumerate(inorder):
            inor_dict[num] = i
        pre_iter = iter(preorder)

        def helper(start, end):
            if start > end:
                return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inor_dict[root_val]
            root.left = helper(start, idx - 1)
            root.right = helper(idx + 1, end)
            return root

        return helper(0, len(inorder) - 1)


s = Solution()
t = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
Tree().front_recursion(t)
