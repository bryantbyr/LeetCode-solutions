#108. Convert Sorted Array to Binary Search Tree

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
#Time:O(N)
#Space:O(N)
#Tree + Recursion
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            left, right = nums[:mid], nums[mid + 1:]
            root.right = self.sortedArrayToBST(right)
            root.left = self.sortedArrayToBST(left)
            return root

#Learn from discuss on 20181020
#Time:O(N)
#Space:O(1)
#Tree + Better Recursion
class Solution(object):
    def sortedArrayToBST(self, nums):
        def convert(left, right):
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(nums[mid])
                node.left = convert(left, mid - 1)
                node.right = convert(mid + 1, right)
                return node
        return convert(0, len(nums) - 1)


s = Solution()
t = s.sortedArrayToBST([-10, -3, 0, 5, 9])
Tree().front_recursion(t)
