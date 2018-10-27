#222. Count Complete Tree Nodes

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181027
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Time Limit Exceeded
# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         leftNode = rightNode = root
#         left_height, right_height = 0, 0
#         while leftNode:
#             left_height += 1
#             leftNode = leftNode.left
#         while rightNode:
#             left_height += 1
#             rightNode = rightNode.right
#         if left_height == right_height:
#             return 2 ** left_height - 1
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#Learn from discuss on 20181027
#Time:O(Log(N)^2)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftNode, rightNode = root.left, root.right
        left_height, right_height = 0, 0
        while leftNode:
            left_height += 1
            leftNode = leftNode.left
        while rightNode:
            right_height += 1
            rightNode = rightNode.left
        if left_height == right_height:
            return pow(2, left_height) + self.countNodes(root.right)
        return pow(2, right_height) + self.countNodes(root.left)

#Learn from discuss on 20181027
#Time:O(Log(N)^2)
#Space:O(1)
#Tree + Recursion-->Iteration
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h, res = self.height(root), 0
        while root:
            if self.height(root.right) == h - 1:
                res += 2 ** h
                root = root.right
            else:
                res += 2 ** (h - 1)
                root = root.left
            h -= 1
        return res

    def height(self, root):
        return -1 if not root else 1 + self.height(root.left)


s = Solution()
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.left.left = TreeNode(0)
t.left.right = TreeNode(2)
t.right.left = TreeNode(7)
print(s.countNodes(t))
