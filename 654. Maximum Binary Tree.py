#654. Maximum Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
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

#Created by bryantbyr on 20181108
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        Max = max(nums)
        partition = nums.index(Max)
        root = TreeNode(Max)
        root.left = self.constructMaximumBinaryTree(nums[:partition])
        root.right = self.constructMaximumBinaryTree(nums[partition + 1:])
        return root


s = Solution()
root = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
Tree().front_recursion(root)
